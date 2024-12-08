# media-downloader
Descrição do Aplicativo:
Nome do Aplicativo: MediaDloader

O MediaGrabber é um aplicativo de interface gráfica desenvolvido para facilitar o download de vídeos e áudios diretamente da internet. Através de uma interface simples e intuitiva, o usuário pode rapidamente baixar conteúdo de plataformas de streaming como YouTube, escolhendo entre os formatos de vídeo (MP4) ou áudio (MP3).

Características:
Download de Vídeos e Áudios: O aplicativo permite que você baixe vídeos no formato MP4 ou extraia áudios em MP3 com alta qualidade.
Interface Gráfica Intuitiva: Utilizando o Tkinter e a biblioteca ttkbootstrap, o aplicativo oferece uma interface visualmente atraente e fácil de usar, com suporte a temas escuros para uma experiência de usuário confortável.
Seleção de Diretório de Download: O usuário pode selecionar facilmente o diretório onde o arquivo será salvo através de um seletor de diretório integrado.
Progresso de Download: Uma barra de progresso mostra em tempo real o status do download, permitindo que o usuário acompanhe a porcentagem concluída.
Múltiplas Qualidades de Áudio: Para downloads de áudio, a qualidade do arquivo pode ser configurada para garantir o melhor som possível.
Nomes de Arquivos Personalizados: O nome do arquivo será automaticamente extraído do título do vídeo e ajustado para evitar caracteres inválidos. Além disso, o aplicativo assegura que arquivos com o mesmo nome não sobrescrevam os existentes, gerando versões numeradas automaticamente, caso necessário.
Multithreading: O download é feito em uma thread separada, garantindo que a interface do aplicativo permaneça responsiva durante o processo de download.
Como Funciona:
Inserção de URL: O usuário insere a URL do vídeo ou áudio desejado na interface.
Escolha do Formato: O formato do arquivo pode ser selecionado entre MP4 (vídeo) ou MP3 (áudio).
Seleção do Diretório de Download: O usuário escolhe a pasta onde o arquivo será salvo.
Download: Após pressionar o botão de download, o aplicativo inicia o processo de captura e armazenamento do conteúdo. Durante o processo, a barra de progresso será atualizada com o andamento do download.
Tecnologias Utilizadas:
Python: Linguagem de programação principal usada para o desenvolvimento.
Tkinter: Biblioteca padrão de Python para criação de interfaces gráficas.
ttkbootstrap: Extensão do Tkinter para facilitar a criação de interfaces modernas e atrativas.
yt-dlp: Ferramenta de linha de comando usada para realizar o download de vídeos e áudios de diversas plataformas online.
Descrição para o Repositório:
Repositório: media-downloader (exemplo)

Este repositório contém o código-fonte para o MediaGrabber, uma ferramenta gráfica simples e poderosa que permite baixar vídeos e áudios de sites de streaming como YouTube. Com suporte a formatos MP4 e MP3, a aplicação é ideal para quem deseja salvar conteúdo multimídia para uso offline de maneira rápida e eficiente.

Funcionalidades:
Baixar vídeos em MP4 com a melhor qualidade disponível (vídeo e áudio combinados).
Extrair áudio em MP3 de vídeos com qualidade máxima.
Interface Gráfica de Usuário (GUI) simples e intuitiva construída com Python, Tkinter e ttkbootstrap.
Monitoramento de progresso com barra de progresso dinâmica.
Seleção de diretório de download com possibilidade de escolha de pasta.
Geração automática de nomes de arquivos com base no título do vídeo, evitando conflitos de arquivos existentes.
Multithreading para garantir que o aplicativo continue responsivo durante o download.
Como Usar:
Instalação:

Certifique-se de ter o Python instalado.
Instale as dependências utilizando o comando:
bash
Copiar código
pip install ttkbootstrap yt-dlp
Executando o Aplicativo:

Clone este repositório ou baixe o código.
Execute o arquivo mediadloader.py:
bash
Copiar código
python mediadloader.py
Instruções de Uso:

Insira a URL do vídeo ou áudio desejado.
Selecione o formato desejado (MP4 ou MP3).
Escolha o diretório onde o arquivo será salvo.
Clique em "Baixar" para iniciar o download.
Acompanhe o progresso do download através da barra de progresso.
Pré-requisitos:
Python 3.x
yt-dlp instalado no sistema (utilizado para capturar o conteúdo das URLs fornecidas).
