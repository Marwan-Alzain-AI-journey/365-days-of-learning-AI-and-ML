def f1():
    is_handsom = True
    is_male = False
    if is_handsom and is_male:
        print("you are a handsome man")
    elif not(is_handsom) and is_male:
        print("HI there")
    elif is_handsom and not(is_male):
        print("you are welcome!")
    else:
        print("you are a pretty woman\"")
def e1(m1, m2, m3, m4):
    if m1 >= m2 and m1 >= m3 and m1 >= m4:
        print(m1)
    elif m2 >= m1 and m2 >= m3 and m2 >= m4:
        print(m2)
    elif m3 >= m1 and m3 >= m2 and m3 >= m4:
        print(m3)
    else:
        print(m4)
def r1():
    w1 = input("enter a name:") 
    print(w1.capitalize())
def q1():
    num1 = float(input("enter first num: "))
    op = input("enter an operator: ")
    num2 = float(input("enter a second number: "))

    if op == "+":
        result = num1 + num2
        print(result)
    elif op == "-":
        result = num1 - num2
        print(result)
    elif op == "/":
        result = num1 / num2
        print(result)
    elif op =="*":
        result = num1 *num2
    else:
        print("invalid operator!!")

s1 = {
    1 : "marwan alzain, fourth year,  english literature",
    2 : "ali bittar, fifth year, medicine ",
    3 : "mahmoud maraash,third year, geographgy ",
    4 : "mallek bittar, first year, english literature",
}
print(s1.get(5, "invalid key"))


i = 1
while i < 10:
    print(i)
    i += 1



secret_num = 56
geuss = ""
num_of_geuss = 0
geuss_limit = 10
out_of_geusses = False
while geuss != secret_num and not(out_of_geusses) :
    if num_of_geuss < geuss_limit:
        geuss = float(input(" enter a number: "))
        num_of_geuss = num_of_geuss + 1
        if geuss < secret_num:
            print("HIGHER")
        elif geuss > secret_num:
            print("LOWER")
    else:
        out_of_geusses = True
        print(" ^^ out of geusses ")

if not(out_of_geusses):
    print("!!!you win")
