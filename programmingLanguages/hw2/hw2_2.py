# procedure outer () is
# a : int = 7
# n : int = 2
# b : int = 1
#
#   procedure inner (int n) is
#   a : integer = 3
#       procedure innermost (int n) is
#       begin
#           if n == 1 then
#               print(b)
#           else
#               b := a + b
#               innermost(n-1)
#           end if;
#       end;
#   begin
#       innermost(a)
#   end;
#
# begin
#
#   for j from 1 to n do
#       inner(b);
#   end for
#
# end;

def outer():
    a = 7
    n = 2
    b = 1

    def inner(n: int):
        a = 3

        def innermost(n: int):
            # begin
            if n == 1:
                print(b)
            else:
                b = a + b
                innermost(n - 1)
            # end

        # begin
        innermost(a)
        # end

    for j in range(1, n):
        inner(b)


outer()
