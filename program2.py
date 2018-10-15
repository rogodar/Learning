user_name = input("Enter your name : ")
print("Hello, {name}".format(name=user_name))


principal=eval(input("Enter Loan Amount:"))
interest=12.99
periods=4
n_years=2
print(f"Entered:{principal}")
final_cost = principal * (1+interest/100.0/periods)**n_years

print("{cost:0.0f}".format(cost=final_cost))
print("Total Interest Paid:  {interest:0.0f}".format(interest=final_cost-principal))
print("Montly Paiments: {payment:0.0f}".format(payment=final_cost/24))

