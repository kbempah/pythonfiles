def isPhoneNumber(text:str)->bool:
    if len(text) != 12: # if there aren't 12 digits
        return False
    index = 0
    while index < 3: # first 3 digits
        if not text[index].isdecimal():
            return False
        index += 1
    if text[index] != '-': # delimiter
        return False
    index += 1
    while index < 7: # middle 3 digits
        if not text[index].isdecimal():
            return False
        index += 1
    if text[index] != '-': # delimiter
        return False
    index += 1
    while index < 12:
        if not text[index].isdecimal():
            return False
        index += 1
    return True

if __name__ == '__main__':
    message = 'Call me at 978-427-8696 tomorrow. 978-654-0867 is my office.'
    
    for i in range(len(message)):
        chunk = message[i:i+12]
        if isPhoneNumber(chunk):
            print('Phone number found:', chunk)
            
    print('Done')