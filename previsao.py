import requests
from datetime import datetime, timedelta


# Api criada para buscar dados de temperatura pelo globo - utilizado o openweather para realizar a busca

class Previsao:
    def __init__(self, cidade, dias):
        self.cidade = cidade.lower()
        self.dias = int(dias)
        self.api_key = "090e11094e8623ff3e4062bf14cf556b"
        self.link_atual = f"https://api.openweathermap.org/data/2.5/weather?q={self.cidade}&appid={self.api_key}&units=metric"
        self.link_previsao = f"https://api.openweathermap.org/data/2.5/forecast?q={self.cidade}&cnt={self.dias * 8}&appid={self.api_key}&units=metric"

    def previsao_tempo(self):
        # Verifica qual API usar com base no número de dias
        if self.dias == 0:
            link = self.link_atual
        elif 1 <= self.dias <= 5:
            link = self.link_previsao
        else:
            aviso = ("Por favor, insira um número entre 0 e 5 para pesquisar a previsão do dia para o seu local informado."
                     "")
            return aviso

        # Criando uma requisição para coletar os dados
        requisicao = requests.get(link)
        if requisicao.status_code != 200:
            return "Erro ao acessar a API. Verifique o nome da cidade e tente novamente."

        requisicao_dic = requisicao.json()

        if self.dias == 0:
            # Informações do tempo atual
            temperatura = requisicao_dic['main']['temp']
            sensacao = requisicao_dic['main']['feels_like']
            maxima = requisicao_dic['main']['temp_max']
            minima = requisicao_dic['main']['temp_min']
            descricao = requisicao_dic['weather'][0]['description']

            # Retorno das informações como um dicionário
            return {
                "cidade": self.cidade.capitalize(),
                "temperatura": temperatura,
                "sensacao_termica": sensacao,
                "temperatura_maxima": maxima,
                "temperatura_minima": minima,
                "descricao": descricao
            }
        elif 1 <= self.dias <= 5:
            # Processamento dos resultados da previsão
            previsoes = requisicao_dic['list']
            hoje = datetime.now().date()
            dia_alvo = hoje + timedelta(days=self.dias)
            previsao_meio_dia = None
            menor_diferenca = timedelta(hours=24)

            for previsao in previsoes:
                data_previsao = datetime.strptime(previsao['dt_txt'], "%Y-%m-%d %H:%M:%S")
                diferenca_horas = abs(
                    data_previsao - datetime.combine(dia_alvo, datetime.strptime("12:00:00", "%H:%M:%S").time()))

                if data_previsao.date() == dia_alvo and diferenca_horas < menor_diferenca:
                    previsao_meio_dia = previsao
                    menor_diferenca = diferenca_horas

            if previsao_meio_dia:
                temperatura = previsao_meio_dia['main']['temp']
                sensacao_termica = previsao_meio_dia['main']['feels_like']
                temperatura_maxima = previsao_meio_dia['main']['temp_max']
                temperatura_minima = previsao_meio_dia['main']['temp_min']
                descricao = previsao_meio_dia['weather'][0]['description']

                return {
                    "data": dia_alvo,
                    "temperatura": temperatura,
                    "sensacao_termica": sensacao_termica,
                    "temperatura_maxima": temperatura_maxima,
                    "temperatura_minima": temperatura_minima,
                    "descricao": descricao
                }
            else:
                return f"Não há previsão disponível para {dia_alvo}."
