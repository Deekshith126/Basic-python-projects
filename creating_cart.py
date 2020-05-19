from IPython.display import clear_output
#global list variable
cart = []

# ACTIONS

# 1. Adding Items
def addItem(item):
    clear_output()
    cart.append(item)
    print('{} has been added'.format(item))

# 2. Remove Items
def removeItem(item):
    clear_output()
    
    try:
        cart.remove(item)
        print('{} has been removed'.format(item))
    except:
        print('Sorry! Unable to remove item')
		
# 3. Show Items
def showCart( ): 
    clear_output() 
    if cart:
        print("Here is your cart:") 
        for item in cart: 
            print( "- {}".format(item) ) 
    else: 
        print("Your cart is empty.")
		
# 4. Clearing Cart
def clearCart( ): 
    clear_output() 
    cart.clear() 
    print("Your cart is empty.")
	
# 5. Calling all actions

def main():
    done = False
    while not done:
        ans = input('quit/add/remove/show/clear: ').lower()
        if ans =='quit':
            showCart()
            print('Thanks for using our program')
            break
            done = True
        elif ans=='add':
            item = input('what you would like to add: ').title()
            addItem(item)
        elif ans=='remove':
            showCart()
            item = input('what you would like to remove: ').title()
            removeItem(item)
        elif ans=='show':
            showCart()
        elif ans=='clear':
            clearCart()
        else:
            print('Sorry that was no option')
			
# 6. FINAL-- Run the cart program
main()