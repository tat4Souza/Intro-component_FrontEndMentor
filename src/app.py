from flask import Flask, render_template, url_for, redirect, flash
from forms import FormLogin

app = Flask(__name__)
app.config["SECRET_KEY"] = "ba7783e47efacd4b8c6b40475222bbac"


@app.route("/", methods=["GET", "POST"])
def index():
    form = FormLogin()

    if form.validate_on_submit():
        return redirect(url_for('index'))
        

    return render_template('index.html', form = form)


if __name__ == "__main__":
    app.run(debug=True)