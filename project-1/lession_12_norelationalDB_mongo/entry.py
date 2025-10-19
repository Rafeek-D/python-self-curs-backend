

############################## Part 1 ########################################




#%pip install "pymongo[srv]"

'''
from bson import ObjectId
from pymongo import MongoClient
'''
from os import remove

###-------------------------
#client = MongoClient("mongodb+srv://rafeekslack_db_user:......ldwJTBVs2h6i@clus0.jnqagzn.mongodb.net/?retryWrites=true&w=majority&appName=Clus0")
###-------------------------

###-------------------------
'''
## DB1: K00P
database = client.DB1
collection = database.Coll1
usr = collection.find({})
for x in usr:
    print(x)

'''
###-------------------------


'''
###-------------------------
## DB school: K00P
# Define a database name "school". If a given database is not found, a new one will be created when data is inserted.
database = client.school

# Define a collection name "course". If a given collection is not found, a new one will be created when data is inserted.
collection = database.students

students_from_collection = collection.find({})
print(students_from_collection)
###-------------------------
'''


'''
###-------------------------
for student in students_from_collection:
    print(student)

    #if isinstance(student, ObjectId):
    #if student:
        #print(type(student))  => <class 'dict'>
    #else:
       # print("empty")
###-------------------------
'''



###-------------------------
'''
# Insert one document into the collection

collection.insert_one({
    "_id": ObjectId("626bccb9697a12204fb22ea3"),
    "name": "John Doe",
    "location": "Homburg",
    "courses": ["Python", "MongoDB"],
    "age": 25
})
'''
###-------------------------


###-------------------------
'''
# Insert multiple documents
collection.insert_many([
    {
        "name": "Jane Doe",
        "location": "Munich",
        "courses": ["Java", "MySQL"],
        "age": 28
    },
    {
        "name": "max",
        "location": "Berlin",
        "courses": "Java",
        "age": 30
    }
    ])
'''
###-------------------------


'''
###-------------------------
# Find studnets from  DB School and collection Student, and the student is in Munich
for student in collection.find({"location": 'Munich'}):
    print(student)
###-------------------------
'''

'''
###-------------------------
# Find studnets from  DB School and collection Student, and studnets either in Munich or Homburg
students = collection.find({"location": {"$in": ["Munich", "Homburg"]}})

for student in students:
    print(student)
###-------------------------
'''

'''
###-------------------------
# Filter by student's name. if not in the collection, then will be None as a reuslt.
# the reulst is with big or small letter max != Max.

#1)
# and it will take only one result, if two max are
#name_result= collection.find_one({"name": "max"})
#print(name_result)

#2)
#ore with all the entry:
name_result2 = collection.find({})
for student in name_result2:
    #print(student.get("name"))
    #print(student.get("courses"))
    if student["name"] == "max":
        print(student)
        #print(student.get("name"),student.get("location"),student.get("courses"),student.get("age"))
###-------------------------
'''

'''
###----------not work!!!---------------
# Update a property within the document to a new value
#collection.update_one({"_id": max["_id"]}, {"$set": {"age": 40}})
#print(collection.update_one({"_id": max["_id"]}))

##this ist work:, after than get a none ???
print(collection.find_one(ObjectId("68f40b238354267aded36924")))

###-------------------------
'''

'''
###----------not work!!!---------------
# Filter by student's name
#print(collection.find_one({"_id": Jane Doe["_id"]}))

###-------------------------
'''

'''
###-------------------------
# Delete a document using Object ID
#print(collection.find_one({"name": "max"}))
print(print(collection.find_one(ObjectId("68f40b238354267aded36925"))))
collection.delete_one({"_id": ObjectId("68f40b238354267aded36925")})
###-------------------------
'''

'''
###-------------------------
# Delete all documents in the collection
collection.delete_many({})
###--------------------------
'''




##############################Part 2########################################


#%pip install mongoengine
from mongoengine import connect, disconnect, Document
from mongoengine import StringField, IntField, ListField

##-----------------------------------------------
# if the db=name. and the name of DB not exist than you will not get a error and if you create a collection than it will create a DB with this collection!!
#connect(host="mongodb+srv://rafeekslack_db_user:.......ldwJTBVs2h6i@clus0.jnqagzn.mongodb.net/?retryWrites=true&w=majority&appName=Clus0", db="school3")
##-----------------------------------------------


'''
##-----------------------------------------------
# Student here represent a collection in the database
class Student(Document):
    name = StringField(max_length=64, required=True)
    location = StringField(max_length=64)
    courses = ListField(StringField(max_length=64))
    age = IntField(min_value=17, max_value=99)

    def get_info(self):
        return f"the name:{self.name}, the location:{self.location}, the courses:{self.courses}, the age:{self.age} "
        #return f"the name:{self.name}, the location:{self.location}, the courses:{self.courses[0]}, the age:{self.age} "

##-----------------------------------------------
'''




'''
##-----------------------------------------------
# Create new Student object which translate into a document in the student collection
newstudent = Student(name="Naoto", location="Japan", courses=["Marketing"], age=34)
newstudent2 = Student(name="max", location="MU", courses=["DB"], age=20)
##-----------------------------------------------
'''


'''
##-----------------------------------------------
# Saving the student's instance.
newstudent.save()
newstudent2.save()
##-----------------------------------------------
'''

'''
##-----------------------------------------------
# Print the auto generated student's id, name, location
print(newstudent.id)
print(newstudent.name)
print(newstudent.location)
##-----------------------------------------------
'''

'''
##-----------------------------------------------
# Prints out the names of all the students in the database
for user in Student.objects:
    print(user.name)
##-----------------------------------------------
'''

'''
##-----------------------------------------------
## delete instance, one from many with same name
#first Naoto: 68f422af5d7429408687ed29

#1)
for user in Student.objects:
    if user.name == "Naoto":
        print(user.id)
        #user.delete()
        break
    break

#2)
#direct remove:
#Student.objects(id=new_st1.id).delete()
##-----------------------------------------------
'''


'''
##-----------------------------------------------
# Count number of students
print(Student.objects.count())
##-----------------------------------------------
'''

'''
##-----------------------------------------------
# Check whether the new student's state is valid
#newstudent2.age = 14
#newstudent2.validate()   # not work!!!

for user in Student.objects:
    if user.name != "max":
        pass
    else:
        print(type(user)) #<class '__main__.Student'>
        print(user.get_info())
        print(user.age )

##-----------------------------------------------
'''






'''
##-----------------------------------------------
# Disconnect your connection
disconnect()
##-----------------------------------------------
'''


