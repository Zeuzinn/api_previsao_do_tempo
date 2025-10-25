# Previsão do Tempo

Este projeto fornece **previsões do tempo** para qualquer cidade do mundo, usando a API do **OpenWeatherMap**. Ele permite que o usuário consulte as condições meteorológicas para os próximos dias e exibe informações como temperatura, umidade, e possíveis alertas de eventos climáticos extremos (como calor extremo, chuva, etc.). Além disso, os dados obtidos são salvos em arquivos JSON.

---

## Funcionalidades

- **Consulta à previsão do tempo:** O programa consulta a API do OpenWeatherMap para obter a previsão do tempo.

- **Exibição de dados:** Para cada dia, é mostrado:

    - Clima predominante (ex: "céu limpo", "chuva leve", etc.)

    - Temperatura mínima e máxima.

    - Umidade média.

    - Alertas de eventos climáticos extremos (calor, frio, chuva, variação brusca de temperatura).

- **Salvamento de dados em JSON:** Os dados brutos da previsão são salvos em arquivos JSON, facilitando o armazenamento ou futuras consultas.

---

## Tecnologias Utilizadas

- **Python:** Linguagem principal do projeto.

- **Requests:** Para realizar chamadas HTTP à API de previsão do tempo.

- **dotenv:** Para carregar variáveis de ambiente, como a chave da API.

- **Datetime:** Para manipulação e exibição das datas.

- **Collections (defaultdict):** Para organizar os dados da previsão por dia.

---
## Como Rodar o Projeto

**1. Clonar o Repositório**

```bash
git clone https://github.com/Zeuzinn/api_previsao_do_tempo.git
cd previsao_do_tempo
```

**2. Instalar Dependências**
```bash
python -m venv venv

source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate     # Para Windows
```
Instale as dependências:
```
pip install -r requirements.txt
```

**3. Configuração da Chave da API**

O projeto utiliza a API do [OpenWeatherMap](https://openweathermap.org/api). Para utilizá-la, você precisa obter uma chave de API no site oficial.

Crie um arquivo `.env` na raiz do projeto e adicione sua chave de API nele:
```
KEY_API=sua_chave_da_api_aqui
```

**4. Executando o Projeto**
```
python app.py
```
O programa solicitará que você insira o nome de uma cidade e, em seguida, exibirá a previsão do tempo para os próximos dias.

