import os

class Person:

    #  Static list for contain all person
    persons_list = []

    def __init__(self, person_data):
        first_name, last_name, address, born_year, phone, tall, weight, gender = person_data
        self.first_name = first_name
        self.last_name = last_name

        self.address = address
        self.born_year = born_year
        self.phone = phone
        self.tall = tall
        self.weight = weight
        self.gender = gender

        self.persons_list.append(self)

    def person_counter(self, gender_type):
        """
        This is general function for count of male/female persons
        """
        counter = 0
        for item in self.persons_list:
            if item.gender == gender_type:
                counter += 1
        return counter

try:
    with open("persons.txt", 'r+') as file:
        array = [Person(row.strip().split(';')) for row in file]
except Exception:
    print("Can't open file persons.txt")

print(array[0].person_counter("Male"))
