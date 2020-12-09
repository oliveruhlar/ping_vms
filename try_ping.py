import paramiko
import time

def ping_vms(vm1,vm2_ip):
    ping_cmd = "ping -c 3 " + vm2_ip
    vm1_stdin, vm1_stdout, vm1_stderr = vm1.exec_command(ping_cmd)
    lines = vm1_stdout.readlines()
    print(lines)
    vm1_stderr.close()
    vm1_stdin.close()
    vm1_stdout.close()

vm_u = paramiko.SSHClient()
vm_u2 = paramiko.SSHClient()

vm_u.set_missing_host_key_policy(paramiko.AutoAddPolicy())
vm_u2.set_missing_host_key_policy(paramiko.AutoAddPolicy())

vm_u.connect('192.168.56.2',port=22, username='oliveruhlar', password='', key_filename='w_rsa')
vm_u2.connect('192.168.56.3',port=22, username='oliveruhlar', password='', key_filename='vm_u2_rsa')

print('\n','ping VM n1 -> VM n2','\n')
ping_vms(vm_u,"10.2.0.24")
print('\n','ping VM n2 -> VM n1','\n')
ping_vms(vm_u2,"10.2.0.23")