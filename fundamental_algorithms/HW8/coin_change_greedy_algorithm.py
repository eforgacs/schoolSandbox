def give_coin_change_greedy():
    count = 0
    quarters, dimes, nickels, pennies = 0, 0, 0, 0
    change = int(input("Please input the amount of change:"))
    while change > 0:
        while change >= 25:
            count += 1
            quarters += 1
            change = change - 25
        while change >= 10:
            count += 1
            dimes += 1
            change = change - 10
        while change >= 5:
            count += 1
            nickels += 1
            change = change - 5
        while change >= 1:
            count += 1
            pennies += 1
            change -= 1
    print(f"Quarters: {quarters}\n"
          f"Dimes: {dimes}\n"
          f"Nickels: {nickels}\n"
          f"Pennies: {pennies}\n"
          f"Coins used: {count}")


give_coin_change_greedy()
