# Use a imagem base do Python
FROM python:3.12

# Instale o Poetry
RUN pip install poetry

# Configure o diretório de trabalho
WORKDIR /app

# Copie o arquivo de definição de dependências do Poetry
COPY pyproject.toml poetry.lock ./

# Instale a dependência pangocairo manualmente
RUN apt-get update && \
    apt-get install -y libpango1.0-dev

# Instale as dependências usando o Poetry
RUN poetry install --no-dev

# Copie os arquivos do projeto para o contêiner
COPY . .

# Exponha a porta em que o Streamlit será executado (se necessário)
EXPOSE 8501

# Comando de entrada para iniciar o Streamlit
CMD ["poetry", "run", "streamlit", "run", "test.py", "--server.port=8501", "--server.address=0.0.0.0"]
