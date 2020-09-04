#Vinicius farineli freire
#Data 25/08/2020
#--------------------------
#GITHUB: https://github.com/Farivini?tab=repositories
#COMPARANDO DADOS QUANDO LIGADO AQUECEDORES


#LENDO TEMPERATURA E UMIDADE
import dht
import machine
import time
import urequests
import network


#CONECTANDO WIFI
print("Aguarde conectando....")

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect("KEOLINK")
  


#AUTOMATIZANDO CONEXAO

if not station.isconnected():
   print("Não conectado...")
   time.sleep(1)
else:
  print("conectado...")
  print("Enviando informação...")
  d = dht.DHT11(machine.Pin(4))
  d.measure()    #FUNÇÃO PARA COMEÇAR A UTILIZAR SENSOR
  link = 'https://api.thingspeak.com/update?api_key='
  chave = '2WKWI8H8GXHS3IDE'
  header = '&field1={}&field2={}'.format (d.temperature(), d.humidity())
       
  novo_link=link+chave+header
  print(novo_link)
  data=urequests.get(novo_link) #ENVIA REQUISIÇÃO HTTP
           
  print(data)
           
  time.sleep(5)
           
          
            
  print("Temp = {}     Umid = {}%".format(d.temperature(), d.humidity()))
  time.sleep(5)
  station.disconnect()
       
       #    resposta = urequests.get(" https://api.thingspeak.com/update?api_key= L3IDEI2QQAXC6FKA & field1 = {}".format(d.temperature))
        #   resposta = urequests.get(" https://api.thingspeak.com/update?api_key= L3IDEI2QQAXC6FKA & field2 = {}".format(d.humidity))
    