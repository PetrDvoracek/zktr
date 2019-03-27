from flask import Flask, render_template
from flask_socketio import SocketIO
import Adafruit_BBIO.GPIO as GPIO
import time


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@socketio.on('my event')
def handle_my_event(message):
    print(message)


@socketio.on('message')
def handle_message(message):
    try:
        print('handled message:' + str(message))
#        exec(message)
#        GPIO.setup(message, GPIO.OUT)
#        GPIO.output(message, GPIO.OUT)
    except Exception as e:
        print('EXCEPTION:' + str(e))
    
@app.route('/')
def sessions():
    return render_template('index.html')


if __name__ == '__main__':
    socketio.run(app, debug=True, host='158.196.21.78')
