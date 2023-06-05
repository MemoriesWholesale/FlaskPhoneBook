from app import app, db
from flask import render_template,redirect,url_for,flash
from flask_login import login_user, logout_user, login_required, current_user
from app.forms import ContactForm,SignupForm,LoginForm,EditForm
from app.models import Contact,User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/addcontact',methods=["GET","Post"])
@login_required
def addcontact():
    form = ContactForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        phone = form.phone.data
        address = form.address.data
        email = form.email.data
        print(first_name,last_name,phone,*address)
        try:
            print(float(phone))
        except:
            flash('Phone entries must be numbers')
            return redirect(url_for('index'))
        new_contact = Contact(first_name=first_name,last_name=last_name,phone=phone,address=address)
        db.session.add(new_contact)
        db.session.commit()
        flash(f'{first_name} {last_name} has been added to your little black book','danger-subtle')
        return redirect(url_for('index'))
    return render_template('addcontact.html',form=form)

@app.route('/signup',methods=['GET','Post'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        username = form.username.data
        address = form.address.data
        email = form.email.data
        phone = form.phone.data
        password = form.password.data
        checkusername = db.session.execute(db.select(User).where((User.username==username))).scalars().all()
        if checkusername:
            flash(f'Username {username} is taken! Please choose another.','warning')
            return redirect(url_for('signup'))
        new_user = User(first_name=first_name,last_name=last_name,username=username,address=address,email=email,phone=phone,password=password)
        db.session.add(new_user)
        db.session.commit()
        flash(f'You have signed up as {username}!','danger')
        return redirect(url_for('index'))
    return render_template('signup.html',form=form)


@app.route('/login',methods=['GET','Post'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = db.session.execute(db.select(User).where(User.username==username)).scalars().one_or_none()
        if user is not None and user.check_password(password):
            login_user(user)
            flash(f'Logged in as {username}','danger')
            return redirect(url_for('index'))
        elif user is None:
            flash(f'Username {username} not found')
            return redirect(url_for('login'))
        else:
            flash('Incorrect password')
            return redirect(url_for('login'))
    return render_template('login.html',form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You are logged out.')
    return redirect(url_for('index'))

@app.route('/viewcontacts',methods=['GET','Post'])
@login_required
def viewcontacts():
    contacts = db.session.execute(db.select(Contact).where(Contact.user==current_user.id)).scalars().all()
    return render_template('viewcontacts.html',contacts=contacts)

@app.route('/editcontact',methods=['GET','Post'])
@login_required
def editcontact():
    form = EditForm()
    return render_template('editcontact.html',form=form)


@app.route('/deletecontact',methods=['GET','Post'])
@login_required
def deletecontact():
    flash('Contact deleted')
    return redirect(url_for('index'))


@app.route('/profile',methods=['GET','Post'])
@login_required
def viewprofile():
    return render_template('profile.html')

@app.route('/search',methods=['GET','Post'])
@login_required
def search():
    return render_template('search.html')

