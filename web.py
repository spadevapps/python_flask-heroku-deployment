from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('HomepageTemplate/index.html')

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
