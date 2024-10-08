import http.client
import json
import pandas as pd

def get_address_by_cep(cep):

    cn = http.client.HTTPSConnection('viacep.com.br')

    cn.request("GET", f"/ws/{cep}/json")

    response = cn.getresponse()

    data = response.read()

    address = json.loads(data.decode("utf-8"))

    cn.close()

    if "erro" not in address:
        return address
    else:
        return "CEP Não encontrado"

