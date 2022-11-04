
print ("Today you are going on a journey :) I'll ask you a few questions. \nThink carefully before you decide what to take with you.\nWhich one do you want to pick up: match OR flashlight ?")   
q = (str(input('I would like take: ')))
print("\n")

if q == "match":                                                                   
    print("You choosed ", q, "\nAnd right noooow, next question for your trip :) ");
    print("\n")

    q_1 =  (str(input("What would you like to take:me or her? ")))
    if q_1 == "me":                                                          
            print("You choosed ", q_1, "\nAnd neeeeext question for your trip :)" );

            q_2_1 = (str(input("dark or blue\n")))
            if q_2_1 == "dark":
                print("You took", q_2_1);
            elif q_2_1 == "blue":
                print("You took", q_2_1);
            else:
                print ("get out here!");




    elif q_1 == "her":
            print("You choosed ", q_1, "\nAnd neeeeext question for your trip :)");
        
            q_2_2 = (str(input("happy or mad\n")))
            if q_2_2 == "happy":
                print("You are ", q_2_2);
            elif q_2_2 == "mad":
                print ("You are", q_2_2);
            else:
                print("get out of here");
######################################################################################################################################
elif q == "flashlight":                                                                   
    print("You choosed ", q, "\nAnd right noooow, next question for your trip :) ");
    print("\n")

    q_1 =  (str(input("What would you like to take:fish or meat? ")))
    if q_1 == "fish":                                                          
            print("You choosed ", q_1, "\nAnd neeeeext question for your trip :)" );

            q_2_1 = (str(input("sugar or salt\n")))
            if q_2_1 == "sugar":
                print("You took", q_2_1);
            elif q_2_1 == "salt":
                print("You took", q_2_1);
            else:
                print ("get out here!");

    elif q_1 == "meat":
            print("You choosed ", q_1, "\nAnd neeeeext question for your trip :)");
        
            q_2_2 = (str(input("iPhone or Android\n")))
            if q_2_2 == "iPhone":
                print("You are ", q_2_2);
            elif q_2_2 == "Android":
                print ("You are", q_2_2);
            else:
                print("get out of here");





else:
    print("GET OUT OF HERE!!!! ");

#add timing