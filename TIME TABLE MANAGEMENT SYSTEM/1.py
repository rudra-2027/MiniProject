import mysql.connector

# Replace these variables with your own database information
host = "your_host"
user = "your_username"
password = "your_password"
database = "your_database"

try:
    # Create a connection to the MySQL server
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    if connection.is_connected():
        print("Connected to MySQL database")

    # Perform database operations here

except mysql.connector.Error as error:
    print(f"Error: {error}")
finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection closed")
