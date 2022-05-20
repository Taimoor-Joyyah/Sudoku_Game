def select_numeric_option(num_range: (int, int), input_prompt: str | None,
                          menu_prompt: str | None, invalid_prompt: str | None):
    if menu_prompt:
        print(menu_prompt)
    while True:
        if input_prompt:
            opt = input(input_prompt)
        else:
            opt = input()
        if opt and opt.isnumeric() and num_range[0] <= int(opt) <= num_range[1]:
            return int(opt)
        else:
            if invalid_prompt:
                print(invalid_prompt)