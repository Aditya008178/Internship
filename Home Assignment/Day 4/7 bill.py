# 7.	A shop gives discount:
# o	Total bill < 500 → No discount
# o	500 to 1000 → 5% discount
# o	Above 1000 → 10% discount
# Take bill amount as input and display final amount to be paid.



total = float(input("Enter your total bill amount: "))

if bill_amount < 500:
    discount = 0
elif bill_amount <= 1000:
    discount = 0.05 * total
else:
    discount = 0.10 * total

final_amount = bill_amount - discount

print(f"Final amount : {final_amount}")