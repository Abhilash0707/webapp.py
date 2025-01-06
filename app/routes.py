from flask import render_template,url_for,flash,redirect
from app import app
from app.forms import RegistrationForm,LoginForm
from app.models import User ,Post



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

@app.route("/register",methods=['GET','POST'])
def register():
   form=RegistrationForm()
   if form.validate_on_submit():
      flash(f'Account created for {form.username.data}!','success')
      return redirect(url_for('home'))
   return render_template("register.html",title='Register',form=form)

@app.route("/login",methods=['GET','POST'])
def login():
   form=LoginForm()
   if form.validate_on_submit():
      if form.email.data=='admin@blog.com' and form.password.data=='password':
         flash('You have been logged in!','success')
         return redirect(url_for('home'))
      else:
         flash('Login Unsuccessful. Please check username and password.','danger') 
   return render_template("login.html",title='Login',form=form)