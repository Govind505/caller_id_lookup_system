import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Data structure to store caller information
caller_database = {}

# Function to add caller information
def add_caller():
    name = input("Enter caller's name: ")
    number = input("Enter caller's number: ")
    caller_database[number] = name
    print("Caller added successfully!")

# Function to view all callers
def view_callers():
    if caller_database:
        print("List of Callers:")
        for number, name in caller_database.items():
            print(f"Name: {name}, Number: {number}")
    else:
        print("No callers in the database.")

# Function to search for a caller by number
def search_caller():
    number = input("Enter caller's number to search: ")
    if number in caller_database:
        print(f"Caller's name: {caller_database[number]}")
    else:
        print("Caller not found.")

# Function to update caller information
def update_caller():
    number = input("Enter caller's number to update: ")
    if number in caller_database:
        name = input("Enter updated name: ")
        caller_database[number] = name
        print("Caller information updated successfully!")
    else:
        print("Caller not found.")

# Function to delete caller information
def delete_caller():
    number = input("Enter caller's number to delete: ")
    if number in caller_database:
        del caller_database[number]
        print("Caller information deleted successfully!")
    else:
        print("Caller not found.")

# Function to plot a graph of caller statistics
def plot_caller_statistics():
    if caller_database:
        df = pd.DataFrame(list(caller_database.items()), columns=['Number', 'Name'])
        name_lengths = df['Name'].apply(len)
        plt.figure(figsize=(8, 6))
        plt.bar(df['Number'], name_lengths)
        plt.xlabel('Caller Number')
        plt.ylabel('Name Length')
        plt.title('Name Length of Callers')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        print("No data to plot.")

# Main menu function
def main_menu():
    while True:
        print("\n----- Caller ID Lookup System -----")
        print("1. Add Caller")
        print("2. View Callers")
        print("3. Search Caller")
        print("4. Update Caller")
        print("5. Delete Caller")
        print("6. Plot Caller Statistics")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_caller()
        elif choice == '2':
            view_callers()
        elif choice == '3':
            search_caller()
        elif choice == '4':
            update_caller()
        elif choice == '5':
            delete_caller()
        elif choice == '6':
            plot_caller_statistics()
        elif choice == '7':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point of the program
if __name__ == "__main__":
    main_menu()
