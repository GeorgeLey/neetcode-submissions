class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """

        stack

        loop through asteroids
            while stack and stack[-1] > 0 and asteroid < 0:
                diff = stack[-1] + asteroid
                if diff > 0:
                    asteroid = 0
                elif diff < 0:
                    stack.pop()
                else:
                    asteroid = 0
                    stack.pop()
            add asteroid to the stack
                
        
        return the stack
        """

        stack = []

        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                diff = stack[-1] + asteroid
                if diff > 0:
                    asteroid = 0
                elif diff < 0:
                    stack.pop()
                else:
                    asteroid = 0
                    stack.pop()
            if asteroid != 0:
                stack.append(asteroid)
        
        return stack



        