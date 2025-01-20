string = "Hello     worlddddddd python3"

strings = string.split()

strings = [ 
    word[::-1] for word in strings   
]    
# for word in strings:
#     word = word[::-1]
#     word = ''.join(reversed(word))
    
string = " ".join(strings)
print(string)