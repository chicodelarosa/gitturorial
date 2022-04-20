name = "Dev1"
age = 15

def namemodifier(str_):
	return str_.upper()

def agemodifier(age):
	return age - 2

print(f"Hi my name is {namemodifier(name)}. My age is {agemodifier(age)}.")
