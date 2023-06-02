from app import app, db
from flask import render_template,redirect,url_for,flash
from app.forms import ContactForm
from app.models import Contact

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/addcontact',methods=["GET","Post"])
def addcontact():
    form = ContactForm()
    if form.validate_on_submit():
        print('Success!')
        first_name = form.first_name.data
        last_name = form.last_name.data
        phone = form.phone.data
        address = form.address.data
        print(first_name,last_name,phone,*address)
        try:
            print(float(phone))
        except:
            flash('Phone entries must be numbers')
            return redirect(url_for('index'))
        contact_check = db.session.execute(db.select(Contact).where(Contact.phone==phone)).scalars().all()
        if contact_check:
            flash('A contact with that phone number already exists!','warning')
            return redirect(url_for('index'))
        new_contact = Contact(first_name=first_name,last_name=last_name,phone=phone,address=address)
        db.session.add(new_contact)
        db.session.commit()
        flash(f'{first_name} {last_name} has been added to your little black book','success-subtle')
        return redirect(url_for('index'))
    return render_template('addcontact.html',form=form)