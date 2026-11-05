# Final Project Amazon Price Calculator

print("   Amazon Price Calculator")

# Product Information

Product_Name = input("Enter Product Name ")

selling_price = float(input("Enter Selling Price"))

product_cost = float(input("Enter Product Cost"))

referral_percent = float(input("Enter Referral Fee Percentage"))

fba_fee = float(input("Enter FBA Fulfilment Fee"))

shipping_cost = float(input("Enter Shipping Cost"))

prep_cost = float(input("Enter Prep Cost"))

# Calculate Amazon Fees

referral_fee_amount = (selling_price * referral_percent) / 100

#Calculate Total Fees

total_expenses = (
product_cost + referral_fee_amount + fba_fee + shipping_cost + prep_cost
)

#Calculate net profit

profit = selling_price - total_expenses

#Calculate ROI (Return on Investment)

investment = product_cost + shipping_cost + prep_cost

if investment > 0:
    roi = (profit / investment) * 100
else:
    roi = 0

    #calculate profit margin

if selling_price > 0:
    margin = (profit / selling_price) * 100
else:
    margin = 0

# Display Results

print(" Profit Results")

print("product name: ", Product_Name)

print("Selling Price: $", round(selling_price, 2))

print("Total Expenses: $", round(total_expenses, 2))

print("Net Profit: $", round(profit, 2))

print("ROI: ", round(roi, 2), "%")

print("Profit Margin: ", round(margin, 2), "%")


#Decide if the product is profitable

if profit >=5:
    print("Status: Great Product")

elif profit > 0:
    print("Status: PROFITABLE")

else:
    print("Status: NOT PROFITABLE")
    

                     
                    