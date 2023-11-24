# Cryptarithmetic problem: SEND + MORE = MONEY

# Iterating through all possible digit combinations for S, E, N, D, M, O, R, Y
for S in range(1, 10):
    for E in range(0, 10):
        for N in range(0, 10):
            for D in range(0, 10):
                for M in range(1, 10):
                    for O in range(0, 10):
                        for R in range(0, 10):
                            for Y in range(0, 10):
                                if len(set([S, E, N, D, M, O, R, Y])) == 8:  # Check for unique digits
                                    send = S * 1000 + E * 100 + N * 10 + D
                                    more = M * 1000 + O * 100 + R * 10 + E
                                    money = M * 10000 + O * 1000 + N * 100 + E * 10 + Y
                                    if send + more == money:
                                        print(f"S = {S}, E = {E}, N = {N}, D = {D}, M = {M}, O = {O}, R = {R}, Y = {Y}")
                                        print(f"SEND = {send}, MORE = {more}, MONEY = {money}")
                                        print("Cryptarithmetic problem solved!")
                                        break
