import customtkinter as ctk
from PIL import Image
import os
from collections import Counter

# Create the main window
root = ctk.CTk()
root.geometry("600x600")
root.title("Café Del-Sol")

# List to store the ordered items
order_list = []

# Function to display the welcome page
def welcome_page(root):

    # Create a frame for the welcome page
    frame = ctk.CTkFrame(master=root,
                         width=350,
                         height=550,
                         fg_color="#C7DEA4"
                         )
    frame.pack(pady=40,
               padx=50,
               fill="both",
               expand=True
               )

    # Create "Welcome to Café Del-Sol" label
    label = ctk.CTkLabel(master=frame,
                         font=("beautiful barbies", 30),
                         text="Welcome to Café Del-Sol"
                         )
    label.pack(pady=18)

    # Create "Are you ready to order?" label
    label1 = ctk.CTkLabel(master=frame,
                          font=("Sweetie Bubble Gum", 25),
                          text="Are you ready \n to order?"
                          )
    label1.pack(pady=50)

    # Create "Menu" button
    button = ctk.CTkButton(master=frame,
                           command=lambda: menu(frame),
                           text="Menu",
                           font=("Sweetie Bubble Gum", 16),
                           fg_color="#75965A",
                           corner_radius=12,
                           width=80,
                           height=28,
                           hover_color="#577046"
                           )
    # Attach the "menu" function to the button
    button.pack(pady=10)

    # Add a cute sloth image
    '''image_path = os.path.join(os.path.dirname(__file__), 'Download_Cute_sloth_loves_coffee_cartoon__vector_illustration_for_free-removebg-preview.png')
    image = ctk.CTkImage(light_image=Image.open(image_path), size=(300, 300))
    image_label = ctk.CTkLabel(frame, image=image, text='')
    image_label.pack(pady=60)
    '''
    # The cute sloth is commented out since its source is only available on my own laptop so it wouldn't cause any errors

# Function to add an item to the order list
def add_item(radiobutton_var):

    # Append the selected item to the order_list
    order_list.append(radiobutton_var.get())
    

# Function to update the cart display
def update_cart(frame_order):

    # Remove all widgets from the frame_order
    for widget in frame_order.winfo_children():
        widget.destroy()
    
    # Create a label indicating "Your Cart:"
    label_cart = ctk.CTkLabel(master=frame_order,
                              font=("Sweetie Bubble Gum", 18),
                              text="Your Cart:",
                              text_color="#75965A"
                              )
    label_cart.pack(pady=5, padx=65)

    # Create a button to update the cart
    button_updateCart = ctk.CTkButton(master=frame_order,
                                      command=lambda: update_cart(frame_order),
                                      text="Update Cart",
                                      font=("Sweetie Bubble Gum", 16),
                                      fg_color="#75965A",
                                      corner_radius=12,
                                      width=80,
                                      height=30,
                                      hover_color="#577046"
                                      )
    button_updateCart.pack(pady=5)

    # Create a dictionary with the count of each item in the order_list
    order_list_menu = dict(Counter(order_list))

    # Display each item in the cart along with its count and price
    for item in order_list_menu.keys():
        # Create a label for each item in the cart
        label = ctk.CTkLabel(master=frame_order,
                              font=("Peach Cake", 18),
                              text=f"{order_list_menu[item]}- {item[0]}: ${item[1]:.2f}",
                              text_color="#75965A"
                              )
        label.pack(pady=2)






# Command for the Menu button
def menu(frame):
    # Remove the elements from the welcome page
    for widget in frame.winfo_children():
        widget.destroy()

    # Create a frame for the menu
    frame_menu = ctk.CTkFrame(master=root,
                               width=300,
                               height=500,
                               fg_color="#d9f4d4"
                               )
    frame_menu.place(x=60,
                     y=50
                     )

    # Create a frame for the order
    frame_order = ctk.CTkFrame(master=root,
                                width=200,
                                height=500,
                                fg_color="#d9f4d4"
                                )
    frame_order.place(x=320,
                      y=50
                      )

    # Create a label indicating "Your Cart:"
    label_cart = ctk.CTkLabel(master=frame_order,
                              font=("Sweetie Bubble Gum", 18),
                              text="Your Cart:",
                              text_color="#75965A"
                              )
    label_cart.pack(pady=5, padx=65)

    # Create a button to update the cart
    button_updateCart = ctk.CTkButton(master=frame_order,
                                      command=lambda: update_cart(frame_order),
                                      text="Update Cart",
                                      font=("Sweetie Bubble Gum", 16),
                                      fg_color="#75965A",
                                      corner_radius=12,
                                      width=80,
                                      height=30,
                                      hover_color="#577046"
                                      )
    button_updateCart.pack(pady=5)

    # Create a label for Coffee
    label2 = ctk.CTkLabel(master=frame_menu,
                          font=("Sweetie Bubble Gum", 18),
                          text="Coffee:"
                          )
    label2.pack(pady=5)

    # Create a list of drinks with their names and prices
    drink_items = [("Mocha", 5),
                   ("Latte", 6),
                   ("Espresso", 3),
                   ("Caramel Macchiato", 5.5),
                   ]

    # Create a variable for radio buttons
    radiobutton_var = ctk.Variable(value=0)

    # Create radio buttons for each drink item
    for item in drink_items:
        radiobutton = ctk.CTkRadioButton(master=frame_menu,
                                         variable=radiobutton_var,
                                         value=item,
                                         text=f"{item[0]}, ${item[1]:.2f}",
                                         text_color="#577046",
                                         font=("Peach Cake", 20),
                                         fg_color="#75965A",
                                         hover_color="#577046",
                                         radiobutton_width=12,
                                         radiobutton_height=12,
                                         )
        radiobutton.pack(pady=5, padx=10)

    # Create a button to add the selected drink item to the cart
    button_addItem = ctk.CTkButton(master=frame_menu,
                                   command=lambda: add_item(radiobutton_var),
                                   text="Add Item",
                                   font=("Sweetie Bubble Gum", 16),
                                   fg_color="#75965A",
                                   corner_radius=12,
                                   width=80,
                                   height=30,
                                   hover_color="#577046"
                                   )
    button_addItem.pack(pady=5)

    # Create a label for Baked Goods
    label2 = ctk.CTkLabel(master=frame_menu,
                          font=("Sweetie Bubble Gum", 18),
                          text="Baked Goods:"
                          )
    label2.pack(pady=5)

    # Create a list of baked goods with their names and prices
    baked_goods_items = [["Croissant", 4.5],
                         ["Lemon Tart", 6],
                         ["Brownie", 3],
                         ["Red Velvet Cake", 4.75]
                         ]

    # Create a variable for radio buttons
    radiobutton_var1 = ctk.Variable(value=0)

    # Create radio buttons for each baked goods item
    for item in baked_goods_items:
        radiobutton = ctk.CTkRadioButton(master=frame_menu,
                                         variable=radiobutton_var1,
                                         value=item,
                                         text=f"{item[0]}, ${item[1]:.2f}",
                                         text_color="#577046",
                                         font=("Peach Cake", 20),
                                         fg_color="#75965A",
                                         hover_color="#577046",
                                         radiobutton_width=12,
                                         radiobutton_height=12,
                                         )
        radiobutton.pack(pady=5, padx=10)

    # Create a button to add the selected baked goods item to the cart
    button_addItem = ctk.CTkButton(master=frame_menu,
                                   command=lambda: add_item(radiobutton_var1),
                                   text="Add Item",
                                   font=("Sweetie Bubble Gum", 16),
                                   fg_color="#75965A",
                                   corner_radius=12,
                                   width=80,
                                   height=30,
                                   hover_color="#577046"
                                   )
    button_addItem.pack(pady=5)

    # Create a button to place the order and proceed to additionals
    button_placeOrder = ctk.CTkButton(master=frame_menu,
                                      text="Place Order",
                                      font=("Sweetie Bubble Gum", 16),
                                      fg_color="#75965A",
                                      corner_radius=14,
                                      width=100,
                                      height=40,
                                      hover_color="#577046",
                                      command=lambda: additionals(frame, frame_order, frame_menu)
                                      )
    button_placeOrder.pack(pady=10)



def additionals(frame, frame_order, frame_menu):

    # Destroy the frames for order and menu
    frame_order.destroy()
    frame_menu.destroy()

    # Clear the widgets in the current frame
    for widget in frame.winfo_children():
        widget.destroy()

    # Create a label asking if the customer wants to add additionals
    label_adtn = ctk.CTkLabel(master=frame,
                              font=("Sweetie Bubble Gum", 25),
                              text="Would you like to add\nany additionals\nto your coffee?"
                              )
    label_adtn.pack(pady=10)

    # Create labels and option menus for different additionals: Milk, Toppings, Espresso Shot, Syrup
    label_1 = ctk.CTkLabel(master=frame,
                           font=("Sweetie Bubble Gum", 18),
                           text="Milk:",
                           text_color="#577046"
                           )
    label_1.pack(pady=0)

    milk_choice = ctk.CTkOptionMenu(master=frame,
                                    values=["2% Milk (Standard)", "Almond Milk", "Heavy Cream", "Vanilla Sweet Cream", "Lactose-Free Beverage"],
                                    width=140,
                                    height=28,
                                    corner_radius=8,
                                    font=("Peach Cake", 18),
                                    fg_color="#A7BA89",
                                    button_color="#9CB873",
                                    button_hover_color="#77895b",
                                    dropdown_fg_color="#A7BA89",
                                    dropdown_hover_color="#77895b",
                                    dropdown_text_color="#577046",
                                    text_color="#577046",
                                    dropdown_font=("Peach Cake", 18),
                                    )
    milk_choice.pack(pady=8, padx=10)
    milk_choice.set("Milk Options:")

    label_2 = ctk.CTkLabel(master=frame,
                           font=("Sweetie Bubble Gum", 18),
                           text="Toppings:",
                           text_color="#577046"
                           )
    label_2.pack(pady=0)

    topping_choice = ctk.CTkOptionMenu(master=frame,
                                        values=["Milk Foam (Standard)", "Caramel Drizzle", "Whipped Cream", "Chocolate Curling", "Cinnamon Dolce Sprinkles"],
                                        width=140,
                                        height=28,
                                        corner_radius=8,
                                        font=("Peach Cake", 18),
                                        fg_color="#A7BA89",
                                        button_color="#9CB873",
                                        button_hover_color="#77895b",
                                        dropdown_fg_color="#A7BA89",
                                        dropdown_hover_color="#77895b",
                                        dropdown_text_color="#577046",
                                        text_color="#577046",
                                        dropdown_font=("Peach Cake", 18),
                                        )
    topping_choice.pack(pady=8, padx=10)
    topping_choice.set("Topping Options:")

    label_3 = ctk.CTkLabel(master=frame,
                           font=("Sweetie Bubble Gum", 18),
                           text="Espresso Shot:",
                           text_color="#577046"
                           )
    label_3.pack(pady=0)

    espresso_choice = ctk.CTkOptionMenu(master=frame,
                                        values=["Signature Espresso Roast (Standard)", "Blonde Espresso Roast", "Decaf Espresso Roast"],
                                        width=140,
                                        height=28,
                                        corner_radius=8,
                                        font=("Peach Cake", 18),
                                        fg_color="#A7BA89",
                                        button_color="#9CB873",
                                        button_hover_color="#77895b",
                                        dropdown_fg_color="#A7BA89",
                                        dropdown_hover_color="#77895b",
                                        dropdown_text_color="#577046",
                                        text_color="#577046",
                                        dropdown_font=("Peach Cake", 18),
                                        )
    espresso_choice.pack(pady=8, padx=10)
    espresso_choice.set("Espresso Shot Options:")

    label_4 = ctk.CTkLabel(master=frame,
                           font=("Sweetie Bubble Gum", 18),
                           text="Syrup:",
                           text_color="#577046"
                           )
    label_4.pack(pady=0)

    syrup_choice = ctk.CTkOptionMenu(master=frame,
                                      values=["Vanilla Syrup (Standard)", "Caramel Syrup", "Chestnut Syrup", "Pistachio Syrup", "Cinnamon Dolce Syrup", "Hazelnut Syrup"],
                                      width=140,
                                      height=28,
                                      corner_radius=8,
                                      font=("Peach Cake", 18),
                                      fg_color="#A7BA89",
                                      button_color="#9CB873",
                                      button_hover_color="#77895b",
                                      dropdown_fg_color="#A7BA89",
                                      dropdown_hover_color="#77895b",
                                      dropdown_text_color="#577046",
                                      text_color="#577046",
                                      dropdown_font=("Peach Cake", 18),
                                      )
    syrup_choice.pack(pady=8, padx=10)
    syrup_choice.set("Syrup Options:")

    # Create a button to save the chosen additionals and proceed to the Daily Delish page
    button_additionals = ctk.CTkButton(master=frame,
                                       command=lambda: daily_delish(frame),
                                       text="Save Choices",
                                       font=("Sweetie Bubble Gum", 16),
                                       fg_color="#75965A",
                                       corner_radius=12,
                                       width=80,
                                       height=30,
                                       hover_color="#577046"
                                       )
    button_additionals.pack(pady=20)



def daily_delish(frame):

    # Destroy all widgets in the current frame
    for widget in frame.winfo_children():
        widget.destroy()

    # Create a label asking if the customer wants a Daily Delish
    label1 = ctk.CTkLabel(master=frame,
                          font=("Sweetie Bubble Gum", 25),
                          text="Would you like\na Daily Delish?"
                          )
    label1.pack(pady=25)

    # Create a list of Daily Delish items with their prices
    drink_items = [["Hummus & Crackers", 5],
                   ["Ham & Swiss on Baguette", 6],
                   ["Crispy Grilled Cheese", 3],
                   ["Chicken & Bacon on Brioche", 5.5],
                   ]

    # Use a variable to track the selected item
    radiobutton_var = ctk.Variable(value=0)

    # Create radio buttons for each Daily Delish item
    for item in drink_items:
        radiobutton = ctk.CTkRadioButton(master=frame,
                                          variable=radiobutton_var,
                                          value=item,
                                          text=f"{item[0]}, ${item[1]:.2f}",
                                          text_color="#577046",
                                          font=("Peach Cake", 18),
                                          fg_color="#75965A",
                                          hover_color="#577046",
                                          radiobutton_width=12,
                                          radiobutton_height=12,
                                          )
        radiobutton.pack(pady=5, padx=10)

    # Create a button to add the selected Daily Delish item to the order list
    button_addItem = ctk.CTkButton(master=frame,
                                   command=lambda: add_item(radiobutton_var),
                                   text="Add Item",
                                   font=("Sweetie Bubble Gum", 16),
                                   fg_color="#75965A",
                                   corner_radius=12,
                                   width=80,
                                   height=30,
                                   hover_color="#577046"
                                   )
    button_addItem.pack(pady=10)

    # Create a button to finalize the order and proceed to the receipt
    button_finalizeOrder = ctk.CTkButton(master=frame,
                                          text="Finalize Order",
                                          font=("Sweetie Bubble Gum", 16),
                                          fg_color="#75965A",
                                          corner_radius=14,
                                          width=100,
                                          height=40,
                                          hover_color="#577046",
                                          command=lambda: receipt(frame, order_list)
                                          )
    button_finalizeOrder.pack(pady=25)



def receipt(frame, order_list):

    # Destroy all widgets in the current frame
    for widget in frame.winfo_children():
        widget.destroy()

    # Calculate the total amount of the order
    total = sum(item[1] for item in order_list)

    # Create a label for the receipt header
    label1 = ctk.CTkLabel(master=frame,
                          font=("Sweetie Bubble Gum", 25),
                          text="Your Receipt"
                          )
    label1.pack(pady=25)

    # Count occurrences of each item in the order
    order_list_menu = dict(Counter(order_list))

    # Display each item and its quantity in the receipt
    for item in order_list_menu.keys():
        label = ctk.CTkLabel(master=frame,
                             font=("Peach Cake", 18),
                             text=f"{order_list_menu[item]}- {item[0]}: ${item[1]:.2f}",
                             text_color="#75965A"
                             )
        label.pack(pady=2)

    # Create a label for the total amount of the order
    label2 = ctk.CTkLabel(master=frame,
                          font=("Peach Cake", 18),
                          text=f"Total Amount: ${total:.2f}")
    label2.pack(pady=10)

    # Create a label asking the user to enter the tip percentage
    label2 = ctk.CTkLabel(master=frame,
                          font=("Peach Cake", 18),
                          text="Enter Tip Percentage:")
    label2.pack(pady=10)

    # Create an entry widget for the user to input the tip percentage
    tip_percentage = ctk.DoubleVar(value=0)
    tip_entry = ctk.CTkEntry(master=frame,
                             textvariable=tip_percentage
                             )
    tip_entry.pack(pady=5)

    # Create a button to update the final amount with the tip
    button_updateAmount = ctk.CTkButton(master=frame,
                                        text="Update Amount",
                                        font=("Peach Cake", 18),
                                        command=lambda: updateAmount(total, tip_percentage, label3),
                                        fg_color="#75965A",
                                        corner_radius=12,
                                        width=80,
                                        height=30,
                                        hover_color="#577046"
                                        )
    button_updateAmount.pack(pady=5)

    # Create a label for the final amount after applying the tip
    label3 = ctk.CTkLabel(master=frame,
                          font=("Peach Cake", 18),
                          text=f"Final Amount: ${total:.2f}")
    label3.pack(pady=25)

    # Create a label for thanking the customer
    label4 = ctk.CTkLabel(master=frame,
                          font=("beautiful barbies", 18),
                          text="Thank you, see you soon!"
                          )
    label4.pack(pady=12)

# Create a function for updating the total amount button
def updateAmount(total, tip_percentage, label3):
    # Get the tip percentage from the entry widget
    tip_percentage = tip_percentage.get()

    # Calculate the final amount by adding the tip
    total = (1 + tip_percentage/100) * total

    # Update the label with the final amount
    label3.configure(text=f"Final Amount: ${total:.2f}")



# Run the main program
welcome_page(root)



# Run the window
root.mainloop()
