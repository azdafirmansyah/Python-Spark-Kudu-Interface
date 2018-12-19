from impala.dbapi import connect

def get_db_connection():
    connection = connect(host='xxx.xxx.xxx.xxx', database='dbtest')
    return connection
