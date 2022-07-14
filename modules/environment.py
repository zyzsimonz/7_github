#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 11:29:30 2022

@author: omg
"""

import os

def run(**args):
    print("[*] In environment module.")
    return str(os.environ)