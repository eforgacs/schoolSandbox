# var i=0, j=1;
# mystery(i, i+1, i*3,j)
# procedure mystery (a1, a2, a3, a4)
#   for count from 1 to 3 do // 1 to 3 inclusive
#       a1 = a2 + a3 + a4;
#       a4 = a4 + 1;
#   end for;
# end procedure;

i, j = 0, 1


def mystery(a1, a2, a3, a4):
    for iterator in range(1, 4):  # 1 to 3 inclusive
        a1 = a2 + a3 + a4
        a4 = a4 + 1


mystery(i, i + 1, i * 3, j)
# call by name
# before iteration 1: a1 = 0, a2 = 0 + 1, a3 = 0 * 3, a4 = 1
# after iteration 1:
# a1 = (0 + 1) + (0 * 3) + 1 = 1 + 0 + 1 = 2
# a4 = 1 + 1 = 2

# after iteration 2: a
# run 2: a1 =
