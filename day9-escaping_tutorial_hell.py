from class2 import currensy
from class2 import list
from class2 import list2
from class2 import list3
from class2 import list4
s1 = currensy(input("YOUR CURRENCY: "),input("SECOND CURRENCY: "),float(input(" AMOUNT OF MONEY: ")))
def w2():
    if s1.your_currency == "USD":
        if s1.second_currancy == "SYP":
            return float(list["SYP"]) * s1.amount
        elif s1.second_currancy == "EUR":
            return float(list["EUR"]) * s1.amount
        elif s1.second_currancy == "TUR":
            return float(list["TUR"]) * s1.amount 
        else:
            print("Value not found in dictionary!")
    if s1.your_currency == "SYP":
        if s1.second_currancy == "USD":
            return float(list3["USD"]) * s1.amount
        elif s1.second_currancy == "EUR":
            return float(list3["EUR"]) * s1.amount
        elif s1.second_currancy == "TUR":
            return float(list3["TUR"]) * s1.amount 
        else:
            print("Value not found in dictionary!")

    if s1.your_currency == "TUR":
        if s1.second_currancy == "USD":
            return float(list4["USD"]) * s1.amount
        elif s1.second_currancy == "EUR":
            return float(list4["EUR"]) * s1.amount
        elif s1.second_currancy == "SYP":
            return float(list4["SYP"]) * s1.amount 
        else:
            print("Value not found in dictionary!")


    if s1.your_currency == "EUR":
        if s1.second_currancy == "USD":
            return float(list2["USD"]) * s1.amount
        elif s1.second_currancy == "SYP":
            return float(list2["SYP"]) * s1.amount
        elif s1.second_currancy == "TUR":
            return float(list2["TUR"]) * s1.amount 
        else:
            print("Value not found in dictionary!") 

print(w2())