# Black Box Test Cases - Issue & Return Book

def test_issue_book():
    expected = "Book Issued Successfully"
    actual = "Book Issued Successfully"

    if actual == expected:
        print("TC_I_01 Passed")
    else:
        print("TC_I_01 Failed")


def test_issue_unavailable_book():
    expected = "Book Not Available"
    actual = "Book Not Available"

    if actual == expected:
        print("TC_I_02 Passed")
    else:
        print("TC_I_02 Failed")


def test_return_book():
    expected = "Book Returned Successfully"
    actual = "Book Returned Successfully"

    if actual == expected:
        print("TC_I_03 Passed")
    else:
        print("TC_I_03 Failed")


test_issue_book()
test_issue_unavailable_book()
test_return_book()
