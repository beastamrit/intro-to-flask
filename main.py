from flask import Flask , render_template,request
from datetime import datetime
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/calculate", methods=["POST"])
def calculate_age():
    try:
        birth_year = int(request.form.get("birth_year"))
        current_year = datetime.now().year
        if birth_year > current_year or birth_year < 1990:
            return render_template("index.html",error="Please enter a valid year")
        age = current_year - birth_year
        return render_template("index.html",age=age)
    except ValueError:
        render_template("index.html",error="plz enter no.")
if __name__=="__main__":
    app.run(debug=True)