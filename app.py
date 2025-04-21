from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'test_key'  # Arbitrary, needed by Flask
socketio = SocketIO(app, cors_allowed_origins="*")  # Allow any origin

@app.route('/')
def index():
    return render_template('chat.html')

@socketio.on('message')
def handle_message(msg):
    print(f"Received: {msg}")
    send(msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
