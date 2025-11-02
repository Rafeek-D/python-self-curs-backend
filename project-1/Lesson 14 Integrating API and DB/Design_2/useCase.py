from db import myDatabase

class studentsUseCase:
    database = myDatabase

    def __init__(self, database) -> None:
        self.database = database

    def matchStudentsWithCourse(self, course):
        students = self.database.getStudents()
        result = []
        for student in students:
            if course in student["courses"]:
                result.append(student["name"])
        return result
    

    