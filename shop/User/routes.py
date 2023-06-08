from flask import render_template, url_for, flash, redirect, request, Blueprint
from shop.forms import AddUserForm, SearchForm, SellForm
from shop import conn, bcrypt
from shop.models import insert_user, search_for_laptop, sell_laptop



User = Blueprint("User", __name__)


@User.route("/addUser", methods=['GET', 'POST'])
def addUser():
    form = AddUserForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        username = form.username.data
        insert_user(username, hashed_password)
        flash('Account has been created! The user is now able to log in', 'success')
        return redirect(url_for('Login.home'))
    else:
        return render_template('addUser.html', title='Add Customer', form=form)

@User.route("/search", methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        company = form.company.data
        product = form.product.data
        typename = form.typename.data
        inches = form.inches.data
        resolution = form.resolution.data
        cpu = form.cpu.data
        ram = form.ram.data
        memory = form.memory.data
        gpu = form.gpu.data
        opsys = form.opsys.data
        weight = form.weight.data
        price_euros = form.price_euros.data
        res = search_for_laptop(company, product, typename, inches, resolution, cpu, ram, memory, gpu, opsys, weight, price_euros)
        return render_template('search.html', title="Search", form=form, results=res)
    else:
        return render_template('search.html', title="Search", form=form, results=None)

@User.route("/sell", methods=['GET', 'POST'])
def sell():
    form = SellForm()
    if form.validate_on_submit():
        company = form.company.data
        product = form.product.data
        typename = form.typename.data
        inches = form.inches.data
        resolution = form.resolution.data
        cpu = form.cpu.data
        ram = form.ram.data
        memory = form.memory.data
        gpu = form.gpu.data
        opsys = form.opsys.data
        weight = form.weight.data
        price_euros = form.price_euros.data
        sell_laptop(company, product, typename, inches, resolution, cpu, ram, memory, gpu, opsys, weight, price_euros)
        flash('Laptop has been listed for sale!', 'success')
        return redirect(url_for('Login.home'))
    else:
        return render_template('sellLaptop.html', title="Sell", form=form)