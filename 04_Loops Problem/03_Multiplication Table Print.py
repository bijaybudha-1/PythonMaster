# Multiplication Table Printer
# Problem: Print the multiplication table for a given up to 10, but skip the fifth iteration

multiplication_table = int(input("Enter a table of multiplication: "))

for table in range(1, 10 + 1):
    if table == 5:
        continue
    print(f'{multiplication_table} X {table} = {multiplication_table * table}')