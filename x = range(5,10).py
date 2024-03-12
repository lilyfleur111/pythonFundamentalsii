x = range(5,10)
petName = ("snowy", "blacky", "bruno")

# for loop
# for (inititialization;codition;incrementation/decre) - JAVA

# for num in x:
#     print(num)

# Slicing a lists
# for name in petName[0:2]:
#     print(name)

# Looping Dicitionaries
# key: value   
# user = {
#     "first_name" : "vgds",
#     "last_name" : "aaaa",
#     "age" : 25,
#     "average" : 81.76,
#     "list_subjects" : ["Programming", "Mathematics", "English"]
# }

# ctrl + / - shortcut for comment

# for key in user:
#     print(key, ":", user[key])

# Looping list of Dictionaries
list_of_users = [
    {
        "first_name" : "vgds",
        "last_name" : "aaaa",
        "age" : 25,
        "average" : 81.76,
        "list_subjects" : ["Programming", "Mathematics", "English"]
    },
    {
        "first_name" : "def",
        "last_name" : "wdew",
        "age" : 23,
        "average" : 82.54,
        "list_subjects" : ["Programming", "Mathematics", "English"]
    },
    {
        "first_name" : "scaa",
        "last_name" : "efee",
        "age" : 27,
        "average" : 86,
        "list_subjects" : ["Programming", "Mathematics", "English"]
    }
]

for key in list_of_users:
    for x in key:
        print(x, ":", key[x])

x = range(1,10)
for i in x[::-1]:
    print(i)