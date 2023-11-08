from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        rating = request.form['rating']
        print(f"Ocena: {rating}")
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/sport")
def sport():
    return render_template("sport.html")

@app.route("/sport/narty")
def sport_narty():
    return render_template("sport_narty.html")
        
@app.route("/sport/boks")
def sport_boks():
    return render_template("sport_boks.html")
    
@app.route("/sport/siata")
def sport_siata():
    return render_template("sport_siata.html")

@app.route("/sport/zagle")
def sport_zagle():
    return render_template("sport_zagle.html")

if __name__ == "__main__":
    app.run(debug=True)