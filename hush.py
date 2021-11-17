#!/usr/bin/env python3
import os

def main():
    os.chdir('/home/suppafuzz/.myscripts/')
    f = open('secrets.txt', 'r')
    contents = f.read()
    print(contents)

#
if __name__ == "__main__":
    main()