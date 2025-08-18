class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        print(f"Hello my name is {self.name}, I'm friend with Chyntemir, I was born in {self.birth_date} and currently I'm working as {self.occupation}.")

class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        print(f"Hello my name is {self.name}, I'm Chyntemir's classmate, I was born in {self.birth_date}, currently I'm working as an {self.occupation} and we were on the same {self.group_name} group.")

class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        print(f"Hello my name is {self.name}, I'm friend with Chyntemir, I was born in {self.birth_date}, currently I'm working as a {self.occupation} and my hobby is {self.hobby}.")

classmate_1 = Classmate("Nurbol", 2001, "Artist", True, '11-V')
classmate_2 = Classmate('Alisher', 2002, "Office manager", True, '11-V')
friend_1 = Friend("Danil", 2000, "Programmer", False, 'sports')
friend_2 = Friend("Sadyr", 1998, "Pilot", True, 'painting')
for person in [classmate_1, classmate_2, friend_1, friend_2]:
    person.introduce()