'''
A simple program that converts numeric values to their
corresponding roman numerals and vise versa

Arthur @Julius alias CEO
'''

class Convertor:
    def __init__(self, number):
        self.number = number
        
    def program(self):
        container_of_numbers = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        roman = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        i = 12
        
        #result is stored in variable: roman_numeral
        roman_numeral = ''
        while self.number != 0:
            if container_of_numbers[i] <= self.number:
                roman_numeral += roman[i]
                self.number = self.number - container_of_numbers[i]
            else:
                i -= 1
        return roman_numeral
    
    
convert = Convertor(5)
print(convert.program())

