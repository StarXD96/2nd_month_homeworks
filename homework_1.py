class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

person_daniel = Person("Daniel", 2000,  "writer",  True)
person_islam = Person("Islam",  1998, "coder",  True)
person_bael = Person("Bael",  2007,  "student",  False)
print(f'name: {person_daniel.name}, birth date: {person_daniel.birth_date}, occupation: {person_daniel.occupation}, availability of higher education: {person_daniel.higher_education}')
print(f'name: {person_islam.name}, birth date: {person_islam.birth_date}, occupation: {person_islam.occupation}, availability of higher education: {person_islam.higher_education}')
print(f'name: {person_bael.name}, birth date: {person_bael.birth_date}, occupation: {person_bael.occupation}, availability of higher education: {person_bael.higher_education}')