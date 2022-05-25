from textwrap import dedent
# print(__main__)
from __main__ import app


class Reflection :
        name_ens = None
        def __init__(self,name_ens) -> None:
            self.name_ens = name_ens
            # print(name_ens , "YO")

            for name_en in name_ens:
                if  name_en.endswith('s') :
                    name_en = name_en[:len(name_en)-1]


                show_callback =f'''
                        @app.route('/{name_en}s' , methods=['GET' , 'POST'])
                        def {name_en}s():
                            {name_en}s = DB.select('devs' ,  where ='type_id = "{name_en}s" ')
                            return render_template('devs/show_all.html' , type ='{name_en}s' ,data={name_en}s )
                        '''
                add_callback = f'''
                            @app.route(f'/add_{name_en}s' , methods=['GET' , 'POST'])
                            def add_{name_en}s():
                                if request.method == 'POST' :

                                    # return request.form
                                    DB.insert('devs' , [Device(request.form['name'] ,  request.form['sn'] , request.form['place'] ,request.form['type_id'] ,request.form['status']).json()])
                                    return redirect(url_for('index'))

                                else :
                                    return render_template('devs/add_dev.html' , type ='{name_en}s' ,add_action ='add_{name_en}s')
                            '''

                edit_callback = '''
                    @app.route('/edit_dev/<id>' ,  methods=['GET' , 'POST'])
                    def edit_dev(id):



                        if request.method == 'POST' :

                            dev_route = request.form['type_id']
                            # print(request.form)
                            print ("IN REFLECTION" ,  request.form['place'])
                            DB.update('devs' , Device(request.form['name'] ,  request.form['sn'] , request.form['place'] ,request.form['type_id'] ,request.form['status']).json() , f'id = {id} ')
                            return redirect(f'/{dev_route}')

                        else :

                            dev = DB.select('devs',  where= f'id = {id}')[0]

                            return render_template('devs/edit_dev.html' , dev = dev , type = dev['type_id'] )

                    '''

                delete_callback = '''
                        @app.route('/del_dev/<type>/<id>')
                        def del_dev(type , id):

                            DB.delete('devs'  , f'id = {id} ')


                            return redirect(f'/{type}')

                        '''
                self.dispatch(show_callback)
        @staticmethod
        def register():
            pass


        # @staticmethod
        def dispatch(self ,cb):
            # print(cb)
            # callbacks = [self.show_callback ,self.add_callback,self.edit_callback , self.delete_callback]
            print(dedent(cb))
            exec(dedent(cb))

            # callbacks = [self.show_callback ]
            # for callback in callbacks:
            #     eval(callback)







