'''
A simple program that converts numeric values to their
corresponding roman numerals and vise versa

Arthur @Julius alias CEO
'''
class CEO:
    def __init__(self, number):
        self.number = number
        
    def program(self):
        warehouse= [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        roman = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        i = 12 
        roman_numeral = ''
        while self.number != 0:
            if warehouse[i] <= self.number:
                roman_numeral += roman[i]
                self.number = self.number - warehouse[i]
            else:
                i -= 1
        return roman_numeral
    
    
converter = CEO(5)
print(converter.program())
