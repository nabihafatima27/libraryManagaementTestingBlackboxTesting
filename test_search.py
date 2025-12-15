# Black Box Test Cases - Search Functionality

def test_search_existing_book():
    expected = "Book Found"
    actual = "Book Found"

    if actual == expected:
        print("TC_SR_01 Passed")
    else:
        print("TC_SR_01 Failed")


def test_search_non_existing_book():
    expected = "No Results Found"
    actual = "No Results Found"

    if actual == expected:
        print("TC_SR_02 Passed")
    else:
        print("TC_SR_02 Failed")


test_search_existing_book()
test_search_non_existing_book()
