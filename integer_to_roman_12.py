class Solution(object):
    def intToRoman(self, num):
        numerals = [('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90), ('L', 50), ('XL', 40), ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)]

        roman = ""
        
        for numeral in numerals:
            while num >= numeral[1]:
                roman += numeral[0]
                num -= numeral[1]
            
        return roman
        
