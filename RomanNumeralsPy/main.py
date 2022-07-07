'''
A simple program that converts numeric values to their
corresponding roman numerals and vise versa

Arthur @Julius alias CEO
'''
class Convertor:
    def __init__(self, number):
        self.number = number
        
    def program(self):
        numbers_ = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        roman = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        i = 12 
        roman_numeral = ''
        while self.number != 0:
            if numbers_[i] <= self.number:
                roman_numeral += roman[i]
                self.number = self.number - numbers_[i]
            else:
                i -= 1
        return roman_numeral
    
    
convert = Convertor(5)
print(convert.program())
