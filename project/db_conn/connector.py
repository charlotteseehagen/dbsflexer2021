import psycopg2
#from db_conn.config import config

def connect(query):
    """ Connect to the PostgreSQL database server """
    conn = None
 
    try:
        # read connection parameters
        #params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect("dbname='dbsproject' user='postgres' host='localhost' password='dbs'")
        #conn = psycopg2.connect(**params)
        
        # create a cursor
        cur = conn.cursor()
        
        # execute a statement
        cur.execute(query)
        conn.commit()
        data = cur.fetchall()

        #close the communication with the PostgreSQL
        cur.close()
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return(error, False)
        
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

            return(data, True)


if __name__ == '__main__':
    
    #query table information
    query0 = "SELECT table_name, column_name, data_type FROM information_schema.columns WHERE table_name = 'country';"
    query1 = "SELECT * from country where country_code = 'DEU';"
    fetched_tup = connect(query1)

    if fetched_tup[1]:
        for elem in fetched_tup[0]:
            print(elem)
