class Solution:
    def isPalindrome(x: int) -> bool:
        flag = False
        # Negative values are not palindromes.
        if(x < 0):
            return flag
        # set one digit's array
        numbs = [int(n) for n in list(str(x))]
        print(numbs)
        # calculate number of digits
        digitNumber = len(str(x))
        if(digitNumber == 1):
          flag = True
          return flag
        print(digitNumber,"digitNumber")
        numOfLoop = digitNumber // 2
        print(numOfLoop)
        for i in range(numOfLoop):
          print(numbs[i])
          if(numbs[i] == numbs[digitNumber - 1 - i]):
            flag = True
          else: 
            flag = False 
            return flag
        return flag
    print(isPalindrome(1000021))