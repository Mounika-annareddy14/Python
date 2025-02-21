programming_dictionary = {
    "Bug" : "An error in a program that prevents the program from running as expected.",
    "Function" : "A piece of code that you can easily call over again and again",
}

print(programming_dictionary)

#accessing element
print(programming_dictionary['Bug'])

# adding a element
programming_dictionary['Loop'] = "The action of doing something again and again."
print(programming_dictionary)

#wiping the dictionary
empty_dictionary = {}
#programming_dictionary = {}
# print(programming_dictionary)

# editing the item in a dictionary
programming_dictionary['Bug'] = 'A moth in Computer'
print(programming_dictionary)

# iterating the dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])



"""
Nested list and dictionaries
"""
travel_vlog = {
    "France" : ["Paris" , "Lille" , 'Dijon'],
    "Germany" : ['Stuttgart' , "Berlin"]
}
print(travel_vlog["Germany"][1])


nested_list = ["A" , "B" , ["c" , "D"]]

print(nested_list[2][1])

travel_vlog = {
    "France" : {
        "Cities_visitors" : ["Paris" ,"Lille" , 'Dijon' ],
        "Times_visited" : 12
    },

    "Germany" : {
        "cities_visitors" :['Stuttgart' , "Berlin"],
        "Times_visited" : 4
    }
}

print(travel_vlog["Germany"]["Times_visited"])