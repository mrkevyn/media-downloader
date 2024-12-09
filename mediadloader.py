import os
import subprocess
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import filedialog, messagebox
import threading
import tkinter as tk

# Função para adicionar o menu de contexto com as opções de copiar, cortar e colar
def adicionar_menu_contexto(entry_widget):
    def colar(event=None):
        entry_widget.event_generate("<Control-v>")

    def copiar(event=None):
        entry_widget.event_generate("<Control-c>")

    def cortar(event=None):
        entry_widget.event_generate("<Control-x>")

    # Criar o menu de contexto
    menu = tk.Menu(entry_widget, tearoff=0)
    menu.add_command(label="Colar", command=colar)
    menu.add_command(label="Copiar", command=copiar)
    menu.add_command(label="Cortar", command=cortar)

    # Exibir o menu quando o botão direito do mouse for clicado
    def exibir_menu(event):
        menu.post(event.x_root, event.y_root)

    entry_widget.bind("<Button-3>", exibir_menu)

def obter_titulo_video(url):
    comando = ["yt-dlp", "--get-title", url]
    try:
        titulo = subprocess.check_output(comando, text=True).strip()
        return titulo
    except subprocess.CalledProcessError:
        return "mediadl_download"

def selecionar_diretorio():
    diretorio = filedialog.askdirectory(title="Selecione o diretório de download")
    if diretorio:
        entrada_diretorio.delete(0, END)
        entrada_diretorio.insert(0, diretorio)

def monitorar_progresso(process):
    for line in process.stdout:
        if "download" in line:
            try:
                # Tenta extrair a porcentagem de progresso (exemplo: '50.0%' ou '50.0')
                if "%" in line:
                    percentual = float(line.split()[0].replace('%', ''))
                    progresso["value"] = percentual
                    janela.update_idletasks()  # Atualiza a interface gráfica com a nova porcentagem
            except ValueError:
                pass

def baixar_midia():
    url = entrada_url.get().strip()
    formato = formato_var.get()
    diretorio = entrada_diretorio.get().strip()

    if not url:
        messagebox.showerror("Erro", "Por favor, forneça uma URL válida.")
        return

    if not diretorio:
        messagebox.showerror("Erro", "Por favor, selecione um diretório de download.")
        return

    # Obtém o título do vídeo
    nome_arquivo_base = obter_titulo_video(url)

    # Remove caracteres inválidos para nomes de arquivo
    nome_arquivo_base = "".join(c for c in nome_arquivo_base if c not in r'\/:*?"<>|')

    # Gera um nome de arquivo único
    contador = 1
    nome_arquivo = nome_arquivo_base
    while os.path.exists(os.path.join(diretorio, f"{nome_arquivo}.{formato}")):
        nome_arquivo = f"{nome_arquivo_base}-{contador}"
        contador += 1

    nome_arquivo_completo = os.path.join(diretorio, f"{nome_arquivo}.%(ext)s")

    if formato == "mp4":
        comando = [
            "yt-dlp",
            "-f", "bestvideo+bestaudio",
            "--merge-output-format", "mp4",
            "-o", nome_arquivo_completo,
            "--progress",  # Ativa a saída de progresso
            url,
        ]
    elif formato == "mp3":
        comando = [
            "yt-dlp",
            "-f", "bestaudio",
            "--extract-audio",
            "--audio-format", "mp3",
            "--audio-quality", "0",
            "-o", nome_arquivo_completo,
            "--progress",  # Ativa a saída de progresso
            url,
        ]
    else:
        messagebox.showerror("Erro", "Formato inválido!")
        return

    # Rodando o comando em uma thread separada para não travar a interface gráfica
    def executar_download():
        try:
            # Inicia o processo e captura a saída para monitorar o progresso
            process = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            monitorar_progresso(process)  # Chama a função para monitorar o progresso
            process.communicate()  # Espera o processo terminar
            messagebox.showinfo("Sucesso", f"Download concluído! Arquivo salvo em:\n{diretorio}")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Erro", f"Erro ao baixar a mídia: {e}")

    # Inicia o download em uma thread separada
    threading.Thread(target=executar_download, daemon=True).start()

# Configuração da janela principal
janela = ttk.Window(themename="darkly")
janela.title("Media Downloader")
janela.geometry("500x400")

# Layout com grid para um alinhamento melhor
janela.columnconfigure(0, weight=1)

# Widgets
ttk.Label(janela, text="URL do vídeo/áudio:", bootstyle="inverse").grid(row=0, column=0, pady=5, padx=10, sticky="w")
entrada_url = ttk.Entry(janela, width=50, bootstyle="dark")
entrada_url.grid(row=1, column=0, pady=5, padx=10)
adicionar_menu_contexto(entrada_url)

ttk.Label(janela, text="Formato de download:", bootstyle="inverse").grid(row=2, column=0, pady=5, padx=10, sticky="w")
formato_var = ttk.StringVar(value="mp4")
ttk.Radiobutton(janela, text="MP4 (vídeo)", variable=formato_var, value="mp4", bootstyle="success").grid(row=3, column=0, pady=5, padx=10, sticky="w")
ttk.Radiobutton(janela, text="MP3 (áudio)", variable=formato_var, value="mp3", bootstyle="info").grid(row=4, column=0, pady=5, padx=10, sticky="w")

ttk.Label(janela, text="Diretório de download:", bootstyle="inverse").grid(row=5, column=0, pady=5, padx=10, sticky="w")
frame_diretorio = ttk.Frame(janela)
frame_diretorio.grid(row=6, column=0, pady=5, padx=10)

entrada_diretorio = ttk.Entry(frame_diretorio, width=40, bootstyle="dark")
entrada_diretorio.grid(row=0, column=0, padx=5)
btn_selecionar_diretorio = ttk.Button(frame_diretorio, text="Selecionar", command=selecionar_diretorio, bootstyle="primary")
btn_selecionar_diretorio.grid(row=0, column=1)

# Barra de progresso
progresso = ttk.Progressbar(janela, length=300, bootstyle="primary", mode="determinate")
progresso.grid(row=7, column=0, pady=10, padx=10)

# Botão de download
btn_baixar = ttk.Button(janela, text="Baixar", command=baixar_midia, bootstyle="success")
btn_baixar.grid(row=8, column=0, pady=20, padx=10)

# Executar o loop da interface
janela.mainloop()

