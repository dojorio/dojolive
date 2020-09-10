# Please, stop your cursor here >>>

## Challenge
# Say you have an array for which the ith element is the price of a given stock on day i. If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
# Note: You cannot sell a stock before you buy one
# Example
# Input: [7, 1, 5, 3, 6, 4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5. Not 7-1 = 6, as the selling price needs to be larger than buying price.

require 'test/unit'

def stock(prices)
  minimum = prices.first
  maximum = peak = 0
  for price in prices
    minimum = maximum = price if price < minimum
    if price > maximum
      maximum = price
      margin = maximum - minimum
      peak = margin if margin > peak
    end  
  end
  return peak
end

class DojoTest < Test::Unit::TestCase
  def test_another_longer_situation
    assert_equal 399, stock([2, 10, 7, 1, 5, 3, 6, 4, 11, 3, 400, 5, 8, 2, 3, 4, 5, 6, 2, 3, 4])
  end

  def test_situation_that_wont_break
    assert_equal 10, stock([2, 10, 7, 1, 5, 3, 6, 4, 11])
  end

  def test_situation_that_will_break
    assert_equal 8, stock([2, 10, 7, 1, 5, 3, 6, 4])
  end

  def test_problem_example
    assert_equal 5, stock([7, 1, 5, 3, 6, 4])
  end

  def test_4_1_3_return_2
    assert_equal 2, stock([4, 1, 3])
  end

  def test_1_4_3_return_3
    assert_equal 3, stock([1, 4, 3])
  end

  def test_1_4
    assert_equal 3, stock([1, 4])
  end

  def test_1_3
    assert_equal 2, stock([1, 3])
  end

  def test_1_2
    assert_equal 1, stock([1, 2])
  end
end
