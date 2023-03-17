
def display():

    print(f" Spending and Saving program")
    print()

def calculations(total_monthly_revenue, mortgage_month_cost, food_month_cost,clothing_month_cost, entertainment_month_cost ):

    # total cost of items from total revenue
    monthly_cost = mortgage_month_cost + food_month_cost + clothing_month_cost + entertainment_month_cost

    # total left over from monthly expenses
    monthly_revenue_aftercost = total_monthly_revenue - monthly_cost

    # Mortgage percent amount for month
    monthly_mortgage_percent = (mortgage_month_cost / total_monthly_revenue) * 100

    # Food percent amount for month
    monthly_food_percent = (food_month_cost / total_monthly_revenue) * 100

    # Clothing percent amount for month
    monthly_clothes_percent = (clothing_month_cost/ total_monthly_revenue) * 100

    # Entertainment perent amount for month
    monthly_entertainment_percent = (entertainment_month_cost/ total_monthly_revenue) * 100

    return monthly_cost, monthly_revenue_aftercost, monthly_mortgage_percent, monthly_food_percent, monthly_clothes_percent, monthly_entertainment_percent


def main():

    display()

    total_monthly_revenue = float(input(f"Enter your Monthly revenue: "))
    print("")
    mortgage_month_cost = float(input(f" Enter your Monthly Mortgage cost: "))
    food_month_cost = float(input(f" Enter your Monthly Food cost: "))
    print("")
    clothing_month_cost = float(input(f" Enter your Monthly Clothing cost: "))
    print("")
    entertainment_month_cost = float(input(f" Enter your Monthly Entertainment cost: "))

    monthly_cost_total, monthly_revenue_aftercost_total, monthly_mortgage_percent_total, monthly_food_percent_total,\
    monthly_clothing_percent_total, monthly_entertainment_percent_total = calculations(total_monthly_revenue, 
    mortgage_month_cost, food_month_cost, clothing_month_cost, entertainment_month_cost)

    print()
    print(f" your total monthly revenue is: {total_monthly_revenue}")
    print()
    print(f" your total monthly cost is: {monthly_cost_total}")
    print(f" your total monthly cost for your Mortgage is: {mortgage_month_cost}")
    print(f" your total monthly percentage spending on your mortgage is: {monthly_mortgage_percent_total}")
    print()
    print(f" your total monthly cost of food is: {food_month_cost}")
    print(f" your total percentage spending on food per month is: {monthly_food_percent_total}")
    print()
    print(f" your total monthly cost of clothing is: {clothing_month_cost}")
    print(f" your total percentage spending on clothing per month is: {monthly_clothing_percent_total}")
    print()
    print(f" your total monthly cost of entertainment is: {entertainment_month_cost}")
    print(f" your total percentage spending on entertainment per month is: {monthly_entertainment_percent_total}")




if __name__=="__main__":
    main()




