# Using pm4py image
FROM javert899/pm4py:latest
# Defining working directory and copy the requirements file
WORKDIR /usr/src/myapp
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python3","app.py"]