import paramiko
import time


def print_ifconffig(vm):
    vm_stdin, vm_stdout, vm_stderr = vm.exec_command("ifconfig")
    lines = vm_stdout.readlines()
    print(lines,'\n')
    vm_stderr.close()
    vm_stdin.close()
    vm_stdout.close()

def ping_vms(vm1,vm2_ip):
    ping_cmd = "ping -c 3 " + vm2_ip
    vm1_stdin, vm1_stdout, vm1_stderr = vm1.exec_command(ping_cmd)
    lines = vm1_stdout.readlines()
    print(lines,'\n')
    vm1_stderr.close()
    vm1_stdin.close()
    vm1_stdout.close()

def set_ip(vm,ip):
    set_ip_cmd = "sudo ifconfig enp0s8 " + ip + " up"
    vm.exec_command(set_ip_cmd)
    vm.exec_command('sudo service network-manager restart')
    time.sleep(1)

vm_u = paramiko.SSHClient()
vm_u2 = paramiko.SSHClient()

vm_u.set_missing_host_key_policy(paramiko.AutoAddPolicy())
vm_u2.set_missing_host_key_policy(paramiko.AutoAddPolicy())

vm_u.connect('10.13.6.103',port=22, username='oliveruhlar', password='', key_filename='w_rsa')
vm_u2.connect('10.13.6.106',port=22, username='oliveruhlar', password='', key_filename='vm_u2_rsa')
vm_u.exec_command('sudo ifconfig enp0s8 down')
vm_u2.exec_command('sudo ifconfig enp0s8 down')
time.sleep(1)

print('\n','\n',"Interface configuration berfore setting interfaces and ip for Internal Network",'\n')
print("VM n.1")
print_ifconffig(vm_u)
print("VM n.2")
print_ifconffig(vm_u2)

print('\n', "Ping Vms before setting IPs for Internal network",'\n')

print('ping VM n.1 -> VM n.2')
ping_vms(vm_u,"10.2.0.21")

print('ping VM n.2 -> VM n.1')
ping_vms(vm_u2,"10.2.0.20")


print('\n',"Interface configuration after setting interfaces and ip for Internal Network",'\n')

print("VM n.1")
set_ip(vm_u,"10.2.0.22")
print_ifconffig(vm_u)

print("VM n.2")
vm_u2.exec_command('sudo ifconfig enp0s8 10.2.0.21 up')
vm_u2.exec_command('sudo service network-manager restart')
time.sleep(1)
print_ifconffig(vm_u2)

print('\n',"Ping VMs between each other",'\n')

print('ping VM n.1 -> VM n.2')
ping_vms(vm_u,"10.2.0.21")

print('ping VM n.2 -> VM n.1')
ping_vms(vm_u2,"10.2.0.20")

vm_u.close()
vm_u2.close()