import pprint

if __name__ == '__main__':
    text = 'He who sits in heaven laughs. I sit in heaven so I laugh.'
    count = dict()

    for char in text:
        count.setdefault(char, 0) # inserts the key into the dict if it doesn't already exist. Returns the value associated with the key if it already does
        count[char] += 1
    
    pprint.pprint(count)
    
