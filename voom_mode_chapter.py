#! /usr/bin/env python
# -*- coding: utf-8 -*-

# voom_mode_chapter.py
# Last Modified: 2017-1-09
# VOoM -- Vim two-pane outliner, plugin for Python-enabled Vim 7.x
# Website: http://www.vim.org/scripts/script.php?script_id=2657
# Author: Vlad Irnov (vlad DOT irnov AT gmail DOT com)
# License: CC0, see http://creativecommons.org/publicdomain/zero/1.0/

"""
VOoM markup mode for headlines marked with #'s (atx-headers, a subset of Markdown format), or chapters.
See |voom-mode-hashes|,  ../../doc/voom.txt#*voom-mode-hashes*

# heading level 1
##heading level 2
### heading level 3

Or:
第一章
第二章
  .
  .
  .
"""
from __future__ import unicode_literals
import sys
import re

# Marker character can be changed to any ASCII character.
CHAR = '#'

# Use this if whitespace after marker chars is optional.
headline_match = re.compile(r'^(%s+)' %re.escape(CHAR)).match

chapter_match = re.compile(r'^第[0-9０-９〇零一二三四五六七八九十百千万]{1,5}[卷册集章回节幕]'
                        r'|^(序|自序|代序|楔子|尾声|跋|后记|番外)'
                        r'|^☆、'
                        ).match
is_Py2 = False
if sys.version < '3':
    is_Py2 = True
    range = xrange

# Use this if a whitespace is required after marker chars (as in org-mode).
#headline_match = re.compile(r'^(%s+)\s' %re.escape(CHAR)).match

def hook_makeOutline(VO, blines):
    """Return (tlines, bnodes, levels) for Body lines blines.
    blines is either Vim buffer object (Body) or list of buffer lines.
    """
    Z = len(blines)
    tlines, bnodes, levels = [], [], []
    tlines_add, bnodes_add, levels_add = tlines.append, bnodes.append, levels.append
    for i in range(Z):
        if not blines[i].startswith(CHAR.encode('utf-8')):
            bline = blines[i]
            if is_Py2:
                bline = bline.decode('utf-8')
            bline = bline.strip()
            if bline == '':
                continue
            m = chapter_match(bline)
            if not m:
                continue
            lev = 1
            head = bline
        else:
            bline = blines[i]
            m = headline_match(bline)
            # Uncomment the next line if whitespace is required after marker chars.
            #if not m: continue
            lev = len(m.group(1))
            head = bline[lev:].strip()
            # Do this instead if optional closing markers need to be stripped.
            #head = bline[lev:].strip().rstrip(CHAR).rstrip()


        tline = '  %s|%s'.encode('utf-8') %('. '.encode('utf-8')*(lev-1), head)
        tlines_add(tline)
        bnodes_add(i+1)
        levels_add(lev)
    return (tlines, bnodes, levels)


def hook_newHeadline(VO, level, blnum, tlnum):
    """Return (tree_head, bodyLines).
    tree_head is new headline string in Tree buffer (text after |).
    bodyLines is list of lines to insert in Body buffer.
    """
    tree_head = 'NewHeadline'
    bodyLines = ['%s %s' %(CHAR * level, tree_head), '']
    return (tree_head, bodyLines)


def hook_changeLevBodyHead(VO, h, levDelta):
    """Increase of decrease level number of Body headline by levDelta."""
    if levDelta==0: return h
    m = headline_match(h)
    level = len(m.group(1))
    return '%s%s' %(CHAR * (level+levDelta), h[m.end(1):])




