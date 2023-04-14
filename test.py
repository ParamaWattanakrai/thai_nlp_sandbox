import re

string = "This string contains nxains"

# Use a regular expression pattern that matches 'nx', followed by any character, followed by 'ains'
pattern = re.compile("n.{1}ains")

# Search for the pattern within the string
match = pattern.search(string)

# Check if the pattern was found
if match:
    # If the pattern was found, print out the actual substring that was matched
    substring = match.group()
    print("Found", substring, "in string")
else:
    print("Did not find 'nxains' in string")
