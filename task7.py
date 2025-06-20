import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_rolls):
    outcomes = {i: 0 for i in range(2, 13)}

    for _ in range(num_rolls):
        roll = random.randint(1, 6) + random.randint(1, 6)
        outcomes[roll] += 1

    for key in outcomes:
        outcomes[key] /= num_rolls

    return outcomes


num_rolls = 100000
probabilities = simulate_dice_rolls(num_rolls)

print(f"Емпіричні ймовірності після {num_rolls} кидків:")
for sum_val, prob in sorted(probabilities.items()):
    print(f"Сума {sum_val}: {prob:.4f}")

print("\nТеоретичні ймовірності для порівняння:")
# Теоретичні ймовірності (1/36 * кількість комбінацій)
theoretical_probabilities = {
    2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36,
    7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
}
for sum_val, prob in sorted(theoretical_probabilities.items()):
    print(f"Сума {sum_val}: {prob:.4f}")

