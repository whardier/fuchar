# -*- coding: UTF-8 -*-

# MIT License

# Copyright (c) 2018 Shane R. Spencer <spencersr@gmail.com>

# https://github.com/whardier/fuchar

# Font future by Sam Hocevar <sam@hocevar.net> released under WTFPL via http://sam.zoy.org/wtfpl/COPYING

"""Fuchar renders the future font found in the toilet project

Missing: # % ( ) * / < > \ ^ ~

Ex:

python -m fuchar --prefix='  <!-- ' --postfix=' -->' --ignore-missing hi there##
  <!-- ╻ ╻╻   ╺┳╸╻ ╻┏━╸┏━┓┏━╸ -->
  <!-- ┣━┫┃    ┃ ┣━┫┣╸ ┣┳┛┣╸  -->
  <!-- ╹ ╹╹    ╹ ╹ ╹┗━╸╹┗╸┗━╸ -->

"""

from . import font

def render_string(s, newline='\n', prefix='', postfix='', ignore_missing=False):
    """Really simple rendering of font into 3 lines"""

    line_0 = prefix
    line_1 = prefix
    line_2 = prefix

    for c in s:
        char = font.chars.get(c, None)

        if not char:
            if ignore_missing:
                char = font.chars.get(' ', ('', '', ''))
            else:
                char = (' ', ' ', c)

        line_0 = ''.join((line_0, char[0]))
        line_1 = ''.join((line_1, char[1]))
        line_2 = ''.join((line_2, char[2]))

    line_0 = line_0 + postfix
    line_1 = line_1 + postfix
    line_2 = line_2 + postfix

    return newline.join((line_0, line_1, line_2))

__all__ = ['font', 'render_string']

__version__ = '0.01'
__author__ = 'Shane R. Spencer'
__author_email__ = 'spencersr@gmail.com'
__url__ = 'https://github.com/whardier/fuchar'
__license__ = 'MIT'
