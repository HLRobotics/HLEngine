#author:Akhil P Jacob
#HLDynamic-Integrations

import mysql.connector
from mysql.connector import Error

def dml_select(host,db,user,psd,query):
    try:
        mySQLconnection = mysql.connector.connect(host=host,
                                                  database=db,
                                                  user=user,
                                                  password=psd)
        sql_select_Query = query
        cursor = mySQLconnection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        return (records)



    except:
        return ("HLEngine:Cannot select")

def dml_insert(host,db,user,psd,query):
    try:
        con = mysql.connector.connect(host=host,
                                      database=db,
                                      user=user,
                                      password=psd)
        if (con.is_connected()):
            print("Connected Succesfully")
        sql_insert_Query = query
        cursor = con.cursor()
        cursor.execute(sql_insert_Query)
        con.commit()
        return ("HLEngine: Inserted Successfuly")


    except Error as e:
        return (e)

    finally:
        cursor.close()
        con.close()

def dml_del(host,db,user,psd,query):
    try:
        con = mysql.connector.connect(host=host,
                                      database=db,
                                      user=user,
                                      password=psd)

        sql_del_Query = query
        cursor = con.cursor()
        cursor.execute(sql_del_Query)
        con.commit()

        return ("HLEngine: Deleted Successfuly")

    except Error as e:
        return (e)

    finally:
        cursor.close()
        con.close()

