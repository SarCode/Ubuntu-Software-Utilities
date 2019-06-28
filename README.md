# Ubuntu-Software
Instructions and Commands to install softwares on Ubuntu Machine
<br>
<br>
<br>
<br>
<br>

## Commands

Most useful day-to-day usage commands can be found [here](https://github.com/SarCode/Ubuntu-Software-Utilities/tree/master/Useful-Commands).

## Anaconda

Install [anaconda](https://github.com/SarCode/Ubuntu-Software-Utilities/tree/master/Anaconda) in few easy steps


## Clean your system
Removes:
- Cache
- Unwanted libraries
- Binaries
- Kernel etc

Majority of the junk is deleted. 
<br>
`sudo apt-get autoclean && sudo apt-get autoremove`

## Complete Update and Upgrade your system
 
 Use command:
 <br>
 `sudo apt-get update && sudo apt-get upgrade && sudo apt-get dist-upgrade && sudo apt-get upgrade --with-new-pkgs`




## Ever closed a terminal that was running important command?

All of us have at-least once accidentally closed a terminal which has our command running, and then we have re-iniliase the whole setup.

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
