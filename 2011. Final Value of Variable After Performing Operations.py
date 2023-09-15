class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        
        x = 0

        for exp in operations:
            if exp == "++X" or exp == "X++":
                x += 1
            else:
                x -= 1


        return x
