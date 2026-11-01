# function named `update_file` that takes in two parameters: `import_file` and `remove_list`

def update_file(import_file, remove_list):
    # `with` statement to read in the initial contents of the file

    with open(import_file, "r") as file:

        # `.read()` to read the imported file and store it in a variable named `ip_addresses`

        ip_addresses = file.read()
        ip_addresses_new = []

    # `.split()` to convert `ip_addresses` from a string to a list

    ip_addresses = ip_addresses.split()

    for ip in ip_addresses:
        # If current element is NOT in `remove_list`,
        if not ip in remove_list:
            # then current element should be appended to `ip_addresses_new`


            ip_addresses_new.append(ip)





    # Converting `ip_addresses_new` back to a string so that it can be written into the text file

    ip_addresses_new = " ".join(ip_addresses_new)

    #`with` statement to rewrite the original file

    with open(import_file, "w") as file:

        # Rewriting the file, replacing its contents with `ip_addresses_new`

        file.write(ip_addresses_new)
        return ip_addresses_new


# Calling `update_file()` and passing in "allow_list.txt" and an list of IP addresses to be removed
if __name__ == "__main__":

    update_file("allow_list.txt", ["192.168.25.60", "192.168.140.81", "192.168.203.198"])
    
    # Build `with` statement to read in the updated file
    
    with open("allow_list.txt", "r") as file:
    # Read in the updated file and store the contents in `text`
    
        text = file.read()
    
    # Display the contents of `text`
    
    print(text)
    
