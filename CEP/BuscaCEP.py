import http.client
import json
import pandas as pd
import os

sample_cep = "02411000"

file_dir = os.path.dirname(os.path.abspath(os.path.abspath(__file__)))

filename = os.path.join(file_dir, 'CEP.xlsx')

cep_file = pd.read_excel(filename, sheet_name='CEP')

cep_data = cep_file['CEP'].dropna()

address_results = pd.DataFrame(columns=['CEP', 'Logradouro', 'Bairro', 'Localidade', 'UF'])


def get_address_by_cep(cep):
    cn = http.client.HTTPSConnection("viacep.com.br")

    cn.request("GET", f"/ws/{cep}/json/")

    response = cn.getresponse()

    if response.status != 200:

        cn.close()

        return None

    data = response.read()

    address = json.loads(data.decode("utf-8"))

    cn.close()

    return address if "erro" not in address else None


def save_address_to_excel(address, filename="address.xlsx"):

    if "erro" not in address:

        df = pd.DataFrame([address])

        df.to_excel(filename, index=False)

        print(f"Dados salvos com sucesso em {filename}")
    else:
        print("Não foi possivel salvar os dados: CEP não encontrado.")


for cep in cep_data:

    address = get_address_by_cep(str(cep).replace('-', ''))

    if address:

        new_line = pd.DataFrame([{
            'CEP': cep,
            'Logradouro': address.get('logradouro', ''),
            'Bairro': address.get('bairro', ''),
            'Localidade': address.get('localidade', ''),
            'UF': address.get('uf', '')
        }])

        address_results = pd.concat([address_results, new_line], ignore_index=True)


with pd.ExcelWriter(filename, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:

    address_results.to_excel(writer, sheet_name='Dados', index=False)

# address_result = get_address_by_cep(sample_cep)

# save_address_to_excel(address_result)
print('Foi.')