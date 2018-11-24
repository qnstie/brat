#!/usr/bin/env python
# -*- Mode: Python; tab-width: 4; indent-tabs-mode: nil; coding: utf-8; -*-
# vim:set ft=python ts=4 sw=4 sts=4 autoindent:

"""Auto-annotatation handlers for the auto-annotation remote service.

Author:     Pawel Kunstman
Version:    2018-11-24
"""

import os
from document import real_directory
from docimport import (DATA_DIR, InvalidDirError, isdir, isfile,
                       NoWritePermissionError, TEXT_FILE_SUFFIX, JOINED_ANN_FILE_SUFF,
                       FileExistsError, open_textfile, join_path)

def str2bool(v):
    return v.lower() in ("yes", "true", "t", "1")

def autoannotate(text, collection, document, overwrite = 'false'):
    """
    1. HERE GOES CALL TO A REMOTE SERVICE TO PREPARE ANNOTATIONS
    """
    ann_text = "T1	Protein 0 7	Protein"

    json_dic = {}
    try:
        json_dic = save_file(text, ann_text, collection, document, str2bool(overwrite))
    except Exception as e:
        json_dic = {
            'result': 'error',
            'error': type(e).__name__,
            'message': str(e)
        }
    
    return json_dic


def save_file(text, ann_text, collection, docid, do_overwrite):
    '''
    A modified procedure taken from docimport.py
    '''

    directory = collection

    if directory is None:
        dir_path = DATA_DIR
    else:
        # XXX: These "security" measures can surely be fooled
        if (directory.count('../') or directory == '..'):
            raise InvalidDirError(directory)

        dir_path = real_directory(directory)

    # Is the directory a directory and are we allowed to write?
    if not isdir(dir_path):
        raise InvalidDirError(dir_path)
    if not os.access(dir_path, os.W_OK):
        raise NoWritePermissionError(dir_path)

    base_path = join_path(dir_path, docid)
    txt_path = base_path + '.' + TEXT_FILE_SUFFIX
    ann_path = base_path + '.' + JOINED_ANN_FILE_SUFF

    # Before we proceed, verify that we are not overwriting
    if not do_overwrite:
        for path in (txt_path, ann_path):
            if isfile(path):
                raise FileExistsError(path)

    # Make sure we have a valid POSIX text file, i.e. that the
    # file ends in a newline.
    if text != "" and text[-1] != '\n':
        text = text + '\n'

    with open_textfile(txt_path, 'w') as txt_file:
        txt_file.write(text)

    # Touch the ann file so that we can edit the file later
    with open(ann_path, 'w') as ann_file:
        ann_file.write(ann_text)

    return {'result': 'success',
            'document': docid}