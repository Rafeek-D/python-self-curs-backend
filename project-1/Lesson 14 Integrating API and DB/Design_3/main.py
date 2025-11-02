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
import uvicorn
from db import myDatabase, Course, StudentsCoursesRepository
from dotenv import load_dotenv

app = FastAPI()
db: StudentsCoursesRepository = myDatabase()
load_dotenv()

@app.get("/")
def root():
    return {"message": "Welcome to ReDI Students API"}

@app.get("/students")
def getStudents():
    students = db.getStudents()
    result = []
    for student in students:
        del student["_id"]
        result.append(student)
    return {"data" : result}

@app.get("/courses")
def getCourses():
    courses = db.getCourses()
    result = []
    for course in courses:
        del course["_id"]
        result.append(course)
    return {"data" : result}

@app.post("/courses")
def addCourse(course: Course):
    db.addCourse(
        course=course
    )
    return {"message": "successful"}

@app.put("/courses/{course_name}")
def updateCourse(course_name: str, course: Course):
    db.updateCourseByName(
        name=course_name,
        courseUpdated=course
    )
    return {"message": "successful"}

@app.delete("/students/{student_name}")
def deleteStudent(student_name: str):
    db.deleteStudentByName(name=student_name)
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
