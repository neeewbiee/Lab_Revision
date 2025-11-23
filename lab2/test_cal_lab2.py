import lab2

def test_min_max():
    input_arr = [2,3,4,5]
    test_arr = [2,5]
    result = lab2.find_min_max(input_arr)
    assert(result == test_arr)
    
def test_average():
    input_arr = [1,2,3,4,5]
    test = 3
    result = lab2.calc_average(input_arr)
    assert(result == test)
    
def test_median():
    input_arr = [1,2,3,4,5]
    test = 3
    result = lab2.calc_median_temperature(input_arr)
    assert(result == test)
    
