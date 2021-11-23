import re
import sys
import argparse
from tokenizer import createToken
from parser import verdictCYK
import grammar
import os

def bannerCompiler() :
  print()
  print("              ____        __  __                 ")
  print("             / __ \__  __/ /_/ /_  ____  ____    ")         
  print("            / /_/ / / / / __/ __ \/ __ \/ __ \   ")        
  print("           / ____/ /_/ / /_/ / / / /_/ / / / /   ")         
  print("        __///_   \__, /\__/_/ /_/\__/_/// /_/    ")         
  print("       / ____/__/__///_ ___  ____  (_) /__  _____")                 
  print("      / /   / __ \/ __ `__ \/ __ \/ / / _ \/ ___/")                                                                  
  print("     / /___/ /_/ / / / / / / /_/ / / /  __/ /    ") 
  print("     \____/\____/_/ /_/ /_/ .___/_/_/\___/_/     ") 
  print("                         /_/                     ")  
  print()

if __name__ == "__main__":
  # Argparse
  parser = argparse.ArgumentParser()
  parser.add_argument('file', type = argparse.FileType('r'))
  args = parser.parse_args()

  # Banner
  bannerCompiler()

  # Token & CNF
  token = createToken(args.file.name)
  CNFgrammar = grammar.convert_grammar(grammar.read_grammar('grammar.txt'))

  # Verdict
  verdictCYK(token, CNFgrammar)

     