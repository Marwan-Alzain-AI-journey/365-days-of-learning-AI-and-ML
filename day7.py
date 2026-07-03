

from studer import student
s1 = student("ahmad".title(), "english literature".title(), float(3.7), False)
s2 = student("marwan".title(), "midacine".title(), float(3.9), True)


print(s2.name)
print(s1.on_honor_roll())  




from studer import Question
q_q = [
    "who wrote Hamle? \n (a)J.K roaing \n (b)Shakespear \n (c)cresropher nollan\n\n",
    "who wrote To THE Light House? \n(a)verginia woolf  \n(b)tom  blake  \n(a)suphclus\n\n",
    "who wrote THE SONG OF ICE AND FORE?\n(a) George R.R. Marten \n(b) mathio white  \n(c)sophia burnnet\n\n",
]

q1 =[
    Question(q_q[0], "b"),
    Question(q_q[1], "a"),
    Question(q_q[2], "a"),
]

def test(q1):
    socre = 0
    for q2 in q1:
        answer = input(q2.question)
        if answer == q2.answer:
            socre += 1
    print("you got " + str(socre) + " out of " + str(len(q_q)) + "correct")        


test(q1)
  


from marwan import suberman
my_hero = suberman()
my_hero.personality()
 