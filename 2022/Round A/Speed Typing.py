class Solution:
    def checkSubSequence(self, I,P):
        l=r=0

        while l < len(I) and r < len(P):
            if I[l] == P[r]:
                l+=1
                r+=1
            else:
                r+=1

        if l==len(I):
            return True
        else:
            return False

    def lettersToDelete(self, I, P):
        if self.checkSubSequence(I,P) == False:
            return "IMPOSSIBLE"
        else:
            return len(P)-len(I)


t = int(input())
for i in range(t):
    I = input()
    P = input()
    res = Solution().lettersToDelete(I, P)
    print(f"Case #{i + 1}: {res}")

