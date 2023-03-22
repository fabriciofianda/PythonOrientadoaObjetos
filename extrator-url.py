url = "http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
print(url)

indice_interrogacao  = url.find('?')
url_base = url[0:indice_interrogacao]
print(url_base)

url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

parametro_de_busca = 'moedaOrigem'
indice_parametro = url_parametros.find(parametro_de_busca)
indice_valor = indice_parametro + len(parametro_de_busca) + 1
indice_e = url_parametros.find('&', indice_valor)

if indice_e == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e]

print(valor)


