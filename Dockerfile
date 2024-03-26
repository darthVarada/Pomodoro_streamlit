FROM python:3.12.2

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Instala as dependências do Manim
RUN pip install manim

# Instala o Scoop
RUN apt-get update && apt-get install -y sudo
RUN apt-get install -y git && apt-get install -y procps curl sudo unzip
RUN sudo apt-get install -y powershell

SHELL ["pwsh", "-Command", "$ErrorActionPreference = 'Stop'; $ProgressPreference = 'SilentlyContinue';"]

RUN Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Instale o Scoop
RUN iwr -useb get.scoop.sh | iex

# Atualize os repositórios
RUN scoop update

# Adicione o diretório do Manim ao PATH
RUN scoop bucket add extras
RUN scoop install ffmpeg

# Copia o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia os arquivos restantes para o diretório de trabalho
COPY . .

# Expor a porta que o Streamlit irá utilizar (substitua pela porta do seu aplicativo, se necessário)
EXPOSE 8501

# Comando para iniciar o seu aplicativo quando o contêiner for iniciado
CMD ["streamlit", "run", "test.py"]