# Flask-IOT-map

A python(flask) implementation of [IOT-Map] . The server accepts temprature details of devices placed along numerous geographical locations via HTTP post and shows them in google map.  Websockets are used to update the map in realtime.

Setup:

```sh
# As on ubuntu 14.04
sudo apt-get build-dep python-eventlet
pip install -r requirements.txt
python init_db.py
python server.py
```

[IOT-Map]: <https://github.com/r3s/IOT-Map>
