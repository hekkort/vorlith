
import random

meals = ["Pizza", "Pasta", "Salad", "Soup", "Sandwich", "Tacos"]

def suggest_meal():
  return random.choice(meals)

if __name__ == "__main__":
  print(f"Suggested meal: {suggest_meal()}")
