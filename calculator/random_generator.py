import random

def generate_random_number(start, end):
  return random.randint(start, end)

if __name__ == "__main__":
  start_range = 1
  end_range = 100
  random_number = generate_random_number(start_range, end_range)
  print(f"A random number between {start_range} and {end_range} is: {random_number}")