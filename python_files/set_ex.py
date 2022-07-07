# Create the sets
been_out_of_country = {'Henry', 'Frank', 'Ashley', 'Sam', 'Rebecca'}
enjoys_travelling = {'Frank', 'Joseph', 'Eliza', 'Sam', 'George'}

# Perform the union
# The "OR" operator is used for this
been_ooc_or_et = been_out_of_country | enjoys_travelling
print(been_ooc_or_et)

# Perform the intersection
# The "AND" operator is used for this
been_ooc_and_et = been_out_of_country & enjoys_travelling
print(been_ooc_and_et)

# Is "Joseph" in the out of country set?
print('Joseph' in been_out_of_country)

# Is "Joseph" in the enjoys travelling set?
print('Joseph' in enjoys_travelling)