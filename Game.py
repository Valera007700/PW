
print ("two items: a  MATCH and a FLASHLIGHT. Which one do you want to pick up?")   
q = (str(input('I would like take\n')))

if q == "1":                                                                   
    print("You choosed ", q, "\nAnd right noooow, next question for your trip :) ");

        q_1 =  (str(input("1.1 OR 1.2, What would you like?\n")))
        if q_1 == "1.1":                                                          
            print("You choosed ", q_1, "\nAnd right noooow, next question for your trip :)" );

            q_2 = (str(input("1.1.1 OR 1.1.2")))
            if q_2 == "1.1.1":
                print("1.1.1");
            elif q_2 == "1.1.2":
                print("1.1.2");
            else:
                print ("get out here!");




    elif q_1 == "1.2":
        print("1.2");
        
        answer_3_2 = (str(input("")))
        if answer_3_2 == "1.2.1":
            print("1.2.1");
        elif answer_3_2 == "1.2.2":
            print ("1.2.2");
    else:
        print("get out of here");
elif q == "2":
    print("2");
    answer_2 =  (str(input("")))
    if answer_2 == "2.1":
        print("2.1")
        answer_2_2 =  (str(input("")))
        if answer_2_2 == "2.1.1":
            print("2.1.1")
        elif answer_2_2 == "2.1.2":
            print ("2.1.2")
    elif answer_2 == "2.2":
        print("2.2");
        answer_2_4 =  (str(input("")))
        if answer_2_4 == "2.2.1":
            print("2.2.1")
        elif answer_2_4 == "2.2.2":
            print ("2.2.2")
else:
    print("wrong");