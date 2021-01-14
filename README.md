# Консольная утилита, выполняющая поиск слова в тексте
### Нечесов Андрей
___

## Поставленная задача
- Реализовать консольную утилиту, выполняющую поиск слова и его словоформ во  
  входном файле. На выходе программа должна выводить контекст и номер строки вхождений слова в тексте 
  
## Установка необходимых библиотек
___
```shell
pip3 install -r requirements.txt
```

## Формат входных данных
___
```shell
usage: main.py [-h] [-i FILE_IN] [-w WORD_TO_FIND] [-enc ENCODING] [-v VERBOSE] [-o FILE_OUT] [-n AMOUNT_OF_STRINGS] file_in word_to_find

Without description

positional arguments:
  file_in               path to text file
  word_to_find          word to find

optional arguments:
  -h, --help            show this help message and exit
  -i FILE_IN            Path to text file
  -w WORD_TO_FIND       Word to find
  -enc ENCODING         Encoding of input file
  -v VERBOSE            Prints the program status to the console
  -o FILE_OUT           Path to output file. If not specified, the utility prints output to the stdout
  -n AMOUNT_OF_STRINGS  Amount of strings to output
```
## Формат выходных данных
___
Вывод в консоль или файл (в зависимости от опциональных аргументов)

## Примеры использования
___
```shell
python3 main.py -n 15 texts/lirika.txt я
```