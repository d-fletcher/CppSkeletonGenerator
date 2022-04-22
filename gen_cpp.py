#!/usr/bin/python3

import sys
import os
import shutil

class GenerateCpp:
    def __init__(self):
        if (len(sys.argv) != 2):
            print(f"Usage: gen_cpp output_file")
            exit(1)
        
        output = sys.argv[1]

        shutil.copyfile("/usr/local/bin/gen_cpp/sample.cc", "./{}".format(output))

if __name__ == "__main__":
    GenerateCpp()
