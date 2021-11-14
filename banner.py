#!/usr/bin/python3

from generate_image import generate_text
from generate_banner_fonts import image_to_banner

#import argparse
import sys

def banner(text):

    text.replace('\n', ' ')
    text = text.split()

    banners = []
    i = j = 0
    len_ = 0
    max_len = 9

    while j < len(text):

        if len_ >= max_len:
        
            generate_text(' '.join(text[i:j]), 'temp.jpg')
            banners.append(image_to_banner('temp.jpg'))
            i = j
            len_ = 0

        else:
            len_ += len(text[j])
            j += 1

    generate_text(' '.join(text[i:j]), 'temp.jpg')
    banners.append(image_to_banner('temp.jpg'))

    return banners


if __name__ == '__main__':
    if not len(sys.argv) > 1:
        print('''Usage: banner string

This is a classic-style banner program similar to the one found in Solaris or
AIX in the late 1990s.  It prints a short string to the console in very large
letters.

Inspired by banner from Kenneth J. Pronovici <pronovic@ieee.org>''')
        sys.exit(1)

    print('\n\n'.join(banner(' '.join(sys.argv[1:]))))
    sys.exit(0)


