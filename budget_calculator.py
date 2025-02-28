# Budget Breakdown Calculator

# Step 1: Get the total budget from the user
total_budget = float(input("Enter your total monthly budget (net income): $"))

# Step 2: Get spending amounts for each category
housing = float(input("Enter amount spent on Housing (rent/mortgage): $"))
utilities = float(input("Enter amount spent on Utilities: $"))
groceries = float(input("Enter amount spent on Groceries: $"))
transportation = float(input("Enter amount spent on Transportation: $"))
health_care = float(input("Enter amount spent on Health Care: $"))
personal_care = float(input("Enter amount spent on Personal Care: $"))
clothing = float(input("Enter amount spent on Clothing: $"))
debt = float(input("Enter amount spent on Debt: $"))

# Step 3: Calculate the percentage of the total budget for each category
def calculate_percentage(amount, total):
    return (amount / total) * 100

housing_percent = calculate_percentage(housing, total_budget)
utilities_percent = calculate_percentage(utilities, total_budget)
groceries_percent = calculate_percentage(groceries, total_budget)
transportation_percent = calculate_percentage(transportation, total_budget)
health_care_percent = calculate_percentage(health_care, total_budget)
personal_care_percent = calculate_percentage(personal_care, total_budget)
clothing_percent = calculate_percentage(clothing, total_budget)
debt_percent = calculate_percentage(debt, total_budget)

# Step 4: Display the results using f-strings
print("\n--- Budget Breakdown ---")
print(f"Housing: {housing_percent:.2f}%")
print(f"Utilities: {utilities_percent:.2f}%")
print(f"Groceries: {groceries_percent:.2f}%")
print(f"Transportation: {transportation_percent:.2f}%")
print(f"Health Care: {health_care_percent:.2f}%")
print(f"Personal Care: {personal_care_percent:.2f}%")
print(f"Clothing: {clothing_percent:.2f}%")
print(f"Debt: {debt_percent:.2f}%")