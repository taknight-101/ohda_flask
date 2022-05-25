from models.user import User
from wtforms.fields.html5 import DateField
from flask_wtf import Form
from models.reg_route import RegRoute

from devs.routes import *
from flaskext.mysql import MySQL
from models.reg_route import RegRoute
from flask import Flask, request, render_template, url_for, session, redirect, flash, send_from_directory
from datetime import datetime
from utils.db import DB
# from utils.reflection import Reflection


import os
from werkzeug.utils import secure_filename
from werkzeug import url_encode, url_decode


# login feature

from werkzeug import generate_password_hash, check_password_hash

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Length, Email, DataRequired, EqualTo
from flask_wtf.file import FileField, FileAllowed


class RegisterForm(FlaskForm):

    # name = StringField('Full name', validators=[InputRequired('This field is required'), Length(max=100, message='The max size 100 char')])
    username = StringField('Username', validators=[InputRequired(
        'This field is required'), Length(max=30, message='The max size 30 char')])
    # email = StringField('Email', validators=[DataRequired('This field is required'), Email("This field requires a valid email address")])
    password = PasswordField('Password', validators=[
                             InputRequired('This field is required')])
    # confirm_password = PasswordField('Confirm_Password', validators=[InputRequired('This field is required'), EqualTo('password')])
    # student_mobile = StringField('Mobile', validators=[InputRequired('This field is required'), Length(max=11)])
    # school = StringField('School', validators=[InputRequired('This field is required'), Length(min=2, max=140)])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):

    # email = StringField('Email', validators=[DataRequired('This field is required'), Email("This field requires a valid email address")])
    username = StringField('Username', validators=[DataRequired(
        'This field is required'), InputRequired("This field is required")])
    password = PasswordField('Password', validators=[
                             InputRequired('This field is required')])
    # remeber = BooleanField('Remember Me')
    submit = SubmitField('login')


#
app = Flask(__name__)
UPLOAD_FOLDER = os.path.abspath('.') + "\\uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# file uploads feature

# print(os.path.abspath('.') + '\uploads')
# exit
# UPLOAD_FOLDER = 'C:\Users\STC\Desktop\ohda#2\uploads'
# print(UPLOAD_FOLDER)
# exit
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_file', name=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


@app.route('/uploads/<name>')
def download_file(name):
    # name = name.replace(',' ,'/')
    name = name.split(',')
    # print("WORKED!" , name)
    import urllib

    # unicode_str = name.decode("gbk")
    # utf8_str = name.encode("utf-8")
    # you_want = urllib.parse.quote(utf8_str)
    # print(os.path.join( app.config["UPLOAD_FOLDER"], name[0] ,  name[1]) , name[2])

    return send_from_directory(os.path.join(app.config["UPLOAD_FOLDER"], name[0],  name[1]), name[2],  as_attachment=True)


# login feature
app.config['SECRET_KEY'] = 'sdlvabvpureavnrjeaverjvnvnvnvoenrvoervno'
#


mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'flask_ohda'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

DB.conn = mysql.connect()


# date FIELD HEH...


class ExampleForm(Form):
    dt = DateField('DatePicker', format='%Y-%m-%d')


@app.route('/dateField', methods=['POST', 'GET'])
def hello_world():
    form = ExampleForm()
    if form.validate_on_submit():
        return form.dt.data.strftime('%Y-%m-%d')
    return render_template('devs/example.html', form=form)

##


# security feature


# login feature


@app.route('/logout', methods=['GET'])
def logout():
    for key in list(session.keys()):
        session.pop(key)
    # session = None
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data

        user = DB.select('user', where=f'username = "{username}"')
        # print(user)

        if not user:
            return render_template('login.html', form=form, message='username or password went wrong!!')

        user = user[0]
        if check_password_hash(user['password'], form.password.data):

            session['user'] = user
            session['userID'] = user['id']
            session['role'] = user['role']
            session['store_ids'] = user['auth_storeID_list']

            return redirect(url_for('root'))

        return render_template('login.html', form=form, message='username or password went wrong!!')

    return render_template('login.html', form=form)


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    # print("inspecting the session" , session)
    if 'user' not in session.keys():
        return redirect(url_for('login'))

    current_username = session['user']['username']
    usernameExists = DB.select('user', where=f'username ="{current_username}"')
    if usernameExists:
        exist_username = usernameExists[0]['username']

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if usernameExists:
            edit_user = {"username": username,
                         "password": generate_password_hash(password)}
            DB.update('user', edit_user, f'username = "{exist_username}"')

            session['user'] = edit_user
            session['userID'] = usernameExists[0]['id']
            session['role'] = usernameExists[0]['role']
            return redirect(url_for('root'))

        else:
            return "are you a hacker?"

    return render_template('profile.html', username=exist_username)


@app.route('/404', methods=['GET'])
def page_404():
    return render_template('devs/404.html')


# @app.route('/signup', methods=["GET", "POST"])
# def signup():
#     form = RegisterForm()
#     if request.method == "POST":
#         print(form.validate_on_submit())
#         if form.validate_on_submit():

#             username = form.username.data
#             usernameExists = DB.select('user' , where = f'username ="{username}"')
#             if usernameExists :
#                  return render_template('login.html', form=form, message='username exists')
#             new_user = User(form.username.data,
#                                generate_password_hash(form.password.data)).json()
#             DB.insert('user', [new_user] )

#             session['user'] = new_user
#             # session['userID'] = new_user['id']

#             # login_user(new_user)

#         return redirect(url_for('index/4'))
#     return render_template('signup.html', form=form)

#

#  ahmed :: i think i don't need this now !! END

# print("sighhhhhhhh" , app.url_map)
# print("sighhhhhhhh" , dir(app.url_map))
# print("sighhhhhhhh" , dir(app.url_map))
# print("sighhhhhhhh" , app.url_map)
# for rule in app.url_map.iter_rules():
#     print("this is type of rule", type(rule))
#     app.url_map.pop("dfg")
#     # Filter out rules we can't navigate to in a browser
#     # and rules that require parameters
#     if "GET" in rule.methods :
#         pass
#         # print(rule.endpoint)
#         # print(dir(rule.empty()))

# print("__________________")
# print("sighhhhhhhh" , app.url_map)


# @app.route('/<test>')
# def test(test):
#     print(test)


@app.route('/')
def ind():
    return redirect('login')


@app.route('/index/<store_id>', methods=['POST', 'GET'])
def index(store_id, toggle=False):
    # print(session)

    if 'user' not in session.keys():
        return redirect(url_for('login'))
    # if request.method == 'POST' :
    #     print("SIGHHHH")
    #     return render_template('devs/index.html' )

    # print(session['role'] ,session['store_ids'] )
    stub = session['store_ids']
    # stub = "['11' ,'2']"

    stubs = []
    for i in stub.split('\''):
        # print('[' not in i)
        if '[' not in i and ']' not in i and ',' not in i:
            stubs.append(i)
    # print(stubs[0])
    # print( [ i for i in stub.split('\'') if  isinstance(int(i), int)] )
    # print(stub.split('\''))
    # print(store_id,session['store_ids'] ,store_id not in [int(i) for i in session['store_ids']] )
    if ('role' not in session or (session['role'] != 0 and store_id not in stubs)):
        return redirect(url_for('page_404'))

    # print(session['user'])
    # username = session['user']['username']
    role = session['role']
    # userID = DB.select('user' , cols=['id' ,'role' ] ,where=f'role ="{role}"')[0]['id']

    store = DB.select('stores', where=f'id = {store_id}')
    if len(store) == 0:
        return redirect(url_for('page_404'))

    store = store[0]
    # print("YO FOR REAL " , userID)
    # userID = session['userID']
    types = DB.select('types', cols=['id', 'type', 'cls', 'icon', 'action_method', 'add_actions',
                      'code', 'import_num', 'source', 'notes'], where=f'store_id = {store_id} ')

    # new STORE
    if not types:
        render_template('devs/index.html', store=store, role=role)

    registered_routes = DB.select('registered_routes', cols=[
                                  'action_method', 'add_actions'], where=f'store_id = {store_id} ')

    # print(types)
    ids = [i['id'] for i in types]
    types_en = [i['type'].split(',')[0] for i in types]
    types_ara = [i['type'].split(',')[1] for i in types]
    classes = [i['cls'] for i in types]
    icons = [i['icon'] for i in types]
    action_methods = [i['action_method'] for i in types]

    add_actions = [i['add_actions'] for i in types]
    code = [i['code'] for i in types]
    import_num = [i['import_num'] for i in types]
    source = [i['source'] for i in types]
    notes = [i['notes'] for i in types]

    reg_action_methods = [i['action_method'] for i in registered_routes]
    # reg_add_actions =  [ i['add_actions'] for i in registered_routes]

    # print(types , types_en , types_ara)

    # reflection code

    # show_routes = DB.select('types' , cols =['action_method'])
    # print(show_routes)
    action_methods_new = [
        action_method for action_method in action_methods if action_method not in reg_action_methods]
    # print("newwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww" , action_methods_new)
    Reflection(action_methods_new, [store_id], store['name'])

    if len(action_methods_new) > 0:

        # print([RegRoute(i).json() for i in action_methods_new])
        DB.insert('registered_routes', [RegRoute(
            i, store_id).json() for i in action_methods_new])

    statues = {}
    for type in action_methods:
        statues[type] = {}
        # print("yoooooooooo" , type)
        statues[type]["masrof"] = DB.select(
            'devs', cols=['count(*) as c'], where=f'type_id ="{type}"')[0]['c']
        # my selected "id => device_type" mapping :-
        # <option value="1" > يعمل وبالعهده  </option>
        # <option value="2" > يعمل وبالمخزن   </option>
        # <option value="3" > لا يعمل وبالمخزن </option>
        # <option value="4" > لا يعمل وبالورشه </option>
        statues[type]["works_ohda"] = DB.select(
            'devs', cols=['count(*) as c'], where=f'status = 1 AND type_id ="{type}"')[0]['c']
        statues[type]["works_maghzan"] = DB.select(
            'devs', cols=['count(*) as c'], where=f'status = 2 AND type_id ="{type}"')[0]['c']
        statues[type]["not_works_maghzan"] = DB.select(
            'devs', cols=['count(*) as c'], where=f'status = 3 AND type_id ="{type}"')[0]['c']
        statues[type]["not_works_warsha"] = DB.select(
            'devs', cols=['count(*) as c'], where=f'status = 4 AND type_id ="{type}"')[0]['c']
        # statues[type]["works_ohda_maghzan"] =DB.select('devs' , cols=['count(*) as c'] , where=f'status = 1 AND type_id ="{type}"')[0]['c']
        # statues[type]["not_works_maghzan_warsha"] =DB.select('devs' , cols=['count(*) as c'] , where=f'status = 2 AND type_id ="{type}"')[0]['c']
        # statues[type]["prepare"] =DB.select('devs' , cols=['count(*) as c'] , where=f'status = 3 AND type_id ="{type}"')[0]['c']
        # DB.select('devs' , cols=['count(*) as c'] , where=f'status = 3 AND type_id ="{type}"')[0]['c']
        statues[type]["baky"] = statues[type]["masrof"] - \
            statues[type]["works_ohda"]

    # print("ALLAH" , statues)
    # total =  DB.select('devs' , cols=['count(*) as c'])[0]['c']
    # works =  DB.select('devs' , cols=['count(*) as c'],where='status = 1')[0]['c']

    # not_works =  DB.select('devs' , cols=['count(*) as c'],where='status = 2')[0]['c']
    # prepare = total - ( works + not_works)

    # print(total , "for realllllllllll")

    toggle = True if request.args.get('toggle') and request.args.get('toggle')[
        0] == 'T' else False
    # print( request.args.get('toggle') )

    if not toggle:
        return render_template('devs/index.html', toggle=toggle, role=role, types_en=types_en, types_ara=types_ara, classes=classes, icons=icons, action_methods=action_methods, add_actions=add_actions, statues=statues, ids=ids, code=code, import_num=import_num, source=source, notes=notes, store=store)
    return render_template('devs/indexToggle.html', toggle=toggle, role=role, types_en=types_en, types_ara=types_ara, classes=classes, icons=icons, action_methods=action_methods, add_actions=add_actions, statues=statues, ids=ids, code=code, import_num=import_num, source=source, notes=notes, store=store)


@app.route('/profile/<path:whatever>')
def error2(whatever):
    return redirect(url_for('page_404'))


@app.route('/root/<path:whatever>')
def error1(whatever):
    return redirect(url_for('page_404'))


@app.route('/root/', methods=['GET', 'POST'])
def root():
    # print(session)
    if 'user' not in session.keys():
        return redirect(url_for('login'))

    # print("HAY" , request.path.split('/'))
    # if len(request.path.split('/')) > 3 or request.path.split('/')[-1] :

    ##
    if request.method == 'POST':

        # role col enum meaning ::  admin = 0  , officer_ohda = 1 , amin_ohda = 2

        # return request.form

        # print(authorized_stores_officer , authorized_stores_amin)

        # print("user" , session["userID"])
        officer_username = request.form['officer_username']
        officer_password = request.form['officer_password']
        authorized_stores_officer = request.form.getlist('store_ohda_officer')

        amin_officer_username = request.form['amin_officer_username']
        # print("HELLOW!!")
        amin_officer_password = request.form['amin_officer_password']
        authorized_stores_amin = request.form.getlist('store_ohda_amin')

        if request.form['ohda_officer_exists'] and request.form['ohda_amin_exists']:
            cursor = DB.update('user', User(officer_username,  generate_password_hash(
                officer_password), 1, str(authorized_stores_officer)).json(), 'role = 1')
            cursor = DB.update('user', User(amin_officer_username, generate_password_hash(
                amin_officer_password), 2, str(authorized_stores_amin)).json(), 'role = 2')
            session['officer_username'] = officer_username
            session['amin_officer_username'] = amin_officer_username
            return redirect(url_for('root'))

        # cursor = DB.update('user' , {"auth_storeID_list" : authorized_stores } ,where = 'id = ' +  str(session["userID"]))
        cursor = DB.insert('user', [User(officer_username,  generate_password_hash(officer_password), 1, str(authorized_stores_officer)).json(
        ), User(amin_officer_username, generate_password_hash(amin_officer_password), 2, str(authorized_stores_amin)).json()])
        return redirect(url_for('root'))

    else:
        userID = session['userID']

        # return redirect(url_for('index'))
        # starting to add support for stores
        # print(DB.select('user', cols=['role' , 'auth_storeID_list'] , where=f'id = "{userID}"'))
        user_id = DB.select(
            'user', cols=['role', 'auth_storeID_list'], where=f'id = "{userID}"')[0]
        stores_id = user_id['auth_storeID_list']
        role = user_id['role']
        if role != 0:
            # print(stores_id)
            stores_id_int = ''
            for ind, num in enumerate(stores_id[1:-1]):
                # print(len(stores_id[1:-1]))
                # print(ind, stores_id[1:-1][ind])
                if num == '\'' or num == ' ':
                    continue
                stores_id_int += num

            stores_id = stores_id_int.split(',')
            if len(stores_id[0]) != 0:
                # print(stores_id, len(stores_id))
                stores_id = [int(i) for i in stores_id]

                stores_id = tuple(stores_id)
                if len(stores_id) == 1:
                    stores_id = str(stores_id)[:-2] + ')'

                stores = DB.select('stores', where=f' id IN {stores_id}')
                return render_template('devs/root.html', stores=stores, role=role)
            else:
                return render_template('devs/root.html', stores=[], role=role)

        stores = DB.select('stores')
        return render_template('devs/root.html', stores=stores, role=role)

    ##
    # print(session['user'])
    username = session['user']['username']
    userID = DB.select('user', cols=['id'],
                       where=f'username ="{username}"')[0]['id']
    # print("YO FOR REAL " , userID)
    # userID = session['userID']
    stores = DB.select('stores', cols=['id', 'name'])

    return render_template('devs/root.html', stores=stores)


# yo yo yo

def seed():

    from faker import Faker

    faker = Faker()


# GLOBAL SEED FLAG
# SEED = True
SEED = False

if __name__ == "__main__":
    # if SEED :
    #     seed()

    #  ahmed :: i think i don't need this now !!
    # BOOOT THE APP ROUTES
    show_routes = DB.select('types', cols=['action_method', 'store_id'])
    # print(show_routes)
    show = [i['action_method'] for i in show_routes]
    store_ids = [i['store_id'] for i in show_routes]
    # print(show, store_ids)
    # exit()

    Reflection(show, store_ids)
    app.run(host='localhost', port=3002)
    # app.run(port =3001)
