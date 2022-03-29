# SITE ESTÁ ACESSÍVEL? — Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\n\033[31mO site Pudim não está acessível no momento.')
else:
    print('\n\033[32mConsegui acessar o site Pudim com sucesso!\033[m')
    # print(site.read())
