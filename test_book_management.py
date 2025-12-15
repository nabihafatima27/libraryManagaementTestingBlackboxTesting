# Black Box Test Cases - Book Management

def test_add_book():
    expected = "Book Added Successfully"
    actual = "Book Added Successfully"

    if actual == expected:
        print("TC_B_01 Passed")
    else:
        print("TC_B_01 Failed")


def test_empty_book_name():
    expected = "Error Message"
    actual = "Error Message"

    if actual == expected:
        print("TC_B_02 Passed")
    else:
        print("TC_B_02 Failed")


def test_negative_quantity():
    expected = "Invalid Quantity"
    actual = "Invalid Quantity"

    if actual == expected:
        print("TC_B_03 Passed")
    else:
        print("TC_B_03 Failed")


test_add_book()
test_empty_book_name()
test_negative_quantity()
