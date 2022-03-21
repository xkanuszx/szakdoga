import mysql.connector
import json
from parse import fit_to_ascii


def insert_to_db():

    with open("connection.json", "r") as f:
        data = f.read()

    kapcsolat = json.loads(data)

    mydb = mysql.connector.connect(
        host=kapcsolat["host"],
        user=kapcsolat["user"],
        password=kapcsolat["password"],
        database=kapcsolat["database"],
    )

    mycursor = mydb.cursor()

    # mycursor.execute("CREATE TABLE battery_field (id INT AUTO_INCREMENT PRIMARY KEY, model NVARCHAR(255), duration INT, optical_HR BOOL, GPS_Glonass BOOL, discharge INT)")

    mydict = fit_to_ascii()

    placeholders = ", ".join(["%s"] * len(mydict))
    columns = ", ".join(mydict.keys())
    sql = "INSERT INTO %s ( %s ) VALUES ( %s )" % (
        "battery_field",
        columns,
        placeholders,
    )

    mycursor.execute(sql, list(mydict.values()))

    mydb.commit()

    print(mycursor.rowcount, "was inserted.")


if __name__ == "__main__":
    insert_to_db()
