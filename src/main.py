from lib.grammar.cfgtocnf import readGrammarFile, convertGrammar, mapGrammar
from lib.tokenizer import createToken
from lib.parser import cykParse
import re, os, sys, argparse

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
  print("      Ayam Bersih Berkah /_/ Production          ")  
  print()

def verdict():
  # Argparse
  parser = argparse.ArgumentParser()
  parser.add_argument('file', type = argparse.FileType('r'))
  args = parser.parse_args()

  # Banner and verdict
  bannerCompiler()
  print("\nLoading...")
  print("Checking your codes...")
  print("File name: " + str(args.file.name))
  print()
  
  # Token & CNF
  token = createToken(args.file.name)
  token = [x.lower() for x in token]
  CNFgrammar = mapGrammar(convertGrammar((readGrammarFile("lib/grammar/cfg.txt"))))
  print("======================VERDICT=========================")
  print()
  cykParse(token, CNFgrammar)
  print()
  print("======================================================")

if __name__ == "__main__":
  verdict()