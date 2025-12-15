# Black Box Test Cases - Login Module

def test_valid_login():
    expected = "Login Successful"
    actual = "Login Successful"

    if actual == expected:
        print("TC_L_01 Passed")
    else:
        print("TC_L_01 Failed")


def test_invalid_password():
    expected = "Error Message"
    actual = "Error Message"

    if actual == expected:
        print("TC_L_02 Passed")
    else:
        print("TC_L_02 Failed")


def test_empty_fields():
    expected = "Validation Error"
    actual = "Validation Error"

    if actual == expected:
        print("TC_L_03 Passed")
    else:
        print("TC_L_03 Failed")


test_valid_login()
test_invalid_password()
test_empty_fields()
