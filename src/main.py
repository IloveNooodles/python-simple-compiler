import re
import sys
import argparse
from tokenizer import createToken

def bannerCompiler() :
  print("             / __ \__  __/ /_/ /_  ____  ____")         
  print("            / /_/ / / / / __/ __ \/ __ \/ __ \ ")        
  print("           / ____/ /_/ / /_/ / / / /_/ / / / /")         
  print("        __///_   \__, /\__/_/ /_/\__/_/// /_/ ")         
  print("       / ____/__/__///_ ___  ____  (_) /__  _____")                 
  print("      / /   / __ \/ __ `__ \/ __ \/ / / _ \/ ___/")                                                                  
  print("     / /___/ /_/ / / / / / / /_/ / / /  __/ /") 
  print("     \____/\____/_/ /_/ /_/ .___/_/_/\___/_/") 
  print("                         /_/       ")  

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('file', type = argparse.FileType('r'))
  args = parser.parse_args()
  bannerCompiler()
  createToken(args.file.name)
  # f = args.file
  # for line in f:
  #   print(line)
     