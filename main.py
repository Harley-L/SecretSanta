import random

from email1 import send_email

names = ["person1", "person2", "person3", "person4"]
emails = ["email1", "email2", "email3", "email4"]

choices = []
for i in range(len(names)):
    choices.append(i)

order_name = []
order_email = []

for i in range(len(choices)):
    random_pick = random.choice(choices)
    choices.remove(random_pick)
    order_name.append(names[random_pick])
    order_email.append(emails[random_pick])

for i in range(len(order_name)):
    if i != len(order_name)-1:
        send_email(order_email[i], order_name[i], order_name[i+1])
    else:
        send_email(order_email[i], order_name[i], order_name[0])
