
> Reference: [Unlock with Face](https://github.com/Boltgolt/howdy)

# Introduction
Don't you feel irritated when you have to type your password again and again everytime you use a sudo command?

Now use your face for sudo command !

### Command
	sudo add-apt-repository ppa:boltgolt/howdy
	sudo apt update
	sudo apt install howdy
	sudo howdy add


# Face-Unlock is Ready !



# Usage

- If in any scenario you need to input your password, the program will automatically start detecting your face, and will unlock.

-  The default wait time is 4 sec . If face not found due to any reason in these 4 sec then you would have to manually input your password.

- At system boot-up ( power-on ), the face recognizer would work but due to security reason you still have to insert your password.

- Except above scenario the program works perfectly.

- You can add multiple face to it, i.e. if your face is not recognized for any reason, then use command to add your face in that light condition.
<br>

	sudo howdy add 
