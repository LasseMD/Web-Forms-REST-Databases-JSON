import requests, time, json, random, pytz
from flask import Flask
from datetime import datetime

app = Flask(__name__)
while True:
    localtime = datetime.now()
    newYork_time = pytz.timezone('America/New_York')
    datetime_NY = datetime.now(newYork_time)
    london = pytz.timezone('Europe/London')
    datetime_London = datetime.now(london)
    data_dict = {"localtime" :localtime.strftime("%H:%M:%S"), "newyork": datetime_NY.strftime("%H:%M:%S"), "London": datetime_London.strftime("%H:%M:%S")}
    r = requests.post('http://127.0.0.1:5000/script', json=data_dict)
    time.sleep(20)

