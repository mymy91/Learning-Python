# This is my first function called name. It will ask the name and
# print a message

def SeperateLession():
	print('--END--')
	print('')
	

#Lession 1
print('--Lession 1--')
def name():
	firstName = input('What is your name?')
	print('So nice to meet you, ' + firstName)
	
name()
SeperateLession()

#Lession 2
print('--Lession 2--')
def addition():
	firstNumber = 30
	secondNumber = 60
	print(firstNumber + secondNumber)
	
addition()
SeperateLession()

#Lession 3
print('--Lession 3--')
def addition_Integer():
	firstNumber = int(input('Input the firstNumber:'))
	secondNumber = int(input('Input the secondNumber:'))
	print(firstNumber + secondNumber)
	
#addition_Integer()
SeperateLession()

#Lession 4
print('--Lession 4--')
def addition_Float():
	firstNumber = float(input('Input the firstNumber:'))
	secondNumber = float(input('Input the secondNumber:'))
	print(firstNumber + secondNumber)

#addition_Float()
SeperateLession()

#Lession 5
print('--Lession 5--')
def subtraction_Int():
	firstNumber = int(input('Input the firstNumber:'))
	secondNumber = int(input('Input the secondNumber:'))
	print('Result: ' + str(firstNumber - secondNumber))

#subtraction_Int()
SeperateLession()		

def mutiply_Int():
	firstNumber = int(input('Input the firstNumber:'))
	secondNumber = int(input('Input the secondNumber:'))
	print('Result: ' + str(firstNumber * secondNumber))

def divide_Int():
	firstNumber = int(input('Input the firstNumber:'))
	secondNumber = int(input('Input the secondNumber:'))
	print('Result: ' + str(firstNumber / secondNumber))
	
#Lession 6
print('--Lession 6--')
def modulo():
	firstNumber = int(input('Input the firstNumber:'))
	secondNumber = int(input('Input the secondNumber:'))
	print('Result: ' + str(firstNumber % secondNumber))

#modulo()
SeperateLession()

def quit():
	global _calcOn
	_calcOn = 0
	
def CalcRun():
	op = input('1,2,3, 4 or 5?')
	if op == '1':
		addition_Integer()
	elif op == '2':
		subtraction_Int()
	elif op == '3':
		mutiply_Int()
	elif op == '4':
		divide_Int()
	elif op == '5':
		modulo()
	else:
		quit()
		
_calcOn = 1

while _calcOn == 1:
	CalcRun()

	