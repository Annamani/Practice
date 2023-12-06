# Multiple strings
first_name="Annamani"
last_name="Kamma"
words="lives in "
Country="Denmark"
# String Concatenation
complete_string=first_name+" "+last_name+","+words+" "+Country+"."
print(complete_string)
# Length of a string
print(len(first_name))
# String Lower case
print(Country.lower())
# String Upper Case
print(first_name.upper())

# String Replace
text = "Denmark is a big country"
new_text = text.replace("big", "small")
print("Modified text:", new_text)

# String Strips
sample = "   Some spaces around   "
stripped_text = sample.strip()
print("Stripped text:", stripped_text)

# Substring
substring = "lives in"
if substring in complete_string:
    print(substring, "found in the text")
