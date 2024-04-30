array = ['{}']
# The Von Neumann ordinals are a number system. Ordinal numbers can be represented as sets of all numbers less than that number:
def ordinals(input):
    # if input == 0:
    #     return '{}'
    # else:
    #     return '{' + ordinals(input-1) + '}'


print(ordinals(0)) # {}
print(ordinals(1)) # {{}}
print(ordinals(2)) # {{}, {}}}