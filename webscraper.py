"""
Functionality: 1. Access MetricWire Research Website
               2. Login with Provided Credentials
               3.

Written by: Shuta Suzuki (shutas@umich.edu)
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

######## Global Variables ########
email_address = ""
password = ""
##################################

# Access MetricWire Research Tool
driver = webdriver.Safari()
driver.get("http://www.research.metricwire.com")

# Send Login Credentials and Log In
element = driver.find_element_by_id("email")
element.send_keys(email_address)
element = driver.find_element_by_id("password")
element.send_keys(password)
element.send_keys(Keys.RETURN)
