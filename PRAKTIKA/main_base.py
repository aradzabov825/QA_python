# import pymysql
# import pymysql.cursors
# from main_config_base import host,user,password,db_name


# try:
#     connection = pymysql.connect(
#     host=host,
#     port=3306,
#     user=user,
#     password=password,
#     database=db_name,
#     cursorclass=pymysql.cursors.DictCursor
#     )
#     print('success')
#     print('#' * 30)
#     try:
#         with connection.cursor() as cursor:
#             create_table_q = 'CREATE TABLE `studdents`(name VARCHAR(32), PRIMARY KEY (id))'
#             cursor.execute('SHOW TABLES')
#             tables = cursor.fetchall()
#             print('tables in database')
#             for table in tables:
#                 print(table['table in' + db_name])

#     finally:
#         connection.close()
# except Exception as ex:
#     print('Connection rufus')
#     print(ex)



##____________________________________________________________________________________________

# import pymysql
# import pymysql.cursors
# from main_config_base import host,user,password,db_name


# try:
#     connection = pymysql.connect(
#     host=host,
#     port=3306,
#     user=user,
#     password=password,
#     database=db_name,
#     cursorclass=pymysql.cursors.DictCursor
#     )
#     print('succsess')
#     print('#' * 30)
#     try:
#         with connection.cursor() as cursor:
#             #тут пишем запросы
#             create_view_query = '''CREATE VIEW good_ice_tea AS
#                                 SELECT id, category_id, name, count, price
#                                 FROM `good`
#                                 WHERE name LIKE "%Айс Ти%"'''
#             cursor.execute(create_view_query)  
#             print('View_ created')


#     except Exception as e:
#         print('An error ')
#         print(e)        
           
#     finally:
#         connection.close()
# except Exception as ex:
#     print('Connection rufus')
#     print(ex)

##____________________________________________________________________________________________

# import pymysql
# import pymysql.cursors
# from main_config_base import host,user,password,db_name


# try:
#     connection = pymysql.connect(
#     host=host,
#     port=3306,
#     user=user,
#     password=password,
#     database=db_name,
#     cursorclass=pymysql.cursors.DictCursor
#     )
#     print('succsess')
#     print('#' * 30)
#     try:
#         with connection.cursor() as cursor:
#             #тут пишем запросы
        


#     except Exception as e:
#         print('An error ')
#         print(e)        
           
#     finally:
#         connection.close()
# except Exception as ex:
#     print('Connection rufus')
#     print(ex)

#____________________________________________________________________________________________

import pymysql
import pymysql.cursors
from main_config_base import host,user,password,db_name


try:
    connection = pymysql.connect(
    host=host,
    port=3306,
    user=user,
    password=password,
    database=db_name,
    cursorclass=pymysql.cursors.DictCursor
    )
    print('success')
    print('#' * 30)
    try:
        with connection.cursor() as cursor:
            #тут пишем запросы
            new_team = '''CREATE TABLE `team`(id INT AUTO_INCREMENT, name VARCHAR(32), surname VARCHAR(32), number VARCHAR(32), PRIMARY KEY (id))

        '''
            cursor.execute(new_team)
            print('table team created')

            insert_team = '''
            INSERT INTO `team` (name,surname,number) VALUES
            ('jon','com',20),
            ('Erik','gmail.com',10),
            ('jon ','pic',30),
            ('jonrik','eriksp',12),
            ('jo','erpih',23),
            ('jytro','erikspich',24),
            ('joqwe','erpich',11),
            ('jower','erich',16),
            ('josdf','eriksch',4),
            ('jojk','erpich',44),
            ('jonrik','eriksp',2),
            ('jo','erpih',3),
            ('jytro','erikspich',1),
            ('joqwe','erpich',2);
'''
            cursor.execute(insert_team)
            connection.commit()
            print('data inserted')

            quantity = '''
            SELECT * FROM `team` WHERE `number` > 5

            '''
            cursor.execute(quantity)
            rows = cursor.fetchmany(10)
            for i in rows:
                print(i)

            name = '''CREATE VIEW new_name AS
            SELECT * FROM `user` WHERE (name LIKE "А%" OR name LIKE "Б%") AND reg_date LIKE "%2018%"; 
            '''
            cursor.execute(name)
            connection.commit()


# SELECT * FROM `good` WHERE `name` NOT LIKE '%Айс Ти%';

    except Exception as e:
        print('An error ')
        print(e)        
           
    finally:
        connection.close()
except Exception as ex:
    print('Connection rufus')
    print(ex)


#____________________________________________________________________________________________

    # with connection.cursor() as cursor:
        #     #заполняю таблицу
        #     insert_team = '''
        #     INSERT INTO `team` (name,email,age) VALUES
        #     ('jon','com',20),
        #     ('Erik','gmail.com',10),
        #     ('jon ','pic',30),
        #     ('jona Erik','erikspichak@gmail.com',12),
        #     ('joner Erik','erikspichak@gmail.com',15);
        #     '''
        #     cursor.execute(insert_query)
        #     connection.commit()
        #     print('data inserted')

#____________________________________________________________________________________________



#____________________________________________________________________________________________



#____________________________________________________________________________________________