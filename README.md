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

## Description
This tool converts a CoNLL-U file to Brat format.

More information on the CONLL-U file format can be found [here](http://universaldependencies.org/format.html).

More information on the brat standoff format can be found [here](http://brat.nlplab.org/standoff.html).

## Using the Tool 

### Installation
If you don't have pip installed on your system, please find the instructions [here] (https://pip.pypa.io/en/stable/installing/).

To install this converter, you can run the following commands:

```
pip install git+https://github.com/cdli-gh/conllu.py.git
```

### Upgrading
To upgrade this tool, you can run the following commands:

```
pip install git+https://github.com/cdli-gh/conllu.py.git --upgrade
```

### Execution
To use/execute this tool on conllu file or folder, run one of the following commands:

```
cconllu2brat -i example-data/cdli/ 
```

To see processing messages on the console, use the --verbose/-v option:
```
conllu2brat -i example-data/cdli/  -v
```

To view all possible options, use the --help option:
```
conllu2brat --help

Usage: conllu2brat [OPTIONS]

Options:
  -i, --input_path PATH  Input the file/folder name.  [required]
  -v, --verbose          Enables verbose mode
  --version              Show the version and exit.
  --help                 Show this message and exit.
```
If you don't use any arguments, it will prompt for the input file path as follows:
```
conllu2brat
Input path: example-data/cdli/
```