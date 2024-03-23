import random
import matplotlib.pyplot as plt


def simulate_dice_rolls(num_rolls):

    probabilities = {}
    for i in range(2, 13):
        probabilities[i] = 0

    for _ in range(num_rolls):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        sum_of_rolls = roll1 + roll2
        probabilities[sum_of_rolls] += 1

    total_rolls = num_rolls
    for sum_of_rolls in probabilities:
        probabilities[sum_of_rolls] /= total_rolls
    return probabilities


def plot_probabilities(probabilities, accuracy):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.bar(sums, probs, tick_label=sums)
    plt.xlabel("Сума чисел на кубиках")
    plt.ylabel("Ймовірність")
    plt.title(f"Ймовірність суми чисел на двох кубиках, кількість кидків: {accuracy}")

    for i, prob in enumerate(probs):
        plt.text(sums[i], prob, f"{prob*100:.2f}%", ha="center")

    plt.show()


if __name__ == "__main__":
    for accuracy in [100, 1000, 10000, 100000]:
        probabilities = simulate_dice_rolls(accuracy)
        plot_probabilities(probabilities, accuracy)
