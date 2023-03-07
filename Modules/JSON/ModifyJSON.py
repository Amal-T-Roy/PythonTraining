import json

def UpdateMail():
    Name = input('Enter person whose mail is to be changed:\n')
    Mail = input('Enter new mail id:\n')
    # Read JSON file
    with open('data.json') as f:
        # Persons = json.loads(f.read())
        Persons = json.load(f)
    NewList = [] # Empty list to which each dictionary is appended
    for Person in Persons:
        if Person['Name'] == Name: # If name maches with the person whose mail is to be updated
            NewRecord = {} # Dictionary to which data is added
            NewRecord['Name'] = Name # Setting key-value pair of Name,where value = name received from CLI
            NewRecord['email'] = Mail # Setting key-value pair of Mail,where value = mail received from CLI
            NewList.append(NewRecord) # Appending the dictionary to the final list
            print('Update')
        else:
            NewRecord = {} # Dictionary to which data is added
            NewRecord['Name'] = Person['Name'] # Setting key-value pair of Mail,where value = name in original JSON file
            NewRecord['email'] = Person['email'] # Setting key-value pair of Mail,where value = mail in original JSON file
            NewList.append(NewRecord)
    # Writing to JSON file
    with open('data.json','w') as f:
            json.dump(NewList, f, indent=2)
    f.close()
            

def AddPerson():
    ID = int(input('Enter ID:\n'))
    Name = input('Enter Name:\n')
    Mail = input('Enter Mail:\n')

    # Read Existing JSON File
    with open('data.json') as f:
        data = json.load(f) # Returns a list of dictionaries
    # Append new object to the list of dictionaries
    data.append({
            "ID": ID,
            "Name": Name,
            "email": Mail
        })
        
    # Create new JSON file
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    # Closing file
    f.close()

# Function to delete a persons data from JSON file
def DeletePerson():
    Name = input('Enter person whose details is to be deleted:\n')
    # Read JSON file
    with open('data.json') as f:
        # Persons = json.loads(f.read())
        Persons = json.load(f)
    NewList = [] # Empty list to which each dictionary is appended
    for Person in Persons:
        if Person['Name'] == Name: # If name maches with the person whose mail is to be updated
            print(f"Deleting {Name}'s info")
        else:
            NewRecord = {} # Dictionary to which data is added
            NewRecord['ID'] = Person['ID']
            NewRecord['Name'] = Person['Name'] # Setting key-value pair of Mail,where value = name in original JSON file
            NewRecord['email'] = Person['email'] # Setting key-value pair of Mail,where value = mail in original JSON file
            NewList.append(NewRecord)
    # Writing to JSON file
    with open('data.json','w') as f:
            json.dump(NewList, f, indent=2)
    
# AddPerson()
# UpdateMail()
DeletePerson()