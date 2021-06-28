import psycopg2
from config import config

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    query = "INSERT INTO country(country_id, co2_id, gdp_id, country_code, population_total, population_relative, year) VALUES (1,1,1, 'DEU', 420.69, 42.0, 2021)"
 
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        
        # create a cursor
        cur = conn.cursor()
        cur1 = conn.cursor()
        
        # execute a statement
        cur.execute(query)
        conn.commit()
        #display data
        data_display = cur.fetchall()
        print(data_display)

        #close the communication with the PostgreSQL
        cur.close()
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    
    connect()

