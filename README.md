# Automated Gym Slot Sign-Up (GymBot)

### What is GymBot?
In August of 2020, The University of Notre Dame enterred into lockdown due to rising COVID cases. As a result, there were a limited number of gym slots to sign up for. GymBot was made to sign up for these limited time slots faster than humanly possible. The user can enter the time slots they desire for the week, and GymBot will complete the SignUpGenius form in about 6 seconds.

### How does it work?
GymBot utilizes [Selenium](https://www.selenium.dev/) and [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) to automate the completion of a SignUpGenius form. The user enters the date and time of the slot(s) they desire into a bash terminal. The program generates the XPATH for each button that has to be clicked. In order to click the checkbox element, the program must use BeautifulSoup to search the inner HTML of each XPATH generated. Finally, Selenium grabs the XPATH of the checkbox button associated with the time slot and clicks it. Once all boxes are clicked, Selenium enters the contact info of the user and submits the sign-up form.

### Input Formatting
Time slots are enterred one after the other in the following format
```bash
{DayCode}[Time]
```
Consult the table below for the Day Codes:
|Day|Letter|
|---|------|
|Monday|M|
|Tuesday|T|
|Wednesday|W|
|Thursday|H|
|Friday|F|
|Saturday|S|
|Sunday|U|

### Test Run
Let's say a user wants to reserve time slots on Monday at 4:15PM, Wednesday at 7:15PM, and Friday at 8:00PM. In a bash terminal, the user would run the following code:
```bash
python gymBot.py M415 W715 F800
```
After Selenium initializes, the user enters the link of the SignUpGenius form and the code will run as follows:
![](Demo.gif)

### Dependencies
- pip 
- selenium
- bs4

### Installing
If you have [pip](https://pip.pypa.io/en/stable/) on your system, you can simply install each of the dependencies listed above:
```bash
pip install -U selenium
pip install -U bs4
```
Download the source code by running the command below:
```bash
git clone https://github.com/jhracho/GymBot.git
cd GymBot
```
### Further Developments
GymBot is hard-coded for a specific type of SignUpGenius form. In the future, I'd like GymBot to be more flexible in the kinds of forms it can automate. Perhaps I can use BeautifulSoup to find checkbox XPATHs based on the dates and times of other elements instead of pre-calculating the XPATHs.

### Acknowledgements
To all of my friends that I stole gym slots from: I'm not sorry ;)

### About
**Credits:** Jake Hracho\
**License:** GNU General Public License v3.0
