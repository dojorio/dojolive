# Please, stop your cursor here >>>  
# Write the code here

require 'test/unit'

def bubble(unsorted)
  thisarray = unsorted.clone
  begin 
    changed = false
    for i in (0...unsorted.size-1)
      if thisarray[i] > thisarray[i+1]
        changed = true
        thisarray[i], thisarray[i+1] = thisarray[i+1], thisarray[i]
      end
    end
  end while changed

  return  thisarray
end

class DojoBubbleSortTest < Test::Unit::TestCase
  data "list of 1", [[1], [1]]
  data "list of 2", [[1, 2], [2, 1]]
  data "list of 2 already sorted", [[1,2], [1,2]]
  data "list of 3 elements", [[1, 2, 3], [1, 3, 2]]
  data "list of 4 elements", [[1, 2, 3, 4], [4, 1, 2, 3]]
  data "list of 4 elements", [[1, 2, 3, 4], [4, 3, 2, 1]]
  data "list of 5 elements", [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]]
  def test_bubble(data)
    expected, params = data
    assert_equal expected, bubble(params)
  end
end
