from flask import Flask, render_template, url_for, redirect, request
from forms import FormLogin

app = Flask(__name__)
app.config["SECRET_KEY"] = "ba7783e47efacd4b8c6b40475222bbac"


@app.route("/", methods=["GET", "POST"])
def index():
    form = FormLogin()

    if form.validate_on_submit():
        return redirect(url_for('index'))
        
    was_submitted = request.method == 'POST' 
    return render_template('index.html', form = form, was_submitted=was_submitted)


if __name__ == "__main__":
    app.run(debug=True)