#!/usr/bin/python3
# -*- coding: utf-8 -*-
import mariadb
import time, sys

# Systempfad zum den Sensor, weitere Systempfade könnten über ein Array
# oder weiteren Variablen hier hinzugefügt werden.
# 28-02161f5a48ee müsst ihr durch die eures Sensors ersetzen!
aussen = '/sys/bus/w1/devices/28-01193a900195/w1_slave'
oben = '/sys/bus/w1/devices/28-01193a9b9a82/w1_slave'
unten = '/sys/bus/w1/devices/28-01193a2b1fcb/w1_slave'

try:
    conn = mariadb.connect(
        user="greenhouse",
        password="housedelagreen",
        host="localhost",
        port=3306,
        database="greenhouse"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

def readTempSensor(sensorName) :
    """Aus dem Systembus lese ich die Temperatur der DS18B20 aus."""
    f = open(sensorName, 'r')
    lines = f.readlines()
    f.close()
    return lines

def readTempLines(sensorName) :
    lines = readTempSensor(sensorName)
    # Solange nicht die Daten gelesen werden konnten, bin ich hier in einer Endlosschleife
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = readTempSensor(sensorName)
    temperaturStr = lines[1].find('t=')
    # Ich überprüfe ob die Temperatur gefunden wurde.
    if temperaturStr != -1 :
        tempData = lines[1][temperaturStr+2:]
        tempCelsius = float(tempData) / 1000.0
        tempCelsius = round(tempCelsius,1)
        tempKelvin = 273 + float(tempData) / 1000
        tempFahrenheit = float(tempData) / 1000 * 9.0 / 5.0 + 32.0
        # Rückgabe als Array - [0] tempCelsius => Celsius...
        return [tempCelsius, tempKelvin, tempFahrenheit]

#    while True :
        # Mit einem Timestamp versehe ich meine Messung und lasse mir diese in der Console ausgeben.
print(("Temperatur aussen um " + time.strftime('%H:%M:%S') +": " + str(readTempLines(aussen)[0]) + " °C"))
print(("Temperatur oben um " + time.strftime('%H:%M:%S') +": " + str(readTempLines(oben)[0]) + " °C"))
print(("Temperatur unten um " + time.strftime('%H:%M:%S') +": " + str(readTempLines(unten)[0]) + " °C"))
        # Nach 10 Sekunden erfolgt die nächste Messung
tOben= str(readTempLines(oben)[0])
tUnten=str(readTempLines(unten)[0])
tAussen=str(readTempLines(aussen)[0])
tAussen = 0
cursor = conn.cursor()
try:
    cursor.execute(
        "Insert into temp (oben, unten, aussen) values (?,?,?)",
        (tOben,tUnten,tAussen))
    print(f"{cursor.rowcount} details inserted")
    conn.commit()
    conn.close()
except mariadb.Error as e:
    print(f"Error: {e}")

#        time.sleep(10)
#except KeyboardInterrupt:
    # Programm wird beendet wenn CTRL+C gedrückt wird.
#    print('Temperaturmessung wird beendet')
#except Exception as e:
#    print((str(e)))
#    sys.exit(1)
#finally:
    # Das Programm wird hier beendet, sodass kein Fehler in die Console geschrieben wird.
#    print('Programm wird beendet.')
#    sys.exit(0)
