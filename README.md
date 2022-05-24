# python-modbus-powerBI
Exemplo de aplicação para coletar dados de um CLP via Modbus e enviar para o PowerBI em tempo real;

Realiza a leitura de 3 endereços Modbus a partir do endereço 40001. Após coletado os dados, faz um request utilizando método POST para a API do PowerBI criando um streaming dos dados e conseguentemente atualizando em tempo real;
Este projeto é apenas um exemplo de como podemos utilizar o Python com sistemas de automação;

Para o exemplo, foi utilizado o Python 3.8.1;
Bibliotecas:
Modbus TCP - pyModbusTCP 0.1.10
requests - requests 2.27.1;


Código baseado na documentação da biblioteca ModbusTCP;

Autor: Douglas Silva.
