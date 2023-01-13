h = float(input("Your height (cm): "))
if h>=120:
    print("Yes! You can play.")
else:
    print("Sorry, you need %.2f more cm to play."
    % (120-h))