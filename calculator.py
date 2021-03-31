print('My Calculator')
print("To exit write 'Quit'\n")
previous=0
run=True
def my_math():
    global run
    global previous
    equation=input("Enter equation: ")	
    if (equation=='Quit'):
        run=False
    else:
        previous=eval(equation)
        print(previous)
while run:
    my_math()

