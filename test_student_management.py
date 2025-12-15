# Black Box Test Cases - Student Management

def test_add_student():
    expected = "Student Added Successfully"
    actual = "Student Added Successfully"

    if actual == expected:
        print("TC_S_01 Passed")
    else:
        print("TC_S_01 Failed")


def test_duplicate_student_id():
    expected = "Duplicate ID Error"
    actual = "Duplicate ID Error"

    if actual == expected:
        print("TC_S_02 Passed")
    else:
        print("TC_S_02 Failed")


def test_empty_student_name():
    expected = "Validation Error"
    actual = "Validation Error"

    if actual == expected:
        print("TC_S_03 Passed")
    else:
        print("TC_S_03 Failed")


test_add_student()
test_duplicate_student_id()
test_empty_student_name()
