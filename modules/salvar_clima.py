import json
import os
from datetime import datetime

def salvar_em_json(cidade, dados):
    os.makedirs("data", exist_ok=True)

    # Formata o nome do arquivo com cidade e data/hora atual
    agora = datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_arquivo = f"data/{cidade}_{agora}.json"

    # Salva os dados brutos da API em formato JSON
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

    print(f"\n💾 Previsão salva em: {nome_arquivo}")
