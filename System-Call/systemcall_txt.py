import os
import time
def criar_arquivo(nome_arquivo, mensagem):
    try:
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(mensagem)
        print(f"Arquivo '{nome_arquivo}' criado com sucesso!")
    except OSError as e:
        print(f"Erro ao criar o arquivo: {e}")

def editar_arquivo(nome_arquivo, nova_mensagem):
    try:
        if os.path.exists(nome_arquivo):
            with open(nome_arquivo, 'w') as arquivo:
                arquivo.write(nova_mensagem)
            print(f"Arquivo '{nome_arquivo}' editado com sucesso!")
        else:
            print(f"Erro: O arquivo '{nome_arquivo}' não existe.")
    except OSError as e:
        print(f"Erro ao editar o arquivo: {e}")

def adicionar_ao_arquivo(nome_arquivo, mensagem):
    try:
        if os.path.exists(nome_arquivo):
            with open(nome_arquivo, 'a') as arquivo:
                arquivo.write("\n" + mensagem)
            print(f"Mensagem adicionada ao arquivo '{nome_arquivo}' com sucesso!")
        else:
            print(f"Erro: O arquivo '{nome_arquivo}' não existe.")
    except OSError as e:
        print(f"Erro ao adicionar ao arquivo: {e}")

def main():
  nome_arquivo = input("Digite o nome do arquivo (ex: arquivo.txt): ")
  mensagem = input("Digite a mensagem para escrever no arquivo: ")

  criar_arquivo(nome_arquivo, mensagem)

  opcao = input("Deseja editar (e) ou adicionar (a) (enter para encerrar): ").lower()

  if opcao == 'e':
      nova_mensagem = input("Digite uma nova mensagem: ")
      editar_arquivo(nome_arquivo, nova_mensagem)
  elif opcao == 'a':
      mensagem_adicional = input("Digite a mensagem para ser adicionada no arquivo: ")
      adicionar_ao_arquivo(nome_arquivo, mensagem_adicional)
  else:
      print("Encerrando o programa.")
      time.sleep(1)
main()
