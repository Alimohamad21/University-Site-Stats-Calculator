
# University Site Stats Calculator

This program is used to scrape Alexandria University Website to automatically calculate some stats about your own account such as the GPA, total count for each grade, and total credit hours earned for each grade.




## How to run the project

```
1- git clone https://github.com/Alimohamad21/University-Site-Stats-Calculator
2- pip install -r requirements.txt
3- Install the msedge web driver from here: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/  
4- Create a .env file in the root of the project.
5- Add the following variables to your .env file:

DRIVER_PATH = ''

Example: DRIVER_PATH = '/Users/Mohamed/Downloads/msedgedriver' (This is the installation directory of the msedge web driver)

SITE_USERNAME = ''

Example: SITE_USERNAME = '5432' (This is your university ID)

SITE_PASSWORD = ''

Example: SITE_PASSWORD = 'qzqt735#' (This you university website password)

6- Run main.py
7- Open the auto-generated csv files to view your stats.

```
