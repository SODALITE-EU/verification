# Using python:3.8-alpine image
FROM python:3.11.0a2-alpine
# Defining working directory and copy the requirements file
WORKDIR /usr/src/myapp
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python3","app.py"]