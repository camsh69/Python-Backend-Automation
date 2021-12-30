import json

courses = '{"name": "RahulShetty", "languages": ["Java", "Python"]}'

# Loads method parses json string and returns dictionary
dict_courses = json.loads(courses)
print(type(dict_courses))
print(dict_courses)
print(dict_courses['name'])
# get first language
# list_languages = dict_courses['languages']
# print(type(list_languages))
# print(list_languages[0])
print(dict_courses['languages'][0])

# *** Parse content present in JSON file (load method)
with open('Documents\\course1.json') as f:
    data = json.load(f)
    print(data)
    print(type(data))
    print(data['courses'][1]['title'])
    print(data['dashboard']['website'])

#  no guarantee indexes will remain same so iterate through list to find a value
    for course in data['courses']:
        if course['title'] == "RPA":
            print(course['price'])
            assert course['price'] == 45
            break

# compare 2 json files to see if the same
with open('Documents\\course2.json') as fi:
    data2 = json.load(fi)
    assert data == data2
