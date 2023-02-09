import math
# imports the fraction that will be simplified
print("Hello,Which 2 numbers would you like to be simplified")
numerator = int(input("numerator: "))
denominator = int(input("denominator: "))
print("numerator/denominator: ")
result=(numerator/denominator)
gcd= (math.gcd(numerator,denominator))
numerator_simplified=int(numerator/gcd)
denominator_simplified=int(denominator/gcd)
print(str(numerator_simplified)+"/"+str(denominator_simplified))
print(result)