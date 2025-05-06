class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join(str(i) for i in digits))
        
        # Step 2: Add 1 to the number
        num += 1
        
        # Step 3: Convert the result back to a list of digits
        return [int(digit) for digit in str(num)]


        