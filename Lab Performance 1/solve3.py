# Task 3: Hill Climbing Algorithm

import random

# Define the function to maximize
def f(x):
  return -x**2 + 4*x

def hill_climbing():
  # Start at a random point
  current_x = random.uniform(-10.0, 10.0)
  step_size = 0.1
  max_iterations = 1000

  print(f"Starting at x = {current_x:.4f}, f(x) = {f(current_x):.4f}")

  for i in range(max_iterations):
    current_value = f(current_x)
    
    # Check neighbors
    neighbor_plus = current_x + step_size
    neighbor_minus = current_x - step_size
    
    value_plus = f(neighbor_plus)
    value_minus = f(neighbor_minus)

    # Find the neighbor with the highest value
    if value_plus > current_value and value_plus >= value_minus:
      current_x = neighbor_plus # Move to the right
    elif value_minus > current_value and value_minus > value_plus:
      current_x = neighbor_minus # Move to the left
    else:
      # No neighbor is better, we have reached a peak
      print("\nReached a local maximum (peak).")
      break
  
  print(f"Found maximum at x = {current_x:.4f}")
  print(f"Maximum value f(x) = {f(current_x):.4f}")

# --- Demonstration ---
hill_climbing()