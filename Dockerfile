FROM python:3.6.8-slim 
RUN mkdir /app
WORKDIR /app
COPY . /app
# RUN pip install --quiet --trusted-host pypi.python.org -r requirements.txt
RUN pip install -r requirements.txt
ADD . /app/
# CMD ["python", "main.py"]
# EXPOSE 8000

