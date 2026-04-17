from flask import Flask, jsonify
import json

app = Flask(__name__)

with open('airports.json', 'r') as f:
    airports = json.load(f)

@app.route('/airport/<icao>')
def get_airport(icao):
    icao = icao.upper()
    
    for airport in airports:
        if airport["icao"] == icao:
            return jsonify({
                "icao": airport["icao"],
                "name": airport["name"],
                "city": airport["city"],
                "country": airport["country"]
            })
    
    return jsonify({"error": "Airport not found"}), 404

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)