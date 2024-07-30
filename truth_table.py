def display_truth_table():
    header = ["P", "Q", "(P AND Q)", "(P OR Q)", "(NOT P)", "(NOT Q)"]
    print(f"{header[0]:<8}{header[1]:<8}{header[2]:<12}{header[3]:<12}{header[4]:<10}{header[5]:<10}")

    comb_list = [(False, False), (False, True), (True, False), (True, True)]

    for p, q in comb_list:
        a = 'T' if p else 'F'
        b = 'T' if q else 'F'
        and_comb = 'T' if p and q else 'F'
        or_comb = 'T' if p or q else 'F'
        not_p = 'T' if not p else 'F'
        not_q = 'T' if not q else 'F'
        print(f"{a:<8}{b:<8}{and_comb:<12}{or_comb:<12}{not_p:<10}{not_q:<10}")


# Generate and display the truth table
display_truth_table()
