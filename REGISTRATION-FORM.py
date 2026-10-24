import tkinter as tk

root = tk.Tk()
root.title("Registration Form")
root.geometry("300x300")

tk.Label(root, text="Registration Form",
         font=("Arial", 16)).pack(pady=10)

tk.Label(root, text="Name").pack()
tk.Entry(root).pack()

tk.Label(root, text="Email").pack()
tk.Entry(root).pack()

tk.Label(root, text="Password").pack()
tk.Entry(root, show="*").pack()

tk.Button(root, text="Register",
          command=lambda: print("Registered!")).pack(pady=15)

root.mainloop()
