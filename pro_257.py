from tkinter import *
from PIL import ImageTk, Image
from web3 import Web3

root = Tk()
root.title("Account Details")
root.configure(background="black")

ganache_url = 'http://127.0.0.1:7545'

web3 = Web3(Web3.HTTPProvider(ganache_url))

img = ImageTk.PhotoImage(Image.open("image.png"))
panel = Label(root, image=img, bg='black')
panel.pack(side="top")

frame = Frame(
    root,
    bg='black',
    padx=5,
    pady=5
)
# create the labels to hold the account numbers

Label(frame,text="Account 1",foreground='white',background='black').grid(row=0,column=0,sticky=W,pady=10)
Label(frame,text="Account 2",foreground='white',background='black').grid(row=1,column=0,sticky=W,pady=10)
Label(frame,text="Account 3",foreground='white',background='black').grid(row=2,column=0,sticky=W,pady=10)
Label(frame,text="Account 4",foreground='white',background='black').grid(row=3,column=0,sticky=W,pady=10)
Label(frame,text="Account 5",foreground='white',background='black').grid(row=4,column=0,sticky=W,pady=10)

#Create entry elements to get the use input for account addresses 
account1=Entry(frame,background="black",foreground="white")
account1.grid(row=0,column=1,sticky=W,pady=10)

account2=Entry(frame,background="black",foreground="white")
account2.grid(row=1,column=1,sticky=W,pady=10)

account3=Entry(frame,background="black",foreground="white")
account3.grid(row=2,column=1,sticky=W,pady=10)

account4=Entry(frame,background="black",foreground="white")
account4.grid(row=3,column=1,sticky=W,pady=10)

account5=Entry(frame,background="black",foreground="white")
account5.grid(row=4,column=1,sticky=W,pady=10)
result=Text(root,background="black",height=10,width=45,foreground="white")
#define a function CHECK_BALANCE() and add the code inside it.
def CHECK_BALANCE():
    
    account_addresses = []
    account_addresses.append(account1.get())
    account_addresses.append(account2.get())
    account_addresses.append(account3.get())
    account_addresses.append(account4.get())
    account_addresses.append(account5.get())

    count = 1
    for i in account_addresses:
        
        balance = web3.eth.get_balance(i)  # Fetch the balance using Web3
        balance_ether = balance * 0.000000000000000001  # Convert gwei to Ether
        result.insert(END, f"Account {count}: {balance_ether} Ether\n")
        
        count += 1
    
frame.pack()

#Create a button element to call the CHECK_BALANCE()
check_balance = Button(root,background="black",foreground="white", text="CHECK BALANCE", width=15, command=CHECK_BALANCE, highlightbackground="green")
check_balance.pack(fill='both', padx=20, pady=20)

    
result.pack(pady=5)
root.mainloop()
