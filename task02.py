number = input('Enter four digit number: ')

digits = [int(digit) for digit in number]

result = 1
for digit in digits:
    result *= digit

print('Digits are: ', digits)
print('Product is: ', result)






