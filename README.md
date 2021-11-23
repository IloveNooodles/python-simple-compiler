# TUBES-TBFO

## Member List

| Nama                           | NIM      | Kelas |
| ------------------------------ | -------- | ----- |
| I Gede Arya Raditya P          | 13520036 | K01   |
| Muhammad Garebaldhie Er Rahman | 13520029 | K01   |
| Adiyansa Prasetya Wicaksana    | 13520044 | K01   |

## Spesification

| Nama               | Link                                                                                                                   |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| Spesifikasi        | [Link Spesifikasi](https://docs.google.com/document/d/1Fd8wLOP_GzJ66atpw1yK1_S1dLCFQcKFTgnePFHql7Y/edit)               |
| Pembagian Kelompok | [Spreadsheet Kelompok](https://docs.google.com/spreadsheets/d/10FTPI8DVEaKu22H90p2-twzi4ZX4vC1FAG4c4aJfvgw/edit#gid=0) |

## Features

This Programs allows you to validate your python file and give verdict, wheter it accepted or not and give the error message on what line the programs fails to run.

## How to use

1. Make sure you have python installed in your computer
2. Create file that you want to validate and put it into `test` folder
3. Run main.py with the argument `python main.py ../test/<filename.py>` and you will get the verdict of your file!

## How it works?

1. The program will read the file through the end of the file
2. After read all the lines the program will transform all of the word into token
3. After the token are created, we use CNF in the grammar to validate it
4. If the token follows the rule of the CNF so the program valid if not, the program will fails and
