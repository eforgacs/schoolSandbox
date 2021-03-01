# procedure P (A,B : real)
#   X : real
#       procedure Q (B,C : real)
#       Y : real
#       ...

#       procedure R (A,C : real)
#       Z : real
#       ... **
# ...

def P(A, B):
    X = 0

    def Q(B, C):
        Y = 1

    def R(A, C):
        Z = 2
        
