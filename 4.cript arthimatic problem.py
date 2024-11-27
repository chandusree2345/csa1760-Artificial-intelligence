import itertools

def solve_cryptarithmetic():
    for perm in itertools.permutations(range(10), 8):
        s, e, n, d, m, o, r, y = perm
        if s and m and (s*1000 + e*100 + n*10 + d) + (m*1000 + o*100 + r*10 + e) == m*10000 + o*1000 + n*100 + e*10 + y:
            print(f"SEND={s}{e}{n}{d}, MORE={m}{o}{r}{e}, MONEY={m}{o}{n}{e}{y}")
            break

solve_cryptarithmetic()
