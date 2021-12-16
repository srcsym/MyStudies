def solution(A, K):
    new_array=[0]*len(A)

    mode=K%len(A)
    print(new_array)

    for i in range(0,len(A)):
        new_array[(i+3)%len(A)]=A[i]

    return new_array
