
# create a loop that ends when the user types 'quit' or 'exit'
while True:
    # get the name of the cat
    name = input('Name: ')

    # if the user typed 'quit' or 'exit', exit the program
    if name == 'quit' or name == 'exit':
        break

    # ask the age of the cat in human years
    age = input('Age in humand years : ')
 
    #translate the age to cat years
    age = int(age) * 7
    

    # get the weight of the cat
    weight = input('Weight: ')

    # calculate if the cat is overweight
    if int(weight) > 25:
        overweight = 'yes'
    else:  
        overweight = 'no'


    # print the information of the cat and if the cat is overweight
    print('{} is {} years old and {} kilograms and is {} overweight'.format(name, age, weight, overweight))

         


    