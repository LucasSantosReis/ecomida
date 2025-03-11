# Usar a imagem base do Python
FROM python:3.9

# Definir o diretório de trabalho
WORKDIR /app

# Copiar o arquivo de dependências para instalar antes
COPY requirements.txt /app/

# Atualizar pip e instalar as dependências do projeto
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código da aplicação
COPY . /app/

# Expor a porta que o Uvicorn usará
EXPOSE 8000

# Comando para rodar a aplicação com Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
