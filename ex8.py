import re
from itertools import product

def evaluate(formula, assignment):
    replaced_formula = formula
    for var, val in assignment.items():
        # Replace the variable as a whole word using regex
        replaced_formula = re.sub(rf'\b{var}\b', str(val), replaced_formula)
    try:
        return eval(replaced_formula)
    except Exception as e:
        print(f"\n💥 Error evaluating: {replaced_formula}")
        print(f"🛑 Reason: {e}")
        return False

def get_variables(formula):
    # Only get standalone variables that are fully uppercase
    return sorted(set(re.findall(r'\b[A-Z]+\b', formula)))

def model_checking(formula):
    variables = get_variables(formula)
    combinations = list(product([False, True], repeat=len(variables)))

    true_count = 0
    for values in combinations:
        assignment = dict(zip(variables, values))
        result = evaluate(formula, assignment)
        if result:
            print(f"✔️ Satisfying assignment: {assignment}")
            true_count += 1
        else:
            print(f"❌ Failed assignment: {assignment}")

    if true_count == len(combinations):
        print("\n□ Result: The formula is VALID (true in all models).")
    elif true_count > 0:
        print("\n□ Result: The formula is SATISFIABLE (true in some models).")
    else:
        print("\n🔴 Result: The formula is UNSATISFIABLE (false in all models).")

# === Example usage ===
if __name__ == "__main__":
    formula = "(A and B) or (not A and not B)"  # Example: Logical equivalence
    print(f"\n🔍 Checking formula: {formula}")
    model_checking(formula)

