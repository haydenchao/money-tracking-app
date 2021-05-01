import sqlite3 as sql3


MENU_PROMPT = """ -- Money Tracker App --

Please choose one of these options
1) Add Transaction (insert)
2) See transaction Group by items
3) Remove Transaction by id
4) Update /Correct Transaction
5) Write the data to a text file
6) Exit

Your selection:"""


INSERT_QUERY = "INSERT INTO transactions (description, amount) VALUES (?,?)"

def add_item(cursor):
    print("*" * 20)
    desc = input("Enter your transaction name: ")
    amount = float(input("Enter the transaction amount: "))
    print("*" * 20, '\n')
    items = (desc, amount)
    cursor.execute(INSERT_QUERY, items)


def data_export_txt(text_file,cursor):
    with open(text_file, "w+") as file:
        if file.readline == []:
            file.write("ID, Description, Amount\n")

        for i in cursor.execute("SELECT * FROM transactions").fetchall():
            file.write("{}, {}, {} \n".format(i[0], i[1], i[2]))


def main():
    conn = sql3.connect("data.db")
    cursor = conn.cursor()


    cursor.execute("CREATE TABLE IF NOT EXISTS transactions(id INTEGER PRIMARY KEY, Description TEXT NOT NULL, Amount FLOAT NOT NULL)")
    #cursor.execute("INSERT INTO transactions (Description, Amount) VALUES('Eating out', 12)")
    cursor.execute("PRAGMA table_info(tablename)")





    while (user_input := input(MENU_PROMPT)) != "6":

        if user_input == "1":
            add_item(cursor)

        elif user_input == "2":
            pass

        elif user_input == "3":
            pass

        elif user_input == "4":
            pass

        elif user_input == "5":
            data_export_txt("user.txt", cursor)
        else:
            print("Invalid input. ")


    conn.commit()
    conn.close()

if __name__ == "__main__":
	main()
