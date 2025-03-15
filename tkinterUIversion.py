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

import tkinter as tk

frame = tk.Tk()
frame.geometry("1200x600")

category_index = 0
label = tk.Label(text=f"Category: {category[category_index]}")
label.pack()

chart = {}
chart[category[category_index]] = 0
def calc():
    items = item.get()
    amounts = amount.get()
    amount_value = float(amounts)
    chart[category[category_index]] += amount_value

def update():
    global category_index
    category_index += 1

    if category_index >= len(category):
        print(chart)
        frame.destroy()
        #pi chart
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
        

    else:
        label.config(text=f"Category: {category[category_index]}")
        chart[category[category_index]] = 0


item = tk.StringVar()
item_label = tk.Label(text="Item: ")
item_entry = tk.Entry(frame, textvariable = item)
item_label.pack()
item_entry.pack(pady=5)

amount_label = tk.Label(text="Amount: ")
amount_label.pack()

amount = tk.StringVar()
amount_entry = tk.Entry(frame, textvariable = amount)
amount_entry.pack(pady=5)

submit = tk.Button(frame, text = "Submit", command = calc)
submit.pack()

finish = tk.Button(frame, text="Finish", command = update)
finish.pack(pady=5)

import random
advise = ["Set Clear Financial Goals", "Calculate your net income", "Track your spending", "Categorize Your Expenses",
          "Create a Realistic Budget", "Build an Emergency Fund", "Reduce Unnecessary Expenses", "Automate Savings and Bill Payments",
          "Take Advantage of Discounts and Cashback Rewards", "Review and Adjust Your Budget Monthly"]

def reco():
    recommendations.config(text = "Recommendation: " + random.choice(advise))
    recommendations.pack(pady=5)

recommendations = tk.Label(text = "")
reco_button = tk.Button(frame, text = "Recommendations ", command = reco)
reco_button.pack(pady=5)



tk.mainloop()
