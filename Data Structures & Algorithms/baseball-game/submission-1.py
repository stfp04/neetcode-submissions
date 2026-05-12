class Solution:

    def check_int(self, s):
        if s[0] in ('-', '+'):
            return s[1:].isdigit()
        return s.isdigit()

    def calPoints(self, operations: List[str]) -> int:
        ans = []
        for i in range(len(operations)):
            op = operations[i]
            if self.check_int(op):
                ans.append(int(op))
            elif op == "+":
                k = len(ans)
                tmp = ans[k - 1] + ans[k - 2]
                ans.append(tmp)
            elif op == "C":
                ans.pop()
            elif op == "D":
                k = len(ans)
                ans.append(ans[k - 1] * 2)
            else:
                print("Operation not recognized", op)
        print(ans)
        return sum(ans)