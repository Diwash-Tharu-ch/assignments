print("""\nStop! Who would cross the Bridge of Death
Must answer me these questions three, 'ere the other side he see""")
user_data = input("\n what is your name?: ")
if  "Arthur" in user_data.capitalize(): # this will check whether the name is authur or not   
    print("My liege! You may pass!")  
elif"Arthur"  not in  user_data.capitalize(): # capitilize will make inital alphebet of the word in capital  
    data_1 = input("What is your quest?")
    if "grail" in data_1.lower(): # this will check whether the words contain grail or not and lower will change all word in lowercase  
        data_2  = input("Ente your faveraout color")
        if user_data.capitalize()[0]==data_2.capitalize()[0]: # it will ceck inital character of name and favourate color
            print("you may pass !") 
        else:
            print("Incorrect! You must now face the Gorge of Eternal Peril")  
    else:
        print("Only those who seek the Grail may pass.")
else:
    print("My liege! You may pass!")        
