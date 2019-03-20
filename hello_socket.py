from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.debug = True

sockets = SocketIO(app)

@sockets.route('/echo')
def echo_socket(ws):
    while True:
        message = ws.receive()
        ws.send(message[::-1])

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/echo_test', methods=['GET'])
def echo_test():
    return render_template('echo_test.html')

if __name__ == '__main__':
    app.run(debug=True, host='158.196.21.78')
