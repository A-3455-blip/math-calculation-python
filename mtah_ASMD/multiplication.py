def mul_calculation():
    multiplication=0
    while True:
        mul_input=input("Enter number to be subtracted:")
        if mul_input.lower()=='done':
            print(f'Value is {multiplication}')
            import main
            main.end_continue()
        else:
            try:
                multiplication=float(mul_input)
            except ValueError:
                print('you may be given incorrect input')
