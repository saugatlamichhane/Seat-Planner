def get_two_digit_string(n):
    num_string = str(n)
    while len(num_string) < 2:
        num_string = "0"+num_string
    return num_string

if __name__ == "__main__":
    print(f"1 becomes {get_two_digit_string(1)}.")
    print(f"0 becomes {get_two_digit_string(0)}.")
    print(f"25 becomes {get_two_digit_string(25)}.")
