valid_coins = "200", "100", "50", "20", "10", "5", "2", "1"
current_coin = 0
current_bag_weight = 0
#--- user ---#
bags_checked = 0
bag_value = ""

# coin_value    bag_value     weight
coins = {
        "£2": [200, 2000, 12.00],
        "£1": [100, 2000, 8.75],
        "50p": [50, 1000, 8.00],
        "20p": [20, 1000, 5.00],
        "10p": [10, 500, 6.50],
        "5p": [5, 500, 3.25],
        "2p": [2, 100, 7.12],
        "1p": [1, 100, 3.56]
        }

def calculate_coin(current_coin):
    current_coin = current_coin.replace("£","") 
    current_coin = current_coin.replace("p","")
    current_coin = int(current_coin)

    for coin in coins:                               # THIS IS THE TRUE VALUE OF THE USER INPUTTED BAG                                     current_bag_weight) / (coins[coin][2])
        correct_bag_weight = (coins[coin][2]) * (coins[coin][1] / coins[coin][0])    #this is the weight of the bag    
        if current_coin == (coins[coin][0]):
            if current_bag_weight == correct_bag_weight:  
                print("Valid bag weight found")
            else:
                if current_bag_weight > correct_bag_weight:
                    print(f"{current_bag_weight - correct_bag_weight} weight needs to be taken away from the bag to be correct")
                    print(f"{round((current_bag_weight - correct_bag_weight) / (coins[coin][2]))} less coins needed")
                else:
                    print(f"{correct_bag_weight - current_bag_weight} weight needs to be added to the bag to be correct")
                    print(f"{round((correct_bag_weight - current_bag_weight) / (coins[coin][2]))} more coins needed")


print("          Coin Count          \n------------------------------")

while True:
    name = input("Enter name: ")
    current_coin = str(input("Enter type of coin: "))
    current_bag_weight = float(input("Enter weight of bag: "))  #int
    print("")

    if (current_coin in coins): 
        if current_coin == "£2":
            current_coin = "200"
        elif current_coin == "£1":
            current_coin = "100"
        print("Valid coin found")
        bags_checked = bags_checked + 1
        calculate_coin(current_coin)
    else:
        if current_coin in valid_coins:
            print("Make sure you specify the value with a '£' or 'p'")
        else:
            print("Invalid coin")

    file = open("log_coin", "a")
    file.write(f"{name}, {current_bag_weight}, {bags_checked}\n")
    file.close()
    file = open("log_coin", "r")
    text = file.readlines()
    print(text)
    file.close()