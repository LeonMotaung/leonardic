def satisfies_conditions(a_i, a_j, a_k):
    """
    Check if the triple (a_i, a_j, a_k) satisfies:
    1. a_i ≡ a_j (mod |a_k|)
    2. a_j ≡ a_k (mod |a_i|)
    """
    if a_i == 0 or a_k == 0:
        return False

    cond1 = (a_i - a_j) % abs(a_k) == 0
    cond2 = (a_j - a_k) % abs(a_i) == 0

    return cond1 and cond2

def test_positive_triples(max_value=10):
    print("=== Leonardic Triple Checker: Positive Integers Only ===\n")
    total_tests = 0
    pass_count = 0

    for a_j in range(1, max_value + 1):
        for a_k in range(1, max_value + 1):
            for a_i in range(1, max_value + 1):
                if len({a_i, a_j, a_k}) < 3:
                    continue  # Skip non-distinct triples

                total_tests += 1
                result = satisfies_conditions(a_i, a_j, a_k)
                status = "PASS ✅" if result else "FAIL ❌"

                print(f"Test ({a_i}, {a_j}, {a_k}) → {status}")
                if result:
                    pass_count += 1

    print(f"\nTotal tests: {total_tests}")
    print(f"Passed: {pass_count}")
    print(f"Failed: {total_tests - pass_count}")

# Run with default max_value
test_positive_triples(max_value=5)
