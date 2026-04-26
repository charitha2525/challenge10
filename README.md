**About project**
This project analyzes student academic data and studies how shallow copy and deep copy behave when changes are made to nested data structures. 
It also checks whether any data drift or copy failure occurs after mutation.

**Objective**
Generate random student data
Store data in nested dictionaries
Apply shallow copy and deep copy
Perform mutations on copied data
Analyze statistical changes using Pandas and NumPy
Detect data drift and copy failure

**What I Did**
Created student dataset using random values
Stored data as list of dictionaries with nested scores
Converted data into Pandas DataFrame
Applied mutation using roll number logic
Used NumPy for mean, median, and standard deviation
Calculated drift between original and modified data
Checked whether original data was affected

**Personalization Applied**
Roll Number used: 22
Formula used:
index = roll_number % 3
This decides which student records will be modified
It ensures different users get different outputs

**Technologies Used**
Python
Pandas
NumPy
Random module
Math module
Copy module

**Conclusion**

This project helped me understand how data behaves when copied in Python.
I learned that shallow copy can cause unintended changes in original data, while deep copy keeps data independent.
I also understood how statistical analysis can be used to detect changes in datasets.
