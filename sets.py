# Sets are defined with curly brackets
S = {'A', 'B', 'C', 'A', 'B', 'C' }
# Sets are unordered and ignore duplicates
print("Printing S (note duplicates are ignored):", S)

S.add('D')
print("Added 'D' to S:", S)

S.remove('D')
print("Removed 'D' from S:", S)

A={1,2,3,4,5}
B={1,3,9, 12}

# The intersection of two sets can be found with &
print("Intersection:", A & B)

# The union of two sets can be found with |
print("Union:" , A | B)
print("Union w/ union method", A.union(B))