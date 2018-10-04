contacts = [
    {
        "firstName": "Akira",
        "lastName": "Laine",
        "number": "0543236543",
        "likes": ["Pizza", "Coding", "Brownie Points"]
    },
    {
        "firstName": "Harry",
        "lastName": "Potter",
        "number": "0994372684",
        "likes": ["Hogwarts", "Magic", "Hagrid"]
    },
    {
        "firstName": "Sherlock",
        "lastName": "Holmes",
        "number": "0487345643",
        "likes": ["Intriguing Cases", "Violin"]
    },
    {
        "firstName": "Kristian",
        "lastName": "Vos",
        "number": "unknown",
        "likes": ["JavaScript", "Gaming", "Foxes"]
    }
];


def look_up_profile(name, field):
    x=0
    y=0
    if field == 'firstName':
        x=1
    if field == 'lastName':
        x=1
    if field == 'number':
        x=1
    if field == 'likes':
        x=1
    if x == 0:
        return 'No such property'
    for contact in contacts:
        if contact['firstName'] == name:
            y=1
            break
    if y == 0:
        return 'No such contact'
    
    return contact[field]
