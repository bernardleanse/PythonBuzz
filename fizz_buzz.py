class FizzBuzz:
  def fizzbuzz(self, number):
    result = ""
    if number % 3 == 0:
      result += "fizz" 
    if number % 5 == 0:
      result += "buzz"
    if len(result) == 0:
      return number
    return result

  
