# Put you pointer here: |

import pytest
pytest.main([__file__, '-v', '-p', 'no:warnings'])


def roberto(maximum_of_pizzas, orders):
    total_time = 0
    total_pizzas = 0

    orders = sorted(orders, reverse=True)

    for time, pizzas in orders:
        if total_pizzas + pizzas <= maximum_of_pizzas:
            total_time += time
            total_pizzas += pizzas
    
    return total_time
   
def test_1_pizza_and_only_one_order():
    amount_of_pizza = 1
    orders = [(10, 1)] 
    expected_time = 10
    assert roberto(amount_of_pizza, orders) == expected_time

def test_1_pizza_and_2_orders():
    amount_of_pizza = 1
    orders = [(5, 1), (42, 1)] 
    expected_time = 42
    assert roberto(amount_of_pizza, orders) == expected_time

def test_1_pizza_and_2_orders_change_position():
    amount_of_pizza = 1
    orders = [(42, 1), (5, 1)] 
    expected_time = 42
    assert roberto(amount_of_pizza, orders) == expected_time

def test_1_pizza_and_2_orders_with_different_number_of_pizzas():
    amount_of_pizza = 1
    orders = [(42, 2), (5, 1)] 
    expected_time = 5
    assert roberto(amount_of_pizza, orders) == expected_time

def test_2_pizza_and_2_orders_with_different_number_of_pizzas():
    amount_of_pizza = 2
    orders = [(5, 1), (45, 1)] 
    expected_time = 50
    assert roberto(amount_of_pizza, orders) == expected_time

def test_2_pizza_and_4_orders_with_different_number_of_pizzas():
    amount_of_pizza = 2
    orders = [(5, 1), (45, 8), (15, 1), (10, 1)] 
    expected_time = 25
    assert roberto(amount_of_pizza, orders) == expected_time

def test_1_problem_case_test():
    amount_of_pizza = 10
    orders = [(15, 5), (23, 4), (21, 2), (16, 4),(19, 5),(18, 2)] 
    expected_time = 62
    assert roberto(amount_of_pizza, orders) == expected_time

