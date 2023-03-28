#url
#url = "http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
url = " "


#Sanitizacao da url
url = url.replace(" ", "")

if url == "":
    raise ValueError("A URL esta vazia ou nao tem formato valido")

print(url)

#separa parametros
indice_interrogacao  = url.find('?')
url_base = url[0:indice_interrogacao]
print(url_base)

url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

#retorna os parametros da url
parametro_de_busca = 'moedaOrigem'
indice_parametro = url_parametros.find(parametro_de_busca)
indice_valor = indice_parametro + len(parametro_de_busca) + 1
indice_e = url_parametros.find('&', indice_valor)

# distingue uma url com mais de um '&'
if indice_e == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e]

print(valor)


