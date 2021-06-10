# import os
# import urllib.parse as up
# import psycopg2

# up.uses_netloc.append("postgres")
# url = up.urlparse(os.environ["postgres://uxowazul:aP4wtBqbCQ55GVkEA9WM-dJEJjYwM5RQ@salt.db.elephantsql.com/uxowazul"])
# conn = psycopg2.connect(database=url.path[1:],
# user=url.username,
# password=url.password,
# host=url.hostname,
# port=url.port
# )




# import psycopg2  
# conn = psycopg2.connect(database="uxowazul", user="uxowazul", password="aP4wtBqbCQ55GVkEA9WM-dJEJjYwM5RQ", host="http://salt.db.elephantsql")
# print(conn)
# postgres://uxowazul:aP4wtBqbCQ55GVkEA9WM-dJEJjYwM5RQ@salt.db.elephantsql.com/uxowazul
# from config import config

# def connect():
#     """ Connect to the PostgreSQL database server """
#     conn = None
#     try:
#         # read connection parameters
#         params = config()

#         # connect to the PostgreSQL server
#         print('Connecting to the PostgreSQL database...')
#         conn = psycopg2.connect(**params)
		
#         # create a cursor
#         cur = conn.cursor()
        
# 	# execute a statement
#         print('PostgreSQL database version:')
#         cur.execute('SELECT version()')

#         # display the PostgreSQL database server version
#         db_version = cur.fetchone()
#         print(db_version)
       
# 	# close the communication with the PostgreSQL
#         cur.close()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()
#             print('Database connection closed.')


# if __name__ == '__main__':
#     connect()