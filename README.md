# Discord Bot
__To get the bot running__: 

Make sure you have a [Discord](https://discord.com/) account set up.

__Optional:__

I always set up a virtual environment, if you want to do the same please follow these steps in a terminal:
```
sudo pip3 install virtualenv
python3 -m venv virenv
```
Now you should see a folder called virenv in your newly created folder. To access it please do the following:
```
source virenv/bin/activate
```
You are now inside your virutal environment and can install packages as usual.

Once you have a Discord accout set up, navigate to wanted terminal and install the discord package:
```
sudo apt-get install Discord
or 
sudo apt-get install discord.py
```
__Now we will set up the bot on Discord developer page__:

Head over to Discord's [developer](https://discord.com/developers/applications) portal. Once logged in click on __Applications__ then __New Application__. Give it a name and then click on it. Now you've created the bot and may change profile picture, name and other settings. However for this tutorial you shall now navigate to __URL Generator__ and click on the box that says __bot__. Then another box with different properties should show up, click on every box within the __Text Permissions__ section. Now copy the link and paste it in a new tab, select what server you want it to join and **voiala**, you have now got a bot in your server. The last thing you need to do is to grab the unique token generated for this bot, to get this, navigate to the **Bot** tab and click **copy** where it says **Token**. You are now set up to run the bot, lets to that.


__Set up the discord environment on your computer__:

First off, create a new folder somewhere on your computer and open it with your text editor. Create a new file called bot.py. Once inside bot.py, paste the code i have provided within this repository, or write new on your own. Please note that its very important that you provide the script with your token.

You should now be ready to run the bot, to run the bot type:
```
python3 bot.py
```
in the console.

__Author Jakob Adamsson__