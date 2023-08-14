# this is a simple program that uses a dictionary to store birthdays


birthdays = {'Karen Akwaboah':'Feb 23', 'Nana Bempah':'Jan 26', 'Kwadwo Bempah':'Mar 27', 'Francisca Bempah':'Jul 8'}

while True:
    name = input('Enter a name: (blank to quit) > ')
    if name == '':
        break
    
    if name in birthdays:
        print(f'{birthdays[name]} is the birthday of {name}.')
    else:
        bday = input(f'I do not have birthday information for {name}, What is their birthday? > ')
        birthdays[name] =  bday
        print('Done!')
         
        