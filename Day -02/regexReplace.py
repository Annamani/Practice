import re

text = "The quick brown fox jumps over the lazy brown dog"
pattern = r"brown"

replacement = "red"
new_text = re.sub(pattern, replacement, text)
print("Modified text:", new_text)

# Search for a key
search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")

# Split Text
textex = "apple,banana,orange,grape"
patternex = r","

split_result = re.split(patternex, textex)
print("Split result:", split_result)