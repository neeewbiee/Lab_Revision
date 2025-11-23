import lab2

def test_under_weight():
    input_arr = -1
    height = 1.57
    weight = 29
    result = lab2.calculate_bmi(height,weight)
    assert(result == input_arr)
    
def test_under_weight():
    input_arr = 0
    height = 1.75
    weight = 68
    result = lab2.calculate_bmi(height,weight)
    assert(result == input_arr)
    
def test_under_weight():
    input_arr = 1
    height = 1.57
    weight = 150
    result = lab2.calculate_bmi(height,weight)
    assert(result == input_arr)