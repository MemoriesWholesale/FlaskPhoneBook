from app import app
from flask import render_template,redirect,url_for,flash
from app.forms import Contact

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/addcontact',methods=["GET","Post"])
def addcontact():
    form = Contact()
    if form.validate_on_submit():
        print('Success!')
        first_name = form.first_name.data
        last_name = form.last_name.data
        phone = form.phone.data
        address = form.address.data
        print(first_name,last_name,phone,*address)
        flash(f'{first_name} {last_name} has been added to your little black book','success-subtle')
        return redirect(url_for('index'))
    return render_template('addcontact.html',form=form)