from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    hasil_input = None
    if request.method == "POST":
        hasil_input = request.form.get("teks_input", "").strip()
    return render_template("index.html", hasil=hasil_input)


if __name__ == "__main__":
    app.run(debug=True)