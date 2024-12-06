from flask import Flask,render_template
app=Flask(__name__)

posts=[{
    'author':'chetan Bhagat',
    'title':'Two States',
    'content':'Love Story',
    'date_posted':'4th Dec 2024'
},
{
    'author':'Abhilash Bhagat',
    'title':'four States',
    'content':'crime Story',
    'date_posted':'4th Sep 2024'
}]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",posts=posts)


@app.route("/about")
def about():
   return render_template("about.html",titile='About')


if (__name__)=='__main__':
    app.run(debug=True)