class Calculo:
    def __init__(self):
        #Factor de Conversión (Unidad en ug/m3)
        self.FCD_SO2=0.80
        self.FCH_SO2=0.28
        self.FCD_NO2=00.00
        self.FCH_NO2=0.50
        self.FCD_PM=2
        self.FCH_PM=0.67
        self.FCoct_O3=0.83
        self.FCH_O3=0.55
        self.FCoct_CO=10.00 #Excepción (Unidad en mg/m3)
        
        #Masa molecular de los contaminantes
        self.MSO2 = 64
        self.MNO2 = 45
        self.MPM = 0
        self.MO3 = 48
        self.MCO = 28
        
        #Constante de los gases ideales
        self.R= 0.082
        
    def IPHorario(self,pollutant):
        IPSO2=round((pollutant[0]*(self.FCH_SO2)),2)
        IPNO2=round((pollutant[1]*(self.FCH_NO2)),2)
        IPPM=round((pollutant[2]*(self.FCH_PM)),2)
        IP03=round((pollutant[3]*(self.FCH_O3)),2)
        IPCO=round((pollutant[4]*(self.FCoct_CO)),2)
        
        LsIPH = [IPSO2,IPNO2,IPPM,IP03,IPCO]
        print("Calculo del Indice parcial Horario finalizado")
        return LsIPH
     
    def IPDiario(self,SO2,NO2,PM,O3,CO):
        auxSO2 = sorted(SO2) 
        auxNO2 = sorted(NO2)
        auxPM = sorted(PM)
        auxO3 = sorted(O3)
        auxCO = sorted(CO)
        
        IPDSO2=round(((auxSO2[len(auxSO2)-1])*(self.FCH_SO2)),2)
        IPDNO2=round(((auxNO2[len(auxNO2)-1])*(self.FCH_NO2)),2)
        IPDPM=round(((auxPM[len(auxPM)-1])*(self.FCH_PM)),2)
        IPD03=round(((auxO3[len(auxO3)-1])*(self.FCH_O3)),2)
        IPDCO=round(((auxCO[len(auxCO)-1])*(self.FCoct_CO)),2)
        
        LsIPDiario = [IPDSO2,IPDNO2,IPDPM,IPD03,IPDCO]
        return LsIPDiario
    
    def IGEDiario(self,LsIPDiario):
        auxLsIPD = sorted(LsIPDiario)
        return auxLsIPD[len(auxLsIPD)-1]
    
    def enlistarC(self,LsC):
        SO2 = []
        NO2 = []
        PM = []
        O3 = []
        CO = []
        for linea in LsC:
            SO2.append(linea[0])
            NO2.append(linea[1])
            PM.append(linea[2])
            O3.append(linea[3])
            CO.append(linea[4])
        return SO2,NO2,PM,O3,CO
        
    def IGEHorario(self,LsIP):
        aux=sorted(LsIP)
        return aux[len(aux)-1]
        
    def guardar_contaminantes(self,LsC):
        tuplaC=[(LsC[0],LsC[1],LsC[2],LsC[3],LsC[4])]
        archivo = open("cache/pollutant.txt", "a")
        for SO2, NO2, PM, O3, CO in tuplaC:
            archivo.write(str(SO2)+","+str(NO2)+","+str(PM)+","+str(O3)+","+str(CO)+"\n")
        archivo.close()
        print("Los datos fueron guardados exitosamente")

    def recuperar_contaminantes(self):
        cacheLsCont = []
        archivo = open("cache/pollutant.txt", "r")
        for línea in archivo:
            SO2, NO2, PM, O3, CO = línea.rstrip("\n").split(",")
            cacheLsCont.append((float(SO2),float(NO2),float(PM),float(O3),float(CO)))
        archivo.close()
        return cacheLsCont
    
    def transform(self,lsPollutant,varclima):
        temp = varclima[0]
        pressure = round((varclima[1]/1013.25),2) #conversion atm

        pollutants = lsPollutant

        #SO2 ppm → SO2 ug/m3 
        transformSO2 = (pollutants[0]*self.MSO2)/((self.R*(temp+273.15))/pressure)
        pollutants[0] = round((transformSO2), 2)
        
        #O3 ppb → O3 ug/m3 
        transformO3 = (pollutants[3]*self.MO3)/((self.R*(temp+273.15))/pressure)
        pollutants[3] = round((transformO3), 2)
        
        #CO ppm → CO mg/m3
        transformCO = (pollutants[4]*self.MCO)/((self.R*(temp+273.15))/pressure)
        pollutants[4] = round((transformCO/1000), 2)
        
        print("Conversion Exitosa")
        return pollutants
        