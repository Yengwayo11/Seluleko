def print_heart_with_message(message):
    # Upper part of heart
    for row in range(9):
        for col in range(13):
            if ((row == 0 and col % 3 != 0) or
                (row == 1 and col % 3 == 0) or
                (row == 2) or
                (row == 3 and col in [0, 6])):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

    # Lower part of heart
    for row in range(11, -1, -1):
        print(" " * (12 - row), end="")
        print("* " * (row + 1))

    # Print the message centered below the heart
    print("\n" + message.center(20, " "))

# Call the function
print_heart_with_message("Happy Birthday Baba")
def print_heart_with_message(message):
    message_row = 6  # Row number where the message will be printed
    width = 55       # Total width of the heart
    for row in range(13):
        line = ""
        for col in range(width):
            dist1 = ((col - 13) ** 2 + (row - 4) ** 2) ** 0.5
            dist2 = ((col - 41) ** 2 + (row - 4) ** 2) ** 0.5
            if (row < 5 and (dist1 < 9 or dist2 < 9)) or \
               (row >= 5 and abs(col - width//2) <= (12 - row)):
                line += "*"
            else:
                line += " "
        
        if row == message_row:
            start = (width - len(message)) // 2
            line = line[:start] + message + line[start+len(message):]
        
        print(line)

# Call the function
print_heart_with_message("Happy Birthday Baba")
