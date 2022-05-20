def select_numeric_option(num_range: (int, int), input_prompt: str | None,
                          menu_prompt: str | None, invalid_prompt: str | None) -> int:
    """
    :rtype:
        int
    :param num_range:
        Range of valid numbers for input,  start and end number
    :param input_prompt:
        specify message to be printed before taking input value
    :param menu_prompt:
        specify menu to be displayed one time on start
    :param invalid_prompt:
        specify message displayed after an invalid input
    :return:
        Numeric option selected in int type
    """

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
