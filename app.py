
from operator import methodcaller
import requests, time, json
from flask import Flask, jsonify , render_template, request 
from collections import defaultdict
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/script', methods=['POST'])
def postTimeSensor():
    print(f'request.is_json: {request.is_json}')
    content = request.get_json()
    print(f'content: {content}')
    conn = sqlite3.connect('data.db')
    push = conn.cursor()
    push.execute('INSERT INTO SensorData (localtime, newYork, London) VALUES (?, ?, ?)',
                (content['localtime'], content['newyork'], content['London']))
    conn.commit()
    conn.close()
    return '{"message": "JSON post success"}'
    

@app.route('/info')
def getData(data):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('SELECT localtime FROM SensorData')
    localtime = c.fetchall()
    c.execute('SELECT newYork FROM SensorData')
    newYork = c.fetchall()
    c.execute('SELECT London FROM SensorData')
    London = c.fetchall()
    conn.commit()
    conn.close()
    return  render_template('info.html',n=data['name'], e=data['ename'], add=data['adress'], post=data['postnumer'], plats=data['ort'], epost=data['epost'], password=data['password'], offer=data['offer'], eform=data['eform'], comment=data['comment'], localtime=localtime, newYork=newYork, London=London)


app.run(debug=True)

