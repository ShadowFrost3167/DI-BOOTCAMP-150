import sqlite3

connection = sqlite3.connect("customer.db")

#create a cursor
c = connection.cursor()

c.execute("SELECT * FROM customers")
# c.fetchone()
# c.fetchmany(3)
print(c.fetchall())
#query the db to see whats there and print it so it displays in terminal

# many_customers = [
#     ('George', 'Lopez', 'glo@gmail.com'),
#     ('Ariel', 'Cane', 'acane@yahoo.com'),
#     ('Judah', 'Polak', 'saj2@yahoo.com')
#     ]

# c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)
#input a lot of info ^^

# c.execute("INSERT INTO customers VALUES('George', 'Lopez', 'glo@gmail.com')")
#input info singularly ^^^

#create a table
# c.execute(""""CREATE TABLE customers (
#           first_name text,
#           last_name text,
#           email text
#           )
#     """")
#without 6 "" you need to write it all on one line, less readable

print("success")

connection.commit()
#comit our command

connection.close()
#close connection