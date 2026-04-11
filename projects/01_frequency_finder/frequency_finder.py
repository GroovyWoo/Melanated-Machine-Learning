


#frequency_finder 

# 1 - The Raw Observation 
observations = ["Afrobeats", "Jazz", "R&B", "Reggae", "Jazz", "R&B", "Afrobeats", "R&B", "Lo-fi", "Reggae", "Jazz", "R&B", "Afrobeats"]

# 2 - The empty map (our stating belief of the world)
frequency_map = {}

# 3 - The Blackwell Logic
for genre in observations: 
    if genre in frequency_map:
        # We've seen this before ! Increment the Knowledge.
        frequency_map[genre] = frequency_map[genre] + 1
    else: 
        # First time seeing this. Initialize the knowledge
        frequency_map[genre] = 1

# 4 - Display the Knowledge 
print("---📊 Blackwell Frequency Finder ___")
print(f"Total Observations: {len(observations)}")
print(f"Unique Categories: {len(frequency_map)}")
print("Distribution:", frequency_map) 

# 5 - The Probabality Calculationo (Normalization)
print("\n--- 🎲 Blackwell Probability Distribution ---")

total = len(observations)

for genre, count in frequency_map.items(): 
    #calculate the probability 
    probability = count / total 

    #Convert to a clean percentage for display 
    percentage = probability * 100 

    print(f"{genre}: {probability: .2f} ({percentage: .0f}%)") 
    

