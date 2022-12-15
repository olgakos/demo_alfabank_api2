API тесты для публичных сервисов Alfabank

<p align="center">
<img title="Logo" width="120" src="images/Alfa-Bank.png" alt="Logo Alfa Bank" width="600">
</p>

## Демо-проект по автоматизации тестирования API: alfabank.by
:earth_americas: <a target="_blank" href="https://developerhub.alfabank.by/developerhub/site/pages/item-info.jag?name=partner.public&version=1.0.1&provider=admin&tab=doc">https://developerhub.alfabank.by</a>
<br>Публичный сервис позволяет получать:
- актуальные курсы валют Альфа-Банка 
- актуальные курсы валют Национального банка Республики Беларусь
- коды банков Республики Беларусь и Российской Федерации

### :watermelon: Реализованы следующие проверки:

#### Для всех запросов проверяем, что:

<br>:white_check_mark: статус-код страницы 200
<br>:white_check_mark: тело api-запроса не пусто (!=0)
<br>:white_check_mark: schema (типы данных всех проверяемых значений) верные
  
#### Курсы валют банка:
<br>:white_check_mark: даты курса актуальна (всегда текущая)
<br>:white_check_mark: параметры запроса соответствуют ожидаемым значениям:

При конвертация валюты Республики Беларусь:
```
['buyCode'] == 933
['buyIso'] == 'BYN'
['sellIso'] == 'EUR'
['name'] == 'евро'
```
При конвертации Российской валюты:
```
['buyCode'] == 643
['buyIso'] == 'RUB'
['sellIso'] == 'EUR'
['name'] == None
```

#### Курсы валют Национального банка Республики Беларусь
<br>:white_check_mark: даты курса актуальна (всегда текущая)
<br>:white_check_mark: параметры запроса соответствуют ожидаемым значениям:
```
['iso'] == "EUR"
['code'] == 978 
['name'] == "евро"
['iso'] == "USD"
['code'] == 840
['name'] == "доллар США"
```
#### Коды банков
<br>:white_check_mark: параметры запроса соответствуют ожидаемым значениям:
```
['totalRowCount'] == 1
["bic"] == "ALFABY2X"
['name'] == "ЗАО 'АЛЬФА-БАНК', Г.МИНСК, РБ"
['address'] == прочерк
```
------
ver2 2022-12-15
