from flask import Flask, request
import json
app = Flask(__name__)
@app.route('/prime/<int:number>')
def check_prime(number):
    if number < 2:
        return json.dumps({"number": number, "is_prime": False})
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return json.dumps({"number": number, "is_prime": False})
    return json.dumps({"number": number, "is_prime": True})
if __name__ == "__main__":
    app.run(use_reloader=True, host = '127.0.0.1', port = 5000)