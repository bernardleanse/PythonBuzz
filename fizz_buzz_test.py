from fizz_buzz import *

class TestFizzBuzz:
  def test_returns_fizz_if_divisible_by_three(self):
    fb = FizzBuzz()
    assert fb.fizzbuzz(3) == 'fizz'

  def test_returns_buzz_if_divisble_by_five(self):
    fb = FizzBuzz()
    assert fb.fizzbuzz(5) == 'buzz'
  
