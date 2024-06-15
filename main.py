# Importa a classe AppCeuAzul do arquivo onde ela está definida
from janela_principal import AppCeuAzul


# font titulos -  kodchasan
# font textos - Noto Sans Hebrew

def main():
    app = AppCeuAzul()  # Cria uma instância da classe AppCeuAzul
    app.run()  # Executa o método run da instância


# Verificação para garantir que main() será chamado apenas se o script for executado diretamente
if __name__ == "__main__":
    main()
