import http.client
import json


cnpj_sample = '55048956000155'


def get_company_by_cnpj(cnpj):

    cn = http.client.HTTPSConnection("www.receitaws.com.br")

    cn.request("GET", f'/v1/cnpj/{cnpj}')

    response = cn.getresponse()

    data = response.read()

    company = json.loads(data.decode('utf-8'))

    cn.close()

    if 'ERROR' ==  company.get('status', ''):
        return company.get('message', 'Unknown error')

    return company

company_data = get_company_by_cnpj(cnpj_sample)



print(company_data)