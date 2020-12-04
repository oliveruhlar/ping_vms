import paramiko
import time

def set_ip(vm,ip):
    set_ip_cmd = "sudo ifconfig enp0s9 " + ip + " up"
    vm.exec_command(set_ip_cmd)
    vm.exec_command('sudo service network-manager restart')
    time.sleep(1)

vm_u = paramiko.SSHClient()
vm_u2 = paramiko.SSHClient()

vm_u.set_missing_host_key_policy(paramiko.AutoAddPolicy())
vm_u2.set_missing_host_key_policy(paramiko.AutoAddPolicy())

vm_u.connect('192.168.56.2',port=22, username='oliveruhlar', password='', key_filename='w_rsa')
vm_u2.connect('192.168.56.3',port=22, username='oliveruhlar', password='', key_filename='vm_u2_rsa')
vm_u.exec_command('sudo ifconfig enp0s9 down')
vm_u2.exec_command('sudo ifconfig enp0s9 down')
time.sleep(1)

set_ip(vm_u,"10.2.0.23")
print("Setting NIC for VM n1 was successful")
set_ip(vm_u2,"10.2.0.24")
print("Setting NIC for VM n2 was successful")