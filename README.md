# 🧠 Quiz + Shopping Cart System (Python)
A Python-based command line project that combines a quiz game with a shopping cart system.
Users answer quiz questions to earn a discount, which is applied to their final shopping bill.
---
## 🚀 Features
* Dynamic Quiz (random questions every time)
* Score-based discount system
* Add multiple items to shopping cart
* Automatic bill calculation
* Discount applied on total bill
* Saves user score and shopping bill in files,
* User name tracking
---
## 🛠️ Tech Used
* Python
* Functions
* Lists & Dictionaries
* Loops
* Conditional Statements
* File Handling
* Random Module
* Datetime Module
---
## 📌 How It Works
1. User enters their name
2. Quiz starts (3 random questions)
3. Each correct answer = 10 points
4. Based on score:
   * 30 → 20% discount
   * 20 → 10% discount
   * Less than 20 → No discount
5. User adds items to cart
6. Final bill is calculated with discount
7. Bill and score are saved in files
---
## ▶️ How to Run
1. Make sure Python is installed
2. Clone the repository:
```bash
   git clone https://github.com/yachikadev/quiz-shopping-system-python.git
   cd quiz-shopping-system-python
```
3. Run the program:
```bash
   python main.py
```
---
## 📂 Output Files
* score.txt → Stores quiz scores with date & time
* bill.txt → Stores detailed shopping bills
---
## 📷 Sample Output
=== QUIZ TIME ===
Question: ...
Correct!
=== SHOPPING CART ===
Item            Price      Quantity
Apple           50         2        100
Subtotal: ₹100
Discount (10%): -₹10
Final Bill: ₹90
---
## 👩‍💻 Author
Yachika Sharma
