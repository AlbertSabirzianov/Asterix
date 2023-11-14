# Asterix
Игра про Астерикса, самого хитрого и отважного война одной непокорной гальской деревушки!
Цель игры - победить армию римлян и самого Юлия Цезаря. Будте осторожны -
Астерикс неуязвим только под действием волшебного напитка, так что не забывайте 
выпить его перед столкновением с римлянами, для этого вам нужно подбежать к
фляге с напитком. Весёлой Игры!
# Технологии
Игра написана на популярано библиотеке pygame
# Установка
Скачайте игру на свой компьютер
```commandline
git clone https://github.com/AlbertSabirzianov/Asterix.git
```
Установите зависимости
```commandline
pip install requirements.txt
```
Запустите игру
```commandline
python main.py
```
# Настройки
Все аспекты игры вы можете настроить под себя, для этого
вам необходимо открыть файл settings.py и найти ту настройку,
которая вам нужна
### Настройка Изображений и музыки
Все переменные, начинающиеся с PATH_ указывают на путь до изображений, как здесь
```python
PATH_TO_LANDSCAPE = 'images/landscape.png'
PATH_TO_ASTERIX = 'images/Asterix_new_3.png'
PATH_TO_ROMANS = 'images/w-romans.png'
PATH_TO_FLASK = 'images/magic-flask.png'
PATH_TO_ASTERIX_AND_IDEA_FIX = 'images/asterix_and_ideafix.png'
PATH_TO_CESAR = 'images/cesar.png'
PATH_TO_SUPER_POWER = 'images/superpower_new.png'
PATH_TO_HELMET = 'images/casca.png'
```
Или до звуковых файлов, как здесь
```python
PATH_TO_GAME_MUSIC = 'music/game_music.mp3'
PATH_TO_HIT_MUSIC = 'music/hit.wav'
PATH_TO_FLASK_MUSIC = 'music/flask.wav'
PATH_TO_CRASH_MUSIC = 'music/mech-zvonkiy-yarkiy.wav'
PATH_TO_WINNING_MUSIC = 'music/fanfar.wav'
PATH_TO_ROMANS_FLY_MUSIC = 'music/romans_fly.mp3'
```
Чтобы заменить изображение любого персанажа, фона или
звукового сопровождения достаточно указать путь до нового
файла здесь.
### Настройки Астерикса
Настройка первоначальной позиции Астерикса
```python
ASTERIX_POSITION = (300, 300)
``` 
Настройка колличества жизней
```python
ASTERIX_LIVES = 100
```
Размер Астерикса (чем больше число - тем меньше Астерикс и наоборот)
```python
ASTERIX_SIZE_DIVIDER = 5
```
Обычная скорость Астерикса
```python
ASTERIX_SPEED = 10
```
Скорость под действием волшебного зелья
```python
ASTERIX_MAGIC_SPEED = 20
```
Время действия волшебного зелья
```python
ASTERIX_SUPER_POWER_TIME_OUT = 200 
```
### Настройки Римлян
Скорость римлян
```python
ROMANS_SPEED = 5
```
Скорость полёта от удара Астерикса
```python
ROMANS_FLY_SPEED = 50
```
Скорость появления нового римлянина
```python
ROMANS_TIME_OUT = 50
```
Максимальное количество римлян на экране
```python
ROMANS_MAX_AMOUNT = 8
```
Размер армии римлян
```python
ROMANS_ARMY_SIZE = 60
```
Размер Римлянина (чем больше число - тем меньше Римлянин и наоборот)
```python
ROMANS_SIZE_DIVIDER = 7
```
Плавность движения Римлянина
```python
ROMANS_SMOOTHNESS = 20
```
### Настройки шрифта
Шрифт
```python
FONT = 'script'
```
Размер шрифта
```python
FONT_SIZE = 80
MINI_FONT_SIZE = 40
```
### Текст конца игры
Текст в случае выйгрыша
```python
WINING_GAME_TEXT = 'YOU_WIN'
```
Текст в случае проигрыша
```python
LOSE_GAME_TEXT = 'GAME_OVER'
```


