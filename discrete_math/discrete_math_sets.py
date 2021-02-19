A = {"a", "c", "e", "g"}
B = {"b", "c", "f", "g", "h"}
C = {"a", "b", "d"}
U = {"a", "b", "c", "d", "e", "f", "g", "h"}
empty_set = set()


def complement(a):
    # difference between a global universal set U and the given set a
    return U - a


a_complement = complement(A)
c_complement = complement(C)
union_of_a_and_c = A.union(C)
print(C.intersection(empty_set))
