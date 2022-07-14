#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 11:25:55 2022

@author: omg
"""

import os

def run(**args):
    
    print("[*] In dirlister module.")
    files = os.listdir(".")
    
    return str(files)