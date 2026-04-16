import random
from datetime import datetime 
def quiz_game():
    print(f"=== QUIZ TIME ===")
    quiz_data = [
    {"question": "Python me list ke liye kaunse brackets?", "answer": "square"},
    {"question": "Function banane ka keyword?", "answer": "def"},
    {"question": "Comment symbol?", "answer": "hash"},
    {"question": "Immutable type example?", "answer": "tuple"},
    {"question": "Output function?", "answer": "print"}
     ]
    question= random.sample(quiz_data,3)
    points=0
    for q in question:
        print(q['question'])
        a=input('enter your answer: ').lower().strip()
        if a==q['answer'].lower():
            points+=10
            print(f'your answer is right, now your point is {points}')
        else:
            print(f"wrong, correct answer: {q['answer']}")
    print('='*50)                
    print(f"total score{points}/30")
    discount=0
    if points==30:
        print('you got of discount 20%!')
        discount=20
    elif points==20:
        print('you got discount of 10%!')
        discount=10
    else:
        print('sorry, but you got discount of 0%')
        discount=0
    print('='*50+'\n')
    with open('score.txt','a') as f:
        f.write(f"{datetime.now()} - score{points}\n ")
    return discount
def shopping_cart(discount,user_name):
    cart=[]
    print('===SHOPPING CART===')
    while True:
        name= input('add item or write "done" if you want to finish: ').strip()
        if name.lower() == "done":
            break

        try:
            price = int(input("Enter price: "))
            quantity = int(input("Enter quantity: "))
        except ValueError:
            print("Invalid input! Try again.")
            continue

        item = {
            "Item": name,
            "Price": price,
            "Quantity": quantity }
        cart.append(item)
        print(f"✅ {name} added!")
    print(f"\n{'Item':<15} {'Price':<10} {'Quantity':<8}")
    print('-' * 43)
    subtotal=0
    for i in cart:
        price=i["Price"]
        quantity=i['Quantity']
        name = i['Item']
        bill= price*quantity
        subtotal+=bill  
        print(f"{name:<15} {price:<10} {quantity:<8} {bill:<10}")
    print('-'*9)
    print('subtotal: ₹',subtotal)
    print('-'*9+'\n')
    dis= (subtotal/100)*discount
    print(f'discount({discount}%) : -₹{dis}')
    print(f'final bill: ₹{subtotal-dis}')
    with open('bill.txt','a') as f:
        f.write('\n ===NEW BILLL===\n')
        f.write(f'date- {datetime.now()}\n')
        f.write(f"User: {user_name}\n")
        for i in cart:
            price=i.get("Price")
            quantity=i.get('Quantity')
            name = i.get('Item')
            bill= price*quantity  
            f.write(f"{name} - {price} x {quantity} = {bill}\n")
        f.write(f"Subtotal: {subtotal}\n")
        f.write(f"Discount: {dis}\n")
        f.write(f"Final Bill: {subtotal-dis}\n")
user_name = input("Enter your name: ")
discount=quiz_game()
shopping_cart(discount,user_name)