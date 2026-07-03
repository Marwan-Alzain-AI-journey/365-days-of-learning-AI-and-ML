class student:

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
        if self.gpa >= 3.7:
            return True
        else:
            return False






class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer





class shazam:
    def ability(self):
        print ("fling mobility")

    def personality(self):
        print("sily")

    def super_abilty(self):
        print("invinsible")


from studer import shazam
class suberman(shazam):
    
    def special_ability(self):
        print("laser")
    
    def personality(self):
        print("serious")

    

        