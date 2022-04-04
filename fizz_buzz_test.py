from fizz_buzz import *

class TestFizzBuzz:
  
  def test_hello_world_reuturned(self):
    fb = FizzBuzz()
    assert fb.fizzbuzz() == 'hello world'
