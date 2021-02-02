Два способа запуска автотеста:
1) Запустить сервер localhost:4444: 
docker run -d -p 4444:4444 selenium/standalone-chrome

2) Сбилдить образ:
docker build -t chrome_autotest:1.0 . 

3) Запустить dockerfile:
docker run chrome_autotest:1.0

ИЛИ

1) Запустить сервер localhost:4444: 
docker run -d -p 4444:4444 selenium/standalone-chrome

2) В комадной строке прописать команду:
pytest -v test_homepage.py
----------------------------------------------
Дебаг для просмотра с помощью VNCViewer:
1) Запустить сервер localhost:5900
docker run -d -p 4444:4444 -p 5900:5900 -v /dev/shm:/dev/shm selenium/standalone-chrome:4.0.0-beta-1-prerelease-20210201

2) Сбилдить образ (если уже сбилдили, то второй раз не нужно):
docker build -t chrome_autotest:1.0 . 

3) Запустить dockerfile:
docker run chrome_autotest:1.0

В VNCViewer по адресу localhost:5900 будет запущен браузер Chrome для демонстрации автотеста
