#      Consider the following grammar, where <S> is the start symbol:
#      <S> ::= <V> ‘=’ <E>
#      | <S> ‘;’ <S>
#      | ‘if’ <B> ‘then’ <S>
#      | ‘if’ <B> ‘then’ <S> ‘else’ <S>
#      <B> ::= <E> ‘===’ <E>
#      <V> ::= ‘x’ | ‘y’ | ‘z’
#      <E> ::= <V> | ‘0’ | ‘1’ | ‘2’ | ‘3’
#      Consider the input “if x === 1 then if y === z then z = 2 else z = 3.”


x = 0
y = 0
z = 0

# Parse Tree 1:
if x == 1:
    # then
    if y == z:
        # then
        z = 2
    else:
        z = 3

# Parse Tree 2:
if x == 1:
    # then
    if y == z:
        # then
        z = 2
else:
    z = 3
