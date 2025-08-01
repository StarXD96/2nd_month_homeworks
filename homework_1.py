class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

person_1 = Person("Daniel", 2000,  "writer",  True)
person_2 = Person("Islam",  1998, "coder",  True)
person_3 = Person("Bael",  2007,  "student",  False)
print(f'name: {person_1.name}, birth date: {person_1.birth_date}, occupation: {person_1.occupation}, availability of higher education: {person_1.higher_education}')
print(f'name: {person_2.name}, birth date: {person_2.birth_date}, occupation: {person_2.occupation}, availability of higher education: {person_2.higher_education}')
print(f'name: {person_3.name}, birth date: {person_3.birth_date}, occupation: {person_3.occupation}, availability of higher education: {person_3.higher_education}')