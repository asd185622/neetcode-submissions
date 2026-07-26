class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        indexStack = []
        ans = [0] * len(temperatures)

        for index,temp in enumerate(temperatures):
            if not stack or temp < stack[-1]:
                stack.append(temp)
                indexStack.append(index)
            else:
                # print("temp:",temp)
                # print("stack:",stack)
                while stack and temp > stack[-1]:
                    # i = temperatures.index(stack[-1])
                    i = indexStack.pop()
                    ans[i] = index - i
                    # print("i:",i)
                    # print(f"ans[{i}]:",ans[i])
                    stack.pop()
                stack.append(temp)
                indexStack.append(index)
        return ans
