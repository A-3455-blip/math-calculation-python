def sub_calculation():
    sub=0
    while True:
        sub_input=input("Enter number to be subtracted:")
        if sub_input.lower()=='done':
            print(f'Value is {sub}')
            import main
            main.end_continue()
        else:
            try:
                sub=float(sub_input)
            except ValueError:
                print('you may be given incorrect input')
