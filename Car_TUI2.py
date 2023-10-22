
LINE_WIDTH = 40

def display_separator(msg=""):
    dashes = "-" * LINE_WIDTH
    print(f"{dashes}\n{msg}\n{dashes}")

def display_completed_message():
    display_separator("Process completed!")

def display_error_message(msg):
    print(f"Error! {msg}\n")

def started(msg=""):
    display_separator(msg)

def menu():
    print("""
    What operation would you like to perform? Please make a selection:
  
    View car information
    [A] Access a car record by ID.
    [B] Access cars by their cylinder number.
    [C] Access cars by body category.
    [D] Access basic information of a car by ID...
  
    Access car names and sales records
    [E] Access car names alphabetically.
    [F] Access total sales of cars based on body type.
    [G] Access the 5 most expensive cars based on body type.
    [H] Access mean sales for each car name.
  
    Access visualization of car records
    [I] View a bar chart of cars per fuel system.
    [J] View a graph of the horsepower for the 5 cheapest cars.
    [K] To exit the program
    """)
    selection = input("Your selection is: ").strip().lower()
    return selection

def started(msg=""):
    display_separator(msg)