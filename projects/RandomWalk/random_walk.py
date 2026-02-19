


import random 

def simulate_random_walk(steps):
    position = 0
    path = [position]

    #Mastery Challenge Addition: Track how much time we spend "in the green"
    above_zero_count = 0 

    for i in range(steps):
        # 0.5 is the 'Fair Coin' - 50/50 chance 
        step = 1 if random.random() > 0.5 else -1
        position += step
        path.append(position)

        if position > 0:
            above_zero_count += 1 
    
    return path, above_zero_count

# 1 - Run The Simulation 
total_steps = 100
walk_path, time_spent_above = simulate_random_walk(total_steps)

# 2 - Output the Results 
print(f"--- 🎲 Blackwell Random Walk (Steps: {total_steps}) ---")
print(f"Final Position: {walk_path[-1]}")
print(f"Total Steps spent above Zero: {time_spent_above}")
print(f"Percentage of journey spent 'Positive': {(time_spent_above/total_steps) * 100}%")

# 3 - Simple Visualization (Showing the last 10 steps of the path)
print(f"\nLast 10 steps of history: {walk_path[-10:]}") 

