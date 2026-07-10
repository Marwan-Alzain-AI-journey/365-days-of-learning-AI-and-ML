from class3 import customer_imformation
import random
cus = customer_imformation(input("Enter your last name: "),input("Enter your first naem: "),input("enter your ID if have and if ont just write N: "), 0)
cus_first_name = cus.first_name
cus_file_name = cus_first_name.capitalize() + " " + cus.last_name.capitalize() + ".txt"
cus_full_name = cus_first_name.capitalize() + " " + cus.last_name.capitalize()

def new():
    if cus.ID == "N":
        cus_file = open(cus_file_name,"w")
        cus_file.write("name: "  + cus_full_name)
        cus_file.close()
        cus_file = open(cus_file_name, "a")
        ID_number = random.randint(1000000000, 9999999999)
        cus_file.write("\nID: " + str(ID_number))
        cus_file.write("\nbalance: \n" + str(cus.balance) )
        cus_file.close()

        return "your ID number: " + str(ID_number) + "\n" + "your balance: " + str(cus.balance)
    else:
        cus_file = open(cus_file_name, "r")
        s1 = cus_file.readlines()[3]
        s2 = int(s1)
        cus.balance += s2
        cus_file.close()
        return "your ID number: " + str(cus.ID) + "\n" + "your balance: " + s1
print(new())
def w1():
    operator =input("enter W if you want to withdraw or D if you want to deposite: ")
    if operator == "w":
        withdrawal = input("enter how much do you want to withdraw: ")
        if cus.balance >= int(withdrawal):
            withdrawal_operation = int(cus.balance) - int(withdrawal)
            cus_file = open(cus_file_name, "a")
            cus_file.write("\n(withdrawal opration)\nyou've withdrew: " + withdrawal + "\nyournew balance: " + str(withdrawal_operation))
            cus_file.close()
            
            cus_file = open(cus_file_name, "r")
            line = cus_file.readlines()
            try:    
                line[3]  = str(withdrawal_operation) +"\n"
                cus_file = open(cus_file_name, "w")
                line = cus_file.writelines(line)
                cus_file.close()
            except:
                print("out of range")
            return "your new balace: " + str(withdrawal_operation)
        elif cus.balance < int(withdrawal):
            return "not enough balance: " +  str(cus.balance)
    elif operator == "d":
        deposite = input("enter how much money do you want to deposite: ")
        deposite_operation = int(cus.balance) + int(deposite)
        cus_file = open(cus_file_name, "a")
        cus_file.write("\n(deposite operation)\nyou've deposited: " + deposite + "\nnew balance: " + str(deposite_operation))
        cus_file.close()
        
        cus_file = open(cus_file_name, "r")
        line = cus_file.readlines()
        cus_file.close()
        try:
                line[3] = str(deposite_operation) + "\n"

                cus_file = open(cus_file_name, "w")
                cus_file.writelines(line)
                cus_file.close()
        except IndexError:
                print("out of range")
        return "your new balance: " + str(deposite_operation)
    else:
        return "invalid input"
print(w1())

condition_for_acount_reveal = input("if you want an acount reveal enter yes and if not no: ")
if condition_for_acount_reveal == "yes":
    def reveal():
        cus_file = open(cus_file_name, "r")
        print("acount reveal")
        line = 0
        for acount_reveal in cus_file:
            line += 1
            if line < 5:
                    continue
            print(acount_reveal.strip())
    reveal()
elif condition_for_acount_reveal == "no":
     print("done")
