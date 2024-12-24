from flask import Flask,render_template,url_for
from forms import RegistrationForm,LoginForm
app=Flask(__name__)
app.config['SECRET_KEY']='ca874ee4eb013eda02ac5f8c687dd702'

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

@app.route("/register")
def register():
   form=RegistrationForm()
   return render_template("register.html",title='Register',form=form)

@app.route("/login")
def login():
   form=LoginForm()
   return render_template("login.html",title='Login',form=form)
 
if (__name__)=='__main__':
    app.run(debug=True)