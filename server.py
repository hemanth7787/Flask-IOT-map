import flask
import flask_socketio
from contextlib import closing
from models import Weather

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'make-a-random-secret!'
socketio = flask_socketio.SocketIO(app)

def replace_stored_data(data):
    # Delete existing data
    query = Weather.delete().where((Weather.lattitude == data['lat']) &  (Weather.longitude==data['long']))
    query.execute()
    # Save new data
    Weather.create(lattitude=data['lat'], longitude=data['long'], temp=data['temp'])

# Process data and broadcast
def handleWeather(data):
    if float(data['lat']) and float(data['long']) and float(data['temp']):
    	replace_stored_data(data);
        socketio.emit('data', { 'lattitude':data['lat'], 'longitude':data['long'], 'temp':data['temp'] })

@app.route('/', methods=['GET', 'POST'])
def index():
    if flask.request.method == 'POST':
        handleWeather(flask.request.values)
        return flask.jsonify(status="ok")
    else:
        return flask.render_template('index.html')

# Initialise Map with already existing values in DB
@socketio.on('connect', namespace='/')
def init_maps():
    data = [x.json() for x in Weather.select()] # Python list comprehension, .json() method is defined in models
    if data:
        socketio.emit('data-multiple',data)

if __name__ == '__main__':
    socketio.run(app,host='127.0.0.1',port=5000)
