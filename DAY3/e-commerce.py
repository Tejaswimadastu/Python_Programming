def add_product(cart):
    pro=input("Enter product to add ")
    cart.append(pro)
    print(f"{pro} added to cart ")
def remove_product(cart):
    pro=input("Enter product to remove ")
    if pro in cart:
        cart.remove(pro)
        print(f"{pro} removed from cart ")
    else:
        print("Product not found ")
def search_product(cart):
    pro=input("Enter product to search ")
    if pro in cart:
        print(f"{pro} found in cart ")
    else:
        print(f"{pro} not found in cart ")
def display_cart(cart):
    print("Cart: ",cart)
def count_product(cart):
    print("Count of products ",len(cart))
def sort_product(cart):
    cart.sort()
    print("Sort alphabetically ",cart)
def clear_product(cart):
    print("Clear cart ",cart.clear())

def ecommerce():
    cart=[]
    while True:
        print("1.Add product\n2.Remove product\n3.Search product\n4.Display cart\n5.Count Product\n6.Sort\n7.clear\n8.Exit")
        ch=int(input("Enter your choice "))
        if ch==1:
            add_product(cart)
        elif ch==2:
            remove_product(cart)
        elif ch==3:
            search_product(cart)
        elif ch==4:
            display_cart(cart)
        elif ch==5:
            count_product(cart)
        elif ch==6:
            sort_product(cart)
        elif ch==7:
            clear_product(cart)
        elif ch==8:
            print("Exiting...")
            break
        else:
            print("Invalid ")
ecommerce()
