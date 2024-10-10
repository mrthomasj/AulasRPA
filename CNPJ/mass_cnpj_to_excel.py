import http.client
import json
import pandas as pd
import os

def get_company_by_cnpj(cnpj):

    cn = http.client.HTTPSConnection('www.receitaws.com.br')

    cn.request('GET', f'/v1/cnpj/{cnpj}/')

    response = cn.getresponse()

    print(f'Status code: {response.status}')

    if 200 != response.status:
        return { 'Status': 'ERROR', 'Message': f'HTTP response status {response.status}'}

    data = response.read()

    cn.close()

    try:
        company_data = json.loads(data.decode("utf-8"))
        print(f'Company data parsed: {company_data}')

        return company_data

    except json.JSONDecodeError as e:
        return {'Status': 'ERROR', 'Message': f'Cannot decode JSON, error: {e}'}

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


file_dir = os.path.dirname(os.path.abspath(os.path.abspath(__file__)))

filename = os.path.join(file_dir, 'CNPJ.xlsx')

cnpj_file = pd.read_excel(filename, sheet_name='CNPJ')

cnpj_data = cnpj_file['CNPJ'].dropna()

company_results = pd.DataFrame(
             columns=['cnpj', 'nome', 'telefone', 'email', 'logradouro', 'bairro', 'municipio', 'uf', 'cep',
                      'atividade_principal'])

for cnpj in cnpj_data:

    if 14 != len(str(cnpj)):
        cnpj = str(cnpj)
        i = 14 - len(str(cnpj))
        placeholder_str = ''.join('0' for x in range(0, i))
        cnpj = placeholder_str + cnpj

    company = get_company_by_cnpj(cnpj)

    if company:

        new_line = pd.DataFrame([{
            'cnpj': cnpj,
            'nome': company.get('nome', ''),
            'telefone': company.get('company', ''),
            'logradouro': company.get('logradouro', ''),
            'bairro': company.get('bairro', ''),
            'municipio': company.get('municipio', ''),
            'uf': company.get('uf', ''),
            'cep': company.get('cep', ''),
            'atividade_principal': company.get('atividade_principal', '')
        }])
        company_results = pd.concat([company_results, new_line], ignore_index=True)

with pd.ExcelWriter(filename, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:

    company_results.to_excel(writer, sheet_name='Dados', index=False)


print('Processo concluido.')