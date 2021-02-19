def distinct_chars_pattern_matcher(t, p):
    n = len(t)
    m = len(p)
    s = 0
    while s <= n - m:
        i = 1
        while i <= m and p[i] == t[s + i]:
            i += 1
        if i == m + 1:
            print(f"Pattern occurs with shift {s}")
        s = max(s + 1, s + i - 1)
