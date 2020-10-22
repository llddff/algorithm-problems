class Solution:
    def VerifySquenceOfBST(self, sequence):
        if not sequence:
            return False
        root = sequence[-1]
        i = 0
        for node in sequence[:-1]:
            if node > root:
                break
            i += 1
        for node in sequence[i:-1]:
            if node < root:
                return False
        left, right = True, True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[:i])
        if i < len(sequence)-2:
            right = self.VerifySquenceOfBST(sequence[i:-1])
        return left and right

a=[1,2,3,4]
b=a[3:-1]
b