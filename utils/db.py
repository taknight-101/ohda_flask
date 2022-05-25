import pymysql

from flask import jsonify
from itertools import chain


# from ..app import mysql

import os
# print(os.environ['HOME'])

class DB :
        # conn = pymysql.connect(host="localhost" , user="root" , passwd="" , db="flask")
        # conn = pymysql.connect(host=os.environ.get('DB_URL') , user="root" , passwd="root" , db="flask")

        # deploy

        # cursor = conn.cursor(pymysql.cursors.DictCursor)
        # conn = pymysql.connect(host='db' , user="ahmed" , passwd="" , db="flask")



        @staticmethod
        def custom_query():
            return DB.conn.cursor()     ## still don't know how safe is this


        @staticmethod
        def select(table , cols='*'  , where = None , distinct = None):
            DB.conn.ping(reconnect=True)
            with DB.conn.cursor(pymysql.cursors.DictCursor) as cursor:
                if where :
                    sql = f'SELECT * FROM {table} WHERE {where}' if cols == '*' else  f'SELECT ' + ','.join([col for col in cols]) + f' FROM {table} WHERE {where}'
                    # print(sql)
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    return list(result) #jsonify(list(result))

                if distinct :

                    sql = f'SELECT DISTINCT {distinct} FROM {table}'
                    # print(sql)
                    cursor.execute(sql)
                    result = cursor.fetchall()

                    return  list(result) #jsonify(list(result))

                sql = f'SELECT * FROM {table}' if cols == '*' else  f'SELECT ' + ','.join([col for col in cols]) + f' FROM {table}'
                # print(sql)
                # print("omg")
                cursor.execute(sql)
                result = cursor.fetchall()

                return  list(result) #jsonify(list(result))

            #test
            # select('assistant' , ['email'] , 'id =2 ')




        # one && many values insertion
        @staticmethod
        def insert(table , data=[]):
            # data = [{key1:val1} , {key2 :val2}]
            DB.conn.ping(reconnect=True)
            with DB.conn.cursor() as cursor:
                sql = f'INSERT INTO {table} (' + ','.join([col for col in data[0].keys()]) + ') VALUES ' + ','.join(['(' + ','.join(['%s' for _ in range(len(data[0].values()))])+ ')' for _ in data ])


                cursor.execute(sql, tuple(chain.from_iterable(tuple([tuple(doc.values()) for doc in data]))) )
                DB.conn.commit()

                # return 'success'
                return cursor


        #test
        # print(insert('assistant' , {"full_name" : "ahmed" , "email" : 'TAKnigiht.com' }))

        @staticmethod
        def update(table , data={} , where = None):

            DB.conn.ping(reconnect=True)
            with DB.conn.cursor() as cursor:
                sql = f'UPDATE {table} SET ' + ','.join([col + '=' + '%s' for (col, _) in data.items()]) + f' WHERE {where}' if where else \
                    f'UPDATE {table} SET ' + ','.join([col + '=' + '%s'  for (col, _) in data.items()])


                print("UPDATE RAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAN~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(table,  data)
                print(cursor.execute(sql, tuple(data.values())))
                # print("inside", sql , cursor.execute(sql, tuple(data.values())))


                DB.conn.commit()

                # return 'success'
                # print(DB.conn.commit())
                # print("it should really work xD")
                return cursor

        #test
        # print(update('assistant' , {"full_name" : "mohaned" , "email" : 'mohaned.com' } , 'id = 3 '))

        @staticmethod
        def delete(table ,where = None):
            DB.conn.ping(reconnect=True)
            with DB.conn.cursor() as cursor:
                sql = f'DELETE FROM {table}' + f' WHERE {where}' if where else 'Are you sure? ' #f'DELETE FROM {table}'
                cursor.execute(sql)
                DB.conn.commit()
                return 'success'


        #test
        # print(delete('assistant'  , 'id = 1 '))

        @staticmethod
        def select_with_join(tables=[] , condition = None , cols='*'  , where = None ):
            DB.conn.ping(reconnect=True)
            with DB.conn.cursor(pymysql.cursors.DictCursor) as cursor:
                join_portion = f' {tables[0]} JOIN {tables[1]} ON {condition} '
                if where :
                    sql = f'SELECT * FROM' + join_portion + f'WHERE {where}' if cols == '*' else  f'SELECT ' + ','.join([col for col in cols]) + f' FROM {join_portion} WHERE {where}'

                    cursor.execute(sql)
                    result = cursor.fetchall()
                    return list(result) #jsonify(list(result))

                sql = f'SELECT * FROM {join_portion}' if cols == '*' else  f'SELECT ' + ','.join([col for col in cols]) + f' FROM {join_portion}'
                cursor.execute(sql)
                result = cursor.fetchall()

                return  list(result) #jsonify(list(result))


# print(DB.select('assistant'))
# print(DB.insert('assistant' , [{"full_name" : "ahmed" , "email" : 'TAKnigiht.com' } , {"full_name" : "mohamed" , "email" : 'mohamed.com' }]))
