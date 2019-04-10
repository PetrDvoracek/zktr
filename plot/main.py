from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO
import time


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

    
@app.route('/')
def sessions():
    return render_template('index.html')

@app.route('/api/potentiometer/', methods=['GET'])
def api_potentiometer():
    with open('/sys/devices/ocp.3/helper.15/AIN0', 'r') as f:
        value = float(f.read())
    return jsonify({'poten_value': value})


if __name__ == '__main__':
    socketio.run(app, debug=True, host='158.196.21.78')
