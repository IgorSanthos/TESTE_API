import tkinter as tk
from tkinter import PhotoImage
import requests


# Função para chamar a API de criar pastas de cliente
def check_version():
    try:
        response = requests.get('https://nome-do-seu-servico.onrender.com/api/version')
        if response.status_code == 200:
            version_info = response.json()
            print(f"Versão Atual: {version_info['version']}")
        else:
            print("Erro ao verificar a versão.")
    except Exception as e:
        print(f"Erro na conexão com a API: {e}")



# Função para chamar a API de importar notas de serviço




def criate():
    try:
        response = requests.post('https://teste-api-ndzk.onrender.com/api/download')
        if response.status_code == 200:
            data = response.json()
            print(data['message'])
        else:
            print("Erro ao iniciar o download.")
    except Exception as e:
        print(f"Erro na conexão com a API: {e}")

def import_serv():
    try:
        response = requests.post('https://teste-api-ndzk.onrender.com/api/download')
        if response.status_code == 200:
            data = response.json()
            print(data['message'])
        else:
            print("Erro ao importar notas de serviço.")
    except Exception as e:
        print(f"Erro na conexão com a API: {e}")

# Função para chamar a API de download de notas de serviço
def download():
    try:
        response = requests.post('https://teste-api-ndzk.onrender.com/api/download')
        if response.status_code == 200:
            data = response.json()
            print(data['message'])
        else:
            print("Erro ao iniciar o download.")
    except Exception as e:
        print(f"Erro na conexão com a API: {e}")


def fechar_janela():
    print('janela fechada')
    root.destroy()

###     INTERFACE       ###
root = tk.Tk()
root.title("Meu Widget com Imagem")
# Remover a moldura da janela (opcional, mas geralmente necessário para transparência)
root.overrideredirect(True)
# Definir o fundo da janela como uma cor que será transparente
root.attributes("-transparentcolor", "gray")
# Definir o tamanho e a posição da janela
root.geometry("500x259+1000+160")
root.title("Janela com Bordas Arredondadas")

# Configurar o frame para os botões
frame_botoes = tk.Frame(root, bg="white")  # Frame colorido para não ser transparente
frame_botoes.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

# Adicionar botões ao frame
botao1 = tk.Button(
    frame_botoes, 
    text="Criar pastas de cliente", 
    command=criate, 
    bg="white", 
    fg="blue", 
    width=30, 
    height=1, 
    font=("Arial", 12),
    bd=0,  # Largura da borda
    activebackground="lightblue"  # Cor do fundo quando o botão é clicado
)
botao1.pack(pady=5)

# Botão 2
botao2 = tk.Button(
    frame_botoes, 
    text="Baixar notas de Serviços", 
    command=download, 
    bg="white", 
    fg="blue", 
    width=30, 
    height=1, 
    font=("Arial", 12),
    bd=0,  # Largura da borda
    activebackground="lightblue"  # Cor do fundo quando o botão é clicado
)
botao2.pack(pady=5)

# Botão 3
botao3 = tk.Button(
    frame_botoes, 
    text="Importar notas de Serviço", 
    command=import_serv, 
    bg="white", 
    fg="blue", 
    width=30, 
    height=1, 
    font=("Arial", 12),
    bd=0,  # Largura da borda
    activebackground="lightblue"  # Cor do fundo quando o botão é clicado
)
botao3.pack(pady=5)

# Botão para fechar a janela
botao_fechar = tk.Button(
    frame_botoes, text="Sair",
    command=fechar_janela, 
    bg="white", 
    width=5, 
    height=1,
    bd=0,  # Largura da borda
    activebackground="#FFAEC9"
    )
botao_fechar.place(x=10, y=200)

# Botão para parar AMELIA
botao_fechar = tk.Button(
    frame_botoes, text="Parar",
    command=fechar_janela, 
    bg="#FFAEC9", 
    width=5, 
    height=1,
    bd=0,  # Largura da borda
    activebackground="red"
    )
botao_fechar.place(x=60, y=200)

# Carregar a imagem
imagem_fundo = PhotoImage(file="amelia.png")
imagem_label = tk.Label(root, image=imagem_fundo, bg="gray")
imagem_label.pack(side=tk.RIGHT, fill=tk.Y)

root.mainloop()