names = ['Aarav','Priya','Dev','Meera','Kabir']
scores = [90,75,88,62,95]

n = len(scores)

print('Score Tracker (n =', n, 'players)')

for i in range(n):
    print(i + 1, '.', names[i], '.', scores[i], sep='')

print()

steps = 1 

print('Score at index 0:', scores[0], '| steps =' ,steps, '| Theta(1) - tight bound')
print()

target = 'Aarav'
steps = 0

for name  in namefffffffffffffffs:
    steps += 1
    if name == target:
        break

print('Search for', target, '| steps =', steps, '| Omega(1) - best case')

target = 'Dev'
steps = 0


for name in names:
    steps += 1
    if name == target:
        break

print("Search for", target, "| steps =", steps, "| Average Case O(n)")
print()

# ── PART 5: Worst Case O(n) ──────────────────────────────────────────────────

# Search for the last player.

target = "Kabir"
steps = 0

for name in names:
    steps += 1
    if name == target:
        break

print("Search for", target,
      "| steps =", steps,
      "| Worst Case O(n)")

print()


# ── PART 6: O(n²) Pair Search ────────────────────────────────────────────────

# Compare every unique pair of players.

steps = 0
target_sum = 150

print("Pairs with total score =", target_sum, ":")

for i in range(n):
    for j in range(i + 1, n):
        steps += 1
        if scores[i] + scores[j] == target_sum:
            print(" ", names[i], "+", names[j], "=", scores[i] + scores[j])

print("Total comparisons :", steps,
      "| O(n^2)")

print()


# ── PART 7: Asymptotic Summary ───────────────────────────────────────────────

# Keep only the dominant term for large n.

print("=== Asymptotic Summary ===")

print("Theta(1) : Direct index access")
print("Omega(1) : Best case search")
print("O(n)     : Average case search")
print("O(n)     : Worst case search")
print("O(n^2)   : Pair comparison")

print()
print("Total pair comparisons =", n * (n - 1) // 2)
print("Drop constants. Keep the dominant term.")
