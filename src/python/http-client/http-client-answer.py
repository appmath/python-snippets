import random
import string

def generate_random_email(domain_list=None, num_emails=1):
    if domain_list is None:
        domain_list = ["example.com", "test.com", "sample.org"]

    email_list = []

    for _ in range(num_emails):
        username_length = random.randint(6, 12)
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))
        domain = random.choice(domain_list)
        email = f"{username}@{domain}"
        email_list.append(email)

    return email_list

# Generate 10 random email addresses
random_emails = generate_random_email(num_emails=10)
for email in random_emails:
    print(email)