
ACL Management Algorithm Module

This repository contains my own python module which can be imported and used by developers for automating cybersecurity tasks such as Access Control List (ACL) Management.

This module allows the users to pass as arguments a text file containing a list of currently allowed IP addresses that can access restricted data and a list of IP addresses that need to be removed.
The module automates the process of removing the required IP addresses from the text file and printing the updated allowed IP addresses as output.

How to import and use this module?
1. Save this acl_management_algorithm.py file to your project directory in your computer.
2. Use 'import acl_management_algorithm' at the top of your project code file.
3. Call the update_file() function with valid arguments in your code.
4. The current allowed IPs must be in the form of a **single string** separated by **blank spaces** and the list of IPs to be removed should be a **list** 
