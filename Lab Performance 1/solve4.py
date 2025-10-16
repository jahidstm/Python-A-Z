# Bonus Task: Gradient Descent Algorithm

# Define the derivative (gradient) of the function f(x) = x^2 + 4x + 4
# The derivative is f'(x) = 2x + 4 [cite: 39]
def gradient(x):
  return 2*x + 4

def gradient_descent():
  # Algorithm parameters
  current_x = 10.0  # Start at an arbitrary point [cite: 30]
  learning_rate = 0.1 # The size of each step [cite: 27]
  iterations = 100
  
  print(f"Starting Gradient Descent at x = {current_x}")

  # Repeat until convergence [cite: 31]
  for i in range(iterations):
    grad = gradient(current_x) # Compute the gradient [cite: 32]
    
    # Update position using the formula: x_new = x_old - alpha * gradient [cite: 24, 33]
    current_x = current_x - learning_rate * grad
    
    # Optional: Print progress
    if (i+1) % 10 == 0:
      print(f"Iteration {i+1}: x = {current_x:.6f}")

  print("\nGradient Descent finished.")
  print(f"Found minimum at x = {current_x:.6f}")

# --- Demonstration ---
gradient_descent()