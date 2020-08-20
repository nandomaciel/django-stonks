<center>

# Stocks

Stock price real-time using Django Channels.

![stonks-meme](stonks.jpeg)

</center>

## Install

``` shell
python -m venv env
source env/bin/activate
pip3 install requirements.txt
```

## Run

``` shell
python manage.py runserver
``` 

## DB

**Redis**

``` shell
docker run -p 6379:6379 -d redis:5
```

## Browser

``` js
http://localhost:8000
```