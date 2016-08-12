# Using a dict comprehension to reverse keys and values in a dict

random_dict = {'z':0, 'y':1, 'x':2, 'w':3}

{value:key for key,value in random_dict.items()}
