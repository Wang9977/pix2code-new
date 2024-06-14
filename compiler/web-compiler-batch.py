#!/usr/bin/env python
from __future__ import print_function
__author__ = 'Tony Beltramelli - www.tonybeltramelli.com'

import sys
import os
from os.path import basename
from classes.Utils import *
from classes.Compiler import *

if __name__ == "__main__":
    argv = sys.argv[1:]
    length = len(argv)
    if length != 0:
        input_path = argv[0]
    else:
        print("Error: not enough argument supplied:")
        print("web-compiler-batch.py <path> ")
        exit(0)

FILL_WITH_RANDOM_TEXT = True


dsl_path = "assets/web-dsl-mapping.json"



def render_content_with_text(key, value):
    if FILL_WITH_RANDOM_TEXT:
        if key.find("btn") != -1:
            value = value.replace(TEXT_PLACE_HOLDER, Utils.get_random_text())
        elif key.find("title") != -1:
            value = value.replace(TEXT_PLACE_HOLDER, Utils.get_random_text(length_text=5, space_number=0))
        elif key.find("text") != -1:
            value = value.replace(TEXT_PLACE_HOLDER,
                                  Utils.get_random_text(length_text=56, space_number=7, with_upper_case=False))
    return value


for input_file in os.listdir(input_path):
    if input_file.find(".gui") != -1:
        TEXT_PLACE_HOLDER = "[]"
        compiler = Compiler(dsl_path)
        file_uid = basename(input_file)[:basename(input_file).find(".")]
        path = input_file[:input_file.find(file_uid)]
        # print('input_file',input_file,'file_uid',file_uid,'path',path)

        input_file_path = "{}{}.gui".format(input_path, file_uid)

        output_file_path = "../datasets/web/html/"+file_uid+".html"


        compiler.compile(input_file_path, output_file_path, rendering_function=render_content_with_text)
