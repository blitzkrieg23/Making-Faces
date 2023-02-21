def convert(string):
    if not string:
        return "Error: Input string is empty"
    elif ":)" not in string and ":(" not in string:
        return "Error: Input string does not contain ':)' or ':('"
    else:
        converted_string = string.replace(":)", "🙂").replace(":(", "🙁")
        return converted_string

def main():
    user_input = input("Please enter a string: ")
    converted_input = convert(user_input)
    print(converted_input)

main()