import psycopg2
from config import config

def connect(data, b):
    """ Connect to the PostgreSQL database server """
    conn = None
    query = "INSERT INTO test(datum, tief, hoch, tagesendwert, handelsvolumen) VALUES(%s, %s, %s, %s, %s)"
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
		
        # create a cursor
        cur = conn.cursor()
        cur1 = conn.cursor()
        cur1.execute('SELECT * from test')
        
        if b :
            # execute a statement
            cur.execute(query, data)
            conn.commit()
            #display data
            data_display = cur1.fetchall()
            print(data_display)

        else:
            # execute a statement
            cur.execute(data)
            #display data
            data_display = cur.fetchall()
            print(data_display)


    
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    
    print("Wanna insert[i] stuff or just fetch[f]")
    c = input()

    if c == 'i':
        print("add data [datum; tief; hoch; tagesendwert; handelsvolumen], AS TUPLE")
        #        data = tuple(input())
        data = ('lenny', 1, 2, 3, 4)
        connect(data, True)

    else:
        print("Enter ur desired quer")
        data = input()
        connect(data, False)

