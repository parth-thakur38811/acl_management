# Define a function named `update_file` that takes in two parameters: `import_file` and `remove_list`
# and combines the steps you've written in this lab leading up to this

def update_file(import_file, remove_list):
    # Build `with` statement to read in the initial contents of the file

    with open(import_file, "r") as file:

        # Use `.read()` to read the imported file and store it in a variable named `ip_addresses`

        ip_addresses = file.read()
        ip_addresses_new = []

    # Use `.split()` to convert `ip_addresses` from a string to a list

    ip_addresses = ip_addresses.split()

    # Build iterative statement
    # Name loop variable `element`
    # Loop through `ip_addresses`

    for ip in ip_addresses:

        # Build conditional statement
        # If current element is not in `remove_list`,

        if not ip in remove_list:
            # then current element should be appended to `ip_addresses_new`


            ip_addresses_new.append(ip)





    # Convert `ip_addresses_new` back to a string so that it can be written into the text file

    ip_addresses_new = " ".join(ip_addresses_new)

    # Build `with` statement to rewrite the original file

    with open(import_file, "w") as file:

        # Rewrite the file, replacing its contents with `ip_addresses_new`

        file.write(ip_addresses_new)


# Call `update_file()` and pass in "allow_list.txt" and a list of IP addresses to be removed

update_file("allow_list.txt", ["192.168.25.60", "192.168.140.81", "192.168.203.198"])

# Build `with` statement to read in the updated file

with open("allow_list.txt", "r") as file:
    # Read in the updated file and store the contents in `text`

    text = file.read()

# Display the contents of `text`

print(text)
