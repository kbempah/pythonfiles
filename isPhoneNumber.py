import re

def isPhoneNumber(text:str)->bool:
    phoneNumberRegex = re.compile(r'\d{3}-\d{3}-\d{4}') # compile is passed a raw string indicating the type of pattern we want to match, returns Regex object
    mo = phoneNumberRegex.search(text) # Regex object's search method is passed text to be searched and returns the first instance of the matching pattern found.
    if mo != None:
        return mo.group()
    else:
        return 'match not found'

if __name__ == '__main__':
    message = 'My phone number is'

    result = isPhoneNumber(message)

    print(f'Phone number found: {result}')

    print('Done')