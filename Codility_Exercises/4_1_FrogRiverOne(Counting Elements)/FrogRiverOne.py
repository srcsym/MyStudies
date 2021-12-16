def solution(X, A):
    if(len(A) == 1 and A[0] == 1):
        return 0
    if(len(A) == 1 and A[0] != 1):
        return -1
    if X in A:
        y=A.index(X)
        return y
    else:
        return -1

print(solution(10,[1,3,1,4,2,3,5,4]))