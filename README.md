conllu.py
=========
CoNLL-U format library for Python

Original code Copyright (c) 2014 Sampo Pyysalo and distributed under the MIT license. (See LICENSE in the main folder)

*2017/07/26 Modifications by Pouya Lajevardi and Émilie Pagé-Perron*


### This tool runs with Python 2

## Operation
Fed a conllu file, this script will output a .txt file containing the unannotated text and a .ann file, containing the brat standoff format annotations. Both files have the same filename so they just need to be put in a subfolder of the brat data folder to render properly.

'''
 conllu2brat -i example-data/cdli
'''