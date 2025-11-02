from pydantic import BaseModel
from pymongo import *
import os


class Student(BaseModel):
    name: str
    location: str
    age: int

class Course(BaseModel):
    name: str
    semester: int
    difficulty: str

class StudentsCoursesRepository:
    def __init__(self) -> None:
        pass

    def getStudents():
        pass

    def getCourses():
        pass

    def addCourse(course: Course):
        pass

    def updateCourseByName(name: str, courseUpdated: Course):
        pass

    def deleteStudentByName(name: str):
        pass

class myDatabase(StudentsCoursesRepository):
    user = os.getenv('MONGO_USER')
    password = os.getenv('MONGO_PASS')
    uri = "mongodb+srv://{}:{}@sandbox.ydeko.mongodb.net/?retryWrites=true&w=majority".format(user,password)
    client = MongoClient(uri)
    database = client.redi_to_go_ahmed
    students_collection = database.students
    courses_collection = database.courses

    def getStudents(self):
        return self.students_collection.find({})
    
    def getCourses(self):
        return myDatabase.courses_collection.find({})
    
    def addCourse(self, course: Course):
        return self.courses_collection.insert_one({
            "name": course.name,
            "semester": course.semester,
            "difficulty": course.difficulty
        })
    
    def updateCourseByName(self, name: str, courseUpdated: Course):
        return self.courses_collection.replace_one({"name": name}, {
            "name": courseUpdated.name,
            "semester": courseUpdated.semester,
            "difficulty": courseUpdated.difficulty
        })
    
    def deleteStudentByName(self, name: str):
        return self.students_collection.delete_one({"name": name})