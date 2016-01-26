# Flask-IOT-map

A python(flask) implementation of [IOT-Map] . The server accepts temprature details of devices placed along numerous geographical locations via HTTP post and shows them in google map.  Websockets are used to update the map in realtime.

#### Tech

This application uses a number of open source projects to work properly:

* [Flask] - a microframework for Python based on Werkzeug, Jinja 2 and good intentions
* [Peewee] - Peewee is a simple and small ORM. It has few (but expressive) concepts
* [Eventlet] - Eventlet is a concurrent networking library for Python
* [Flask-SocketIO] - Flask-SocketIO gives Flask applications access to low latency bi-directional communications between the clients and the server

#### Setup:

```sh
# As on ubuntu 14.04
sudo apt-get build-dep python-eventlet
pip install -r requirements.txt
python init_db.py
python server.py
```

[IOT-Map]: <https://github.com/r3s/IOT-Map>
[Flask]:<http://flask.pocoo.org/>
[Peewee]:<http://docs.peewee-orm.com/en/latest/>
[Eventlet]:<http://eventlet.net/>
[Flask-SocketIO]:<https://flask-socketio.readthedocs.org/en/latest/>
