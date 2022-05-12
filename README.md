# ТЕСТИРОВАНИЕ ИНФОРМАЦИОННОЙ СИСТЕМЫ "Тату-салон"
## Тест-кейсы:

Тест-кейс №1                      | Создать услугу
--------------------------------- | --------------------------------------
Предусловия тест кейса:           | Сайт открыт на странице «Услуги»
Шаги тест кейса:                  | 1)В форме «ADD SERVICE» в поле  
                                  | «Name» ввести название услуги-Пирсинг
                                  | 2)В поле «Price» ввести цену – 500
                                  | 3)Нажать на кнопку «ADD SERVICE»
Ожидаемый результат тест кейса:   | Услуга успешно создана
--------------------------------- | --------------------------------------

Тест-кейс №2                      | Редактировать услугу
--------------------------------- | --------------------------------------
Предусловия тест кейса:           | Сайт открыт на странице «Услуги»
Шаги тест кейса:                  | 1)В форме «UPDATE» в поле «ID»  
                                  | ввести id услуги – 4
                                  | 2)В поле «Name» ввести название 
                                  | услуги - Пирсинг
                                  | 3)В поле «Price» ввести цену – 650
Ожидаемый результат тест кейса:   | Услуга успешно редактирована
--------------------------------- | --------------------------------------

Тест-кейс №3                      | Найти  услугу
--------------------------------- | --------------------------------------
Предусловия тест кейса:           | Сайт открыт на странице «Услуги»
Шаги тест кейса:                  | 1)В форме «GET ABOUT SERVISES»   
                                  | в поле «ID» ввести id услуги – 4
                                  | 2)Нажать на кнопку «GET ONE»
Ожидаемый результат тест кейса:   | Услуга успешно найдена
--------------------------------- | --------------------------------------

Тест-кейс №3                      | Удалить услугу
--------------------------------- | --------------------------------------
Предусловия тест кейса:           | Сайт открыт на странице «Услуги»
Шаги тест кейса:                  | 1)В форме «DELETE SERVISES»   
                                  | в поле «ID» ввести id услуги – 4
                                  | 2)Нажать на кнопку «DELETE»
Ожидаемый результат тест кейса:   | Услуга успешно удалена
--------------------------------- | --------------------------------------