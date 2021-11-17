# Design Your Life Game 
import time 
#import numpy as np 
import statistics
from statistics import mean

def start():
    print("Welcome to Design Your Life Game")
    time.sleep(2)
    print("We will help you brainstorm some paths.")
    time.sleep(2)
    print("To get started, please type in your name.")
    name = input("> ")
    print("Great, thanks %s." % name)
    time.sleep(2)
    path_1()

paths = []

def path_1():
    print("In the next 5 years, what could you see yourself doing?")
    two_strikes = False 
    
    while True:
        
        first_path = input("> ")
    
        if first_path == "nothing" and not two_strikes:
            print("You're not thinking hard enough. Try again.")
            two_strikes = True 
        elif first_path == "nothing" and two_strikes:
            print("I think you might not be taking this exercise seriously. I am booting you from the game. Come back when you are not being so silly. Goodbye.")
            exit(0)
        else:
            print("Great! Let's put that down as one potential option for now.")
            paths.append(first_path)
            path_2()
        
def path_2():
    print("Now, let's assume that your first plan is no longer possible, what's your backup plan?")
    
    second_path = input("> ")
    
    if second_path == "nothing":
        print("Try again.")
        path_2()
    else:
        print("Great! Nice job thinking of two legitimate paths, let's store that and keep moving on.")
        paths.append(second_path)
        time.sleep(2)
        path_3()

def path_3():
    print("In this next path, I want you to imagine you no longer have any more bills to pay.")
    time.sleep(2)
    print("What would you do with your time in that case?")
    
    while True:
    # make sure that 'True' is colored to indicate its being recognized as a Boolean result, otherwise its just an undefined variable
        
        no_bills_path = input("> ")
    
        if no_bills_path == "nothing": 
            print("Mmmm, I don't think so. Even lottery winners have to do something with their day. Dream big. I'll give you a few more seconds this time.")
            time.sleep(10)
            print("Maybe that was too much time, I don't want you to fall asleep. Type in your new thought here.")
        elif no_bills_path == "quit my job":
            print("Congrats on quitting your job. Then what?")
            time.sleep(2)
        elif no_bills_path == "watch netflix": 
            print("Yes I would do that too. But after you've finished binge watching all recommendations and trolling the Netflix instagram account, you still have to do something. Try again.")
            time.sleep(2) 
        else:
            print("Awesome. Keep this third path in mind, even though you might still have bills to pay, it helps you think about things you really want.")
            paths.append(no_bills_path)
            time.sleep(2)
            print("Before we move on, here is a list of the three life paths you've selected so we have it in one place.")
            time.sleep(2)
            print(paths)
            time.sleep(2)
            ranking_paths()
        
energy_levels = []
resource_levels = []
determination_levels = []

def ranking_paths():

    print("In this next step, we want to rank the conviction levels of your three options.")
    time.sleep(1)
    for path in paths:
      
        print("What is your energy, resource, and determination level for %s ?" % path)
        time.sleep(1)
        print("Please type a number 1 - 10, one prompt at a time")
        
        
        energy = input("> ")
        energy_levels.append(int(energy))
        
        resource = input("> ")
        resource_levels.append(int(resource))
                
        determination = input("> ")
        determination_levels.append(int(determination))    
                

    full_list = list(zip(energy_levels, resource_levels, determination_levels))
    
    mean_scores = []
    
    for i in full_list: 
        average_i = int(sum(i) / len(i))
        mean_scores.append(average_i)
        
    test_keys = paths 
    test_values = mean_scores
    
    new_dict = dict(zip(test_keys, test_values))
    print("The average score of each path is as follows: " + str(new_dict))
    time.sleep(1)
    
    max_key = max(new_dict)
    # fix the bug where you want to take the max value and return that corresponding key, not that you want to take the max key itself. 
    print("Based on your responses, it sounds like %s may be the life path you want to think harder about!" % max_key)
    time.sleep(2)
    final_approach() 

def final_approach():
    print("In this last part, we'll talk about how to go about your chosen path.")
    time.sleep(1)
    print("How are you thinking about pursuing your plan?")
    time.sleep(1)
    while True: 
    
        plan_pursuit = input("> ")
    
        if plan_pursuit == "work hard":
            print("That's a great attitude, but working hard is not the only important thing. What else?")
        elif plan_pursuit == "watch netflix and be intentional":
            print("I will let your cheeky netflix habit slide since you mentioned the intentional answer we were also looking for. Best of luck on your journey!")
            exit(0)
        elif plan_pursuit == "be intentional":
            print("Agreed! Being intentional and working hard will hopefully help you get started on your journey. Best of luck!")
            exit(0)
        else: 
            print("Not quite. Here's a hint: 'mindfulness'")

start()
