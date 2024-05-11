import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# main GUI window
root = tk.Tk()
root.title("Café Bistro Management System")
root.geometry("900x600")
root.maxsize(900,600)

# store csv into a dataframe
data_path = "C:\\Users\\LENOVO\\OneDrive\\Computer Engineering\\Programming\\Python\\cafe management project\\cafe_menu .csv"
df = pd.read_csv(data_path)

# displaying the background image
bg_image = Image.open("C:\\Users\\LENOVO\\Downloads\\background.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)
background_label = tk.Label(root, image=bg_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# functions for each menu option 
def ShowCafe():
    messagebox.showinfo("Café Menu", df.to_string()) 

def MenuFilter():
    # GUI for the filter menu 
    filter_window = tk.Toplevel(root)
    filter_window.title("Filters Menu")
    filter_window.geometry("300x150")
    
    label = tk.Label(filter_window, text="Enter a cost you would like to filter below:")
    label.pack()
    entry = tk.Entry(filter_window)
    entry.pack()

    btn_filter = tk.Button(filter_window, text="Apply Filter", command=lambda: apply_filter(float(entry.get())))
    btn_filter.pack()

def apply_filter(cost):
    filtered_df = df[df['Cost '] < cost]
    messagebox.showinfo("Filtered Menu", filtered_df.to_string())

def EditMenu():
    edit_window = tk.Toplevel(root)
    edit_window.title("Edit Menu")
    edit_window.geometry("300x200")

    name_label = tk.Label(edit_window, text="Beverage Name:")
    name_label.pack()
    name_entry = tk.Entry(edit_window)
    name_entry.pack()

    serve_label = tk.Label(edit_window, text="Servings (mL):")
    serve_label.pack()
    serve_entry = tk.Entry(edit_window)
    serve_entry.pack()

    price_label = tk.Label(edit_window, text="Cost :")
    price_label.pack()
    price_entry = tk.Entry(edit_window)
    price_entry.pack()

    def add_item():
        if not name_entry.get() or not serve_entry.get() or not price_entry.get():
            messagebox.showerror("Kindly fill all required fields")
            return

        try:
            float(serve_entry.get())
            float(price_entry.get())
        except ValueError:
            messagebox.showerror("Please enter numeric values. ")
            return

        new_item = {
            'Beverages': name_entry.get(),
            'Servings (mL)': serve_entry.get(),
            'Cost ': price_entry.get()
        }
        global df
        df = df.append(new_item, ignore_index=True)
        df.to_csv(data_path)  
        messagebox.showinfo("Edit Menu", "Item added successfully.")

    btn_add_item = tk.Button(edit_window, text="Add Item", command=add_item)
    btn_add_item.pack()


def DelMenuItem():
    del_window = tk.Toplevel(root)
    del_window.title("Delete Menu Item")
    del_window.geometry("300x100")

    bvg_label = tk.Label(del_window, text="Enter beverage to delete from the menu:")
    bvg_label.pack()
    bvg_entry = tk.Entry(del_window)
    bvg_entry.pack()

    def delete_item():
        global df
        df = df[df['Beverages'] != bvg_entry.get()]
        # saving changes back into the csv
        df.to_csv(data_path, index=False)
        messagebox.showinfo("Delete Menu Item", "Deleted beverage item successfully.")

    btn_del_item = tk.Button(del_window, text="Delete Item", command=delete_item)
    btn_del_item.pack()


def DiscountsMenu():
    discount_window = tk.Toplevel(root)
    discount_window.title("Discounts Menu")
    discount_window.geometry("300x200")

    special_offers = [
        "Iced Lemon Tea + Fruit Punch at Rs. 300/-",
        "Hot Chocolate + Cappuccino at Rs. 325/-",
        "Hazelnut Frappé(order for two) at Rs. 400/-",
        "One complementary Vanilla Latte for orders above Rs. 750/-",
        "5% discount on orders above Rs. 500/-"
    ]

    label = tk.Label(discount_window, text="Current Special Offers:")
    label.pack()

    for offer in special_offers:
        tk.Label(discount_window, text=offer).pack()

    new_offer_label = tk.Label(discount_window, text="New discount offer in the menu:")
    new_offer_label.pack()
    new_offer_entry = tk.Entry(discount_window)
    new_offer_entry.pack()

def BarGraph():
    bar_window = tk.Toplevel(root)
    bar_window.title("Bar Graph Menu")
    bar_window.geometry("300x200")

    label = tk.Label(bar_window, text="Select Bar Graph Option:")
    label.pack()

    selected_option = tk.StringVar(bar_window)  
    options = [
        "Customer Review analysis",
        "Item wise Revenue analysis",
        "Inventory Expenditure analysis",
        "Net Income analysis",
        "Three year Revenue analysis",
        "Three year Inventory Expenditure analysis",
        "Three year Net Income analysis"
    ]


    def plot_graph(option):
        plt.figure(figsize=(8, 6))
        Revenue = [39400, 41000, 37200, 47390, 51600, 39000, 31500, 46000, 41350, 42100]
        Ratings = [3.5, 4.1, 4.5, 3.9, 3.2, 4.0, 4.1, 3.7, 3.9, 4.5]
        Expenditure=[17200,23500,19400,25600,23300,21600,14300,22700,21300,19400]
        rev2020=[23400,31200,27300,26400,29200,26700,29190,25300,24900,24100]
        rev2021=[32100,28900,35700,32900,33400,31020,37200,27600,34200,31800]
        rev2022=[39400,41000,37200,47390,51600,39000,31500,46000,41350,42100]
        exp2020=[14900,18100,13450,12680,14720,12460,16460,12490,12300,13200]
        exp2021=[16340,14530,17200,16700,17800,15400,18790,14270,17290,17830]
        exp2022=[17200,23500,19400,25600,23300,21600,14300,22700,21300,19400]

        if option == "Customer Review analysis":
            plt.bar(df['Beverages'], Ratings, color='#E6DAA6', edgecolor='#A0522D', width=0.5)
            plt.xlabel("Beverage Items")
            plt.ylabel("Customer Ratings")
            plt.title("Customer Review Analysis")
            plt.show()

        elif option == "Item wise Revenue analysis":
            plt.bar(df['Beverages'], Revenue, color='#A9561E', edgecolor='#F5DEB3', width=0.5)
            plt.xlabel("Beverage Items")
            plt.ylabel("Revenue Generated")
            plt.title("Item wise Revenue Analysis")
            plt.show()

        elif option == "Inventory Expenditure analysis":
            plt.bar(df['Beverages'],Expenditure, color='#F5DEB3',edgecolor='#580F41',width=0.5)
            plt.xlabel("Beverage Items")
            plt.ylabel("Inventory/Stock Expenditure")
            plt.title("Inventory Expenditure analysis")
            plt.yticks(range(0,26000,2000))
            plt.show()
        
        elif option == "Net Income analysis": 
            array1=np.array(Revenue)
            array2=np.array(Expenditure)
            NetIncome=array1-array2
            plt.bar(df['Beverages'],NetIncome, color='#DAA520',edgecolor='#F5F5DC',width=0.5)
            plt.xlabel("Beverage Items")
            plt.ylabel("Net Income or Profit Margin")
            plt.title("Net Income analysis")
            plt.yticks(range(0,30000,2000))
            plt.show()
        
        elif option == "Three year Revenue analysis": 
            bvg_axis=np.arange(len(df['Beverages']))
            plt.bar(bvg_axis+0.00,rev2020, color='#D2691E',edgecolor='#E6DAA6',
                    width=0.25,label='2020 Revenue')
            plt.bar(bvg_axis+0.25,rev2021,color='#F0E68C',edgecolor='#D2691E',
                    width=0.25,label='2021 Revenue')
            plt.bar(bvg_axis+0.50,rev2022,color='#A0522D',edgecolor='#F5F5DC',
                    width=0.25,label='2022 Revenue')
            plt.legend(loc='upper right')
            plt.xticks(bvg_axis,df['Beverages'])
            plt.yticks(range(10000,52000,5000))
            plt.xlabel("Consecutive years depicting growth")
            plt.ylabel("Revenue Generated")
            plt.title("Three year Revenue analysis")
            plt.show()

        elif option =="Three year Inventory Expenditure analysis": 
            bvg_axis=np.arange(len(df['Beverages']))
            plt.bar(bvg_axis+0.00,exp2020, color='#F5F5DC',edgecolor='#D2691E',
                    width=0.25,label='2020 Expenses')
            plt.bar(bvg_axis+0.25,exp2021,color='#D2691E',edgecolor='#F0E68C',
                    width=0.25,label='2021 Expenses')
            plt.bar(bvg_axis+0.50,exp2022,color='#E6DAA6',edgecolor='#A0522D',
                    width=0.25,label='2022 Expenses')
            plt.legend(loc='upper right')
            plt.xticks(bvg_axis,df['Beverages'])
            plt.yticks(range(0,28000,2000))
            plt.xlabel("Consecutive years depicting expenditure")
            plt.ylabel("Inventory/Stock Expenditure")
            plt.title("Three year Inventory Expenditure analysis")
            plt.show()

        elif option == "Three year Net Income analysis":
            arr1=np.array(rev2020)
            arr2=np.array(exp2020)
            NetIncome2020=arr1-arr2
            arr3=np.array(rev2021)
            arr4=np.array(exp2021)
            NetIncome2021=arr3-arr4
            arr5=np.array(rev2022)
            arr6=np.array(exp2022)
            NetIncome2022=arr5-arr6
            bvg_axis=np.arange(len(df['Beverages']))
            plt.bar(bvg_axis+0.00,NetIncome2020, color='#A9561E',
                    edgecolor='#F5F5DC',width=0.25,label='2020 Net Income')
            plt.bar(bvg_axis+0.25,NetIncome2021,color='#FFFFCB',
                    edgecolor='#A0522D',width=0.25,label='2021 Net Income')
            plt.bar(bvg_axis+0.50,NetIncome2022,color='#D2691E',
                    edgecolor='#A9561E',width=0.25,label='2022 Net Income')
            plt.legend(loc='upper right')
            plt.xticks(bvg_axis,df['Beverages'])
            plt.yticks(range(0,28000,2000))
            plt.xlabel("Years depicting net income")
            plt.ylabel("Net Income/Profit Margin")
            plt.title("Three year Net Income analysis")
            plt.show()
            
    option_menu = tk.OptionMenu(bar_window, selected_option, *options, command=plot_graph)
    option_menu.pack()



def PieChart():
    pie_window = tk.Toplevel(root)
    pie_window.title("Pie Chart Menu")
    pie_window.geometry("300x200")

    label = tk.Label(pie_window, text="Select Pie Chart Option:")
    label.pack()

    options = [
        "Item wise Revenue analysis",
        "Inventory Expenditure analysis",
        "Net Income analysis"
    ]

    selected_option = tk.StringVar(pie_window)  

    def plot_chart(option):
        Revenue=[39400,41000,37200,47390,51600,
                 39000,31500,46000,41350,42100]
        Expenditure=[17200,23500,19400,25600,23300,
                     21600,14300,22700,21300,19400]
        colr=['#D2691E','#E6DAA6','#F5F5DC','#F5DEB3','#FFFFCB',
                '#A9561E','#D1B26F','#A0522D','#F0E68C','#d9aa55']
        
        if option == "Item wise Revenue analysis":
            expl=[0,0,0,0,0.2,0,0,0,0,0]
            plt.title("Item wise Revenue analysis")
            plt.pie(Revenue,labels=df['Beverages'],explode=expl,
                    colors=colr,autopct="%03.1f%%")
            plt.show()

        elif option == "Inventory Expenditure analysis":
            expl=[0,0,0,0.2,0,0,0,0,0,0]
            plt.title("Inventory Expenditure analysis")
            plt.pie(Expenditure,labels=df['Beverages'],explode=expl,
                    colors=colr,autopct="%03.1f%%")
            plt.show()

        elif option == "Net Income analysis":
            array1=np.array(Revenue)
            array2=np.array(Expenditure)
            NetIncome=array1-array2
            expl=[0,0,0,0,0.2,0,0,0,0,0]
            plt.title("Net Income analysis")
            plt.pie(NetIncome,labels=df['Beverages'],explode=expl,
                    colors=colr,autopct="%03.1f%%")
            plt.show()
        

    option_menu = tk.OptionMenu(pie_window, selected_option, *options, command=lambda option: plot_chart(selected_option.get()))
    option_menu.pack()



# creating buttons for each menu option
btn_show_menu = tk.Button(root, text="Show Café Menu",font ="Modern, 10", command=ShowCafe, bg="#ede7e1")
btn_show_menu.place(relx=0.44, rely=0.4, anchor="w") 

btn_filters = tk.Button(root, text="Apply Filters",font ="Modern, 10", command=MenuFilter, bg="#ede7e1")
btn_filters.place(relx=0.44, rely=0.45, anchor="w") 

btn_edit_menu = tk.Button(root, text="Add Menu Item",font ="Modern, 10", command=EditMenu, bg="#ede7e1")
btn_edit_menu.place(relx=0.44, rely=0.5, anchor="w") 

btn_del_item = tk.Button(root, text="Delete Menu Item",font ="Modern, 10", command=DelMenuItem, bg="#ede7e1")
btn_del_item.place(relx=0.44, rely=0.55, anchor="w") 

btn_discounts = tk.Button(root, text="Add Discounts",font ="Modern, 10", command=DiscountsMenu, bg="#ede7e1")
btn_discounts.place(relx=0.44, rely=0.6, anchor="w") 

btn_bar_graph = tk.Button(root, text="Bar Graph Menu",font ="Modern, 10", command=BarGraph, bg="#ede7e1")
btn_bar_graph.place(relx=0.44, rely=0.65, anchor="w") 

btn_pie_chart = tk.Button(root, text="Pie Chart Menu",font ="Modern, 10", command=PieChart, bg="#ede7e1")
btn_pie_chart.place(relx=0.44, rely=0.7, anchor="w") 


root.mainloop()
