import mysql.connector

def connectionBD():
 mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="tp18_back"

  )
  if mydb:
    print("conection exitosa")
    else:
    print ("error en la conexion a BD")  
    return mydb