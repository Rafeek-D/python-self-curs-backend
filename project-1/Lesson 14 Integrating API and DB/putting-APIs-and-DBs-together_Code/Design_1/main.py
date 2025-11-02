"""ReDI Students API

This API exposes the following endpoints
1. GET /students/ - for fetching all students data
2. DELETE /students/{student_name}} - for deleting a student by {student_name}
3. GET /courses/ - for fetching all courses
4. POST /courses/ - for inserting a new course with request body 
5. PUT /courses/{course_name} - for modifying a course content based on its name with a request body

request body:
{
    name: str
    semester: int
    difficulty: str
}
"""
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from pymongo import *

app = FastAPI()
uri = "mongodb+srv://user-redi-to-go:verysecret@sandbox.ydeko.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
database = client.redi_to_go_ahmed
students_collection = database.students
courses_collection = database.courses


class Student(BaseModel):
    name: str
    location: str
    age: int

class Course(BaseModel):
    name: str
    semester: int
    difficulty: str


@app.get("/")
def root():
    return {"message": "Welcome to ReDI ReDI Students API"}

@app.get("/students")
def getStudents():
    students = students_collection.find({})
    result = []
    for student in students:
        del student["_id"]
        result.append(student)
    return {"data" : result}

@app.get("/courses")
def getCourses():
    courses = courses_collection.find({})
    result = []
    for course in courses:
        del course["_id"]
        result.append(course)
    return {"data" : result}


@app.post("/courses")
def addCourse(course: Course):
    courses_collection.insert_one({
            "name": course.name,
            "semester": course.semester,
            "difficulty": course.difficulty
        })
    return {"message": "successful"}

@app.put("/courses/{course_name}")
def updateCourse(course_name: str, course: Course):
    courses_collection.replace_one({"name": course_name}, {
            "name": course.name,
            "semester": course.semester,
            "difficulty": course.difficulty
        })
    return {"message": "successful"}

@app.delete("/students/{student_name}")
def deleteStudent(student_name: str):
    students_collection.delete_one({"name": student_name})
    return {"message": "successful"}

#############################
## Add your endpoints here ##
#############################

if __name__ == "__main__":
    uvicorn.run("main:app",
                host='0.0.0.0',
                port=4557,
                reload=True,
                log_level="info")
