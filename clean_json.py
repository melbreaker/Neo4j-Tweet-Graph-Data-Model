import re

def replace_functions(match):
    value = match.group(1)  # Extract the value inside ObjectId() or NumberLong()
    return f'"{value}"' # return extracted value as string 

# Read in the text file
with open('tweets.json', 'r', encoding='utf-8') as file:
    text = file.read()

# Define a regular expression pattern to match ObjectId() and NumberLong()
pattern_object_id = r'ObjectId\("([^"]+)"\)'
pattern_number_long = r'NumberLong\((\d+)\)'

# Replace ObjectId() and NumberLong() with string values
text = re.sub(pattern_object_id, replace_functions, text)
text = re.sub(pattern_number_long, replace_functions, text)

# Write the modified text back to a new file
with open('cleaned_tweets.json', 'w', encoding='utf-8') as output_file:
    output_file.write(text)

print("Text file processed and saved as 'cleaned_tweets.json'")
