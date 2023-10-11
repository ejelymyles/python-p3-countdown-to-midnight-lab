import time 
# your code goes here!
def countdown(number):
    while number >= 1:
        print(f"{number} SECOND(S)!")
        number -= 1

    print("HAPPY NEW YEAR!")
    pass 


def countdown_with_sleep(number):
    while number >= 1:
        print(f"{number} SECOND(S)!")
        time.sleep(1)
        number -= 1
    
    print("HAPPY NEW YEAR!")
    pass
