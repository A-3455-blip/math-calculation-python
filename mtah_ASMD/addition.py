"""you chosed addition......."""
"""ENter your number below"""
import main

def add_calculation():
    total=0
    while True:
        add_numbers=input("=")
        if add_numbers.lower()=='done':
            print(f"total is {total}")
            main.end_continue()
        elif add_numbers.lower()!='done':
            try:
                total+=float(add_numbers)
            except ValueError:
                print("Incorrect value")


       

