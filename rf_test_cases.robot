*** Settings ***
Library  OperatingSystem
Library  Process
Library  Collections

Suite Setup    Start vms
Suite Teardown  Teardown vms
*** Variables ***

*** Test Cases ***
NIC config before setting NIC
    Wait Until Keyword Succeeds  2min   10s   Are booted	
    ${result} =  Run Process  C:\\Users\\oliver.uhlar\\Desktop\\Projects\\ping_vms\\.venv\\Scripts\\python.exe  print_nic.py  runserver
    Should Be Empty  ${result.stderr}  msg=${result.stderr}
    Log  ${result.stdout}

Ping VMs before setting NIC	
    ${result} =  Run Process  C:\\Users\\oliver.uhlar\\Desktop\\Projects\\ping_vms\\.venv\\Scripts\\python.exe  try_ping.py  runserver
    Should Be Empty  ${result.stderr}  msg=${result.stderr}
    Should Contain  ${result.stdout}  100% packet loss
    Log  ${result.stdout}

Set NIC
    ${result} =  Run Process  C:\\Users\\oliver.uhlar\\Desktop\\Projects\\ping_vms\\.venv\\Scripts\\python.exe  set_nic.py  runserver
    Should Be Empty  ${result.stderr}  msg=${result.stderr}
    ${ifconfig} =  Run Process  C:\\Users\\oliver.uhlar\\Desktop\\Projects\\ping_vms\\.venv\\Scripts\\python.exe  print_nic.py  runserver
    Should Contain X Times  ${result.stdout}  successful  2  msg=Setting NIC was unsuccessful
    Should Contain X Times  ${ifconfig.stdout}  enp0s9  2  msg=Setting NIC was unsuccessful
    Should Contain  ${ifconfig.stdout}  10.2.0.23  msg=Setting NIC for VM n1 was unsuccessful  values=False
    Should Contain  ${ifconfig.stdout}  10.2.0.24  msg=Setting NIC for VM n2 was unsuccessful  values=False
    Log  ${result.stdout}
    Log  ${ifconfig.stdout}

Ping VMs after setting NIC	
    ${result} =  Run Process  C:\\Users\\oliver.uhlar\\Desktop\\Projects\\ping_vms\\.venv\\Scripts\\python.exe  try_ping.py  runserver
    Should Be Empty  ${result.stderr}  msg=${result.stderr}
    Should Contain X Times  ${result.stdout}  0% packet loss  2  msg=Ping successful
    Log  ${result.stdout}

NIC config after setting NIC
    ${result} =  Run Process  C:\\Users\\oliver.uhlar\\Desktop\\Projects\\ping_vms\\.venv\\Scripts\\python.exe  print_nic.py  runserver
    Should Be Empty  ${result.stderr}  msg=${result.stderr}
    Log  ${result.stdout}

*** Keywords ***
Are booted
    ${result} =  Run Process  C:\\Users\\oliver.uhlar\\Desktop\\Projects\\ping_vms\\.venv\\Scripts\\python.exe  print_nic.py  runserver
    Should Be Empty  ${result.stderr}  msg=${result.stderr}

Start vms
    Start process     C:\\Program Files\\Oracle\\VirtualBox\\VBoxManage.exe  startvm  ubuntu_1  {c0382caa-6ce6-4fd3-aab4-77ea96bff7f7}  --type  headless
    Start process     C:\\Program Files\\Oracle\\VirtualBox\\VBoxManage.exe  startvm  ubuntu_2  {c0382caa-6ce6-4fd3-aab4-77ea96bff7f7}  --type  headless
Teardown vms    
    Start process     C:\\Program Files\\Oracle\\VirtualBox\\VBoxManage.exe  controlvm  ubuntu_1  poweroff
    Start process     C:\\Program Files\\Oracle\\VirtualBox\\VBoxManage.exe  controlvm  ubuntu_2  poweroff
