#!/usr/bin/env python

# Convert to and from CoNLL-U format.

import os
import codecs

# from conllu import *
import conllu

def argparser():
    import argparse
    parser = argparse.ArgumentParser(description="Convert CoNLL-U data.")
    parser.add_argument('-o', '--output', metavar='DIR', default=None,
                        help='Output directory.')
    parser.add_argument('file', nargs='+', help='Source file(s).')
    return parser

def output_document_text(document, output, options=None):
    print >> output, document.text()

def output_document_annotations(document, output, options=None):
    for annotation in document.to_brat_standoff():
        print >> output, unicode(annotation)

def output_document(document, options=None):
    """Output given document according to given options."""
    if options is None:
        # If no output directory is specified, output both to stdout
        output_document_text(document, output_text, options)
        output_document_annotations(document, output_file, options)
    else:
        basefn = os.path.splitext(os.path.basename(document.filename))[0]
        txtfn = os.path.join(options, basefn+'.txt')
        annfn = os.path.join(options, basefn+'.ann')
        if not os.path.exists(options):
            os.makedirs(options)
        with codecs.open(txtfn, 'wt', encoding='utf-8') as txtout:
            output_document_text(document, txtout, options)
        with codecs.open(annfn, 'wt', encoding='utf-8') as annout:
            output_document_annotations(document, annout, options)

def convert(source, options=None):
    # TODO: support conversions other than CoNLL-U to brat.
    for document in conllu.read_documents(source):
        output_document(document, options)

def main(argv):
    args = argparser().parse_args(argv[1:])
    for fn in args.file:
        convert(fn, args)
    return 0

if __name__ == '__main__':
   # sys.exit(main(sys.argv))
   # my_file = open("train-sample.conllu")
   # my_file_lines = my_file.readline()
   # my_file_list = []
   # my_file_list.append(my_file_lines)
   output_file = open("output.ann", "wt")
   output_text = open("output.txt", "wt")
   convert(open((raw_input("file path: "))))
   # output_file.close()
   # print("hi")
