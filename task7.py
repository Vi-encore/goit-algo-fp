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
theoretical_probabilities = {
    2: 1 / 36,
    3: 2 / 36,
    4: 3 / 36,
    5: 4 / 36,
    6: 5 / 36,
    7: 6 / 36,
    8: 5 / 36,
    9: 4 / 36,
    10: 3 / 36,
    11: 2 / 36,
    12: 1 / 36,
}
for sum_val, prob in sorted(theoretical_probabilities.items()):
    print(f"Сума {sum_val}: {prob:.4f}")

# Візуалізація результатів
sums = list(probabilities.keys())
empirical_probs = list(probabilities.values())
theoretical_probs = [theoretical_probabilities[s] for s in sums]

plt.figure(figsize=(10, 6))

bar_width = 0.35
index = [s - 0.5 * bar_width for s in sums]  # Зміщення для стовпців

plt.bar(
    index,
    empirical_probs,
    bar_width,
    label="Емпіричні ймовірності",
    color="skyblue",
    alpha=0.7,
)
plt.bar(
    [s + 0.5 * bar_width for s in sums],
    theoretical_probs,
    bar_width,
    label="Теоретичні ймовірності",
    color="salmon",
    alpha=0.7,
)


plt.xlabel("Сума двох кубиків")
plt.ylabel("Ймовірність")
plt.title(f"Порівняння емпіричних та теоретичних ймовірностей (кидків: {num_rolls})")
plt.xticks(sums)  # Відображаємо цілі числа на осі X
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.legend()
plt.show()


# To generate data for .md

# print("\nТаблиця ймовірностей сум (100 000 кидків):")
# print("{:<5} {:<15} {:<15} {:<10}".format("Сума", "Монте-Карло", "Аналітична", "Різниця"))
# print("-" * 50)

# for sum_val in sorted(probabilities.keys()):
#     emp_prob = probabilities[sum_val]
#     theo_prob = theoretical_probabilities[sum_val]
#     difference = abs(emp_prob - theo_prob) # Абсолютна різниця

#     print("{:<5} {:<15.4f} {:<15.4f} {:<10.4f}".format(sum_val, emp_prob * 100, theo_prob * 100, difference * 100)) # Виводимо у відсотках
