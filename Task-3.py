import random # this module will hepl to choose random values

def mail_check():
    """This function or program is made for chat box for the user in the university"""
    print("\n\nwelcome to pop chat \nOne of our operation will be pleased to hepl you today.")
    domain = "@pop.ac.uk"
    ID = input("\nPlease enter your Poppleton email address: ")
    if ID.index("@") <= 2 or domain not in ID:    # this line of code will first of index or point out the position of @ an chech whether the @ has position of 2 or not  
                                                    #and chech the domain  
        print("Invalid")
    else:
        seprate(ID)                  #pass the  value in seperate function  

def seprate(ID): 
    """this funcion is used for seperating mail id and name """                        # accepting the value for other function 
    user_name = ID.split("@")       # splectin the data by @ 
    name_user = user_name[0]        #indecing the first value of data 
    name = name_user.capitalize()   #make the first alphabet character capital    
    rand_name(name)                 #passing the function in rand_name  
    chat_box(name)                  #passing the function in chat_box                

def rand_name(name): 
    """This function is to communicate the random name form the list """
    print("Hi,{}! Thank you,and it will and welcome to pop chat !".format(name))
    names_user = ["Diwash","Karan","Mukesh","ynike","Saroj","Anish"]
    print("my name is {}, it will be  pleasure to help you today.".format(random.choice(names_user)))
    
def chat_box(name): 
    """This function is to chat with the user """ 
    list_1 = {"Library":("The library is closed today.","library will open 10 am.","do you want to call laberayan."),
    "Wifi":("wifi is exicellent acorss campus.","sorry! today campus network isunder maintanace.","you should tyr working in system."),
    "Deadline":("Your deadline has been extended by two working days.","your death line was yesterday.","If you miss you deathline contact to college."),
    "No":("try with new devide.","sorry! service is not avilable.","You should be college student frist.","contact to your administrator."),"What":("contact to your administartor.",
    "contact to you tutorial.","please do google search.")}    # dictionary are used to store value  
    list_2 = ["Hmmmmmmm","Tell me more","Oh, yes, I see,","No you are wrong","okey!......","I did not understand"] # using list
    
    num = (1,2,3,4,5,6,7,8,9,0,11)
    c = random.choice(num) # chosse random values for num
    if c != 0:
        while True:
            input_queries = input("--->")
            if  input_queries.capitalize() == "Exit" or  input_queries.capitalize() == "Goodbye"(): # this line will help to brek the loop  
                print("\nThanks,{} ,for using popChat. seem!".format(name))
                break
            elif  "Library" in input_queries.capitalize(): # it check wether the workd contain library or not
                print(random.choice (list_1["Library"])) # print the random value form the dictionary with the help or key words
            elif "No" in input_queries.capitalize():
                print(random.choices (list_1["No"]))
            elif "What" in input_queries.capitalize():
                print(random.choice (list_1["What"]))
            elif "deathline" in input_queries.lower():
                print(random.choice(list_1["Deadline"])) 
            elif "wifi" in input_queries.lower():
                print(random.choice(list_1["Wifi"]))       
            else:
                print(random.choice(list_2))    # if the word doesnot match the with the input word than it will print random value form        
    else:
        print("\n***Network Error***")
        print("\nThanks, {}, for using PopChat. See you again soon !".format(name))
mail_check()
