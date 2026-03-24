

#
import random

def simulate_walker(steps, probability_up):
    ups = 0 
    for _ in range(steps): 
        if random.random() < probability_up:
            ups += 1
    return ups 

# 1. The Experiment Parameters 
steps_per_walk = 100
num_experiments = 1000
fair_prob = 0.50 
biased_prob = 0.60 

fair_wins_fake_bias = 0 # Counter for when Fair looks "better" than Biased 

print(f"--- 🕵🏽‍♂️ Running {num_experiments} Blackwell Experiments ---")

for i in range(num_experiments):
    # Run one walk for each 
    fair_ups = simulate_walker(steps_per_walk, fair_prob)
    biased_ups = simulate_walker(steps_per_walk, biased_prob)

    #The "Trick": Does the Faie walker have more 'up-steps' than the Biased one?
    if fair_ups >= biased_ups:
        fair_wins_fake_bias += 1

# 2. The Reveal 
deception_rate = (fair_wins_fake_bias / num_experiments) * 100 

print(f"Fair Walker 'Tricked' us: {fair_wins_fake_bias} times.") 
print(f"Deception Rate: {deception_rate}%")

#3. The Blackwell Insight 
if deception_rate > 10: 
    print("\n⚠️ Insight: 100 steps is NOT enight to be cetain. The noise is too loud.")
else:
    print("\n✅ Insight: The evidence is strong. The Biased Walker's nature is clear.") 

