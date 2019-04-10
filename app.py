#!/usr/local/bin/python3.5

from flask import Flask, jsonify
from flask import render_template
import Adafruit_BBIO.ADC as ADC


app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]
poten_timeserie=[]


@app.route('/api/potenciometer', methods=['GET'])
def get_poten():
    ADC.setup()
    value = ADC.read("AIN0")

    return jsonify({'poten_value': value})

@app.route('/api/pot_data', methods=['GET'])
def get_poten_data():
   return jsonify({'poten_timeserie':poten_timeserie})

@app.route('/potenciometer',methods=['GET'])
def render_poten():
    return render_template('potenciometer.html', message='')

def main():
    app.run(debug=True, host='158.196.21.78')
    print("neco")

if __name__ == '__main__':
    main()
