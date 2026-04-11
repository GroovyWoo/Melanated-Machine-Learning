

# Project 06: Musical Risk Simulator (Expected Value)

---

### 🎯 The Objective
To move beyond simple probability and into **Decision Theory**. This project simulates the financial risk of an independent music label, determining if a positive Expected Value (EV) can survive the "Variance" of a 100-artist signing cycle.

### 🛠️ Technical Stack
* **Language:** Python 3.x
* **Concepts:** Stochastic Modeling, Expected Value (EV) Calculation, Law of Large Numbers.
* **Formula:** $EV = (P(Success) \times Profit) + (P(Failure) \times Loss)$

---

### 🧠 The Discovery
During the laboratory simulation, I discovered that even with an 80% failure rate, a label remains profitable if the "payout" of a success is sufficiently high. 

**Key takeaway:** The "Variance" between my simulation runs was massive (ranging from **$430k to $1.7M**). This demonstrates why **Risk Management** and **Capital Reserves** are more critical than pure mathematical probability for independent entities. A "Good Decision" on paper can still lead to bankruptcy if you don't have the runway to weather the "Loss" cycles.

---

### 📈 Real-World Inference
This logic directly applies to **Recommendation Engines**. An AI must decide whether to recommend a "Safe" artist (High probability/Low reward) or a "Risky" breakout artist (Low probability/High reward). By calculating the EV of user engagement, the algorithm optimizes for long-term "Super-Fan" creation rather than short-term clicks.

> **Blackwell Reflection:** "Judge the process, not the result." A successful outcome from a bad process is just luck; a poor outcome from a good process is just variance.