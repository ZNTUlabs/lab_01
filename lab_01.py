import os

class Person:

    #  Static list for contain all person
    persons_list = []

    def __init__(self, first_name, last_name, parent_name, address, born_year, phone, tall, weight, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.parent_name = parent_name
        self.address = address
        self.born_year = born_year
        self.phone = phone
        self.tall = tall
        self.weight = weight
        self.gender = gender

        self.persons_list.append(self)
        self.write_to_report()
        

    def write_to_report(self):

        report_file = open('report', 'a+')
        report_file.write(self.first_name + "\n")
        report_file.close

    def person_counter(self, gender_type):
        """
        This is general function for count of male/female persons
        """
        counter = 0
        for item in self.persons_list:
            if item.gender == gender_type:
                counter += 1
        return counter

    def __str__(self):
        """
        Convert object to string
        """
        return 'First name: ' + self.first_name

# Create a few persons
Oleh = Person('Oleh', 'Levchenko', 'Anatoliy', 'ZP', 1982, '0992550572', 175, 90, 'male')
Anna = Person('Anna', 'Levchenko', 'Anatoliy', 'ZP', 1986, '0992550524', 165, 50, 'female')
Peter = Person('Peter', 'Johnson', 'Sam', 'NY', 1982, '7012347852', 185, 82, 'male')
Robert = Person('Robert', 'Planck', 'Gregory', 'LA', 1992, '7802136592', 178, 92, 'male')
Mary = Person('Mary', 'Porter', 'Franck', 'FL', 2001, '7023659812', 168, 51, 'female')

# Init list of persons
persons_list = []

# Add persons to list
persons_list.append(Oleh)
persons_list.append(Anna)
persons_list.append(Peter)
persons_list.append(Robert)
persons_list.append(Mary)

# Show count of person's gender
print(Mary.person_counter('female'))
