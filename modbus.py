from pyModbusTCP.client import ModbusClient
import time

# Inicia configuração TCP
c = ModbusClient(host="localhost", port=502, unit_id=1, auto_open=True)
# Parametros conexão
c = ModbusClient()
c.host("localhost")
c.port(502)
c.unit_id(1)


def powerBIModbus():
    # Abre conexão TCP
    c.open()

    #Leitura de 3 registros a partir do 40001
    regs = c.read_holding_registers(0, 3)
    if regs:
        print(regs)
    else:
        print("read error")

    #Escreve em 2 registros a partir do 40004. Escrita apenas para demonstrar.
    if c.write_multiple_registers(3, [40004,40005]):
        print("write ok")
    else:
        print("write error")

    #Fecha conexão    
    c.close()

try:
    while True:  
        powerBIModbus()
        time.sleep(3)
 
except:
    print ("Falha no programa")
    c.close()

    

