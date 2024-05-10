from tkinter import *
import ttkbootstrap as tb
import random
import os
from tkinter import messagebox

class BillApp:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color = "#ccc"
        # title = Label(self.root, text="Billing Software", font=('Helvetica', 20, 'bold'), pady=2, bd=12, bg="#ccc", fg="Black")
        # title.pack(fill=X)
        title = tb.Label(self.root,text="Billing Software",border=12,padding=2,font=("Helvatica",18,'bold'),bootstyle="success, inverse")
        title.pack(fill=X)

        # Medical
        self.sanitizer = IntVar()
        self.mask = IntVar()

        # Grocery
        self.rice = IntVar()
        self.food_oil = IntVar()

        # Beverages
        self.sprite = IntVar()
        self.mineral = IntVar()

        # Total Product Price
        self.medical_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drinks_price = StringVar()

        # Customer info
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()

        # Tax
        self.medical_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drinks_tax = StringVar()


        F1 = tb.Labelframe(self.root,bootstyle="info",text="Customer details",border=10)
        F1.place(x=0,y=50,relwidth=1)

        
        # cname_lbl = Label(F1, text="Customer Name:", bg=bg_color, font=('times new roman', 15, 'bold'))
        # cname_lbl.grid(row=0, column=0, padx=20, pady=5)

        c_name_lbl = tb.Label(F1,text="Customer Name:",border=12,padding=2,font=("Helvetica",12,'bold'),bootstyle="info")
        c_name_lbl.grid(row=0,column=0,padx=20,pady=5)

        # cname_txt = Entry(F1, width=15, textvariable=self.c_name, font='arial 15', bd=7, relief=GROOVE)
        # cname_txt.grid(row=0, column=1, pady=5, padx=10)

        c_name_txt = tb.Entry(F1,width=15,textvariable=self.c_name,font='Helvetica 12')
        c_name_txt.grid(row=0,column=1,pady=5,padx=10)

        # cphn_lbl = Label(F1, text="Customer Phone:", bg="#ccc", font=('times new roman', 15, 'bold'))

        cphn_lbl = tb.Label(F1,text="Phone No:",font=("Helvetica",12,'bold'),bootstyle="info")
        cphn_lbl.grid(row=0, column=2, padx=20, pady=5)

        c_phn_txt = tb.Entry(F1,width=15,textvariable=self.c_phone,font='Helvetica 12')
        c_phn_txt.grid(row=0, column=3, pady=5, padx=10)

        # Search Bill
        # c_bill_lbl = Label(F1, text="Bill Number:", bg="#ccc", font=('times new roman', 15, 'bold'))
        # c_bill_lbl.grid(row=0, column=4, padx=20, pady=5)
        # c_bill_txt = Entry(F1, width=15, textvariable=self.search_bill, font='arial 15', bd=7, relief=GROOVE)
        # c_bill_txt.grid(row=0, column=5, pady=5, padx=10)

        # bil_btn = Button(F1, text="Search", command=self.find_bill, width=10, bd=7, font=('arial', 12, 'bold'), relief=GROOVE)
        # bil_btn.grid(row=0, column=6, pady=5, padx=10)

        # ======Medical======
        F2 =tb.Labelframe(self.root,bootstyle="success",text="Medical and Pharmacy",border=10)
        F2.place(x=5, y=150, width=325, height=380)

        sanitizer_lbl = tb.Label(F2,text="Sanitizer",border=12,padding=2,font=("Helvetica",12,'bold'),bootstyle="success")
        sanitizer_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        sanitizer_txt = tb.Entry(F2,width=15,textvariable=self.sanitizer,font='Helvetica 12',bootstyle="success")
        sanitizer_txt.grid(row=0, column=1, padx=10, pady=10)

        mask_lbl = tb.Label(F2,text="Mask",border=12,padding=2,font=("Helvetica",12,'bold'),bootstyle="success")
        mask_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        mask_txt = tb.Entry(F2,width=15,textvariable=self.mask,font='Helvetica 12',bootstyle="success")
        mask_txt.grid(row=1, column=1, padx=10, pady=10)

        # ======Grocery Items=======
        F3 =tb.Labelframe(self.root,bootstyle="success",text="Grocery Items",border=10)
        F3.place(x=340, y=150, width=325, height=380)

        rice_lbl = tb.Label(F3,text="Rice",border=12,padding=2,font=("Helvetica",12,'bold'),bootstyle="success")
        rice_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        rice_txt = tb.Entry(F3,width=15,textvariable=self.rice,font='Helvetica 12',bootstyle="success")
        rice_txt.grid(row=0, column=1, padx=10, pady=10)

        food_oil_lbl = tb.Label(F3,text="Oil",border=12,padding=2,font=("Helvetica",12,'bold'),bootstyle="success")
        food_oil_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        food_oil_txt = tb.Entry(F3,width=15,textvariable=self.food_oil,font='Helvetica 12',bootstyle="success")
        food_oil_txt.grid(row=1, column=1, padx=10, pady=10)

        # ======Beverages==========
        F4 = tb.Labelframe(self.root,bootstyle="success",text="Beverages",border=10)
        F4.place(x=670, y=150, width=325, height=380)

        sprite_lbl = tb.Label(F4,text="Sprite",border=12,padding=2,font=("Helvetica",12,'bold'),bootstyle="success")
        sprite_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        sprite_txt = tb.Entry(F4,width=15,textvariable=self.sprite,font='Helvetica 12',bootstyle="success")
        sprite_txt.grid(row=0, column=1, padx=10, pady=10)

        mineral_lbl = tb.Label(F4,text="Water",border=12,padding=2,font=("Helvetica",12,'bold'),bootstyle="success")
        mineral_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        mineral_txt = tb.Entry(F4,width=15,textvariable=self.mineral,font='Helvetica 12',bootstyle="success")
        mineral_txt.grid(row=1, column=1, padx=10, pady=10)

        # ==========Billing Area===========
        F5 = tb.Labelframe(self.root,bootstyle="success",border=10,text="Billing Area")
        F5.place(x=1010, y=150, width=350, height=380)

        bill_title = tb.Label(F5,text="Billing Details",border=7)
        bill_title.pack(fill=X)

        scrollY = tb.Scrollbar(F5,orient=VERTICAL)
        self.txtarea = Text(F5,yscrollcommand=scrollY.set)
        scrollY.pack(side=RIGHT, fill=Y)
        scrollY.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        F6 = tb.Labelframe(self.root,bootstyle="success",border=10,text="Billing Area BTM")
        F6.place(x=0, y=535, relwidth=1, height=150)

        m1_lbl = tb.Label(F6,text="Medical Total",border=12,padding=2,font=("Helvetica",12,'bold'),bootstyle="success")
        m1_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        m1_txt = tb.Entry(F6,width=15,textvariable=self.medical_price,font='Helvetica 12',bootstyle="success")
        m1_txt.grid(row=0, column=1, padx=18, pady=1)

        m2_lbl = tb.Label(F6,text="Grocery Total",border=12,padding=2,font=("Helvetica",12,'bold'),bootstyle="success")
        m2_lbl.grid(row=0, column=2, padx=10, pady=10, sticky='W')
        m2_txt = tb.Entry(F6,width=15,textvariable=self.grocery_price,font='Helvetica 12',bootstyle="success")
        m2_txt.grid(row=0, column=3, padx=18, pady=1)

        m3_lbl = tb.Label(F6,text="Beverage Total",border=12,padding=2,font=("Helvetica",12,'bold'),bootstyle="success")
        m3_lbl.grid(row=0, column=5, padx=10, pady=10, sticky='W')
        m3_txt = tb.Entry(F6,width=15,textvariable=self.cold_drinks_price,font='Helvetica 12',bootstyle="success")
        m3_txt.grid(row=0, column=6, padx=18, pady=1)

        m4_lbl = tb.Label(F6,text="Medical Tax",border=12,padding=2,font=("Helvetica",12,'bold'),bootstyle="success")
        m4_lbl.grid(row=1, column=2, padx=10, pady=10, sticky='W')
        m4_txt = tb.Entry(F6,width=15,textvariable=self.medical_tax,font='Helvetica 12',bootstyle="success")
        m4_txt.grid(row=1, column=3, padx=18, pady=1)

        m5_lbl = tb.Label(F6,text="Grocery Tax",border=12,padding=2,font=("Helvetica",12,'bold'),bootstyle="success")
        m5_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        m5_txt = tb.Entry(F6,width=15,textvariable=self.grocery_tax,font='Helvetica 12',bootstyle="success")
        m5_txt.grid(row=1, column=1, padx=18, pady=1)

        m6_lbl = tb.Label(F6,text="Beverage Tax",border=12,padding=2,font=("Helvetica",12,'bold'),bootstyle="success")
        m6_lbl.grid(row=1, column=5, padx=10, pady=10, sticky='W')
        m6_txt = tb.Entry(F6,width=15,textvariable=self.cold_drinks_tax,font='Helvetica 12',bootstyle="success")
        m6_txt.grid(row=1, column=6, padx=18, pady=1)

        # =========Button========
        btn_f=tb.Frame(F6,border=7)
        btn_f.place(x=1030,width=580,height=100)

        total_btn=tb.Button(btn_f,command=self.total,text="Total")
        total_btn.grid(row=0, column=0, padx=5, pady=5)

        generateBill_btn=tb.Button(btn_f,command=self.bill_area,text="Generate Bill",bootstyle="light")
        generateBill_btn.grid(row=0, column=1, padx=5, pady=5)

        clear_btn=tb.Button(btn_f,command=self.clear_data,text="Clear",bootstyle="warning")
        clear_btn.grid(row=0, column=3, padx=5, pady=5)

        exit_btn=tb.Button(btn_f,command=self.exit_app,text="Exit",bootstyle="danger")
        exit_btn.grid(row=0, column=4, padx=5, pady=5)
        self.welcome_bill()


    def total(self):
        self.m_s_p = self.sanitizer.get()*500
        self.m_m_p = self.mask.get()*200
        self.total_medical_price = float(self.m_m_p+self.m_s_p)
        self.medical_price.set("Ks. "+str(self.total_medical_price))
        self.c_tax = round((self.total_medical_price*0.05), 2)
        self.medical_tax.set("Ks. "+str(self.c_tax))

        self.g_r_p = self.rice.get()*10000
        self.g_f_o_p = self.food_oil.get()*5000
        self.total_grocery_price = float(self.g_r_p+self.g_f_o_p)
        self.grocery_price.set("Ks. " + str(self.total_grocery_price))
        self.g_tax = round((self.total_grocery_price*0.05), 2)
        self.grocery_tax.set("Ks. " + str(self.g_tax))

        self.c_d_s_p = self.sprite.get()*500
        self.c_d_w_p = self.mineral.get()*100
        self.total_cold_drinks_price = float(self.c_d_s_p+self.c_d_w_p)
        self.cold_drinks_price.set("Ks. "+str(self.total_cold_drinks_price))
        self.c_d_tax = round((self.total_cold_drinks_price * 0.05), 2)
        self.cold_drinks_tax.set("Ks. "+str(self.c_d_tax))

        self.total_bill = float(self.total_medical_price+self.total_grocery_price+self.total_cold_drinks_price+self.c_tax+self.g_tax+self.c_d_tax)


    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\tWelcome to TZ Grocery Shop")
        self.txtarea.insert(END, f"\nBill Number:{self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name:{self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone Number{self.c_phone.get()}")
        self.txtarea.insert(END, f"\n================================")
        self.txtarea.insert(END, f"\nProducts\t\tQTY\t\tPrice")
    
    def bill_area(self):
        if self.c_name.get() == " " or self.c_phone.get() == " ":
            messagebox.showerror("Error", "Customer Details Are Must")
        elif self.medical_price.get() == "Ks. 0.0" and self.grocery_price.get() == "Ks. 0.0" and self.cold_drinks_price.get()=="Ks. 0.0":
            messagebox.showerror("Error", "No Product Purchased")
        else:
            self.welcome_bill()
    # ============medical===========================
        if self.sanitizer.get() != 0:
            self.txtarea.insert(END, f"\n Sanitizer\t\t{self.sanitizer.get()}\t\t{self.m_s_p}")
        if self.mask.get() != 0:
            self.txtarea.insert(END, f"\n Mask\t\t{self.mask.get()}\t\t{self.m_m_p}")
    # ==============Grocery============================
        if self.rice.get() != 0:
            self.txtarea.insert(END, f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
        if self.food_oil.get() != 0:
            self.txtarea.insert(END, f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_f_o_p}")
    #================ColdDrinks==========================
        if self.sprite.get() != 0:
            self.txtarea.insert(END, f"\n Sprite\t\t{self.sprite.get()}\t\t{self.c_d_s_p}")
        if self.mineral.get() != 0:
            self.txtarea.insert(END, f"\n Mineral\t\t{self.mineral.get()}\t\t{self.c_d_w_p}")
            self.txtarea.insert(END, f"\n--------------------------------")
    # ===============taxes==============================
        if self.medical_tax.get() != '0.0':
            self.txtarea.insert(END, f"\n Medical Tax\t\t\t{self.medical_tax.get()}")
        if self.grocery_tax.get() != '0.0':
            self.txtarea.insert(END, f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")
        if self.cold_drinks_tax.get() != '0.0':
            self.txtarea.insert(END, f"\n Cold Drinks Tax\t\t\t{self.cold_drinks_tax.get()}")

        self.txtarea.insert(END, f"\n Total Bil:\t\t\t Ks.{self.total_bill}")
        self.txtarea.insert(END, f"\n--------------------------------")
        self.save_bill()
    
    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the bill?")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("F:\Tkinter\Project2T\\bills"+str(self.bill_no.get())+".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill no:{self.bill_no.get()} Saved Successfully")
        else:
           return
    
    # def find_bill(self):
    #     present = "no"
    #     for i in os.listdir("bills/"):
    #         if i.split('.')[0] == self.search_bill.get():
    #             f1 = open(f"bills/{i}", "r")
    #             self.txtarea.delete("1.0", END)
    #             for d in f1:
    #                 self.txtarea.insert(END, d)
    #                 f1.close()
    #             present = "yes"
    #     if present == "no":
    #         messagebox.showerror("Error", "Invalid Bill No")

    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to Clear?")
        if op > 0:
            self.sanitizer.set(0)
            self.mask.set(0)
            self.rice.set(0)
            self.food_oil.set(0)
            self.sprite.set(0)
            self.mineral.set(0)
            # ====================taxes================================
            self.medical_price.set("")
            self.grocery_price.set("")
            self.cold_drinks_price.set("")

            self.medical_tax.set("")
            self.grocery_tax.set("")
            self.cold_drinks_tax.set("")

            self.c_name.set("")
            self.c_phone.set("")

            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()

    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            self.root.destroy()



root = tb.Window(themename="superhero")
obj=BillApp(root)
root.mainloop()