

# Project 05: Bayesian Genre Classifier (Inference Logic)

---

### 🎯 The Objective
To build the "Brain" of a classification engine. This project moves beyond simple data observation and into **Inference**, using Bayes' Theorem to work backward from evidence (BPM) to cause (Musical Genre).

### 🛠️ Technical Stack
* **Language:** Python 3.x
* **Concepts:** Bayesian Inference, Conditional Probability, Prior vs. Posterior Beliefs.
* **Formula:** $$P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$$

---

### 🧠 The Discovery
This project demonstrated the "Tug-of-War" between existing knowledge (The Prior) and new data (The Evidence). 

**Key takeaway:** I discovered that even strong evidence (an 80% likelihood) is heavily influenced by the starting context. When the "Prior" for Afrobeats was 30%, a 110 BPM reading pushed the probability of a match to **~77%**. However, when the "Prior" was dropped to 1%, that same evidence only resulted in a **~7%** probability. 

This taught me that an AI's "history" is just as important as the data it is currently seeing.

---

### 📈 Real-World Inference
This logic is the foundation of **Modern Recommendation Systems** (Spotify, Netflix, YouTube). It explains why a single "accidental" click on a video doesn't immediately change your entire feed—the algorithm's "Prior" belief about your tastes is strong enough to filter out the "noise" of a single data point. It only "updates its belief" once the evidence becomes consistent over time.

> **Blackwell Reflection:** "Probability is not about what will happen; it is about the degree of your justified belief."