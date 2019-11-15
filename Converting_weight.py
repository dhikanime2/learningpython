weight = input("Please input you're weight : " )
spec = input("""
 Type 'K' in Kg
 Type 'L' in Lbs : """ )
p=int(weight) * 0.45
k=int(weight)/ 0.45

if spec.upper() == "K":
    print(f'you are {round(k)} pounds')

elif spec.upper() == "L":
    print(f'you are {round(p)} kg')

else:
    print("hey we don't understand this!")
