# module used for connection to MySQL is pymysql
# if not installed open Command Line and type 'pip install pymysql'
# mysql.connector can also be used



# UNCOMMENT BELOW GIVEN CODE FOR SIMPLEST MySQL CONNECTION i.e. remove two '#' from beginning of each line

# import module
##import pymysql
##
### Connection to MySQL server
##connection = pymysql.Connect(host='localhost', database='<DataBase to Connect>', user='<Username>', password='<Your Password>')
### Creating a cursor object to execute commands
##cursor = connection.cursor()
### Executing queries using cursor
##cursor.execute('<YOUR QUERY HERE>')
### To save the executed query we have to commit it to the connection
##connection.commit()
### Getting values of output after execution
### To get only the first line of the execution of query:
##first_value = cursor.fetchone()
### To get all the values of output
##values = cursor.fetchall()



# ---------------------------------------------------------------- #



# import module
import pymysql

# If we have to try to connect to MySQL again and again unless an Exception or any serious error occurs we can
# use try under while loop
running = True
while running:
    try:
        # to make connection
        connection = pymysql.Connect(host='localhost', database='<DataBase to Connect>', user='<Username>', password='<Your Password>')
        cursor = connection.cursor()
        # . . . rest of the program
        values = cursor.fetchall()
        print(values)
        # After successful execution the while loop can be stopped
        # There are however several ways to implement loops with connections this is the minimal reproducible
        # example of a simple loop so right after execution process/loop will stop
        running = False
    except Exception as e:
        # If any Exception occurs then the loop will stop
        print('Error: ', e)
        running = False