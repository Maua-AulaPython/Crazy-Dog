from flask import Flask, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
import json
from classmodel import *
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///BancoDeDadosM.db'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

@app.route("/")
def index():
    return "Nossas rotas sao: '/measures/show', '/measures/new' e '/device/new'"

@app.route('/measures/show', methods=['GET'])
def measure_list():
	measures = []
	for i in Measure.query.all():
		print i.date, i.id_device,i.luminosity, i.temperature
		measures.append({'Data': i.date, 'ID:':i.id_device, 'Luminosidade': i.luminosity, 'Temperatura': i.temperature})

	return json.dumps(measures)


@app.route('/measures/new', methods=['POST'])
def measure_new():
	if not request.json:
		return jsonify({'status': False})

	p = request.get_json()
	m = Measure()
	m.date = datetime.today()
	m.id_device = p['ID']
	m.luminosity = p['Luminosidade']
	m.temperature = p['Temperatura']
	db.session.add(m)
	db.session.commit()
	return jsonify({'status:': True})


@app.route('/device/new', methods = ['POST'])
def estufa_new():
	if not request.json:
		return jsonify({'status': False})
	p = request.get_json()
	d = Device()
	d.latitude = p['Latitude']
	d.longitude = p['Longitude']
	db.session.add(d)
	db.session.commit()
	return jsonify({'status': True})


if __name__ == '__main__':
    app.run(debug=True)

