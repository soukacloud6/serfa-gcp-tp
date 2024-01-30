#on recupere depuis dockerhub une image de base de python 
FROM python:3.12.1-slim
WORKDIR /usr/src/app
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["sh","-c","sleep 5 \ 
&& python -m flask run --host=0.0.0.0"]
