# Imagen base oficial de Python
FROM python:3.10-slim

# Etiqueta con tu nombre
LABEL maintainer="Christopher D. Jimenez"

# Copiar los archivos al contenedor
WORKDIR /app
COPY calculadora.py .
COPY christopherjimenez.yml .

# Comando por defecto al ejecutar el contenedor
CMD ["python", "calculadora.py"]
