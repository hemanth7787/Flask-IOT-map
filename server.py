import flask
from flask import g
import flask_socketio
import sqlite3
from contextlib import closing

app = flask.Flask(__name__)
#app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DATABASE'] = 'flaskr.db'
socketio = flask_socketio.SocketIO(app)

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def init_db():
    """Initializes the database."""
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

# Initialise Map with already existing values in DB
def initUser():
    db = get_db()
    data = db.execute('SELECT * FROM weather WHERE 1')
    # # ipdb.set_trace()
    if data:
        data_list = list()
        for row in data:
            data_list.append({
                'lat':row['lat'],
                'long':row['long'],
                'temp':row['temp']
            })
        return data_list
    else:
        return False

# Check received data and save it to database
def saveData(data):
    # Delete existing data
    db = get_db()
    db.execute('DELETE FROM weather WHERE lat = ? AND long = ?',
        [data['lat'], data['long']])
    db.execute('INSERT INTO weather (lat, long, temp) values (?, ?, ?)',
        [data['lat'], data['long'], data['temp']])
    db.commit()
    db.close()

# Process data and broadcast
def handleWeather(data):
    if float(data['lat']) and float(data['long']) and float(data['temp']):
    	saveData(data);
        socketio.emit('data', {
            'lat':data['lat'],
            'long':data['long'],
            'temp':data['temp']
            })

@app.route('/', methods=['GET', 'POST'])
def index():
    if flask.request.method == 'POST':
        handleWeather(flask.request.values)
        return flask.jsonify(status="ok")
    else:
        return flask.render_template('map_index.html')

@socketio.on('connect', namespace='/')
def init_maps():
    mata = initUser()
    if mata:
        socketio.emit('data-multiple',mata)
    g.sqlite_db.close()

if __name__ == '__main__':
    #socketio.run(app, debug=True)
    socketio.run(app)
