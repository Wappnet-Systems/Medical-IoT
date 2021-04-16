import imagezmq
import socket
import time
import cv2
import zmq

sender = imagezmq.ImageSender(connect_to="tcp://localhost:5555")

context = zmq.Context()
skt = context.socket(zmq.REQ)
skt.connect("tcp://localhost:5556")
skt.send_string('10006')
status = skt.recv()
print(status)

cap = cv2.VideoCapture("output2.avi")
rpiName = socket.gethostname()
print(rpiName)
while True:
    ret, frame = cap.read()
    # Serialize frame

    msg = sender.send_image(rpiName,10003, frame)
    print(msg)


