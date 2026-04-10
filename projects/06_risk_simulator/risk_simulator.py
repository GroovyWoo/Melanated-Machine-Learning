


import random

# --- 📊 Part 1: The Math --- 
p_success = 0.20
p_failure = 0.80

profit_success = 100000  # $100K
loss_failure = -10000  # -$10K

#Formula: (P(Success) * Profit) + (P(Failure) * Loss)
expected_value = (p_success * profit_success) + (p_failure * loss_failure)

print(f"--- 🏛️ Blackwell Decision Room ---")
print(f"Calculated Expected Value (EV) per artist: ${expected_value}")

# --- 🎲 Part 2: The Simulation --- 
num_artists = 100
bank_account = 0
success_count = 0 

for _ in range(num_artists):
    # Simulate the outcome based on 20% probability
    if random.random() <p_success:
        bank_account += profit_success
        success_count += 1 
    else:
        bank_account += loss_failure

print(f"\n--- 📈 Results after signing {num_artists} Artists ---")
print(f"Total Successes: {success_count}")
print(f"Total Failures: {num_artists - success_count}") 
print(f"Final Bank Account Balance: ${bank_account}")

# --- 🧠 The Blackwell Insight --- 
if bank_account > 0:
    print("\n✅ The Label Survived. The Positive EV played out over time.")
else:
    print("\n⚠️ The Label is Bankrupt. Even with Positive EV, variance was too high.")