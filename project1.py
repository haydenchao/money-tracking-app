import pandas as pd
import os
import tkinter as tk



"""
A Program that ask user
input: Date(Autofill), Description, transaction amount
Transform in a Dataframe, columns = Date, Description, amount

"""

# def add_item():
#     """ Allow users to add new item into the category and
#         and also display the current item list
#     """
#
#     #display the item list
#
#
#     return category

def new_trans():
    desc = input("What did you buy? ").strip() # remove whitespace in the beginning and end
    money = float(input("How much is it? "))
    data = str(desc + ',' + str(money))
    return data


def analysis():
    df = pd.read_csv("user.txt")
    df = df.groupby(['Transaction']).sum()
    print(df)


def get_file_item(f):
    """ Retrieve the item list """
    data = pd.read_csv(f)
    item_list = list(data['Transaction'])
    return item_list


def main():
    file = open("user.txt", "a+")
    # Write header if not exist
    if os.path.getsize("user.txt") == 0:
        file.write("Transaction, Amount \n")
        file.close()
        file = open("user.txt", "a+")
    #
    # data = new_trans()
    # file.write(data + '\n')
    # file.close()
    #
    # print('*' * 10, "Recording Completed.", '*' * 10)

    window = tk.Tk()

    window.title("Money Spending App")
    window.geometry("600x300-8-200")

    window.columnconfigure(0, weight =3)
    window.columnconfigure(1, weight =2)
    window.columnconfigure(2, weight =3)
    window.columnconfigure(3, weight =4)



    # List box
    file_path = "/Users/hayden/Documents/Py-Project/user.txt"
    x = get_file_item(file_path)
    file_list = tk.Listbox(window, width = 20)
    file_list.grid(row=1, column=0, sticky="w")
    for i in x:
        if i not in file_list.get(0, tk.END):
            file_list.insert(tk.END, i)

    def pout():
        print(file_list.get(file_list.curselection()))

    def add_item():
        x = entrybox.get()
        entrybox.delete(first=0,last=tk.END)
        y = amount.get()
        amount.delete(first=0, last=tk.END)

        with open("/Users/hayden/Documents/Py-Project/user.txt", 'a+') as file:
            transaction = x + ',' + y
            file.write(transaction + '\n')

        if x not in file_list.get(0, tk.END):
            file_list.insert(tk.END, x)





    text0 = tk.Label(window, text = "*"*40)
    text0.grid(column=0, row=0, sticky="nw")

    text1 = tk.Label(window, text = "Amount")
    text1.grid(column=0, row=2, sticky="nw")

    entrybox = tk.Entry(window, bd=3)
    entrybox.grid(column=0, row=3)

    amount = tk.Entry(window, bd=1)
    amount.grid(column=1, row=3)

    button1 = tk.Button(window, text="Enter", width=10, bd=70, command=pout)
    button1.grid(column=2, row=3)

    button1 = tk.Button(window, text="Add item", width=10, bd=70, command=add_item)
    button1.grid(column=3, row=3)

    window.mainloop()


if __name__ == "__main__":
	main()
