#!/usr/bin/env python3
import re                         
from collections import namedtuple
class TokenClass: # defining Class Name
  Token = namedtuple('Tokens', 'text') # namedTuple() creates tuple subclasses with named fields
  def __init__(self, tokens):
    self.tokens = tokens               # initialising tokens with the self keywords
    tok1_list = []
    for tok, tok1 in self.tokens:
      tok1_list.append('(?P<%s>%s)' % (tok, tok1))
    self.re = re.compile('|'.join(tok1_list))
  def iter_tokens(self, input, ignore_ws=True):
    for match in self.re.finditer(input):               #The expression re.finditer() returns an iterator yielding MatchObject instances over all non-overlapping matches for the re pattern in the string. 
      if ignore_ws and match.lastgroup == 'Whitespace': #Checks for WhiteSpace after every string to ensure end of a string
        continue
      yield TokenClass.Token(match.group(0))    #returns name
  def tokenize(self, input, ignore_ws=True):
    return list(iter_tokens(input, ignore_ws))  #converting the tuple into a list and returning

if __name__ == "__main__":
  Tuple_Token = [                               #Creating a tuple of tokens, and their names
    ('Nil'        , r"nil|\'()"),               # for 'nil'
    ('Number'     , r'\d+'),                    # for numbers
    ('String'     , r'"(\\.|[^"])*"'),          # for strings enclosed in ""
    ('Symbol'     , r'[\x21-\x26\x2a-\x7e]+'),  # for symbols
    ('Dot'        , r'\.'),                     # for dot/s 
    ('Quote'      , r"'"),                      # for quotations
    ('OBracket'   , r'\('),                     # for opening brackets
    ('CBracket'   , r'\)'),                     # for closing brackets
    ('True'       , r'true|#t'),                # for 'true'
    ('False'      , r'false|#f'),               # for 'false'
    ('Whitespace' , r'\w+'),                    # for checking of whitespace in the end                 
  ]
  S=raw_input("Enter your string : ")           #taking the input from the user
  for i in TokenClass(Tuple_Token).iter_tokens(S): 
    print(i)




    
    
