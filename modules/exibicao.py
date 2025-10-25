from datetime import datetime

def exibir_previsao(data, temp_min, temp_max, humidade, clima, alerta):
    data_formatada = datetime.strptime(data, "%Y-%m-%d").strftime("%d/%m/%Y")

    print(f"""📅 {data_formatada}
- Clima predominante: {clima}
- Mínima: {temp_min:.1f}°C | Máxima: {temp_max:.1f}°C
- Humidade média: {humidade:.0f}%
- 🔔 Alertas: {alerta}
-------------------------------""")
