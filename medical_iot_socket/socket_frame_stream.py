import socketio
import eventlet

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio)


@sio.event
def connect(sid, environ):
    print('connected to server----->', sid)
    print('environ----->', environ)


@sio.event
def videostream(sid, data):
    print('I received a message from zmq server')
    print(data)
    sio.emit('videostream_mobile', {'data': data[0], 'deviceid': data[1]})


eventlet.wsgi.server(eventlet.listen(('127.0.0.1', 1234)), app)
