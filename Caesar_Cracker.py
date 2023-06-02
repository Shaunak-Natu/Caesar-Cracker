import customtkinter as ctk

list_alphabet_lower = [chr(i) for i in range(97,123)]
num_list = [num for num in range(1,27)]

lower_dict = dict(zip(list_alphabet_lower,num_list))
rev_dict_lower = dict(zip(num_list,list_alphabet_lower))

list_alphabet_upper = [chr(i) for i in range(65,91)]

upper_dict = dict(zip(list_alphabet_upper,num_list))
rev_dict_upper = dict(zip(num_list,list_alphabet_upper))

def decrypt(msg,n):
    d_msg = ""
    for letter in msg:
        if letter in lower_dict:
            bound = (lower_dict[letter] - n) % 26
            diff = n - lower_dict[letter]
            if bound >= 1:
                d_msg += rev_dict_lower[bound]
            else:
                d_msg += rev_dict_lower[26 - diff]

        elif letter in upper_dict:
            bound = (upper_dict[letter] - n) % 26
            diff = n - upper_dict[letter]
            if bound >= 1:
                d_msg += rev_dict_upper[bound]
            else:
                d_msg += rev_dict_upper[26 - diff]

        else:
            d_msg += letter
    return d_msg

def decrypt_message():
    input_text.configure(text_color="white")
    message = input_text.get("1.0", tk.END).strip()
    decrypted_msgs = []

    for n in range(1, 26):
        decrypted_msg = decrypt(message, n)
        decrypted_msgs.append(" For n = {}, Message = {}\n".format(n, decrypted_msg))


    decrypted_text.delete("1.0", tk.END)  # Clear previous content
    decrypted_text.insert(tk.END, "\n".join(decrypted_msgs))  # Update content

# Create the main window
root = ctk.CTk()
root.geometry("760x460")
root.title("Caesar Cracker")

# Set the window icon
root.iconbitmap("Images/icons/icon-julius-caesar.ico")

font=ctk.CTkFont(family='Helvetica')

# Creating a background label
bg_label = ctk.CTkLabel(master=root, text="",fg_color="gray")
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create input label and text box
input_label = ctk.CTkLabel(root, text="Enter Text\n To Decrypt:",text_color="white",fg_color="#1e1e1e")
input_label.grid(row=0, column=0, padx=10, pady=10,sticky="n")

# Creating input text box
input_text = ctk.CTkTextbox(root, height=350, width=300)
input_text.grid(row=0, column=1, padx=10, pady=10)

# Create decrypt button
decrypt_button = ctk.CTkButton(root, text="Generate",text_color="white",fg_color="#1e1e1e",bg_color="#1e1e1e", command=decrypt_message)
decrypt_button.grid(row=2, column=1, padx=10, pady=10,sticky="nsew")

# Create decrypted messages text box
decrypted_text = ctk.CTkTextbox(root, height=350, width=300)
decrypted_text.grid(row=0, column=4, columnspan=15, padx=10, pady=10)

root.resizable(False,False)
# Run the GUI event loop
root.mainloop()

