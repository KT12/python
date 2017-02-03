# Using a dict comprehension to reverse keys and values in a dict

random_dict = {'z':0, 'y':1, 'x':2, 'w':3}

{value:key for key,value in random_dict.items()}

# This only works if the values of the dict are immutable.
# Procedure fails for lists in the dict

# Alternate Method
reverse = dict(zip(random_dict.values(), random_dict.keys()))
