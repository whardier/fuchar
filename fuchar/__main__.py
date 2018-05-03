# -*- coding: UTF-8 -*-

# MIT License

# Copyright (c) 2018 Shane R. Spencer <spencersr@gmail.com>

# https://github.com/whardier/fuchar

# Font future by Sam Hocevar <sam@hocevar.net> released under WTFPL via http://sam.zoy.org/wtfpl/COPYING

from __future__ import print_function

import argparse

import fuchar

def main():

    parser = argparse.ArgumentParser(
        description=fuchar.__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        '-i', '--ignore-missing',
        action='store_true'
    )

    parser.add_argument(
        '-s', '--prefix-string',
        type=str, default=''
    )

    parser.add_argument(
        '-e', '--postfix-string',
        type=str, default=''
    )

    parser.add_argument(
        'string',
        type=str, nargs='+'
    )

    args = parser.parse_args()

    print(
        fuchar.render_string(
            ' '.join(args.string),
            prefix=args.prefix_string,
            postfix=args.postfix_string,
            ignore_missing=args.ignore_missing
        )
    )

if __name__ == '__main__':

    main()
