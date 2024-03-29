<p align="left"> <img src="https://komarev.com/ghpvc/?username=sarcode&label=Profile%20views&color=0e75b6&style=flat" alt="sarcode" /> </p>

[![LinkedIn][linkedin-shield]][linkedin-url]


# Ubuntu-Software
Instructions and Commands to install softwares on Ubuntu Machine
<br>
<br>

## Anaconda

Install [anaconda](https://github.com/SarCode/Ubuntu-Software-Utilities/tree/master/Anaconda) in few easy steps

<br>

## Clean your system
Removes:
- Cache
- Unwanted libraries
- Binaries
- Kernel etc

Majority of the junk is deleted. 
<br>
`sudo apt-get autoclean -y && sudo apt-get autoremove -y`

<br>


## Complete Update and Upgrade your system
 
 Use command:
 <br>
 `sudo apt-get update -y && sudo apt-get upgrade -y && sudo apt-get dist-upgrade -y && sudo apt-get upgrade --with-new-pkgs -y`

<br>

## Ever closed a terminal that was running important command?

All of us have at-least once accidentally closed a terminal which has our command running, and then we have to re-iniliaze the whole setup.

Well I give you a life-long solution to it.

`nohup` command

Example:

`nohup sudo apt-get upgrade`

Now, even if I close the terminal, the command won't stop and will work on the background.

Nice ! 

You can use it to run software via terminal and then close the terminal.

Example:
`nohup spyder`

Just simply, run a command and close the tab.

<br>

## Linux Cheat Sheet

Do more than you do on linux with this [cheat-map](https://github.com/SarCode/Ubuntu-Software-Utilities/raw/master/linux-cheat-sheet.png)



[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/sarthak-agarwal-dell/
