import os
import time

os.system('clear')
print()
print ('\033[1m Important  \033[0m')
print("Command should be valid")
print("Keyword that you want should not pre-exist")
print()
print("Example : reboot is already a command so it can't be over-written")
print()


while True:
    
    command = input("Enter Command ")

    alias = input("Enter Keyword to Represent Command ")

    #Append alias to .bashrc file present in /home/user/.bashrc
    os.system("echo \"alias {}=\'{}\'\" >> /home/$USER/.bashrc".format(alias,command)) 
    
    print()
    print("Command {} is now represented by {} ".format(command,alias))
    print()
    command = input("Add more Commands? [yes/no] ")
    if command == 'no':
        break
    print()
    
#Make linux recognise the command
os.system('. ~/.bashrc')
print()
command = input("Check whether the command now exist? [yes/no] ")


if command == 'yes':
    print()
    print("Scroll Down to the end of file and see if command is written !" )
    time.sleep(3)
    os.system('gedit /home/$USER/.bashrc')
    print()
    print()


print()
os.system('clear')
print("Happy Linuxing !")
print()
    
