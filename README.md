# Travian-Bot

## Installation:
To run the bot the user requires to have both Python (3.10), Selenium and undetected_chromedriver.
Download required libraries run:
```
pip install selenium
pip install undetected_chromedriver
```
 
## Easy Run: 
To run the bot you should use the following format: 
```
python program.py "https://serverurl.domain" "username" "password" "0,1,2,3" 50 1000
```
- https://serverurl.domain is the game's default link, username is your username and password is your pass. 
- The parameters 0,1,2,3 represents the list indexes that the program should send (farm list) [index starts at 0 and ends with length minus one].
- The parameters 50 and 1000 state the minimum and maximum seconds the bot will randomlly time itself to seld farm list.
- For example: to randomlly send farm list between 30m to 60m you will input 1800 3600.
 
 
To make it easier, we are recommending creating batch file (ends with .bat) and write the following command.
### Note: Your current village MUST have rally point to run the farm lists, because the bot enters the rally point of current village. 
