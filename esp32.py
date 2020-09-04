import machine
import time

r = machine.Pin(2, machine.Pin.OUT) # DIZEMOS AO MICRO PINO DOIS VAI SER A PORTA DE SAIDA
while True:
    r.value(1)
    time.sleep(2)
    r.value(0)
    time.sleep(2)


#LENDO TEMPERATURA E UMIDADE
import dht
import machine
import time

d = dht.DHT11(machine.pIN(4))

while True:
    print(d.temperature)
    print(d.humidity)
    if d.temperature <31 and d.humidity > 70:
        d.measure()
        print("Temp={}     Umid={}".format(d.temperature, d.humidity()))
        time.sleep(3)

#CONECTANDO AO WIFi


def conecta(ssid, senha):
    import networkx

    estacao = networkx.WLAN(networkx.STA_IF)
    estacao.active(True)
    estacao.scan()
    estacao.connect(ssid, senha)
    for i in range(50):
        if estacao.isconnected():
            break
        time.sleep(0.1)
    return estacao

#COMPORTAMENTO DOSISTEMA

from wifi_lib import conecta
import urequests
print('Conectando rede wifi')
estacao = conecta("teste_wifi", "senha_teste_wifi")
if not estacao.isconnected:
    print('Não conectado')
else:
    print('Conectado')
    print('Acessando URL ')
    time.sleep(3)
    response = urequests.get("http://teste.afonsomiguel.com")
    print(response.text)

