# Use a imagem base do Python
FROM python:3.12

# Instale o Poetry
RUN pip install poetry

# Configure o diretório de trabalho
WORKDIR /app

# Copie o arquivo de definição de dependências do Poetry
COPY pyproject.toml poetry.lock ./
COPY app/src /app

# Instale a dependência pangocairo manualmente
RUN apt-get update && \
    apt-get install -y libpango1.0-dev

# Instale as dependências usando o Poetry
RUN poetry install --no-dev

# Exponha a porta em que o Streamlit será executado (se necessário)
EXPOSE 8501

# Comando de entrada para verificar a presença do arquivo test.py e iniciar o Streamlit
CMD ["bash", "-c", "ls -la src/test.py && poetry run streamlit run src/test.py --server.port=8501 --server.address=0.0.0.0"]
