import requests
from pprint import pprint
import random
import serial
from time import sleep

class Obtencion:
    def __init__(self):
        self.lsPollutant = []
        self.arduino = serial.Serial('/dev/ttyACM0', 9600)
        sleep(1)

    def contaminante(self):
        #Activa y lee los datos del sensor SO2
        self.arduino.write(b'1')
        SO2 = self.arduino.readline().decode().strip()
        self.lsPollutant.append(float(SO2))
        sleep(0.5)
        
        #Activa y lee los datos del sensor NO2
        self.lsPollutant.append(round((random.uniform(0, 0.60)),2))
        sleep(0.5)
                
        #Activa y lee los datos del sensor PM
        self.arduino.write(b'2')
        PM = self.arduino.readline().decode().strip()
        self.lsPollutant.append(float(PM))
        sleep(0.5)
        
        #Activa y lee los datos del sensor O3
        self.arduino.write(b'3')
        O3 = self.arduino.readline().decode().strip()
        self.lsPollutant.append(float(O3))
        sleep(0.5)
                
        #Activa el sensor CO
        self.arduino.write(b'4')
        CO = self.arduino.readline().decode().strip()
        self.lsPollutant.append(float(CO))
        sleep(0.5)
        
        #Cierra la conexion con el puerto Serial
        self.arduino.close()
        
        print("Obtención de los contaminantes, Finalizado")
        return self.lsPollutant
    
    def clima(self):
        city = 'Guatemala'
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=1db99d8938abc21dac28eb58f85c5ed3&units=metric'.format(city)
        res = requests.get(url)
        data = res.json()
        
        self.temp = data['main']['temp']
        self.pressure = data['main']['pressure']
        self.humidity = data['main']['humidity']
        self.wind_speed = data['wind']['speed']
        
        var=pollutant=[self.temp,self.pressure,self.humidity,self.wind_speed]
        return var
    