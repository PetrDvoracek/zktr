from flask import Flask, render_template
from flask_socketio import SocketIO, emit
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
        exec(message['data'])
#        GPIO.setup(message, GPIO.OUT)
#        GPIO.output(message, GPIO.OUT)
    except Exception as e:
        print('EXCEPTION:' + str(e))
    
@app.route('/')
def sessions():
    return render_template('index.html')

@socketio.on('get_direction')
def handler(message):
    direction = 'right'
    buttons = {'btn_up':27,'btn_down':49,'btn_left':51,'btn_right':48}
    btn_up = 27
    btn_down = 49
    btn_left = 51
    btn_right = 48
    print("GET DIRECTION") 
#    for key, value in buttons.items():
#        if read_btn(value):
#            emit('direction',key)
#            return
#    emit('direction','none')
#    return
    emit('neco','z backendu')   
        
#    with open('/sys/devices/ocp.3/helper.15/AIN0','r') as f:
#        v = int(f.readline())
#    if voltage > 800:
#        direction = 'left'
#    emit('direction', direciton)

def read_btn(number):
    with open('/sys/class/gpio/gpio{0}'.format(number),'r') as f:
        return int(f.readline())


if __name__ == '__main__':
    socketio.run(app, debug=True, host='158.196.21.78')
