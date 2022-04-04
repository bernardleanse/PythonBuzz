class FizzBuzz:
  def fizzbuzz(self, number):
    if number % 3 == 0 and number % 5 == 0:
      return "fizzbuzz" 
  
    return "fizz" if number % 3 == 0 else "buzz"

  
