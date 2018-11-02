#!/usr/bin/env python

# Minimal demonstration of conllu.py use.

import sys

import conllu

def main(argv):
    # process sentence at a time
    for f in argv[1:]:
        try:
            sent_count, word_count = 0, 0
            for sentence in conllu.read_conllu(f):
                sent_count += 1
                word_count += len(sentence.words())
            print '%s: %d sentences, %d words' % (f, sent_count, word_count)
        except conllu.FormatError, e:
            print >> sys.stderr, 'Error processing %s: %s' % (f, str(e))

    # process document at a time
    for f in argv[1:]:
        try:
            sent_count, word_count = 0, 0
            for document in conllu.read_documents(f):
                sent_count += len(document.sentences())
                word_count += len(document.words())
            print '%s: %d sentences, %d words' % (f, sent_count, word_count)
        except conllu.FormatError, e:
            print >> sys.stderr, 'Error processing %s: %s' % (f, str(e))
            
if __name__ == '__main__':
    sys.exit(main(sys.argv))
