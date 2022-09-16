

alphabet = 'abcdefghijklmnopqrstuvwxyz'

alphabet = list(alphabet)

print(alphabet)

#Output a number with each letter 

#method 1 

Dict_A = {} 
for i in alphabet: 
    Dict_A[i] = alphabet.index(i)
print(Dict_A)


#method 2 

Dict_B = {} 
for i in range(len(alphabet)):
    Dict_B[alphabet[i]] = i 

    print(Dict_B)

