# Simple Python Compiler

## Member List

| Name                            | NIM      | Class |
| ------------------------------- | -------- | ----- |
| I Gede Arya Raditya Parameswara | 13520036 | K01   |
| Muhammad Garebaldhie Er Rahman  | 13520029 | K01   |
| Adiyansa Prasetya Wicaksana     | 13520044 | K01   |

## Specification

| Name          | Link                                                                                                                |
| ------------- | ------------------------------------------------------------------------------------------------------------------- |
| Specification | [Specification Link](https://docs.google.com/document/d/1Fd8wLOP_GzJ66atpw1yK1_S1dLCFQcKFTgnePFHql7Y/edit)          |
| Groups        | [Group Spreadsheet](https://docs.google.com/spreadsheets/d/10FTPI8DVEaKu22H90p2-twzi4ZX4vC1FAG4c4aJfvgw/edit#gid=0) |

## Features

This Programs allows you to validate your python file and give verdict, whether it accepted or not the program will print the result into your terminal.

## How to use

1. Make sure you have python installed in your computer
2. `git clone https://github.com/gedearyarp/TUBES-TBFO.git`
3. Create file that you want to validate and put it into `test` folder
4. `cd src`
5. Run main.py with the argument `python main.py test/<filename.py>` and you will get the verdict of your file!

## How it works?

1. The program will read the file through the end of the file
2. After read all the lines the program will transform all of the word into token
3. After the token are created, we use CNF in the grammar to validate it
4. If the token follows the rule of the CNF. So whether the program is valid or not it will print the verdict!
