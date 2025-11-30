# ✂️ Rock Paper Scissors Game (Python + Streamlit)

### 🔗 **Live Demo:**  
👉 https://rock-paper-sciapprs-game-kvm7mbye47xskkkgrd7llj.streamlit.app/

An interactive **Rock Paper Scissors Game** built with **Python OOP** and **Streamlit**.  
Try your luck against the computer and see if you can beat it in a best-of-3 challenge! 🎮

---

## 🚀 Features

- Fully object-oriented backend using Python classes  
- Play against computer with real-time input  
- Tracks **player score** and **computer score**  
- Handles invalid inputs gracefully  
- Streamlit UI for web interaction  
- Simple and clean interface for easy use  

---

## 📂 Project Structure

```
NumberGuessingGame/
│
├── src/
│ ├── init.py # Marks src as a Python package
│ ├── main.py # Core game logic (CLI and OOP)
│ └── run.py # Streamlit interactive UI
│
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```

### Explanation of Files:

- **src/** : All source code is inside this package for proper imports  
- **main.py** : Contains `rockPaperScissorsGame` class with all game logic  
- **run.py** : Streamlit interface for web version of the game  
- **requirements.txt** : Lists dependencies (Streamlit)  
- **README.md** : Project documentation, instructions, and future plans  

---

## 🎮 How The Game Works

1. Player inputs a choice: **rock**, **paper**, or **scissors**.  
2. Computer randomly selects a choice.  
3. Compare the choices to determine the winner of the round.  
4. Update scores for **player** or **computer**.  
5. Game continues until either player or computer reaches **3 points**.  
6. Streamlit version provides a web interface with buttons and real-time feedback.

---

## 🖥️ Running the Streamlit App

### 1️⃣ Install dependencies
Make sure you have Python installed, then run:

## 2️⃣ Run the app

From the project root directory, execute:
```
streamlit run src/run.py
```
## 📘 Documentation

### Class: `rockPaperScissorsGame` (`main.py`)

**Attributes:**

| Attribute        | Description                       |
|-----------------|-----------------------------------|
| `player_score`   | Player's current score            |
| `computer_score` | Computer's current score          |
| `valid_choices`  | Allowed moves: rock, paper, scissors |

**Methods:**

| Method                                  | Description                                   |
|----------------------------------------|-----------------------------------------------|
| `get_computer_choice()`                 | Randomly selects computer's move             |
| `get_player_choice()`                   | Get valid input from player (CLI)            |
| `specify_winner(player_choice, computer_choice)` | Determines winner of a round and updates scores |
| `play()`                                | Runs a single round in CLI                    |

### Streamlit (`run.py`)

- `st.text_input` to take player's move  
- `st.button` to submit and play  
- `st.error` for invalid input  
- `st.info` to display round result  
- Generates a random computer choice for each round  
- Updates scores and shows feedback immediately  

---

## 🛠 Future Improvements

- Add **best-of-N mode** for flexible rounds  
- Add **difficulty levels** (Easy / Medium / Hard)  
- Display **score history** using Streamlit charts  
- Enhance **UI design** with Streamlit components and CSS  
- Add **unit tests** for game logic  
- Deploy publicly on **Streamlit Cloud**  

---

## 👤 Author

**Ermia Razavi**  

If you enjoy this project, feel free to ⭐ star it on GitHub and share your results!
