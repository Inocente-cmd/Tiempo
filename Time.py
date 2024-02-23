import time
from time import sleep
import time
import datetime

print('ya va acomenzar')

while True:

    fecha = '8:46:00 AM' # 7:29 - 7:40

    hora = datetime.datetime.now() 
    #print(type(hora))
    #print(hora.strftime('%I:%M:%S %p'))
    hora = (hora.strftime('%I:%M:%S %p')) 
    #print(hora)
    #print(fecha)

    if fecha == hora:
        print('en accion')
        break
        
    else:
        print('ahora son las ', hora)
        print(fecha)
