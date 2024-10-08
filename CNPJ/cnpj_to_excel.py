import http.client
import json
import pandas as pd


def get_company_by_cnpj(cnpj):
    cn = http.client.HTTPSConnection('www.receitaws.com.br')

    cn.request('GET', f'/v1/cnpj/{cnpj}')

    response = cn.getresponse()

    print(f'Status Code: {response.status}')

    if 200 != response.status:
        return {'Status': 'ERROR', 'Message': f'HTTP Status {response.status}'}

    data = response.read()

    cn.close()

    try:

        company = json.loads(data.decode("utf-8"))
        print(f'Company data parsed: {company}')

        return company

    except json.JSONDecodeError as e:
        print(f'Error trying to JSON parse: {e}')
        return {'Status': 'ERROR', 'Message': f'Error trying to JSON parse: {e}'}


def treat_nested_data(data):
    if 'atividade_principal' in data:
        data['atividade_principal'] = '; '.join(ativ['text'] for ativ in data['atividade_principal'])

    if 'atividades_secundarias' in data:
        data['atividades_secundarias'] = '; '.join(ativ['text'] for ativ in data['atividades_secundarias'])

    if 'billing' in data:
        data['billing'] = str(data['billing'])

    if 'extra' in data:
        data['extra'] = str(data['extra'])

    if 'qsa' in data:
        data['qsa'] = '; '.join([f"{q['nome']} ({q.get('qual', '')})" for q in data['qsa']])

    return data

def write_data_to_excel(company, filename='dados_empresa.xlsx'):
    if 'ERROR' != company.get('status'):
        company = treat_nested_data(company)

        # df = pd.DataFrame(
        #     columns=['cnpj', 'nome', 'telefone', 'email', 'logradouro', 'bairro', 'municipio', 'uf', 'cep',
        #              'atividade_principal'])

        df = pd.DataFrame([company])

        df.to_excel(filename, index=False)

        print(f'Dados exportados com sucesso no arquivo {filename}')
    else:
        print('Não foi possivel exportar os dados.')

cnpj_sample = '55048956000155'

company_data = get_company_by_cnpj(cnpj_sample)
print(company_data)


write_data_to_excel(company_data)
