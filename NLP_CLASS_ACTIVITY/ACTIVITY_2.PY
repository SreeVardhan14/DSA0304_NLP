import re

text = "My email is student@gmail.com and my phone number is 9876543210."

email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
email = re.search(email_pattern, text)

phone_pattern = r'\b\d{10}\b'
phone = re.search(phone_pattern, text)

if email:
    print("Email:", email.group())

if phone:
    print("Phone Number:", phone.group())