from pyModbusTCP.client import ModbusClient
import requests
import time
import datetime

# Inicia configuração TCP
c = ModbusClient(host="localhost", port=502, unit_id=1, auto_open=True)

# Parametros conexão
c = ModbusClient(host="127.0.0.1", auto_open=True, auto_close=True)
c = ModbusClient()
c.host("localhost")
c.port(502)
c.unit_id(1)

def powerBIModbus():
    data= datetime.datetime.now()
    print(data)

    # Abre conexão TCP
    c.open()

    #Leitura de 3 registros a partir do 40001
    regs = c.read_holding_registers(0, 3)
    if regs:
        print(regs)

        try:
        #Envia dados da leitura Modbus para PowerBI streaming, somente quando a leitura é concluída
            url = 'https://api.powerbi.com/beta/ecaa386b-c8df-4ce0-ad01-740cbdb5ba55/datasets/1907fbc1-593d-475b-8971-4520a1669d74/rows?key=LJ7FEK6Xg3ZSsD3nLSHUivoOSyI9Bo7AZJj1FnfJPos9OJl%2B5LJB%2B5XoQ0sFVZ53z1ib8E8hRQ0%2FipeozECqzQ%3D%3D'
            myobj = [{'valor1':regs[0] ,'valor2':regs[1] ,'valor3': regs[2] }]

            x = requests.post(url, json =myobj)
            print(x)
        except:
            print("erro powerBI")
    else:
        print("read error")

    #Escreve de 2 registros a partir do 40004. Excrita apenas para demonstrar.
    if c.write_multiple_registers(3, [40004,40005]):
        print("write ok")
    else:
        print("write error")

    #Fecha conexão    
    c.close()



try:
    while True:  
        powerBIModbus()
        time.sleep(2)

       
 
except:
    print ("Falha de Leitura")
    c.close()
    

    

