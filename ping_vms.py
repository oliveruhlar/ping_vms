import paramiko
import time


def print_ifconffig(vm):
    vm_stdin, vm_stdout, vm_stderr = vm.exec_command("ip -o address")
    lines = vm_stdout.readlines()
    print(lines,'\n')
    vm_stderr.close()
    vm_stdin.close()
    vm_stdout.close()

vm_u = paramiko.SSHClient()
vm_u2 = paramiko.SSHClient()

vm_u.set_missing_host_key_policy(paramiko.AutoAddPolicy())
vm_u2.set_missing_host_key_policy(paramiko.AutoAddPolicy())

vm_u.connect('10.13.6.103',port=22, username='oliveruhlar', password='', key_filename='w_rsa')
vm_u2.connect('10.13.6.106',port=22, username='oliveruhlar', password='', key_filename='vm_u2_rsa')

print('\n',"Interface configuration berfore setting interfaces and ip for Internal Network",'\n')
print("VM n.1")
vm_u_stdin, vm_u_stdout, vm_u_stderr = vm_u.exec_command("ip -o address")
lines = vm_u_stdout.readlines()
print(lines,'\n')
print("VM n.2")
vm_u2_stdin, vm_u2_stdout, vm_u2_stderr = vm_u2.exec_command("ip -o address")
lines = vm_u2_stdout.readlines()
print(lines)


print('\n',"Interface configuration after setting interfaces and ip for Internal Network",'\n')

print("VM n.1")
vm_u.exec_command('sudo ifconfig enp0s8 10.2.0.20 up')
vm_u.exec_command('sudo service network-manager restart')
time.sleep(1)
vm_u_stdin, vm_u_stdout, vm_u_stderr = vm_u.exec_command("ip -o address")
lines = vm_u_stdout.readlines()
print(lines,'\n')

print("VM n.2")
vm_u2.exec_command('sudo ifconfig enp0s8 10.2.0.21 up')
vm_u2.exec_command('sudo service network-manager restart')
time.sleep(1)
vm_u2_stdin, vm_u2_stdout, vm_u2_stderr = vm_u2.exec_command("ip -o address")
lines = vm_u2_stdout.readlines()
print(lines)

print('\n',"Ping VMs between each other",'\n')

print('ping VM n.1 -> VM n.2')
vm_u_stdin, vm_u_stdout, vm_u_stderr = vm_u.exec_command('ping -c 3 10.2.0.21')
lines = vm_u_stdout.readlines()
print(lines,'\n')

print('ping VM n.2 -> VM n.1')
vm_u2_stdin, vm_u2_stdout, vm_u2_stderr = vm_u2.exec_command('ping -c 3 10.2.0.20')
lines = vm_u2_stdout.readlines()
print(lines)

vm_u_stderr.close()
vm_u_stdin.close()
vm_u_stdout.close()
vm_u.close()

vm_u2_stderr.close()
vm_u2_stdin.close()
vm_u2_stdout.close()
vm_u2.close()