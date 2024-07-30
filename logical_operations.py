def compute_operations():
    inputA = input("Enter A (True, False, 1 or 0): ")
    inputB = input("Enter B (True, False, 1 or 0): ")

    if inputA.lower() == 'true' or inputA == '1':
        A = True
    else:
        A = False

    if inputB.lower() == 'true' or inputB == '1':
        B = True
    else:
        B = False

    conjunction = A and B  # A ∧ B
    disjunction = A or B   # A ∨ B
    negation_A = not A     # ¬A
    negation_B = not B     # ¬B
    implication = not A or B  # A → B
    biconditional = A == B  # A ↔ B

    return {
        "A": A,
        "B": B,
        "conjunction (AND)": conjunction,
        "disjunction (OR)": disjunction,
        "negation_A (NOT)": negation_A,
        "negation_B (NOT)": negation_B,
        "implication (IF...THEN)": implication,
        "biconditional (IF AND ONLY IF)": biconditional
    }

results = compute_operations()
for operation, result in results.items():
    print(f"{operation}: {result}")

