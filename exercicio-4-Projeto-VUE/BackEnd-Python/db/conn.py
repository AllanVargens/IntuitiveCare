import mysql.connector

config = {
    'user': 'root',
    'password': 'allanzinho10',
    'host': '127.0.0.2',
    'database': 'exercicio_4',
    'raise_on_warnings': True
}
try:
    connection = mysql.connector.connect(**config)
except mysql.connector.Error as erro:
    print("Trate o seguinte erro e tente novamente: ", erro)
