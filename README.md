# Travian-Bot

## Installation:
To run the bot the user requires to have both Python (recommended 3.6) and Selenium (for the bot to work). 
Download selenium using pip install selenium. 
 
## Webdrivers: 
The bot uses chrome webdriver which is located in source/webdrivers/chromedriver however this is for a spesific version of chrome. 
If you are having troubles running it, recommended to dowload the newest version for you. 
 
## Easy Run: 
To run the bot you should use the following format: 
```
python program.py https://serverurl.domain username password lang 0,1,2
```
whereas https://serverurl.domain is the game's default link, username is your username and password is your pass. 
the parameters 0,1,2 represents the list indexes that the program should send (farm list) [index starts at 0 and ends with length minus one] 
 
To make it easier, we are recommending creating batch file (ends with .bat) and write the following command: 
  
### Note: Do NOT use smart farmlist. use the old one which shows all of the farm lists open when entering the farm lists. 
### Note: Your current village MUST have rally point to run the farm lists, because the bot enters the rally point of current village. 
 
Have fun! 
