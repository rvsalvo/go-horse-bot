FROM python:3
WORKDIR /go-horse-bot
COPY ./src/main.py /go-horse-bot/main.py
RUN pip install discord
RUN pip install requests
RUN pip install python-dotenv
CMD [ "python", "-u", "./main.py" ]