from fizz_buzz import *

class TestFizzBuzz:
  def test_returns_fizz_if_divisible_by_three(self):
    fb = FizzBuzz()
    assert fb.fizzbuzz(3) == 'fizz'
  
