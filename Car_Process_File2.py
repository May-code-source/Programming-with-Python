import Car_TUI2 as TUI
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define function to retrieve car details based on car ID
def access_car_record_by_id(file):
    TUI.display_separator("Showing Car Details")
    try:
        car_id = int(input("Enter car ID: "))
        if 2 <= car_id <= 206:
            car_details = file[car_id]
            print(f"Find below your information:\n\n {car_details}")
        else:
            print("Car ID should be between 2 and 206.")
    except ValueError:
        print("Invalid input. Please enter a valid number for car ID.")
    TUI.display_completed_message()

# Define function to retrieve car details based on cylinder number
def access_car_record_by_cylinder_no(file):
    TUI.display_separator("Showing Car Details")
    cylinder_no = input("Enter cylinder number: ")
    car_cylinder_details = [f for f in file if f[13] == cylinder_no]
    print(f"Find below your information:\n\n {car_cylinder_details}")
    TUI.display_completed_message()

# Define function to retrieve car details based on car body category
def access_car_by_body_category(file):
    TUI.display_separator("Showing Car Details")
    car_body = input("Enter body type: ")
    car_body_details = [f for f in file if f[4] == car_body]
    print(f"Find below your information:\n\n {car_body_details}")
    TUI.display_completed_message()

# Define function to retrieve basic car details based on car ID
def access_basic_car_information(file):
    TUI.display_separator("Showing Car Details")
    try:
        car_id = int(input("Enter car ID between 2 - 206: "))
        if 2 <= car_id <= 206:
            car_info = file[car_id][1:5]
            print(f"Find below your information:\n\n {car_info}")
        else:
            print("Car ID should be between 2 and 206.")
    except ValueError:
        print("Invalid input. Please enter a valid number for car ID.")
    TUI.display_completed_message()

# Define function to access car names alphabetically
def access_car_names_alphabetically(file):
    TUI.display_separator("Showing Car Details")
    car_arr = input("Type 'order' to access cars in alphabetical order: ")
    if car_arr.lower() == 'order':
        car_names = [f[1] for f in file]
        sorted_car_names = sorted(car_names)
        print(f"Find below your information:\n\n {sorted_car_names}")
    TUI.display_completed_message()

# Define function to access total sales of cars by car body
def access_total_sales_of_cars_by_car_body(file):
    TUI.display_separator("Showing total sales of cars for each car body")
    file_frame = pd.read_csv("CarPrice.csv")
    car_sales = input("Type 'total' to access the total sales for each car body:\n\n ")
    if car_sales.lower() == 'total':
        file_frame_grouped = file_frame.groupby(['carbody'])['price'].sum().reset_index()
        print(f"Find below your information:\n\n {file_frame_grouped}")
    TUI.display_completed_message()

# Define function to access the 5 most expensive cars based on body type
def access_5_most_expensive_cars_by_body_type(file):
    TUI.display_separator("Showing 5 most expensive cars based on body type")
    file_frame = pd.read_csv("CarPrice.csv")
    top_car = input("Type 'top sale' to access the 5 most expensive cars for each body type:\n\n ")
    if top_car.lower() == 'top sale':
        sorted_sale = file_frame.sort_values(by=["carbody", "price"], ascending=[1, 0])
        top_5_expensive_cars = sorted_sale.groupby('carbody').head(5)
        print(f"Top 5 most expensive cars per body type:\n\n {top_5_expensive_cars}")
    TUI.display_completed_message()

# Define function to access mean sales for each car name
def access_mean_sales_of_each_car(file):
    TUI.display_separator("Showing mean sales of each car type")
    file_frame = pd.read_csv("CarPrice.csv")
    mean_sales = input("Type 'average' to access the mean sales for each car name:\n\n ")
    if mean_sales.lower() == 'average':
        mean_sales_data = file_frame.groupby('CarName')['price'].mean().reset_index()
        print(f"Find below your information:\n\n {mean_sales_data}")
    TUI.display_completed_message()

def view_bar_chart_of_car_per_fuel_system(file):
    #calling TUI function
    TUI.display_separator("Showing bar chart of car vs fuel system")
    #loading file into pandas dataframe
    file_frame = pd.read_csv("CarPrice.csv")
    chart = input("Type 'display' to view information on the cars per fuel system:\n\n ")
    #using value_count function to determine the number of cars per fuel system 
    fuel_sys_sort  = file_frame["fuelsystem"].value_counts()
    #adding fuel_system and car_no to list for plotting graph 
    fuel_system = fuel_sys_sort.tolist()
    car_no = fuel_sys_sort.index.tolist()
    #plotting bar chart 
    fig = plt.figure() 
    plt.bar(car_no, fuel_system)
    plt.xlabel("Fuel System")
    plt.ylabel("No. of Cars")
    plt.title("Number of Cars per Fuel System")
    plt.show()
    TUI.display_completed_message()
    
def view_graph_of_horsepower_of_5_cheapest_car(file):
    TUI.display_separator("Showing graphical information")
    #loading file into pandas dataframe
    file_frame = pd.read_csv("CarPrice.csv")
    plot = input("Type 'display' to view information on the horse power of the 5 cheapest cars :\n\n ")
        
    #sort data by cheapest price 
    file_plot = file_frame.sort_values(by=["price"], ascending=True) [['CarName','horsepower']]
    #Create a new dataframe for 5 cheapest cars
    plot_5 = file_plot.head(5)
        
    fig, ax = plt.subplots(figsize=(15, 12))
    plt.suptitle("Horsepower of 5 Cheapest Cars ", fontsize=18, y=0.95)
    #Get the car name from the sorted dataframe and covert to list
    cars = plot_5['CarName'].tolist()
        
    #Get the horse power from the sorted dataframe and covert to list
    horsepower = plot_5['horsepower'].tolist()
        
    #loop through the length of car list in dataframe of 5 cheapest cars
    for i in range(len(plot_5['CarName'])):
        #iteratively add new subplot
        ax = plt.subplot(1, 5, i + 1)
        #filter df and plot horsepower on the new subplot axis
        ax.bar(cars[i],horsepower[i])
        #format chart 
        ax.set_ylim(0,100)
    #calling TUI function
    TUI.display_completed_message()
