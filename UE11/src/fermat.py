"""
__author__ = "Paul Waldecker"
__email__ = "0157@htl.rennweg.at"
__version__ = "0.1"
__copyright__ = "Copyright 2024"
__license__ = "GPL"
__status__ = "In Progress"
"""

def fermat_test(p):
    results = {}
    for a in range(1, p):
        result = pow(a, p-1, p)
        if result in results:
            results[result] += 1
        else:
            results[result] = 1
    return results

def analyze_results(results):
    total_tests = sum(results.values())
    percent_one = (results.get(1, 0) / total_tests) * 100
    unique_results = len(results)
    return percent_one, unique_results, results

primes = [2, 3, 5, 7, 11, 997]
non_primes = [9, 15, 21, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 6601, 89112]

print("Primzahlen:")
for p in primes:
    results = fermat_test(p)
    percent_one, unique_results, result_counts = analyze_results(results)
    print(f"{p} -> {percent_one:.0f} % -> res[1]={results.get(1, 0)}, len(res)={unique_results} - {list(result_counts.items())}")

print("\nNicht-Primzahlen:")
for p in non_primes:
    results = fermat_test(p)
    percent_one, unique_results, result_counts = analyze_results(results)
    print(f"{p} -> {percent_one:.0f} % -> res[1]={results.get(1, 0)}, len(res)={unique_results} - {list(result_counts.items())}")

