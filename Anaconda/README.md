


> Written with [StackEdit](https://stackedit.io/).
> Reference: [Installation of Anaconda on Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-install-anaconda-on-ubuntu-18-04-quickstart)

 # Instructions
[command.sh](https://github.com/SarCode/Ubuntu-Software/blob/master/Anaconda/command.sh) contains all the necessary commands

### Easy Method
- Open Terminal and type
	- git clone --depth 1 https://<span></span>github.com/SarCode/Ubuntu-Software Anaconda
	- cd Anaconda
	- chmod +x command.sh
	- bash command.sh
	

### Manual Method
If above method doesn't work for you

 -    cd /tmp

 - curl -O https://<span></span>repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh

 - bash Anaconda3-2019.03-Linux-x86_64.sh
	- Press Enter till you reach end of License Agreement.
	- Type yes to agree to license aggrement.
	- Press Enter if default location doesn't bother you, else change location. [ Recommended to not change location ]
	- Type yes to use conda command
	
- source ~/.bashrc

Update and Upgrade all packages.

- conda update --all && conda upgrade --all

  

# Anaconda is Ready !

Commands to open internal software:

	- anaconda-navigator
	- jupyter-notebook
