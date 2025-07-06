# 🚀 MML Launchpad (MMLLaunchpad.py)

A mini Python automation script that opens a set of selected websites in your default browser with just one click. 
Created as part of the **Melanated Machine Learning (MML)** learning journey to practice scripting, workflow automation, and basic Python skills.

---

## 🧠 Purpose

This was my first working Python script — a beginner-friendly way to understand how automation can simplify repetitive tasks. 
The goal was to:

- Automate the process of opening multiple browser tabs
- Get familiar with writing and running `.py` scripts
- Learn how to use the `webbrowser` module in Python
- Build confidence with small, repeatable wins early in the journey

---

## 🛠️ Features

- Automatically opens multiple websites in separate browser tabs
- Easily customizable — just replace or add any URLs to suit your workflow

---

## 📦 Requirements

- Python 3.x installed  
- A code editor (e.g., [VS Code](https://code.visualstudio.com/))  
- Works on macOS, Windows, and Linux  
- Internet connection for opening web pages

---

## 💻 How to Use

1. Clone or download the repository
2. Open the `MMLLaunchpad.py` file in your text editor
3. Customize the URL list (optional)
4. Run the script in terminal or command prompt:

## 💻 Code Overview 

```bash
python MMLLaunchpad.py 

import webbrowser

sites = [
    "https://github.com/GroovyWoo/Melanated-Machine-Learning",  # MML GitHub
    "https://www.youtube.com/@MMLVision",  # YouTube Channel
    "https://x.com/MMLVision",  #  MML on Twitter (X)
    "https://www.instagram.com/mmlvision/",  # MML on IG 
    "https://www.linkedin.com/in/mmlvision",  # MML on LinkedIn 
]

for site in sites:
    webbrowser.open(site) 

```
<!-- End of Code Overview block --> 
 

---

## 🪪 License 
-  https://choosealicense.com/licenses/mit/ 

This project is licensed under the **MIT License**. 
Feel free to use and modify - just give credit if you build on top of it. 


---

## ✍🏾 Author 
**Q aka Groovy Woo**  
- Creator of the Melanated Machine Learning (MML) journey
- 🧠⚙️ Documenting and building in public for other dreamers, learners, and community leaders…


---

## 🚧 Project Status 
✅ Completed – Initial version ready.  
🚀 Future additions may include:
- Customizable site sets
- User input for URLs
- GUI version with Tkinter or Streamlit







