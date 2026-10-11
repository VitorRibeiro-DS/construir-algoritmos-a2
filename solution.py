import datetime
import requests

h = datetime.date.today()
R = []

def cotar():
    for i in range(365):
        dia = h - datetime.timedelta(days=i)

        url = (f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@cotacao)?@cotacao='{dia.strftime('%m-%d-%Y')}'&$top=100&$format=json"   )

        resposta = requests.get(url, timeout=15)
        dados = resposta.json()

        if dados['value']:
            R.append(dados['value'][0]['cotacaoCompra'])
    return R

resultado = cotar()
print(resultado)