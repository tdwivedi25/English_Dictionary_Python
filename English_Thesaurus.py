import json
from difflib import get_close_matches
data=json.load(open('data.json'))

def find_meaning(w):
  
   if word in data :
      meaning=' '.join(data[word])
      return meaning

   elif w.title() in data:
        return ' '.join(data[w.title()])

   elif len(get_close_matches(word,data.keys()))>0:
      yn=input("Did you mean %s? Enter y for yes and n for no: " % get_close_matches(word,data.keys())[0] )
      if yn=='Y' or yn=='y':
            return ' '.join(data[ get_close_matches(word,data.keys())[0]])
      elif yn=='N' or yn=='n':
         return "Word doesn't exist. Try again."
      else:
         return "I didn't understand you input."

   else:
      return ("Word doesn't exist. Try again.")

word=input('Enter the word you want to find the meaning of: ').lower()
print(find_meaning(word))
