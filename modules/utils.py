from modules import language

def get_user_interval():
    prompt = language.langString.get('question_interval', "question_interval")
    err = language.langString.get('question_interval_e', "question_interval_e")
    while True:
        try:
            val = int(input(f"❔ {prompt}\n→ "))
            return val
        except ValueError:
            print(err)

def get_fullTimeFormat(seconds):
    # Logic

    # 1. Horas (HH):
    # - Quantas horas tem em um total de segundos, dividimos por 3600:
    # 1 hora = 60 minutos * 60 segundos = 3600 segundos

    # 2. Minutos (MM):
    # - Depois de retirar as horas, o que sobra pode conter minutos:
    # minutos = (segundos_restantes) // 60

    # 3. Segundos (SS):
    # - O restante disso tudo são os segundos que não completam mais nenhum minuto:
    # segundos_restantes = segundos % 60

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    # Formatar com dois dígitos (ex: 01:05:09)
    return f"{hours:02}:{minutes:02}:{secs:02}"