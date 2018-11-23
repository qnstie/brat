#!/usr/bin/env python
# -*- Mode: Python; tab-width: 4; indent-tabs-mode: nil; coding: utf-8; -*-
# vim:set ft=python ts=4 sw=4 sts=4 autoindent:

"""Auto-annotatation handlers for the auto-annotation remote service.

Author:     Pawel Kunstman
Version:    2018-11-24
"""


def autoannotate():
    """
    JUST A STUB - IMPLEMENT:
    1. CALL TO A REMOTE SERVICE TO PREPARE ANNOTATIONS
    2. RETRIEVE ANNOTATIONS AND PREPARE LOCAL TEXT AND ANN FILES (MISSING ARGUMENTS!!!)
    3. RETURN POSITIVE RESULT
    """
    json_dic = {}
    json_dic['ann'] = "T1	Protein 34 54	apolipoprotein B-100"
    return json_dic
