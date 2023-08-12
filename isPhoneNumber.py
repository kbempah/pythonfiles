import re

if __name__ == '__main__':
    message = 'My phone number is 978-427-8696.'

    phoneNumberRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})') # compile is passed a raw string indicating the type of pattern we want to match, returns Regex object
    mo = phoneNumberRegex.search(message) # Regex object's search method is passed text to be searched and returns the first instance of the matching pattern found.

    print(mo.group()) # matches and returns whole pattern
    print(mo.group(1)) # matches and returns first group enclosed in ()
    print(mo.group(2)) # matches and returns second group enclosed in () and so on...
    print(mo.groups()) # matches and returns all groups as a tuple