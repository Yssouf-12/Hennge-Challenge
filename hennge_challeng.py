"""
Variables:
An integer N (1 ≤ N ≤ 100): the number of test cases to process.

Each test case consists of two lines:
Line 1 of the case: an integer X (0 < X ​​≤ 100) indicating how many numbers should follow.

Line 2 of the case: a space-separated list of integers, expected to contain X integers (but sometimes it can be more or less).

i → the current index in the list of lines,

lines → the list of all input lines,

n → the number of cases remaining to process,

results → the accumulated list of results (sum or -1).

To run the python3/ python script hennge_challenge.py < test_input_file.txt
"""


import sys

def treat_case(i, lignes, n, résultats):
    
    # When all cases have been processed (n == 0), the calculated results are returned.
    if n == 0:
        return résultats
    
    # We make sure that each case has 2 lines (line i for X, line i+1 for values). If not, we add -1 to the list and move on to the next one.
    if i + 1 >= len(lignes):
        return treat_case(i + 2, lignes, n - 1, résultats + [-1])

    # Normal treatment of a case
    try:
        x = int(lignes[i])
        valeurs = list(map(int, lignes[i + 1].split()))
        if len(valeurs) != x:
          return treat_case(i + 2, lignes, n - 1, résultats + [-1])
        else:
            def power4_negatives(l):
                if not l:
                    return 0
                tête, *reste = l
                if tête < 0:
                    return (tête ** 4) + power4_negatives(reste)
                else:
                    return power4_negatives(reste)
            somme = power4_negatives(valeurs)
            return treat_case(i + 2, lignes, n - 1, résultats + [somme])
    except:
        return treat_case(i + 2, lignes, n - 1, résultats + [-1])

def main():
    lignes = sys.stdin.read().splitlines()
    if not lignes:
        return
    try:
        n = int(lignes[0])
    except:
        return
    résultats = treat_case(1, lignes, n, [])
    for r in résultats:
        print(r)

if __name__ == "__main__":
    main()
