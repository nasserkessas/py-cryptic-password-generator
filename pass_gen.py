import random
nums = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['#','$','%','&','\'','(',')','*','+','-','.','/',':','<','=','>','?','@','[','\\',']','^','_','`','{','|','}','~']
l_letters = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
u_letters = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
password = []

def make_password(strength):
    if strength == '1':
        chars = [l_letters, u_letters]
        length = 3
        name = "very veak"
    elif strength == '2':
        chars = [l_letters, u_letters]
        length = 5
        name = "weak"
    elif strength == '3':
        chars = [l_letters, u_letters, nums]
        length = 6
        name = "average"
    elif strength == '4':
        chars = [l_letters, u_letters, nums, symbols]
        length = 6
        name = "good"
    elif strength == '5':
        chars = [l_letters, u_letters, nums, symbols]
        length = 7
        name = "high"
    elif strength == '6':
        chars = [l_letters, u_letters, nums, symbols]
        length = 8
        name = "very high"

    for i in range(length):
        this_char = (random.choice(random.choices(chars, weights=map(len, chars))[0]))
        password.append(this_char)
    print ("Your password is " + ''.join(password))
    print ("Your password is of " + name + " strength")

while True:
    a = input("How strong would you like your password?(1-6) ")
    try:
        val = int(a)
        if int(a) > 6:
            print ("This is not a valid input, please write a lower value")
        elif int(a) < 1:
            print ("This is not a valid input, please write a higher value")
        else:
            break
    except ValueError:
        print ("This is not a valid input, please write an integer")


make_password(a)