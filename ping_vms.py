import paramiko
ssh = paramiko.SSHClient()
host = "10.13.6.102"
username = "user"
password = ""
command = "ls"

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('10.13.6.103',port=22, username='oliveruhlar', password='xxxxx', key_filename='w_rsa')

ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('ping -c 3 10.13.6.104')
lines = ssh_stdout.readlines()
print(lines)

ssh_stderr.close()
ssh_stdin.close()
ssh_stdout.close()
ssh.close()