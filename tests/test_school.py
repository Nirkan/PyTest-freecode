import pytest

from source.school import Classroom, Teacher, Student, TooManyStudents

# Fixture for creating a Classroom instance
@pytest.fixture
def harry_potter_classroom():
    teacher = Teacher("Professor Snape")
    students = [Student(f"Student_{i}") for i in range(8)]  # Creating 8 students initially
    course_title = "Potions"

    return Classroom(teacher, students, course_title)


# Test add_student method with TooManyStudents exception
def test_add_student(harry_potter_classroom):
    # Adding 8 students, the classroom limit is 10
    for i in range(8, 10):
        new_student = Student(f"Student_{i}")
        harry_potter_classroom.add_student(new_student)
    
    # Attempting to add one more student should raise TooManyStudents exception
    with pytest.raises(TooManyStudents):
        harry_potter_classroom.add_student(Student("Extra_Student"))


# Test remove_student method
def test_remove_student(harry_potter_classroom):
    # Removing an existing student from the classroom
    student_to_remove = harry_potter_classroom.students[0].name
    harry_potter_classroom.remove_student(student_to_remove)
    
    # Check that the student is removed
    assert all(student.name != student_to_remove for student in harry_potter_classroom.students)


# Test change_teacher method
def test_change_teacher(harry_potter_classroom):
    new_teacher = Teacher("Professor McGonagall")
    harry_potter_classroom.change_teacher(new_teacher)
    
    assert harry_potter_classroom.teacher == new_teacher
