def test_manhattan_distance():
    # Test case 1: Blank tile at index 0
    state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    assert manhattan_distance(state) == 4

    # Test case 2: Blank tile at index 4
    state = [1, 2, 3, 0, 4, 5, 6, 7, 8]
    assert manhattan_distance(state) == 2

    # Test case 3: Blank tile at index 8
    state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    assert manhattan_distance(state) == 4

def test_get_blank_index():
    # Test case 1: Blank tile at index 0
    state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    assert get_blank_index(state) == 0

    # Test case 2: Blank tile at index 4
    state = [1, 2, 3, 0, 4, 5, 6, 7, 8]
    assert get_blank_index(state) == 3

    # Test case 3: Blank tile at index 8
    state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    assert get_blank_index(state) == 8

# Run the test functions
test_manhattan_distance()
test_get_blank_index()