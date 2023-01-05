from flask import Flask, render_template
app = Flask(__name__)

# add as many pages as you need
# You can add other things here as well

@app.route("/")
def index():
    return render_template("index.html.j2", title="your-title - Home", add_css=False)

@app.route("/about")
def about():
    return render_template("about.html.j2", title="your-title - About", add_css=False)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
