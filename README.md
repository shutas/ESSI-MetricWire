# ESSI-MetricWire
Python script for an automated webscraper  
by Shuta Suzuki (shutas@umich.edu)

This is a script that automates the process of logging into a MetricWire Research account.
  
  
# Prerequisites
You need to make sure that you have all of the following for the code to run properly:

1. Mac (specifically Safari)  
Sorry to all of the Windows/Linux fans out there. The code won't run unless you have Safari;)

2. Selenium package for Python 2.7 or 3.4+  
If you have no clue what I'm talking about, you probably don't have it. It's easy though. Just run the following command in your terminal:
```
pip install -U selenium
```

If you have all this, you should be good to go!
   
   
# Usage
Running this script is easy as 1, 2, 3! (Actually easier than that)

1. Modify `webscraper.py`  
You need to provide the login credentials for MetricWire Research. In the `Global Variables` section at the top of `webscraper.py`, replace the empty strings with strings of your login credentials.

2. Run the Webscraper!  
Type the following command in your directory containing `webscaper.py`, sit back, and let the magic happen on its own:)
```
python webscraper.py
```
   
# Troubleshooting
Don't worry. I got your back;) Here are some common problems you might run into...  

1. I don't have 'pip'!   
-> Easy fix. Just run the following command:
```
sudo easy_install pip
```

2. I don't know what version of Python I am using?  
-> This one's simple too. Check your python's version using:
```
python --version
```

3. I can't start Safari...  
-> If you're getting errors along the lines of `unable to start the server: another safaridriver is already running`, then make sure that you're Safari is allowing remote automation. To enable, click Safari's `Develop` menu, and check `Allow Remote Automation`.

4. What is 'Python'?  
-> Nope. I'm not answering this one. If you don't know what Python is, you shouldn't be here. Go watch YouTube instead.
