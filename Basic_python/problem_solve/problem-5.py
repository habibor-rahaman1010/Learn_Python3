import pyautogui

# Get the number of rows for the pyramid from the user
num_rows = int(input("Enter the number of rows for the pyramid: "))

# Define the starting position for drawing the pyramid
start_x = 500
start_y = 500

# Set the distance between each asterisk
spacing = 20

# Set the initial x and y positions
x = start_x
y = start_y

# Loop through each row and draw the pyramid
for row in range(num_rows):
    # Calculate the number of asterisks for the current row
    num_asterisks = (row * 2) + 1

    # Calculate the starting x position for the current row
    row_start_x = x - (num_asterisks * spacing // 2)

    # Move the mouse to the starting position of the current row
    pyautogui.moveTo(row_start_x, y)

    # Loop through each asterisk in the current row and draw it
    for _ in range(num_asterisks):
        pyautogui.click()  # Simulate a mouse click to draw an asterisk
        pyautogui.move(spacing, 0)  # Move the mouse horizontally to the next position

    # Move the mouse to the next row
    y -= spacing

# Move the mouse to a different location after drawing the pyramid
pyautogui.moveTo(start_x, start_y + (num_rows * spacing))
