class Solution(object):
    def reverse(self, x):
        tmp = str(x)[::-1]

        if x != 0:
            tmp = str(x)[::-1].strip('0')

        if tmp[-1] == "-":
            tmp = "-" + tmp[0:-1]

        if abs(int(tmp)) > ((2 ** 31) - 1):
            return 0
        return(tmp)