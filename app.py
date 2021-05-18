import sqlite3 as sql3
import pandas as pd


MENU_PROMPT = """\n -- Money Tracker App --

Please choose one of these options
\t1) Add Transaction (insert)
\t2) See transaction Group by items
\t3) Remove Transaction by id
\t4) Update /Correct Transaction
\t5) Write the data to a text file
\t6) Exit

Your selection:"""


INSERT_QUERY = "INSERT INTO transactions (description, amount) VALUES (?,?)"

def add_item(cursor):
    print("*" * 20)
    desc = input("Enter your transaction name: ").capitalize()
    amount = float(input("Enter the transaction amount: "))
    print("*" * 20, '')
    print("{} number of row(s) updated\n".format(cursor.rowcount))
    items = (desc, amount)
    cursor.execute(INSERT_QUERY, items)

def trans_groupby_name(cursor):
    items = {}
    for id, desc, amount in cursor.execute("SELECT * FROM transactions"):
        items[id] = [desc, amount]

    df = pd.DataFrame.from_dict(items,orient='index')
    df.columns = ["description","amount"]

    df = df.groupby(['description']).sum()
    print("-" * 20)
    print(df)
    print("-" * 20, '\n')

    while input("Press any key to continue:\n"):
        break

def remove_trans(cursor):
    DELETE_QUERY = "DELETE FROM transactions WHERE id = ?"
    items = {}
    for id, desc, amount in cursor.execute("SELECT * FROM transactions"):
        items[id] = [desc, amount]

    df = pd.DataFrame.from_dict(items,orient='index')
    df.columns = ["description","amount"]

    n = 0
    while (user_input := input("Please type 'stop' to exit: (or press Enter to continue) ")) !='stop':
        print()
        print(df[n:n+5])
        n += 5
        print('-'*20)

        query = input("Enter the id that you want to delete:(or press Enter to continue) ")
        if query != "":
            query = int(query)
            cursor.execute(DELETE_QUERY, (query,))
            print(cursor.rowcount, "row(s) deleted. ")









def data_export_txt(text_file,cursor):
    with open(text_file, "w+") as file:
        file.write("ID, Description, Amount\n")

        for i in cursor.execute("SELECT * FROM transactions").fetchall():
            file.write("{}, {}, {} \n".format(i[0], i[1], i[2]))


def main():
    conn = sql3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS transactions(id INTEGER PRIMARY KEY, Description TEXT NOT NULL, Amount FLOAT NOT NULL)")
    cursor.execute("PRAGMA table_info(tablename)")


    while (user_input := input(MENU_PROMPT)) != "6":

        if user_input == "1":
            add_item(cursor)

        elif user_input == "2":
            trans_groupby_name(cursor)

        elif user_input == "3":
            remove_trans(cursor)

        elif user_input == "4":
            pass

        elif user_input == "5":
            data_export_txt("user.txt", cursor)
        else:
            print("Invalid input. ")

    cursor.connection.commit()
    #conn.commit(), cursor.connection is perferable
    conn.close()

if __name__ == "__main__":
	main()
