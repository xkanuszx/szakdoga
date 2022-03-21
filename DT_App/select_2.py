import mysql.connector
import json


def specific_AVG(model):

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

    sql = "SELECT AVG(discharge) FROM battery_field WHERE model = %s"
    val = (model,)

    mycursor.execute(sql, val)

    myresult = mycursor.fetchall()

    return round(float(myresult[0][0]), 3)


def specific_HR_GPS(model, hr_condition, gps_condition):
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

    sql = "SELECT AVG(discharge) FROM battery_field WHERE model = %s AND optical_HR = {} AND GPS_Glonass = {}".format(
        hr_condition, gps_condition
    )
    val = (model,)

    mycursor.execute(sql, val)

    myresult = mycursor.fetchall()

    if type(myresult[0][0]) is float:
        return round(float(myresult[0][0]), 3)
    else:
        return round(float(0), 3)


def select_models():

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

    mycursor.execute("SELECT model FROM battery_field")

    myresult = mycursor.fetchall()

    # print(set(myresult))

    eredmeny = set()

    for x in myresult:

        eredmeny.add(x[0])

    return sorted(list(eredmeny))


if __name__ == "__main__":

    print(specific_AVG("fr735xt"))
    print(specific_HR_GPS("fr735xt", 0, 0))
    print(specific_HR_GPS("fr735xt", 0, 1))
    print(specific_HR_GPS("fr735xt", 1, 0))
    print(specific_HR_GPS("fr735xt", 1, 1))
