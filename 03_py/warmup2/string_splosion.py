"""Given a non-empty string like "Code" return a string like "CCoCodCode".
"""

def string_splosion(str):
  s = ""
  index = 0
  for i in str:
    s += str[:index +1]
    index += 1
  return s


print(string_splosion('Code')) # → 'CCoCodCode'
print(string_splosion('abc')) # → 'aababc'
print(string_splosion('ab')) # → 'aab'

