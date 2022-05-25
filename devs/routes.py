
from app import app, os
from wtforms.fields.html5 import DateField
from flask_wtf import Form
from flask import Flask, request, render_template, url_for, redirect, session, flash, send_from_directory

from utils.db import DB
# from utils.reflection import Reflection
from werkzeug.utils import secure_filename
from models.device import Device
from models.type import Type
from models.user import User
from models.DevHistory import DevHistory
from textwrap import dedent
import string
import random
from werkzeug import generate_password_hash


import json


def robust_s_remove(text):
    text = text[::-1]
    ind = 0
    for index, i in enumerate(text):

        if i == 's' and index == 0:
            ind = index

        elif i == 's' and (index - ind) == 1:
            ind = index

        elif i != 's' and index == 0:

            text = text[::-1]
            return text

    # print("hi" , ind)
    ind = len(text) - 1 - ind
    text = text[::-1]
    # print(text[:ind])
    return text[:ind]


# file upload feature
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


class ExampleForm(Form):
    dt = DateField('DatePicker', format='%Y-%m-%d')

# @app.route('/dateField', methods=['POST','GET'])
# def hello_world():
#     form = ExampleForm()
#     if form.validate_on_submit():
#         return form.dt.data.strftime('%Y-%m-%d')
#     return render_template('devs/example.html', form=form)


class Reflection:
    name_ens = None

    def __init__(self, name_ens, store_ids, store_name=None) -> None:
        self.name_ens = name_ens
        self.store_ids = store_ids
        self.store_name = store_name
        # print(name_ens , "YO")
        for ind, name_en in enumerate(name_ens):
            # if  name_en.endswith('s') :
            #     name_en = name_en[:len(name_en)-1]
            name_en = robust_s_remove(name_en)

            randomString = ''.join(random.choices(
                string.ascii_uppercase + string.digits, k=5))
            show_callback = f'''

                        is_registered = len(DB.select('routes_in_code' , where ='routeName = "{name_en}s" '))
                        # print(is_registered, '"YOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO {name_en}"' )
                        
                        if not is_registered :
                            @app.route('/{name_en}s' , methods=['GET' , 'POST'])
                            def {name_en}s():
                                {name_en}s = DB.select('devs' ,  where ='store_id = {store_ids[ind]} and type_id = "{name_en}s" ')

                                #to get the latest place from the list of places from history ...
                                ## i will select all then group by type_id then order desc and the first one is the latest one :)
                                # didn't find a way to do it in sql so i will do it in python :)
                                # current_places =  DB.select('dev_history' , where = '1=1 group by dev_id order by id DESC ' )
                                all_places =  DB.select('dev_history' , where = '1=1 order by id ASC')
                                # distinct_device_ids =  DB.select('dev_history' ,distinct = dev_id )
                                # ownership_ids =  DB.select('dev_history' ,cols =['id'] )
                                latest_places =dict()
                                for record in all_places :
                                    latest_places[record['dev_id']] = [record['id'],record['owner']]

                                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",latest_places)
                                # print("hahaha" , latest_places)
                                # print({name_en}s)

                                # NOW , updating the place per device to the latest place and thus we achieve complete 2-way binding
                                for index , device in enumerate({name_en}s) :
                                    if device['id'] in list(latest_places.keys()) :
                                        {name_en}s[index]['place'] = latest_places[device['id']][1]

                                #print({name_en}s)

                                #finally : i need to update the original place col in the dev table
                                # print(latest_places, list(latest_places.keys()))
                                for index , device_id in enumerate(list(latest_places.keys())) :
                                    #print(index ,device_id )

                                    cursor = DB.update('devs' , {{"place" : latest_places[device_id][1] }} , where = 'store_id = {store_ids[ind]} and '+ 'id = ' +  str(device_id))
                                    # print(request.form['place'])

                                # print({name_en}s)
                                # for ind, device in enumerate({name_en}s) :
                                #     if {name_en}s[ind]['permit_requester'] :
                                #         print("hi" ,ind ,  {name_en}s[ind]['permit_requester'] + app.config["UPLOAD_FOLDER"]) #
                                #         print(send_from_directory)
                                #         print(send_from_directory(app.config["UPLOAD_FOLDER"], {name_en}s[ind]['permit_requester'] , as_attachment=True))
                                #         {name_en}s[ind]['permit_requester'] = send_from_directory(app.config["UPLOAD_FOLDER"], {name_en}s[ind]['permit_requester'])
                                #         {name_en}s[ind]['permit_request'] = send_from_directory(app.config["UPLOAD_FOLDER"], {name_en}s[ind]['permit_request'] )
                                #         {name_en}s[ind]['file_193'] = send_from_directory(app.config["UPLOAD_FOLDER"], {name_en}s[ind]['file_193'] )

                                #print({name_en}s)
                                userID = session['user']['id']
                                store_name = DB.select('stores' , cols = ['name'] , where = 'id = {store_ids[ind]}')[0]['name']

                                return render_template('devs/show_all.html' , type ='{name_en}s' ,data={name_en}s ,userID=userID ,latest_places=latest_places ,store_name=store_name)
                        else:
                            print("~~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            userID = session['user']['id']

                            {name_en}s = DB.select('devs' ,  where ='store_id = {store_ids[ind]} and type_id = "{name_en}s" ')

                            #to get the latest place from the list of places from history ...
                            ## i will select all then group by type_id then order desc and the first one is the latest one :)
                            # current_places =  DB.select('dev_history' ,  'group by type_id order by id DESC ' )
                            # print(current_places)

                            store_name = DB.select('stores' , cols = ['name'] , where = 'id = {store_ids[ind]}')[0]['name']

                            render_template('devs/show_all.html' , type ='{name_en}s' ,data={name_en}s ,userID=userID , store_name=store_name)

                        '''

            add_callback = f'''
                            is_registered = len(DB.select('routes_in_code' , where ='routeName = "{name_en}s" '))
                            # print(is_registered, '"emmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm {name_en}"' )
                            if not is_registered :
                                @app.route(f'/add_{name_en}s' , methods=['GET' , 'POST'])
                                def add_{name_en}s():
                                    if request.method == 'POST' :


                                        submitted_names =  [file for file in request.files ]
                                        # print( [request.files[i].filename for i in submitted_names ] )
                                        filenames = [request.files[i].filename for i in submitted_names ]
                                        files = [request.files[i] for i in submitted_names ]

                                       # file_upload part
                                        for ind, file_name in enumerate(filenames) :
                                            # if 'file' not in submitted_names:
                                            #     flash('No file part')
                                            #     print("REALLLLY???????????????????????")
                                            #     return redirect(request.url)
                                            # file = request.files['file']
                                            # If the user does not select a file, the browser submits an
                                            # empty file without a filename.
                                            # if file_name == '':
                                            #     flash('No selected file')
                                            #     print("AGAIN???????????????????????")
                                            #     return redirect(request.url)
                                            if file_name and allowed_file(file_name):
                                                # print("before secure name ")
                                                # print(file_name)
                                                # filename = secure_filename(file_name)
                                                filename = file_name
                                                # print("after secure name ")
                                                # print(request.form['permit_num'])
                                                store_name = DB.select('stores' , cols = ['name'] , where = 'id = {store_ids[ind]}')[0]['name']
                                                # print("AHMED" , os.path.join(app.config['UPLOAD_FOLDER'], store_name , filename))

                                                cat_path = os.path.join(app.config['UPLOAD_FOLDER'], store_name)
                                                if not os.path.exists(cat_path) :
                                                    os.mkdir(cat_path)
                                                cat_path = os.path.join(app.config['UPLOAD_FOLDER'], store_name + '/' + '{name_en}s')
                                                if not os.path.exists(cat_path) :
                                                    os.mkdir(cat_path)

                                                files[ind].save(os.path.join(app.config['UPLOAD_FOLDER'], store_name , '{name_en}s' ,  filename))
                                                # return redirect(url_for('download_file', name= '/' + store_name +'/' + filename))

                                        name_to_filename_mapping = {{  name : request.files[name].filename for  name  in request.files }}
                                        #  if form.validate_on_submit():
                                        #     return form.dt.data.strftime('%Y-%m-%d')
                                        form = ExampleForm()
                                        cursor = DB.insert('devs' ,  [Device( {store_ids[ind]} , request.form['name'] ,  request.form['sn'] , request.form['place'] ,request.form['type_id'] ,request.form['status'],form.dt.data.strftime('%Y-%m-%d'),request.form['destination'],request.form['permit_num'],name_to_filename_mapping['permit_requester'],name_to_filename_mapping['permit_request'],name_to_filename_mapping['file_193']).json()])
                                        #cursor = DB.insert('devs' , [Device(request.form['name'] ,  request.form['sn'] , request.form['place'] ,request.form['type_id'] ,request.form['status'],request.form['date'],request.form['destination'],request.form['permit_num'],filenames[0] , filenames[1]  ,filenames[2]).json()])
                                        DB.insert('dev_history' , [DevHistory(request.form['place'] , cursor.lastrowid ).json()])
                                        return redirect(url_for('index', store_id = {store_ids[ind]}))

                                    else :
                                        form = ExampleForm()

                                        return render_template('devs/add_dev.html' , type ='{name_en}s' ,add_action ='add_{name_en}s' , form=form)
                            else :

                                @app.route('/add_{randomString}s' , methods=['GET' , 'POST'])
                                def add_{randomString}s():
                                    if request.method == 'POST' :
                                        cursor = DB.insert('devs' , [Device({store_ids[ind]} , request.form['name'] ,  request.form['sn'] , request.form['place'] ,request.form['type_id'] ,request.form['status']).json()])
                                        DB.insert('dev_history' , [DevHistory(request.form['place'] , cursor.lastrowid ).json()])
                                        return redirect(url_for('index', store_id = {store_ids[ind]}))


                            '''

            # print(show_callback ,add_callback)
            self.dispatch([show_callback, add_callback])

    @staticmethod
    def register():
        pass

    @staticmethod
    def dispatch_edit_delete():
        show_owners_callback = '''
                    @app.route('/show_owners/<id>' ,  methods=['GET' , 'POST'])
                    def show_owners(id):

                        # if request.method == 'POST' :

                        #     dev_route = request.form['type_id']
                        #     # print(request.form)
                        #     DB.insert('dev_history' , [{"dev_id" : id , "owner" : request.form['place']  }] )
                        #     return redirect(f'/{dev_route}')

                        # else :

                        dev_history = DB.select('dev_history',  where= f'dev_id = {id} order by id DESC ')

                        current_owner_id = None
                        if dev_history :
                            current_owner_id = dev_history[0]['id']



                        # print(dev_history , "OOOOOOOOO" )
                        # owners = [owner['owner'] for owner in dev_history]
                        # owners = [owner['owner'] for owner in dev_history]
                        # print(owners)

                        return render_template('devs/dev_history.html'  ,dev_history =dev_history ,current_owner_id=current_owner_id )

                    '''
        add_new_owner_callback = '''
                    @app.route('/add_new_owner/<id>' ,  methods=['GET' , 'POST'])
                    def add_new_owner(id):

                        if request.method == 'POST' :

                            dev_route = request.form['type_id']
                            # print(request.form)
                            DB.insert('dev_history' , [{"dev_id" : id , "owner" : request.form['place']  }] )
                            return redirect(f'/{dev_route}')

                        else :

                            dev = DB.select('devs',  where= f'id = {id}')[0]

                            return render_template('devs/add_new_owner.html' , dev = dev , type = dev['type_id'] )

                    '''
        edit_callback = '''
                    @app.route('/edit_dev/<id>,<store_id>' ,  methods=['GET' , 'POST'])
                    def edit_dev(id, store_id):
                        

                        if request.method == 'POST' :
                            print ("IN REFLECTION" ,  request.form['place'])

                            dev_route = request.form['type_id']

                            device = DB.select('devs' , where = f' store_id = {store_id} AND id = {id} ')[0]

                            device_inDB_files = {'permit_requester' : device['permit_requester'] ,'permit_request' : device['permit_request'] , 'file_193': device['file_193']}



                            # filenames = [request.files[i].filename for i in submitted_names ]


                            name_to_filename_mapping = {  name : request.files[name].filename for  name  in request.files }
                            rest = { key : val for key, val in device_inDB_files.items() if val not in list(name_to_filename_mapping.values()) }
                            # print(device_inDB_files , name_to_filename_mapping ,rest)

                            # error = device_inDB_files[10000]
                            keys =  list(name_to_filename_mapping.keys())
                            # print(keys, "KEYSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
                            # print(not name_to_filename_mapping['permit_requester']  , not name_to_filename_mapping['permit_request'] , not name_to_filename_mapping['file_193'])
                            # if not 'permit_requester' in keys  :
                            if not name_to_filename_mapping['permit_requester'] :
                                # print("got here")
                                # print(device_inDB_files)
                                name_to_filename_mapping['permit_requester'] = device_inDB_files['permit_requester']
                            # if not 'file_permit_request' in keys  :
                            if not name_to_filename_mapping['permit_request'] :
                                # print("got here")
                                name_to_filename_mapping['permit_request'] = device_inDB_files['permit_request']
                            # if not 'file_193' in keys  :
                            if not name_to_filename_mapping['file_193'] :
                                # print("got here")
                                name_to_filename_mapping['file_193'] = device_inDB_files['file_193']

                            #print("NEWWWWWWWWWWWWWWWWWWWWW" ,name_to_filename_mapping ,device_inDB_files )
                            #//ahmed
                            submitted_names =  [file for file in request.files ]
                            #print(submitted_names)
                            store_name = DB.select('stores' , cols = ['name'] , where = f'id = {store_id}')[0]['name']
                            files = [request.files[i] for i in submitted_names ]
                            for ind , name in enumerate(submitted_names) :
                                if name in rest.keys() :
                                   #print(session)
                                #    oooooooooo[100]
                                   files[ind].save(os.path.join(app.config['UPLOAD_FOLDER'], store_name , device['type_id'] ,  name_to_filename_mapping[name]))

                            # print("AHMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD" , request.form['place'] , id , store_id )
                            print ("IN REFLECTION" ,  request.form['place'])
                            cursor = DB.update('devs' ,  Device( store_id , request.form['name'] ,  request.form['sn'] , request.form['place'] ,request.form['type_id'] ,request.form['status'],request.form['date'],request.form['destination'],request.form['permit_num'],name_to_filename_mapping['permit_requester'],name_to_filename_mapping['permit_request'],name_to_filename_mapping['file_193']).json() , f'id = {id} ')
                            # print(Device( store_id , request.form['name'] ,  request.form['sn'] , request.form['place'] ,request.form['type_id'] ,request.form['status'],request.form['date'],request.form['destination'],request.form['permit_num'],name_to_filename_mapping['permit_requester'],name_to_filename_mapping['permit_request'],name_to_filename_mapping['file_193']).json())
                            # print(request.form['place'])
                            #print("HOPE" ,cursor.lastrowid )
                            max_id = DB.select('dev_history', cols = ["max(id) as m "] )[0]['m']
                            if not max_id :
                                max_id = 1
                                DB.insert('dev_history' , [DevHistory( request.form['place'] , {id} ).json() ] )

                            # return "hi"
                            #print(
                            else :
                                DB.update('dev_history' , DevHistory( request.form['place'] , {id} ).json() , f'dev_id = {id} AND id = {max_id} ')
                            # print("YO OG")
                            return redirect(f'/{dev_route}')

                        else :

                            dev = DB.select('devs',  where= f' store_id = {store_id} AND id = {id}')[0]

                            return render_template('devs/edit_dev.html' , dev = dev , type = dev['type_id'] , store_id = store_id )

                    '''
        edit_cat_callback = '''
                    @app.route('/edit_cat/<id>/<store_id>' ,  methods=['GET' , 'POST'])
                    def edit_cat(id,store_id):
                        

                        if request.method == 'POST' :

                            cat_id = request.form['type_id']
                            # print(request.form)
                            new_name =  request.form['name_en'] +"," + request.form['name']
                            # print(DB.update('types' , {"type": new_name} , f'id = {id} '))

                            no_change = DB.select('types' , ['cls'  , 'icon'  ,  'action_method'  , 'add_actions' ] , f'  store_id ={store_id} and  id = {id} ')[0]
                            # print('what is going on ' , no_change)
                            DB.update('types' , Type(new_name , cls = no_change['cls'] , icon = no_change['icon'] , action_method = no_change['action_method'] , add_actions =no_change['add_actions'] , code = request.form['code'] ,import_num =  request.form['import_num'] , source = request.form['source'] , notes = request.form['notes'] , store_id = store_id ).json() , f'id = {id} ')
                            return redirect(url_for('index' , store_id = store_id ))

                        else :

                            cat = DB.select('types',  where= f'id = {id}')[0]
                            # print(cat)
                            name = cat['type'].split(',')[1]
                            name_en = cat['type'].split(',')[0]
                            id = cat['id']
                            store_id = cat['store_id']

                            return render_template('devs/edit_cat.html' , name_en = name_en, name = name,id = id , code = cat['code'], import_num =cat['import_num'], source =cat['source'], notes =cat['notes'], store_id = store_id )

                    '''

        delete_callback = '''
                        @app.route('/del_dev/<type>/<id>')
                        def del_dev(type , id):

                            DB.delete('devs'  , f' id = {id} ')


                            return redirect(f'/{type}')

                        '''
        delete_cat_callback = '''
                        @app.route('/del_cat/<type>/<id>/<store_id>')
                        def del_cat(type ,id,store_id):

                            json = {"routeName" : type }
                            # print(jsons)
                            # print("omg" ,  f'{"routeName": "{type}" }')
                            #print(f'{"routeName": "{type}" }')
                            #exit
                            DB.insert('routes_in_code' , [ json ])
                            DB.delete('types'  , f'store_id = {store_id} and id = {id} ')

                            DB.delete('registered_routes'  , f'store_id = {store_id} and action_method = "{type}" ')
                            DB.delete('devs'  , f'store_id = {store_id} and type_id  = "{type}" ')

                            return redirect(url_for('index' , store_id = store_id ))

                        '''
        # print(delete_cat_callback)
        for cb in [edit_callback, delete_callback, edit_cat_callback, delete_cat_callback, add_new_owner_callback, show_owners_callback]:
            exec(dedent(cb))

    # @staticmethod
    def dispatch(self, cbs):
        # print(cb)
        # callbacks = [self.show_callback ,self.add_callback,self.edit_callback , self.delete_callback]
        # print(dedent(cb))
        # exec(dedent(cb))

        # callbacks = [self.show_callback ]
        for cb in cbs:
            exec(dedent(cb))
            # eval(callback)


Reflection.dispatch_edit_delete()  # only once

## not hereeee
# show_routes = DB.select('types' , cols =['action_method'])
# # print(show_routes)
# show = [i['action_method'] for i in show_routes ]
# # print(show)
# Reflection( show )


# bruh
# convention for showing :: device type in plural form  i.e. pcs
# @app.route('/pcs' , methods=['GET' , 'POST'])
# def pcs():


#     pcs = DB.select('devs' ,  where ='type_id = "pcs" ')

#     return render_template('devs/show_all.html' , type ='pcs' , data= pcs  )


# @app.route('/laptops' , methods=['GET' , 'POST'])
# def laptops():
#     laptops = DB.select('devs' ,  where ='type_id = "laptops" ')
#     print(laptops , 'for real')
#     return render_template('devs/show_all.html' , type ='laptops' ,data=laptops )


# @app.route('/monitors' , methods=['GET' , 'POST'])
# def monitors():
#     monitors = DB.select('devs' ,  where ='type_id = "monitors" ')
#     return render_template('devs/show_all.html' , type ='monitors' ,data=monitors )


# @app.route('/printers' , methods=['GET' , 'POST'])
# def printers():
#     printers = DB.select('devs' ,  where ='type_id = "printers" ')
#     return render_template('devs/show_all.html' , type ='printers' ,data=printers )

# bruh


# bruh

# convention for adding a device :: add_device type in plural form i.e. add_pcs
# how i will do it :: only 1 template and a hidden input field with the type as the name's attribute value
# @app.route('/add_pcs' , methods=['GET' , 'POST'])
# def add_pcs():

#     if request.method == 'POST' :

#         # return request.form
#         DB.insert('devs' , [Device(request.form['name'] ,  request.form['sn'] , request.form['place'] ,request.form['type_id'] ,request.form['status']).json()])
#         return redirect(url_for('index'))

#     else :

#         return render_template('devs/add_dev.html' , type ='pcs' ,add_action ='add_pcs' )

# @app.route('/add_laptops' , methods=['GET' , 'POST'])
# def add_laptops():
#     if request.method == 'POST' :

#         # return request.form
#         DB.insert('devs' , [Device(request.form['name'] ,  request.form['sn'] , request.form['place'] ,request.form['type_id'] ,request.form['status']).json()])
#         return redirect(url_for('index'))

#     else :
#         return render_template('devs/add_dev.html', type ='laptops' ,add_action ='add_laptops' )


# @app.route('/add_monitors' , methods=['GET' , 'POST'])
# def add_monitors():
#     if request.method == 'POST' :

#         # return request.form
#         DB.insert('devs' , [Device(request.form['name'] ,  request.form['sn'] , request.form['place'] ,request.form['type_id'] ,request.form['status']).json()])
#         return redirect(url_for('index'))

#     else :
#         return render_template('devs/add_dev.html' , type ='monitors' ,add_action ='add_monitors')

# @app.route('/add_printers' , methods=['GET' , 'POST'])
# def add_printers():
#     if request.method == 'POST' :

#         # return request.form
#         DB.insert('devs' , [Device(request.form['name'] ,  request.form['sn'] , request.form['place'] ,request.form['type_id'] ,request.form['status']).json()])
#         return redirect(url_for('index'))

#     else :
#          return render_template('devs/add_dev.html' , type ='printers' ,add_action ='add_printers' )


# bruh


# bruh

# @app.route('/edit_dev/<id>' ,  methods=['GET' , 'POST'])
# def edit_dev(id):


#     # DB.update('quiz' , {"full_name" : "mohaned" , "email" : 'mohaned.com' } , f'id = {id} ')
#     if request.method == 'POST' :

#         dev_route = request.form['type_id']
#         # print(request.form)
#         DB.update('devs' , Device(request.form['name'] ,  request.form['sn'] , request.form['place'] ,request.form['type_id'] ,request.form['status']).json() , f'id = {id} ')
#         return redirect(f'/{dev_route}')

#     else :

#         # return DB.select('quiz',  where= f'id = {id}')[0]
#         dev = DB.select('devs',  where= f'id = {id}')[0]
#         print(dev)

#         # teacher_id = quiz['teacher_id']
#         # selected_teacher = DB.select('teacher' , where = f'id ={teacher_id}')[0]


#         # teachers = DB.select('teacher')
#         return render_template('devs/edit_dev.html' , dev = dev , type = dev['type_id'] )
# bruh

# bruh

# @app.route('/del_dev/<type>/<id>')
# def del_dev(type , id):

#     DB.delete('devs'  , f'id = {id} ')


#     return redirect(f'/{type}')

# bruh

@app.route('/assign_role', methods=['GET', 'POST'])
def assign_role():
    #     #role col enum meaning ::  admin = 0  , officer_ohda = 1 , amin_ohda = 2

    # get current assigneeS if exist :
    # role = session['role']
    ohda_officer = DB.select('user', where=f'role = 1')
    ohda_amin = DB.select('user', where=f'role = 2')

    stores = DB.select('stores')
    if ohda_officer and ohda_amin:
        return render_template('devs/assign_role.html',  stores=stores, ohda_officer=ohda_officer[0], ohda_amin=ohda_amin[0])

    else:
        return render_template('devs/assign_role.html',  stores=stores, ohda_officer=None, ohda_amin=None)


@app.route('/add_catagory', methods=['GET', 'POST'])
def add_catagory():
    if request.method == 'POST':
        if 'new' in request.form and request.form['new']:
            # print("OHA" , request.form )
            return render_template('devs/add_catagory.html', store_id=request.form['store_id'], store_name=request.form['store_name'])

        else:
            # print(request.form )
            print("shii")
            store_id = request.form['store_id']
            store_name = request.form['store_name']

            name_en = request.form['name_en']
            code = request.form['code']
            import_num = request.form['import_num']
            source = request.form['source']
            notes = request.form['notes']
            # name_en = request.form['name_en']
            white_space = name_en.find(' ')
            if white_space != -1:
                trimmed = name_en.replace(" ", "")
                name_en = trimmed[:white_space] + "_" + trimmed[white_space:]
            # print(name_en.endswith('s') , "whyyyyyyyyyy")

            # if name_en.endswith('s'):

            #     name_en =name_en[:len(name_en)-1]
            #     print(name_en , "after modificationnn")
            # else :
            #     name_en =name_en + 's'
            name_en = robust_s_remove(name_en) + 's'

            DB.insert('types', [Type(name_en + ',' + request.form['name_ara'], request.form['cls'],
                      request.form['icon'], name_en, 'add_' + name_en, code, import_num, source, notes, store_id).json()])

            # uploading the cat's folder in server
            # upload_folder = store_name
            cat_path = os.path.join(app.config['UPLOAD_FOLDER'], store_name)
            if not os.path.exists(cat_path):
                os.mkdir(cat_path)
            cat_path = os.path.join(
                app.config['UPLOAD_FOLDER'], store_name + '/' + name_en)
            if not os.path.exists(cat_path):
                os.mkdir(cat_path)

            return redirect(url_for('index', store_id=store_id))

    else:
        # return render_template('devs/add_catagory.html', type ='laptops' ,add_action ='add_laptops' )
        return render_template('devs/add_catagory.html')
