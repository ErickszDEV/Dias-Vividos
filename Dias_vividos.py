from datetime import datetime
def calcular_dias_vividos():
    while True:
        data_nascimento_str = input("Digite a data de nascimento (formato: DD-MM-AAAA): ")
        try:
            data_nascimento = datetime.strptime(data_nascimento_str, "%d-%m-%Y")
            data_atual = datetime.now()
            dias_vividos = (data_atual - data_nascimento).days
            print(f"Você já viveu {dias_vividos} dias.")
            break
        except ValueError:
            print("Data de nascimento inválida. Certifique-se de usar o formato DD-MM-AAAA.")

if __name__ == "__main__":
    calcular_dias_vividos()
