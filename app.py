from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/places')
def get_places():
    places = [
        "Kanyakumari",
        "Courtallam",
        "Padmanabhapuram Palace",
        "Meenakshi Amman Temple",
        "Rameswaram",
        "Thanjavur Big Temple"
    ]
    return jsonify(places)

if __name__ == '__main__':
    app.run(debug=True)