from flask import render_template, url_for, flash, redirect, request, Blueprint
from shop.forms import AddUserForm, SearchForm, SellForm, EditForm
from shop import conn, bcrypt, sessionDetails
from shop.models import insert_user, search_for_laptop, sell_laptop, get_laptops_from_user, get_user_from_lid, get_laptop_from_id, update_laptop, add_to_cart
from flask_login import current_user, login_required
from werkzeug.datastructures import MultiDict



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
        return render_template('search.html', title="Search", form=form, results=res, current_user = sessionDetails["id"])
    else:
        return render_template('search.html', title="Search", form=form, results=None, current_user = sessionDetails["id"])

@User.route("/sell", methods=['GET', 'POST'])
@login_required
def sell():
    print(f"CURRENT USER:{current_user}")
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
        sell_laptop(company, product, typename, inches, resolution, cpu, ram, memory, gpu, opsys, weight, price_euros, current_user)
        flash('Laptop has been listed for sale!', 'success')
        return redirect(url_for('Login.home'))
    else:
        return render_template('sellLaptop.html', title="Sell", form=form)
    
@User.route("/profil", methods=['GET', 'POST'])
def profil():
    res = get_laptops_from_user(current_user)
    print(res)
    return render_template('profil.html', title="Profil", res = res)

@User.route("/<l_id>/edit", methods=['GET', 'POST'])
def edit(l_id):
    userN = get_user_from_lid(l_id)
    if current_user[1] != userN:
        return redirect(url_for('Login.home'))
    else:
        posting = get_laptop_from_id(l_id)
        form = EditForm()
        if form.validate():
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
            update_laptop(l_id, company, product, typename, inches, resolution, cpu, ram, memory, gpu, opsys, weight, price_euros)
            return redirect(url_for('User.profil'))
        else:
            return render_template('edit.html', title="Edit", posting = posting, form = form)

@User.route("/<l_id>/addcart")
def addcart(l_id):
    u_id = current_user[0]
    add_to_cart(u_id, l_id)
    return redirect(url_for('User.search'))

