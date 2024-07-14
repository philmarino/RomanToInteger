
def romanToInt(s):
    sum = 0
    index = 0

    while index < len(s):
        match s[index]:
            case "I":
                if index + 1 < len(s) and s[index + 1] == "V":
                    sum += 4
                    index += 1    
                elif index + 1 < len(s) and s[index + 1] == "X":
                    sum += 9
                    index += 1    
                else:
                    sum += 1
            case "V":
                sum += 5
            case "X":
                if index + 1 < len(s) and s[index + 1] == "L":
                    sum += 40
                    index += 1
                elif index + 1 < len(s) and s[index + 1] == "C":
                    sum += 90
                    index += 1
                else:
                    sum += 10
            case "L":
                sum += 50
            case "C":
                if index + 1 < len(s) and s[index + 1] == "D":
                    sum += 400
                    index += 1
                elif index + 1 < len(s) and s[index + 1] == "M":
                    sum += 900
                    index += 1
                else:
                    sum += 100
            case "D":
                sum += 500
            case "M":
                sum += 1000
        index += 1

    return sum

#Example 1:
#Input: 
s = "III"
print(romanToInt(s))
#Output: 3
#Explanation: III = 3.

#Example 2:
#Input: 
s = "LVIII"
print(romanToInt(s))
#Output: 58
#Explanation: L = 50, V= 5, III = 3.

#Example 3:
#Input: 
s = "MCMXCIV"
print(romanToInt(s))
#Output: 1994
#Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 