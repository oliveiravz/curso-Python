import urllib.request

# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

try :
    site = urllib.request.urlopen('http://www.google.com.br')
except urllib.error.URLerror :
    print('Site indisponível')
else :
    print('Site disponível')