from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/welcome")
def welcome():
    return render_template('welcome.html')

@app.route("/news")
def news():
    return render_template('news.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/products")
def products():
    return render_template('products.html')

@app.route("/gallery")
def gallery():
    return render_template('gallery.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/feedback")
def feedback():
    return render_template('feedback.html')

if __name__ == '__main__':
    app.run(debug=True)