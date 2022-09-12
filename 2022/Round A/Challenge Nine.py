class Solution:
    def findSmllestOne(self,N):
        given_sum = 0

        for n in N:
            given_sum+=int(n)

        new = 0
        for i in range(0,10):
            curr = i+given_sum
            if curr%9==0:
                new=i
                break

        for i in range(len(N)):
            if i == 0 and new == 0:
                continue
            if new < int(N[i]):
                return N[:i] + str(new) + N[i:]


        return N + str(new)









t = int(input())
for i in range(t):
    N = input()
    res = Solution().findSmllestOne(N)
    print(f"Case #{i+1}: {res}")



