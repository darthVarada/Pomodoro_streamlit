
FROM python:3.12.2

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia os arquivos restantes para o diretório de trabalho
COPY . .

# Expor a porta que o Streamlit irá utilizar (substitua pela porta do seu aplicativo, se necessário)
EXPOSE 8501

# Comando para iniciar o seu aplicativo quando o contêiner for iniciado
CMD ["streamlit", "run", "seu_arquivo_streamlit.py"]
