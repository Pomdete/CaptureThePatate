with open('petite_frappe_2.txt', 'r') as file:
    data = file.read()

# Split the data into lines
lines = data.split('\n')
print("Number of lines:", len(lines))


current_pressed_keys = []
input_sequence = []
# Iterate through each line of the key logger
for line in lines:
    # Check if the line starts with "key press"
    if line.startswith("key press"):
        key = line.split()[2]
        current_pressed_keys.append(key)
    elif line.startswith("key release"):
        key = line.split()[2]
        if key in current_pressed_keys:
            input_sequence.append(current_pressed_keys.copy())
            current_pressed_keys.remove(key)

# Print the input sequence
for i, keys in enumerate(input_sequence):
    print(f"Input sequence {i + 1}: {keys}")
