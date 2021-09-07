from difflib import SequenceMatcher

string1 = "apple pie available"
string2 = "come have some apple pies"


    
testCases = int(input())
for i in range(testCases):
  a = input()
  b = input()
  match = SequenceMatcher(None, a, b).find_longest_match(0, len(a), 0, len(b))
  result = (len(a)+len(b))-match.size*2
  print(result)
  