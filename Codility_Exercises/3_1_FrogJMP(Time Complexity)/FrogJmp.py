def solution(X, Y, D):

    if (Y-X)%D==0:
        return int((Y-X)/D)
    else:
        return int(((Y-X)+D)/D)
