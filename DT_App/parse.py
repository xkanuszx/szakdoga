import json
from logging import exception
import fitparse
from tkinter import Tk
from tkinter.filedialog import askopenfilename


def fit_to_ascii():

    Tk().withdraw()
    filename = askopenfilename()
    fitfile = fitparse.FitFile(filename)

    with open("names.json") as f:
        nevek = f.read()
    names = json.loads(nevek)

    adat = {
        "model": "",  # NVARCHAR(255)
        "duration": 0,  # INT
        "optical_HR": 0,  # BOOL: FALSE=0 TRUE=1
        "GPS_Glonass": 0,  # BOOL: FALSE=0 TRUE=1
        "discharge": 0.0,  # FLOAT
    }
    recordcount = 0
    merules = set()

    for record in fitfile.get_messages():

        if record.name == "file_id":

            for data in record:

                if format(data.name) == "garmin_product":
                    if str(data.value) in names:
                        adat["model"] = names[str(data.value)]
                    else:
                        adat["model"] = str(data.value)

        if record.name == "record":

            for data in record:

                if format(data.name) == "Myakksi2":
                    merules.add(data.value)

                elif recordcount == 0:

                    if format(data.name) == "heart_rate":
                        adat["optical_HR"] = 1

                    if (
                        format(data.name) == "position_lat"
                        or format(data.name) == "position_long"
                    ):
                        adat["GPS_Glonass"] = 1
                        recordcount += 1

        if record.name == "activity":

            for data in record:

                if format(data.name) == "total_timer_time":

                    adat["duration"] = round(data.value)
    #

    if len(merules) != 0:
        adat["discharge"] = float((max(merules) - min(merules)))

    return adat


if __name__ == "__main__":
    print(fit_to_ascii())
