## Genius-Finance App
<p> The Genius Finance App is a tool that provides an individual with the oportunity too closely monitor their stock through real-time data from a Yahoo API. <p>

## Dependency
<p>Please make sure that you have the following dependencies installed:</p>

+ msvc-runtime==14.29.30133
+ python-dateutil==2.8.2
+ Python Version: 3.10.0
+ Uses Yahoo API yh-finance.p.rapidapi.com
+ Uses http client
+ Download MySQL following the instructions here: https://www.mysql.com/de/downloads/

#### If you get matplotlib error: This worked for me on Windows 10 (using the Anaconda prompt):
> pip uninstall matplotlib <p>
> pip install --upgrade matplotlib <p>


## Running the App:
+ run main.py make sure all dependencies are installed
+ All configurable variables are defined in main.py
+ This means if you need to change the API key or the SQL configuration, this is where you do it

## Changing the Yahoo API key
+ The API is limited to 500 free calls
+ To get a new key go to https://rapidapi.com/apidojo/api/yh-finance/
+ Create an account and click test endpoint and select the free trial version (basic plan)

## Configuring the MySQL server:
+ configurations are made in main.py in set_env_variables()
+ The MySQL password should be set to the users password that they set up when downloading MySQL for their machine.
+ By default the MySQL user is root and the MySQL host is localhost.
+ YOu may also change the database name in the same location

## Test cases 
+ Test cases are downloaded with the rest of the code.
+ Simply open the spreadsheets to view them.

