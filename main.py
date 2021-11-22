import re
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file', type = argparse.FileType('r'))
args = parser.parse_args()

f = args.file
for line in f:
  print(line)

