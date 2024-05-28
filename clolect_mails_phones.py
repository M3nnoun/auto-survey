import pandas as pd

df=pd.read_csv("data_me.csv")
# Call the function to locate columns and retrieve values
cols=["ادخال البريد الالكتروني:", "رقم الهاتف (رقم الوتساب)"]

print(df[cols[1]].unique())
print(df[cols[0]].unique())

def check_and_add_emails(email_list_file, new_emails):
    # Read existing email list from file
    with open(email_list_file, 'r') as file:
        existing_emails = file.read().splitlines()

    added_emails = []
    # Check each new email
    for email in new_emails:
        # Check if the new email already exists
        if email in existing_emails:
            print(f"Email {email} already exists.")
        else:
            # Add the new email to the list
            existing_emails.append(email)
            added_emails.append(email)

    # Write the updated email list back to the file
    with open(email_list_file, 'a') as file:
        file.write('\n'.join(map(str, added_emails)))
        file.write('\n')
    
    print("Emails added successfully.")

def check_and_add_phones(phone_list_file, new_phones):
    # Read existing phone list from file
    with open(phone_list_file, 'r') as file:
        existing_phones = file.read().splitlines()

    added_phones = []
    # Check each new phone number
    for phone in new_phones:
        # Check if the new phone number already exists
        if phone in existing_phones:
            print(f"Phone number {phone} already exists.")
        else:
            # Add the new phone number to the list
            existing_phones.append(phone)
            added_phones.append(phone)

    # Write the updated phone list back to the file
    with open(phone_list_file, 'a') as file:
        file.write('\n'.join(map(str, added_phones)))
        file.write('\n')
    
    print("Phone numbers added successfully.")

email_list_file = r'contacts/email_list.txt'
new_emails =df[cols[0]].unique()
check_and_add_emails(email_list_file, new_emails)

phone_list_file = r'contacts/phone_list.txt'
new_phones = df[cols[1]].unique()
check_and_add_phones(phone_list_file, new_phones)
