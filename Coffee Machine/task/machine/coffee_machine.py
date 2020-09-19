# print("Starting to make a coffee")
#print("Grinding coffee beans")
#print("Boiling water")
#print("Mixing boiled water with crushed coffee beans")
#print("Pouring coffee into the cup")
#print("Pouring some milk into the cup")
#print("Coffee is ready!")
#
#
#print("STAGE 2")
#
#
#cups = int(input("Write how many cups of coffee you will need:"))
#water = int (cups)*(200)
#milk = int (cups)*(50)
#beans = int (cups)*(15)
#
#print("For"), cups, ("cups of coffee you will need:")
#print (water, "ml of water")
#print (milk, "ml of milk")
#print (beans, "g of coffee beans")


print("STAGE 3 - ENOUGH COFFEE FOR EVERYONE")


wgot = int(input("Write how many ml of water the coffee machine has:"))
mgot = int(input("Write how many ml of milk the coffee machine has:"))
cgot = int(input("Write how many grams of coffee the coffee machine has:"))
cwant = int(input("Write how many cups of coffee you will need:"))

water: int = 200
milk: int = 50
beans: int = 15

available: int = min(wgot//water, mgot//milk, cgot//beans)
more = available-cwant

if cwant == available:
    print('Yes, I can make that amount of coffee')
elif cwant < available:
    print("Yes, I can make that amount of coffee (and even", more, "more than that)")
elif cwant > available:
    print("No, I can make only", available, "cups of coffee")
