from flask import Flask, render_template, url_for
# http://localhost:5000/
# http://localhost:5000/about

app = Flask(__name__)

posts = [
    {
        'author': 'S Smith',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': '8Jan2021'

    },
    {
        'author': 'I Smith',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': '8Jan2021'

    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == "__main__":
    app.run(debug=True)
