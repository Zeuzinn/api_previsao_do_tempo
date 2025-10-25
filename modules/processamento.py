from collections import defaultdict
from modules.exibicao import exibir_previsao


def extrair_dados(dados):
    dias = agrupar_por_dia(dados)

    print("\n=== Previsão para os próximos dias ===\n")

    for data, previsoes in list(dias.items())[:5]:
        temps = [p['main']['temp'] for p in previsoes]
        temp_min = min([p['main']['temp_min'] for p in previsoes])
        temp_max = max([p['main']['temp_max'] for p in previsoes])
        humidade = sum([p['main']['humidity'] for p in previsoes]) / len(previsoes)

        descricoes = [p['weather'][0]['description'] for p in previsoes]

        # Pega a descrição do clima que mais se repete e armazena em 'clima'
        clima = max(set(descricoes), key=descricoes.count)

        chuva = verificar_chuva(previsoes)
        variacao = verificar_variacao_bruta(previsoes)
        alerta = gerar_alertas(temp_max, temp_min, chuva, variacao)

        exibir_previsao(data, temp_min, temp_max, humidade, clima, alerta)
    

def agrupar_por_dia(dados):
    dias = defaultdict(list)
    for item in dados['list']:
        data = item['dt_txt'].split(' ')[0]
        dias[data].append(item)
    return dias


def verificar_chuva(dados_dia):
    return any('rain' in item and '3h' in item['rain'] for item in dados_dia)


def verificar_variacao_bruta(dados_dia):
    temps = [item['main']['temp'] for item in dados_dia]
    return (max(temps) - min(temps)) > 8


def gerar_alertas(temp_max, temp_min, chuva, variacao):
    alertas = []

    if temp_max > 35:
        alertas.append(f"⚠️ Calor extremo: {temp_max}°C")
    if temp_min < 5:
        alertas.append(f"❄️ Frente fria: {temp_min}°C")
    if chuva:
        alertas.append("🌧️ Chuva prevista – leve guarda-chuva")
    if variacao:
        alertas.append("📉 Variação brusca de temperatura (>8°C)")

    return " | ".join(alertas) if alertas else "Sem alertas significativos"
