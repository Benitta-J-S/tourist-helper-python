from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/places')
def get_places():
    places = [
      {"name": "Kanyakumari", "info": "Southern tip of India, famous for sunrise and Vivekananda Rock."},
        {"name": "Courtallam", "info": "Known for waterfalls and herbal baths."},
        {"name": "Padmanabhapuram Palace", "info": "Historic wooden palace near Nagercoil."},
        {"name": "Meenakshi Amman Temple", "info": "Iconic temple in Madurai with stunning architecture."},
        {"name": "Rameswaram", "info": "Sacred pilgrimage site with long sea bridge."},
        {"name": "Thanjavur Big Temple", "info": "UNESCO World Heritage site built by Cholas."}

    ]
    return jsonify(places)

if __name__ == '__main__':
    app.run(debug=True)