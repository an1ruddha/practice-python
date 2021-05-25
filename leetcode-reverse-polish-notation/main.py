class Solution:
    def evalRPN(self, tokens: list) -> int:
        list_stack = []
        for token in tokens:
            if token == "+":
                val2 = list_stack.pop()
                val1 = list_stack.pop()
                list_stack.append(val1 + val2)
            elif token == "-":
                val2 = list_stack.pop()
                val1 = list_stack.pop()
                list_stack.append(val1 - val2)
            elif token == "*":
                val2 = list_stack.pop()
                val1 = list_stack.pop()
                list_stack.append(val1 * val2)
            elif token == "/":
                val2 = list_stack.pop()
                val1 = list_stack.pop()
                list_stack.append(int(val1 / val2))                
            else:
                list_stack.append(int(token))
        return list_stack[0]
def main():
    obj = Solution()
    list_tokens = [["2","1","+","3","*"],
                  ["10","6","9","3","+","-11","*","/","*","17","+","5","+"],
                  ["4","13","5","/","+"]]
    
    for tokens in list_tokens:
        print(obj.evalRPN(tokens), " = ", tokens)
if __name__ == "__main__":
    main()

