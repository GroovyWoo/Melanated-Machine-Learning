


# --- 🏛️ Stage 1: The Blackwell Bayesian Lab ---

# 1. The Prior: P(Afrobeats)
#30% of your library is Afrobeats
p_afrobeats = 0.30 

# 2. The Likelihood: P(110_BPM | Afrobeats)
#80% of Afrobeats songs are 110 BPM 
p_110_given_afrobeats = 0.80

# 3. The Other Side: P(Other Genres)
p_others = 1 - p_afrobeats # 70%

# 4. The Likelihood For Others: P(110_BPM | Others)
# Only 10% of other genres are 110 BPM 
p_110_given_others = 0.10 

# 5. The Marginal Likelihood: P(110_BPM) 
# THis is the total probabability of seeing 110 BPM across Everything 
# Calculation: (Prob of 110 in Afro * Afro count) + (Prob of 110 in Others * Other count)
p_110_total = (p_110_given_afrobeats * p_afrobeats) + (p_110_given_others * p_others)

# 6. The Posterior: P(Afrobeats | 110_BPM) - THe "Blackwell Update"
# Using your formula: (Likelihood * Prior) / Marginal 
posterior_afrobeats = (p_110_given_afrobeats * p_afrobeats) / p_110_total 

print(f"--- 🎵 Blackwell Genre Classifier Results ---")
print(f"Prior Probability (Before evidence): {p_afrobeats * 100}%")
print(f"New Posterior Probability (After 110 BPM Evidence): {round(posterior_afrobeats * 100, 2)}%") 

# --- 🧠 Strategy Room Reflection --- 
if posterior_afrobeats > p_afrobeats:
    print("\n✅ The evidence Strongly supported the Afrobeats hypothesis.")
else:
    print("\n❌ The evidence Weakend the hypothesis.") 
