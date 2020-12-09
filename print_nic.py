import paramiko
from prettytable import PrettyTable

def print_ifconffig(vm):
    vm_stdin1, vm_stdout1, vm_stderr1 = vm.exec_command("""ip a | grep "scope global" | grep -Po '(?<=inet )[\d.]+'""")
    vm_stdin, vm_stdout, vm_stderr = vm.exec_command(str("""ip link | awk -F: '$0 !~ "lo|vir|^[^0-9]"{print $2a;getline}'"""))
    ip_addrs = [i.strip() for i in vm_stdout1.readlines()]
    nic_names = [i.strip() for i in vm_stdout.readlines()]
    rows = [list(i) for i in zip(nic_names, ip_addrs)]
    nic_tb = PrettyTable(["NIC name","IPv4"])
    for row in rows:
        nic_tb.add_row(row)
    print(nic_tb)
    vm_stderr.close()
    vm_stdin.close()
    vm_stdout.close()

vm_u = paramiko.SSHClient()
vm_u2 = paramiko.SSHClient()

vm_u.set_missing_host_key_policy(paramiko.AutoAddPolicy())
vm_u2.set_missing_host_key_policy(paramiko.AutoAddPolicy())

vm_u.connect('192.168.56.2',port=22, username='oliveruhlar', password='', key_filename='w_rsa')
vm_u2.connect('192.168.56.3',port=22, username='oliveruhlar', password='', key_filename='vm_u2_rsa')

print('\n',"VM n1")
print_ifconffig(vm_u)
print('\n',"VM n2")
print_ifconffig(vm_u2)