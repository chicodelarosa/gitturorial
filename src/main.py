name = "Dev2"

age = 20

def namemodifier(name):
	newname = name + ' a string'

	return newname

def agemodifier(age):
	newage = age - 2

	return newage

print(f"Hi my name is {namemodifier(name)}. My age is {agemodifier(age)}.")