import price_info

def test_total_cost():
    expected_result = 46.75
    
    result = price_info.total_cost_shopping()
    
    assert(result == expected_result)
    
def test_total_cost():
    fruit = "apple"
    quantity = 20
    expected_result = 24.0
    
    result = price_info.cost_of_fruits(fruit,quantity)
    
    assert(result == expected_result)