
# Final Project Amazon Price Calculator

# Function for Single Product Calculator

def single_product_calculator():

    print()
    print("Amazon Price Calculator")

    # Product Information

    Product_Name = input("Enter Product Name ")

    selling_price = float(input("Enter Selling Price "))
    product_cost = float(input("Enter Product Cost "))
    referral_percent = float(input("Enter Referral Fee Percentage "))
    fba_fee = float(input("Enter FBA Fulfillment Fee "))
    shipping_cost = float(input("Enter Shipping Cost "))
    prep_cost = float(input("Enter Prep Cost "))

    # Calculate Amazon Fees

    referral_fee_amount = (selling_price * referral_percent) / 100

    # Calculate Total Expenses

    total_expenses = (
        product_cost + referral_fee_amount + fba_fee + shipping_cost + prep_cost
    )

    # Calculate Net Profit

    profit = selling_price - total_expenses

    # Calculate ROI (Return on Investment)

    investment = product_cost + shipping_cost + prep_cost

    if investment > 0:
        roi = (profit / investment) * 100
    else:
        roi = 0

    # Calculate Profit Margin

    if selling_price > 0:
        margin = (profit / selling_price) * 100
    else:
        margin = 0

    # Display Results

    print()
    print("Profit Results")

    print("Product Name: ", Product_Name)
    print("Selling Price: $", round(selling_price, 2))
    print("Total Expenses: $", round(total_expenses, 2))
    print("Net Profit: $", round(profit, 2))
    print("ROI: ", round(roi, 2), "%")
    print("Profit Margin: ", round(margin, 2), "%")

    # Decide if the Product is Profitable

    if profit >= 5:
        print("Status: Great Product")

    elif profit > 0:
        print("Status: PROFITABLE")

    else:
        print("Status: NOT PROFITABLE")


# Function for Bulk Purchase Calculator

def bulk_purchase_calculator():
    print()
    print("Bulk Purchase Calculator")

    # Product Information

    Product_Name = input("Enter Product Name ")
    quantity = int(input("Enter Number of Units "))

    selling_price = float(input("Enter Selling Price Per Unit "))
    product_cost = float(input("Enter Product Cost Per Unit "))
    referral_percent = float(input("Enter Referral Fee Percentage "))
    fba_fee = float(input("Enter FBA Fulfillment Fee Per Unit "))
    shipping_cost = float(input("Enter Total Shipping Cost "))
    prep_cost = float(input("Enter Prep Cost Per Unit "))

    # Calculate Total Revenue

    if quantity > 0:

        total_revenue = selling_price * quantity

        # Calculate Amazon Fees

        referral_fee_amount = (total_revenue * referral_percent) / 100

        #Calculate Total Expenses

        total_product_cost = product_cost * quantity
        total_fba_fee = fba_fee * quantity
        total_prep_cost = prep_cost * quantity

        total_expenses = (
            total_product_cost + referral_fee_amount + total_fba_fee
            + shipping_cost + total_prep_cost
        )

        #Calculate Net Profit

        profit = total_revenue - total_expenses

        #Calculate ROI

        investment = total_product_cost + shipping_cost + total_prep_cost

        if investment > 0:
            roi = (profit / investment) * 100
        else:
            roi = 0

        # Calculate Profit Margin

        if total_revenue > 0:
            margin = (profit / total_revenue) * 100
        else:
            margin = 0

        #Calculate Profit Per Unit

        profit_per_unit = profit / quantity

        #Display Results

        print("\nBulk Purchase Results")

        print("Product Name: ", Product_Name)
        print("Units Purchased: ", quantity)
        print("Total Revenue: $", round(total_revenue, 2))
        print("Total Expenses: $", round(total_expenses, 2))
        print("Total Profit: $", round(profit, 2))
        print("Profit Per Unit: $", round(profit_per_unit, 2))
        print("ROI: ", round(roi, 2), "%")
        print("Profit Margin: ", round(margin, 2), "%")

        # Decide if the Purchase is Profitable

        if profit >= 50:
            print("Status: Great Bulk Purchase")

        elif profit > 0:
            print("Status: PROFITABLE")

        else:
            print("Status: NOT PROFITABLE")

    else:
        print("Please enter a quantity greater than zero")


# Function for Product Comparison

def compare_products():

    print()
    print("Product Comparison")

    # First Product Information

    Product1_Name = input("Enter First Product Name ")
    selling_price1 = float(input("Enter First Product Selling Price "))
    product_cost1 = float(input("Enter First Product Cost "))
    referral_percent1 = float(input("Enter First Product Referral Fee Percentage "))
    fba_fee1 = float(input("Enter First Product FBA Fee "))
    shipping_cost1 = float(input("Enter First Product Shipping Cost "))
    prep_cost1 = float(input("Enter First Product Prep Cost "))

    # Calculate First Product Profit

    referral_fee1 = (selling_price1 * referral_percent1) / 100

    total_expenses1 = (
        product_cost1 + referral_fee1 + fba_fee1
        + shipping_cost1 + prep_cost1
    )

    profit1 = selling_price1 - total_expenses1

    investment1 = product_cost1 + shipping_cost1 + prep_cost1

    if investment1 > 0:
        roi1 = (profit1 / investment1) * 100
    else:
        roi1 = 0

    # Second Product Information

    Product2_Name = input("Enter Second Product Name ")
    selling_price2 = float(input("Enter Second Product Selling Price "))
    product_cost2 = float(input("Enter Second Product Cost "))
    referral_percent2 = float(input("Enter Second Product Referral Fee Percentage "))
    fba_fee2 = float(input("Enter Second Product FBA Fee "))
    shipping_cost2 = float(input("Enter Second Product Shipping Cost "))
    prep_cost2 = float(input("Enter Second Product Prep Cost "))

    # Calculate Second Product Profit

    referral_fee2 = (selling_price2 * referral_percent2) / 100

    total_expenses2 = (
        product_cost2 + referral_fee2 + fba_fee2
        + shipping_cost2 + prep_cost2
    )

    profit2 = selling_price2 - total_expenses2

    investment2 = product_cost2 + shipping_cost2 + prep_cost2

    if investment2 > 0:
        roi2 = (profit2 / investment2) * 100
    else:
        roi2 = 0

    # Display Comparison Results

    print()
    print("Product Comparison Results")

    print(Product1_Name, "Profit: $", round(profit1, 2))
    print(Product1_Name, "ROI: ", round(roi1, 2), "%")

    print(Product2_Name, "Profit: $", round(profit2, 2))
    print(Product2_Name, "ROI: ", round(roi2, 2), "%")

    # Compare Products

    if profit1 > profit2:
        print(Product1_Name, "has higher profit")

    elif profit2 > profit1:
        print(Product2_Name, "has higher profit")

    else:
        print("Both products have equal profit")




#Main Menu

def main_menu():

    choice = ""

    while choice != "4":

        print()
        print("Amazon Smart Calculator")
        print("1. Single Product Calculator")
        print("2. Bulk Purchase Calculator")
        print("3. Product Comparison")
        print("4. Exit")

        choice = input("Select an Option ")

        if choice == "1":
            single_product_calculator()

        elif choice == "2":
            bulk_purchase_calculator()

        elif choice == "3":
            compare_products()

        elif choice == "4":
            print("Thank you for using Amazon Smart Calculator")

        else:
            print("Invalid Option. Please Try Again")

#Start Program

main_menu()
