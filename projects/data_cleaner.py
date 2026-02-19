


import pandas as pd

# 1. Create the 'dirty' dataset (The Raw Observations) 
data = { 
    'Song': ['Midnight City', 'Rush', 'Unavailable', 'Vibration', None],
    'Artist': ['M83', 'Ayra Starr', 'Davido', None, 'Unknown'], 
    'Plays': [150, 200, None, 80, 10] 
}

df = pd.DataFrame(data)
print("--- 📊 Original Data ---\n", df)

# 2. The Cleaning Logic (Noise Reduction)
#Remove rows where 'Song" is missing 
df_cleaned = df.dropna(subset=['Song']).copy()  #.copy() prevents a common python warning 

#Fill missing 'Plays' with 0 (A 'Conservative' Decision)
df_cleaned['Plays'] = df_cleaned['Plays'].fillna(0)

print("\n--- ✅ Cleaned Data ---\n", df_cleaned)

#3. The Blackwell Decision Filter (High Impact Only)
high_impact = df_cleaned[df_cleaned['Plays'] > 100] 
print("\n--- 🎯 High Impact Songs ---\n", high_impact) 

