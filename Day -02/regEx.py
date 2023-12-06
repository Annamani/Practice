import re

text="My name is Annamani Kamma.My husband name is Kranthi Kumar Nuvvula.My sis name is Anu."
keyword=r"name"
match_word=re.search(keyword,text)

if match_word:
    print(keyword +"found")
else:
    print("Keyword doesnot found in given text")