


> Written with [StackEdit](https://stackedit.io/).
> Reference: [Installation of Anaconda on Ubunt](https://www.digitalocean.com/community/tutorials/how-to-install-anaconda-on-ubuntu-18-04-quickstart)

 # Instructions
[command.sh] () contains all the necessary commands

## Easy Method
- Download [command.sh] ()

- Open terminal and go to folder where command.<span></span>sh is downloaded.
- Type in terminal 
	-  chmod +x command.<span></span>sh
	- bash command.<span></span>sh
	

## Manual Method
If above method doesn't work for you

 -    cd /tmp

 - curl -O https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh

 - bash Anaconda3-2019.03-Linux-x86_64.sh
	- Press Enter till you reach end of License Agreement.
	- Type yes to agree to license aggrement.
	- Press Enter if default location doesn't bother you, else change location. [ Recommended to not change location ]
	- Type yes to use conda command
	
- source ~/.bashrc

Update and Upgrade all packages.

- conda update --all && conda upgrade --all

  

# Anaconda is ready !

