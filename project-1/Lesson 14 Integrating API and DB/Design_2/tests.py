import unittest
from unittest.mock import Mock
from useCase import studentsUseCase

class Testing(unittest.TestCase):
    def test_matchStudentsWithCourse(self):
        # First we create a database mock, and we'll set expectations on the database methods
        databaseMock = Mock()
        databaseMock.getStudents = Mock(return_value= [
            {
                "name": "Federico",
                "courses": ["DataScience", "FrontEnd"]
            },
            {
                "name": "Marco",
                "courses": ["Backend", "Mobile"]
            }
        ])
        # Then we create the useCase object, and try to execute the function with some input
        useCase = studentsUseCase(database=databaseMock)
        result = useCase.matchStudentsWithCourse("Backend")

        # Last step is the assertion, which we compare the result from the function with the expected result
        self.assertEqual(result, ["Marco"])

if __name__ == '__main__':
    unittest.main()