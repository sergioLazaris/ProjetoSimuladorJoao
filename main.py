import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Importar PIL para carregar imagens

# Função para calcular a velocidade média
def calcular_velocidade_media():
    try:
        distancia = float(entry_distancia.get())
        tempo = float(entry_tempo.get())

        if tempo == 0:
            raise ValueError("O tempo não pode ser zero!")

        # Calcula a velocidade média
        velocidade_media = distancia / tempo
        label_resultado.config(text=f"Velocidade média: {velocidade_media:.2f} km/h")

        # Inicia a animação do carrinho
        animar_carrinho(velocidade_media)

    except ValueError as ve:
        messagebox.showerror("Erro", f"Entrada inválida: {ve}")

# Função para animar o carrinho
def animar_carrinho(velocidade_media):
    # Limpa a tela antes de iniciar a animação
    canvas.delete("all")

    # Define a largura da tela e a posição inicial do carrinho
    largura_tela = canvas.winfo_width()
    posicao_inicial = 0
    velocidade_pixels_por_segundo = velocidade_media * 10  # Multiplicador para visibilidade

    # Carregar a imagem de fundo (estrada)
    estrada_img = Image.open("estrada.png")  # Coloque o caminho correto da sua imagem da estrada
    estrada_img = estrada_img.resize((600, 400))  # Ajuste o tamanho da imagem
    estrada_tk = ImageTk.PhotoImage(estrada_img)

    # Adiciona a imagem de fundo (estrada) no canvas
    canvas.create_image(0, 0, image=estrada_tk, anchor=tk.NW)
    canvas.image = estrada_tk  # Manter a referência da imagem de estrada

    # Carregar a imagem do carrinho
    carrinho_img = Image.open("carrinho.png")  # Coloque o caminho correto da sua imagem
    carrinho_img = carrinho_img.resize((50, 30))  # Ajuste o tamanho da imagem do carrinho
    carrinho_tk = ImageTk.PhotoImage(carrinho_img)

    # Desenha o carrinho com a imagem
    carrinho = canvas.create_image(posicao_inicial, 165, image=carrinho_tk)
    canvas.image = carrinho_tk  # Manter a referência da imagem do carrinho

    # Função para mover o carrinho
    def mover_carrinho():
        nonlocal posicao_inicial

        # Mover a estrada para dar a sensação de movimento infinito
        canvas.move(estrada, -velocidade_pixels_por_segundo * 0.1, 0)

        # Se a estrada sair da tela, resetamos ela (movimento infinito)
        if posicao_inicial > largura_tela:
            canvas.coords(estrada, 0, 0)
            posicao_inicial = 0

        if posicao_inicial < largura_tela:
            posicao_inicial += velocidade_pixels_por_segundo * 0.1  # Atualiza a posição (0.1 para controle)
            canvas.coords(carrinho, posicao_inicial, 165)  # Atualiza a posição da imagem do carrinho
            root.after(50, mover_carrinho)  # Chama a função a cada 50ms (ajusta a velocidade)

    # Inicia a animação
    mover_carrinho()

# Criando a janela principal
root = tk.Tk()
root.title("Simulador de Velocidade Média")

# Definindo o tamanho da janela
root.geometry("600x400")

# Rótulos
label_distancia = tk.Label(root, text="Distância (km):")
label_distancia.pack(pady=5)

entry_distancia = tk.Entry(root)
entry_distancia.pack(pady=5)

label_tempo = tk.Label(root, text="Tempo (horas):")
label_tempo.pack(pady=5)

entry_tempo = tk.Entry(root)
entry_tempo.pack(pady=5)

# Botão para calcular
botao_calcular = tk.Button(root, text="Calcular", command=calcular_velocidade_media)
botao_calcular.pack(pady=10)

# Rótulo para mostrar o resultado
label_resultado = tk.Label(root, text="Velocidade média: -")
label_resultado.pack(pady=5)

# Criando o canvas para desenhar o carrinho
canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack(pady=20)

# Iniciar a GUI
root.mainloop()
