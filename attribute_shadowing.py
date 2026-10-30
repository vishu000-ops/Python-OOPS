class Chai():
    temperature = "hot"
    strength = "strong"

cutting = Chai()
print(cutting.temperature)
print(cutting.strength)

cutting.strength = "mild"

print("After changing", cutting.strength)
print("Direct look into the class", Chai.strength)

del cutting.strength

print(cutting.strength)
