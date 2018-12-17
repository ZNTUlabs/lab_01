import random
import re
from faker import Faker
fake = Faker()

def generate_persons():
    first_name = fake.first_name()
    last_name = fake.last_name()

    address = fake.address()
    born_at = fake.date(pattern="%Y-%m-%d", end_datetime=None)
    phone = fake.isbn10(separator="-")
    tall = random.randint(120,200)
    weight = random.randint(45,110)
    gender = "Male" if(random.randint(0,1)) else "Famale"

    s = "%s;%s;%s;%s;%s;%s;%s;%s" % (first_name,last_name,address,born_at,phone,tall,weight,gender)
    return re.sub("\s+|\n", ' ', s) + "\n"

try:
    f = open('persons.txt', 'w+')
    for i in range(1000):
        f.write( generate_persons() )
except Exception:
    print("Can't open file persons.txt")
finally:
    f.close
