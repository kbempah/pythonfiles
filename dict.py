# some common dict methods and operators

registry = {'Apple':1.99, 'Orange':2.00}

registry.keys() # returns a tuple of the keys in the registry

registry.values() # returns a tuple of the values in the registry

registry.items() # returns a tuple of all key-value pairs in registry

None in registry # the in operator checks the presence of a key in registry

None not in registry # the not in operator checks the absence of a key inside registry

registry.get('Apple', 0.00) # the get method returns the value associated with 'Apple' or 0.00 if Apple is not a key in the registry
