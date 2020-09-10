# imports
import mysql.connector
import functools
import operator

from Text_to_Voice import speak_it
from mysql.connector import errorcode
# configuration
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="BhSaPnPh02)#23",
    database = "aidb"
)

# logic
mycursor=mydb.cursor()

sqlformula="INSERT INTO respond (ques,ans) VALUES (%s, %s)"
sqlformula2 = "SELECT ans FROM respond WHERE ques = %s"

#fuction to convert string to tuple
def convertTuple(tup):
    str = functools.reduce(operator.add, (tup))
    return str

#fuctions to input
def add_respond(u_input,p_output):
    a1 = (u_input, p_output)
    mycursor.execute(sqlformula,a1)
    mydb.commit()

#function to output
def get_respond(u_input):
    try:
        a2=(u_input,) #converting string to tuple
        mycursor.execute(sqlformula2,a2)
        myresult=mycursor.fetchone()
        str_myresult=convertTuple(myresult)
        return str_myresult
    except mysql.connector.Error as err:
        print("You     => Sir, would you like to teach me the answer ?")
        speak_it(" Sir, would you like to teach me the answer?")
        print("\t\tPress y for yes and n for no")
        speak_it("Press y for yes and n for no")
        ch = input("You     => ")
        if ch=='y' or ch=='Y':
            print("You     => Please type the answer.")
            speak_it("Please type the answer")
            p_output = input("You     => ")
            add_respond(u_input, p_output)
            return "Thanks for teaching me."
            
        elif ch=='N' or ch=='n':
            return "Hopefully I will learn it someday."
 #testing.           
k = "are joj?"
p_out = get_respond(k)
speak_it(p_out
print(p_out)