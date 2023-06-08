from flask import render_template, url_for, flash, redirect, request, Blueprint
from shop.forms import LoginForm
from shop import bcrypt, login_manager, sessionDetails
from flask_login import login_user, current_user, logout_user, login_required
from shop.models import select_user


Login = Blueprint('Login', __name__)


@Login.route("/")
@Login.route("/home")
def home():
    print(f"CURRENT_USER: {type(current_user)}\n{current_user}")
    print(f"SessionDetails: {sessionDetails}")
    if sessionDetails["username"] != None:
        username = sessionDetails["username"]
    else:
        username = "Guest"
    return render_template('index_hex.html', username=username)


@Login.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(f"USERNAME?????  {form.username.data}")
        user = select_user(form.username.data)
        print(f"USER2: {user[2]}")
        print(form.password.data)
        if user != None and bcrypt.check_password_hash(user[2], form.password.data):
            print("Logged in")
            login_user(user, remember=form.remember.data)
            flash('Login successful.','success')
            sessionDetails["username"] = user[1]
            sessionDetails["id"] = user[0]
            next_page = request.args.get('next')
            if next_page != None:
                return redirect(next_page)
            else:
                return redirect(url_for('Login.home'))
    else:
        flash('Login Unsuccessful. Please check identifier and password', 'danger')
    
    return render_template('login.html', title='Login', form=form)


