# Requirements

Run the following to install all the dependencies if not installed
```
pip install fastapi "uvicorn[standard]"
pip install pymongo
pip install pydantic
pip install dotenv
```


# Running

First you have to modify the ".env" file with your database username and password, then run the database_init.ipynb to prepare the database, this script cleans it first, then insers all documents specified, then you can start the server by running: python main.py



# Testing (Design 2)

As we are using layered Architecture in Desgin_2, I provided you a sample test case of how you test your layers
independantly, all unit testing techniques depend on the concept of "Mocks", lets give the example we have here:

Now we have 3 layers: Api -> useCase -> database

Suppose I want to only test the useCase functionality, and as useCase is using the databse layer under the hood, so we
have to "mock" the database layer by creating an alternative object to be used by the use-case instead of the real object which is connected to the database. Then we control the behaviour of this mock object methods.

Example: we want to create a database mock, and control the behaviour of the method getStudents()
1. Create an alternative object of the database: database = Mock()
2. set the expectation of the getStudents return value: database.getStudents = Mock(return_value= [returnValue])
In this way whenever database.getStudents() is called from inside the useCase, regardless of the input this "returnValue" will be returned

Why we do this "Mocking"? As we're testing the useCase layer, we just want to test the functionaliy of the useCase itself and not the functionality of other layers, suppose we call useCase.matchStudentsWithCourse() and we get wrong results, if we don't use mocks we wouldn't know where the bug is, as it could be in the useCase layer or in the database layer, but if we control the behaviour of the Database layer using mocks, now we know for sure that the problem is in the logic of the useCase.

Note: I did a small update to the useCase object to set the database attribute from the constructor inputs, this facilitates a lot the mocking process, you'll figure it out when you look at the test.