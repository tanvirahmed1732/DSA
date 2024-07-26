import numpy
class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n=len(A)
        s = numpy.sum(A)
        ss=(n*(n+1))//2
        sqs = (n*(n+1)*((2*n)+1))//6
        sq = numpy.sum(numpy.square(A))
        a=ss-s
        b=sqs-sq 
        b=b//a
        x=(a+b)//2
        y=b-x
        ar=[y,x]
        return ar