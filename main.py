# ДЗ
# 1. Необходимо выбрать сайт с однородно-повторяющейся информацией (отзывы о
# чем-то, описание объектов, резюме, вакансии и т.д.) и выполнить парсинг
# однородных данных с помощью библиотеки BeautifulSoup.
# 2. Результаты сохранять в csv файл, содержащий не менее 3-х столбцов. Например,
# модель телефона, отзыв, дата отзыва.
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

# Подключаем библиотеки
from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

# 1. Парсинг сайта по продаже смартфонов

URL = 'https://yaroslavl.blizko.ru/predl/computer/communications/mobile/smartfony'      # адрес сайта
page = requests.get(URL)           # запрос данных без возможности изменения
print(page.status_code)           # код проверки ответа от сайта

soup = BeautifulSoup(page.text, 'html.parser')          # запрашиваем текст и пишем, что хотим парсить

rev_name = []                     # пустой список под наименования
rev_description = []              # пустой список под описания
rev_price = []                    # пустой список для цен

# Получим все наименования смартфонов
name = soup.find_all('a', class_ = 'title- js-ykr-action js-conversion-event js-send-go-to-product-card')     # получаем все теги с указанным классом
print('количество наименований предложений: ', len(name))
print(type(name))          # проверим тип запрашиваемых данных
print('–––––––')

# Пройдём по всем заголовкам объявлений
for rev in name:
    print(rev.text)         # выведем их на экран колонкой
    rev_name.append(rev.text)           # закинем полученные данные в список

print('––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––')

# Получим все описания смартфонов
description = soup.find_all('div', class_ = 'announce-')        # получаем все теги с указанным классом
print('количество описаний объявлений: ', len(description))
print(type(description))            # проверим тип запрашиваемых данных
print('–––––––')

# Пройдем по всем ценам
for desc in description:
    print(desc.text)        # выведем их на экран колонкой
    rev_description.append(desc.text)           # закинем полученные данные в список

print('––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––')

# Получим все цены
prices = soup.find_all('i', class_ = 'bp-price fsn')        # получаем все теги с указанным классом
print('количество цен: ', len(prices))
print(type(prices))                 # проверим тип запрашиваемых данных
print('–––––––')

# Пройдем по всем ценам
for price in prices:
    print(price.text)           # выведем их на экран колонкой
    rev_price.append(price.text)        # закинем полученные данные в список


# 2. Cохраним данные в csv файл в виде таблицы

# Создадаим датафрейм
df = pd.DataFrame({'Модель' : rev_name,
    'Описание' : rev_description,
     'Цена' : rev_price
})
print(df)      # выведем датафрейм для обзора

# Сохраним датафрейм в csv файл
df.to_csv('smartphones.csv')