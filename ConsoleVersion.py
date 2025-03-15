#chatbot
print("Hello! Welcome to the Budgeting Tracker Chatbot.")

#how much you spent
category = []
check = "1"
while(True):
    if check == "1":
        user = input("Add a category to the list: ")
        category.append(user)
        print("These are your categories: ", category)
        check = "2"
    
    if check == "2":
        end = input("Are you done inputting categories: ")
        if end.lower() == "yes":
            print(category)
            break
        elif end.lower() == "no":
            print()
            check = "1"
        else:
            "Please Type Yes or No"
            check = "2"
chart = {}
total = {}
flag = "1"
for each in category:
    print()
    chart[each] = 0
    while(True):
        if flag == "1":
            item = input("What item do you spend on for " + each + ": ")
            spent = float(input("How much did you spend for that item $"))
            total[item] = spent
            chart[each] += spent
            flag = "2"
        
        if flag == "2":
            end = input("Are you done inputting items for " + each + ": ")
            if end.lower() == "yes":
                flag = "1"
                break
            elif end.lower() == "no":
                print()
                flag = "1"
            else:
                "Please Type Yes or No"
                flag = "2"
    print(chart)
    print(total)
#Pi-Chart
percentage = {}
final = sum(chart.values())
for each in chart:
    percentage[each] = round((chart[each] / final) * 100, 2)
for each in percentage:
    percentage[each] = str(percentage[each]) + "%"
print("\n", percentage)

#how much you saved (income/ratio/recommondation)
while(True):
    ask = input("Do you have a job? Or some way of getting money? ")
    if ask.lower() == "yes":
        job = input("What is your salary or how much money do you make? $")
        ratio = float(job)/float(final)
        if ratio > 1:
            print("You have a good ratio. You can be more flexible with your money!")
            break
        else:
            print("You have a bad ratio. You should be more cautious of your spendings. Start saving more!")
            break
    elif ask.lower() == "no":
        print("Ratio can't be calculated.")
        break
    else:
        print("Type yes or no.")

#how much you saved (bank/interest)
import math
bank_money = (input("How much money have you saved in the bank? "))
bank_interest = input("What is the annual interest that the bank offers? ")
while True:
    compounding = input("How is your money compounded? (yearly, monthly, quarterly) ")
    years = input("How many years have you been saving your initial deposit? ")
    if compounding.lower() == "yearly":
        new_money = float(bank_money) * (1+(float(bank_interest)/100)) ** float(years)
        money_interest = new_money - float(bank_money)
        print("You have gained ", "$", round(money_interest,2), "by saving", "$", round(float(bank_money),2), "for", float(years), "years")
        break
    elif compounding.lower() == "quarterly":
        new_money = float(bank_money) * (1+(float(bank_interest)/100)/4) ** (4*float(years))
        money_interest = new_money - float(bank_money)
        print("You have gained ", "$", round(money_interest,2), "by saving", "$", round(float(bank_money),2), "for", (4*float(years)), "quarters")
        break
    elif compounding.lower() == "monthly":
        new_money = float(bank_money) * (1+(float(bank_interest)/100)/12) ** (12*float(years))
        money_interest = new_money - float(bank_money)
        print("You have gained ", "$", round(money_interest,2), "by saving", "$", round(float(bank_money),2), "for", (12*float(years)), "monthly")
        break
