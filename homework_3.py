class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.__birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education

    def introduce(self):
        if self.higher_education:
            print(f"Hello my name is {self.name}, I was born in {self.birth_date} and currently I'm working as {self.occupation} and I have a higher education.")
        else:
            print(f"Hello my name is {self.name}, I was born in {self.birth_date} and currently I'm working as {self.occupation} and I don't have a higher education.")

    @property
    def age(self):
        day, month, year = map(int, self.__birth_date.split("."))
        today_day = 8
        today_month = 8
        today_year = 2025
        age = today_year - year
        if (today_month, today_day) < (month, day):
            age -= 1
        return age

    @property
    def occupation(self):
        return self.__occupation

    @property
    def higher_education(self):
        return self.__higher_education

    @property
    def birth_date(self):
        return self.__birth_date

    @higher_education.setter
    def higher_education(self, value):
        self.__higher_education = value

class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        if self.higher_education:
            print(f"Hello my name is {self.name}, I'm Chyntemir's classmate, I was born in {self.birth_date} so I'm {self.age} years old, currently I'm working as an {self.occupation}, we were on the same {self.group_name} group and I have a higher education.")
        else:
            print(
                f"Hello my name is {self.name}, I'm Chyntemir's classmate, I was born in {self.birth_date} so I'm {self.age} years old, currently I'm working as an {self.occupation}, we were on the same {self.group_name} group and I don't have a higher education.")
class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        if self.higher_education:
            print(f"Hello my name is {self.name}, I'm friend with Chyntemir, I was born in {self.birth_date} so I'm {self.age} years old, currently I'm working as a {self.occupation} and my hobby is {self.hobby} and I have a higher education.")
        else:
            print(
                f"Hello my name is {self.name}, I'm friend with Chyntemir, I was born in {self.birth_date} so I'm {self.age} years old, currently I'm working as a {self.occupation} and my hobby is {self.hobby} and I don't have a higher education.")


classmate_1 = Classmate("Nurbol", "24.12.2001", "Artist", True,  '11-V')
classmate_2 = Classmate('Alisher', "12.8.2002", "Office manager", False, '11-V')
friend_1 = Friend("Danil", "10.2.2000", "Programmer", False, 'sports')
friend_2 = Friend("Sadyr", "12.4.1998", "Pilot", True, 'painting')
for person in [classmate_1, classmate_2, friend_1, friend_2]:
    person.introduce()
