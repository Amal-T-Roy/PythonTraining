''' JavaScript Object Notation '''
import json

#Initial json string in the form of a dictionary
people_string ='''
{
    "people": [
        {
            "name" : "John Doe",
            "Number":1234,
            "single":true
        },
        {
            "name" : "Jane Doe",
            "Number":5678,
            "single":false
        }
    ]

}
'''

data = json.loads(people_string) #load json into python object->Read as load s
print(data)

print(type(data))

#access each person
for person in data['people'] :
    print(person)

#Access only names
for person in data['people'] :
    print(person['name'])

for person in data['people'] :
    print(person['Number'])
    del person['Number'] #deletes number of the members
    #print(person['Number'])

#After deleting load them into new json string
new_string = json.dumps(data)
print(new_string)