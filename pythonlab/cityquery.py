import psycopg2

# This function sends an SQL query to the database
def find_Northfield():

    # You will need to change the Password to use this code
    
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="richardsonc",
        user="richardsonc",
        password="berry437lamp")

    cur = conn.cursor()

    sql = "SELECT * FROM uscitypop WHERE city LIKE '%Northfield' ORDER BY pop DESC;"
  
    cur.execute( sql )

    # fetchone() returns one row that matches your query
    row = cur.fetchone()

    # Note: We could access individual items in the row
    # That is, row[0] would be the name column in the previous example
    #   ... and row[1] would be the abb column

    #IMPORTANT: This function doesn't actually change the database
    #If we are trying to change the database ...
    # ... for example, creating a table
    #Then we need the following command to finalize our changes
    if row == None:
        return "Northfield is not in the database"
    else:
        return "lat: " + row[4] + "long: " + row[5]

# This function sends a query that returns many items
def largest_citypop():

    # You will need to change the Password to use this code
    
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="richardsonc",
        user="richardsonc",
        password="berry437lamp")

    cur = conn.cursor()

    sql = "SELECT * FROM uscitypop WHERE pop>0 ORDER BY pop DESC;"
  
    cur.execute( sql )

    # fetchone() returns one row that matches your query
    row = cur.fetchone()
    
    return "largest city name: " + row[0]

def test_query_all(sql):

    # You will need to change the Password to use this code
    
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="richardsonc",
        user="richardsonc",
        password="berry437lamp")

    cur = conn.cursor()
    
    cur.execute( sql )

    # fetchall() returns a list containing all rows that matches your query
    row_list = cur.fetchall()

    # It is often useful to loop through all rows in a query result
    for row in row_list:
        print( row[1] )
    
    # Note: We could access individual items in the row
    # That is, row[0] would be the name column in the previous example
    #   ... and row[1] would be the abb column

    # Here I am leaving out the conn.commit() because we aren't changing
    #    either the database or the data in the database
    
    return None


#Often we want to put a Python variable into an SQL query
def smallest_MN():
    
    # You will need to change the Port and the Password to use this code

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="richardsonc",
        user="richardsonc",
        password="berry437lamp")

    cur = conn.cursor()


    # Here the %s signals that we will replace this with a variable later
    sql = "SELECT * FROM uscitypop WHERE state LIKE %s ORDER BY pop DESC;"

    state = 'Minnesota'
    
    cur.execute( sql, [state]  )

    # IMPORTANT: We need a list of values for the second input to execute
    #   ... Even if we are only inserting my variable, it must be in a list
    # For example,  [state_abb1]
    
    row_list = cur.fetchall()
    smallest = row_list[0[2]]
    
    for row in row_list:
        if row[2] < smallest:
            smallest = row

    return smallest

print(find_Northfield())
print(largest_citypop())
print(smallest_MN())
