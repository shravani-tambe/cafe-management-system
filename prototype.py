import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

#option one in our main menu.
def ShowCafe():
    df=pd.read_csv("prototype_menu.csv",
                   index_col='Item_ID')
    print(df)    

#option2 in our main menu. 
def MenuFilter(): 
    Opt=0
    df=pd.read_csv("prototype_menu.csv",
                   index_col='Item_ID')
    print("          ☆━━━━━━━━━━━━━━━━━━━☆")
    print("               Filters Menu")
    print("          ☆━━━━━━━━━━━━━━━━━━━☆")
    print("1. Filtering beverages above an entered cost.")
    print("2. Filter for beverages below an entered cost.")
    print("3. Filter for beverages above a servings quantity.")
    print("4. Filter for beverages below a servings quantity.")
    print("5. Return to the Management System.")
    print("          ☆━━━━━━━━━━━━━━━━━━━☆")
    while Opt!=5:
        Opt= int(input("Enter the filter number of your choice: "))
        if Opt==1:  
            num1=int(input("Enter a cost you would like to filter above:"))
            df[df['Cost (in Rs.)']>(num1)]
            print(df[df['Cost (in Rs.)']>(num1)])
        elif Opt==2:
            num2=int(input("Enter a cost you would like to filter below:"))
            df[df['Cost (in Rs.)']<(num2)]
            print(df[df['Cost (in Rs.)']<(num2)])
        elif Opt==3:
            num3=int(input("Enter a serving quantity you want to filter above:"))
            df[df['Servings (in mL)']>(num3)]
            print(df[df['Servings (in mL)']>(num3)])
        elif Opt==4:
            num4=int(input("Enter a serving quantity you want to filter below:"))
            df[df['Servings (in mL)']<(num4)]
            print(df[df['Servings (in mL)']<(num4)])
        elif Opt==5:
            print("Closing Filters Menu...")
            management_system()
        else:
            print("Option entered is invalid. Please try again.")
            management_system()

#option 3 in our main menu 
def EditMenu(): 
    item=input("Enter the new Item_ID:")
    name=input("Enter the new Beverage name:")
    serve=input("Enter the beverage servings in mL:")
    price=input("Enter the cost in Rs:")
    dict={'Item_ID':item,'Beverages':name,
          'Servings (in mL)':serve,'Cost (in Rs.)':price}
    df=pd.DataFrame(dict,index=['Item_ID'])
    #appending this new data into the existing csv file 
    #mode='a' will append this data into our file
    df.to_csv("prototype_menu .csv",
              mode='a', index=False, header=False)
    print(df)
    print("Added data successfully.")   
    
    
#option 4 in our main menu. 
def DelMenuItem():
    bvg=input("Enter beverage to delete from the menu:")
    df=pd.read_csv("prototype_menu.csv",
                   index_col='Item_ID')
    df=df[df.Beverages!=bvg]
    df.to_csv("prototype_menu .csv")
    print("Deleted beverage item successfully.")
    
#option 5 in our main menu.
def DiscountsMenu():
    print("          ☆━━━━━━━━━━━━━━━━━━━☆")
    print("              Discounts Menu")
    print("          ☆━━━━━━━━━━━━━━━━━━━☆") 
    print("Season Special Offers: ")
    print("1. Iced Lemon Tea + Fruit Punch at Rs. 300/-")
    print("2. Hot Chocolate + Cappuccino at Rs. 325/-")
    print("3. Hazelnut Frappé(order for two) at Rs. 400/-")
    print("4. One complementary Vanilla Latte for orders above Rs. 750/-")
    print("5. 5% discount on orders above Rs. 500/- ")
    print("6.",str(input("New discount offer in the menu: ")))
    print("          ☆━━━━━━━━━━━━━━━━━━━☆")
    

#option 6 in our main menu. 
def BarGraph():
    OptBar=0
    df=pd.read_csv("prototype_menu.csv")
    Beverages=df["Beverages"]
    Cost=df["Cost (in Rs.)"]
    print("       ☆━━━━━━━━━━━━━━━━━━━☆")
    print("           Bar Graph Menu")
    print("       ☆━━━━━━━━━━━━━━━━━━━☆") 
    print("1. Customer review analysis.") 
    print("2. Item wise Revenue analysis.")
    print("3. Inventory Expenditure analysis.")
    print("4. Net Income analysis.")
    print("5. Three year Revenue analysis.")
    print("6. Three year Inventory Expenditure analysis.")
    print("7. Three year Net Income analysis")
    print("8. Return to Management System. ")
    print("       ☆━━━━━━━━━━━━━━━━━━━☆")
    while OptBar!=8:
        OptBar=int(input("Enter the option no. for your desired graph:"))
        if OptBar==1: 
            plt.xlabel("Beverage Items")
            plt.ylabel("Customer Ratings")
            plt.title("Customer Review analysis")
            Ratings=[3.5,4.1,4.5,3.9,3.2,4.0,4.1,3.7,3.9,4.5]
            plt.yticks([0,1,2,3,4,5])
            plt.bar(Beverages,Ratings, color='#E6DAA6',
                    edgecolor='#A0522D',width=0.5)
            plt.show()
        elif OptBar==2:
            plt.xlabel("Beverage Items")
            plt.ylabel("Revenue Generated")
            plt.title("Item wise Revenue analysis")
            Revenue=[39400,41000,37200,47390,51600,
                     39000,31500,46000,41350,42100]
            plt.yticks(range(15000,55000,5000))
            plt.bar(Beverages,Revenue, color='#A9561E',
                    edgecolor='#F5DEB3',width=0.5)
            plt.show()
        elif OptBar==3:
            plt.xlabel("Beverage Items")
            plt.ylabel("Inventory/Stock Expenditure")
            plt.title("Inventory Expenditure analysis")
            Expenditure=[17200,23500,19400,25600,23300,
                         21600,14300,22700,21300,19400]
            plt.yticks(range(0,26000,2000))
            plt.bar(Beverages,Expenditure, color='#F5DEB3',
                    edgecolor='#580F41',width=0.5)
            plt.show()
        elif OptBar==4:
            plt.xlabel("Beverage Items")
            plt.ylabel("Net Income or Profit Margin")
            plt.title("Net Income analysis")
            array1=np.array(Revenue)
            array2=np.array(Expenditure)
            NetIncome=array1-array2
            plt.yticks(range(0,30000,2000))
            plt.bar(Beverages,NetIncome, color='#DAA520',
                    edgecolor='#F5F5DC',width=0.5)
            plt.show()
        elif OptBar==5:
            plt.xlabel("Consecutive years depicting growth")
            plt.ylabel("Revenue Generated")
            plt.title("Three year Revenue analysis")
            rev2020=[23400,31200,27300,26400,29200,
                     26700,29190,25300,24900,24100]
            rev2021=[32100,28900,35700,32900,33400,
                     31020,37200,27600,34200,31800]
            rev2022=[39400,41000,37200,47390,51600,
                     39000,31500,46000,41350,42100]
            bvg_axis=np.arange(len(Beverages))
            plt.bar(bvg_axis+0.00,rev2020, color='#D2691E',edgecolor='#E6DAA6',
                    width=0.25,label='2020 Revenue')
            plt.bar(bvg_axis+0.25,rev2021,color='#F0E68C',edgecolor='#D2691E',
                    width=0.25,label='2021 Revenue')
            plt.bar(bvg_axis+0.50,rev2022,color='#A0522D',edgecolor='#F5F5DC',
                    width=0.25,label='2022 Revenue')
            plt.legend(loc='upper right')
            plt.xticks(bvg_axis,Beverages)
            plt.yticks(range(10000,52000,5000))
            plt.show()
        elif OptBar==6: 
            plt.xlabel("Consecutive years depicting expenditure")
            plt.ylabel("Inventory/Stock Expenditure")
            plt.title("Three year Inventory Expenditure analysis")
            exp2020=[14900,18100,13450,12680,14720,
                     12460,16460,12490,12300,13200]
            exp2021=[16340,14530,17200,16700,17800,
                     15400,18790,14270,17290,17830]
            exp2022=[17200,23500,19400,25600,23300,
                     21600,14300,22700,21300,19400]
            bvg_axis=np.arange(len(Beverages))
            plt.bar(bvg_axis+0.00,exp2020, color='#F5F5DC',edgecolor='#D2691E',
                    width=0.25,label='2020 Expenses')
            plt.bar(bvg_axis+0.25,exp2021,color='#D2691E',edgecolor='#F0E68C',
                    width=0.25,label='2021 Expenses')
            plt.bar(bvg_axis+0.50,exp2022,color='#E6DAA6',edgecolor='#A0522D',
                    width=0.25,label='2022 Expenses')
            plt.legend(loc='upper right')
            plt.xticks(bvg_axis,Beverages)
            plt.yticks(range(0,28000,2000))
            plt.show()
        elif OptBar==7:
            plt.xlabel("Years depicting net income")
            plt.ylabel("Net Income/Profit Margin")
            plt.title("Three year Net Income analysis")
            arr1=np.array(rev2020)
            arr2=np.array(exp2020)
            NetIncome2020=arr1-arr2
            arr3=np.array(rev2021)
            arr4=np.array(exp2021)
            NetIncome2021=arr3-arr4
            arr5=np.array(rev2022)
            arr6=np.array(exp2022)
            NetIncome2022=arr5-arr6
            bvg_axis=np.arange(len(Beverages))
            plt.bar(bvg_axis+0.00,NetIncome2020, color='#A9561E',
                    edgecolor='#F5F5DC',width=0.25,label='2020 Net Income')
            plt.bar(bvg_axis+0.25,NetIncome2021,color='#FFFFCB',
                    edgecolor='#A0522D',width=0.25,label='2021 Net Income')
            plt.bar(bvg_axis+0.50,NetIncome2022,color='#D2691E',
                    edgecolor='#A9561E',width=0.25,label='2022 Net Income')
            plt.legend(loc='upper right')
            plt.xticks(bvg_axis,Beverages)
            plt.yticks(range(0,28000,2000))
            plt.show()
        elif OptBar==8:
            print("Closing Bar Graph Menu...")
            management_system()
        else:
            print("Option entered is invalid. Please try again.")
            management_system()
            
#option 7 in our main menu.          
def PieChart():
    OptPie=0
    df=pd.read_csv("prototype_menu .csv")
    Beverages=df["Beverages"]
    print("       ☆━━━━━━━━━━━━━━━━━━━☆")
    print("           Pie Chart Menu")
    print("       ☆━━━━━━━━━━━━━━━━━━━☆") 
    print("1. Item wise Revenue analysis.")
    print("2. Inventory Expenditure analysis.")
    print("3. Net Income analysis.")
    print("4. Return to Management System. ")
    print("       ☆━━━━━━━━━━━━━━━━━━━☆")
    while OptPie!=4:
        OptPie=int(input("Enter the Option no. for your desired Pie Chart:"))
        if OptPie==1:
            Revenue=[39400,41000,37200,47390,51600,
                     39000,31500,46000,41350,42100]
            colr=['#D2691E','#E6DAA6','#F5F5DC','#F5DEB3','#FFFFCB',
                  '#A9561E','#D1B26F','#A0522D','#F0E68C','#C20078']
            expl=[0,0,0,0,0.2,0,0,0,0,0]
            plt.title("Item wise Revenue analysis")
            plt.pie(Revenue,labels=Beverages,explode=expl,
                    colors=colr,autopct="%03.1f%%")
            plt.show()
        elif OptPie==2:
            Expenditure=[17200,23500,19400,25600,23300,
                         21600,14300,22700,21300,19400]
            colr=['#D2691E','#E6DAA6','#F5F5DC','#F5DEB3','#FFFFCB',
                  '#A9561E','#D1B26F','#A0522D','#F0E68C','#C20078']
            expl=[0,0,0,0.2,0,0,0,0,0,0]
            plt.title("Inventory Expenditure analysis")
            plt.pie(Expenditure,labels=Beverages,explode=expl,
                    colors=colr,autopct="%03.1f%%")
            plt.show()
        elif OptPie==3:
            array1=np.array(Revenue)
            array2=np.array(Expenditure)
            NetIncome=array1-array2
            colr=['#D2691E','#E6DAA6','#F5F5DC','#F5DEB3','#FFFFCB',
                  '#A9561E','#D1B26F','#A0522D','#F0E68C','#C20078']
            expl=[0,0,0,0,0.2,0,0,0,0,0]
            plt.title("Net Income analysis")
            plt.pie(NetIncome,labels=Beverages,explode=expl,
                    colors=colr,autopct="%03.1f%%")
            plt.show()
        elif OptPie==4:
            print("Closing Pie Chart menu...")
            management_system()
        else:
            print("Option entered is invalid. Please try again.")
            management_system()
            

#main menu           
def management_system():
    OptMenu=0
    print("         ☆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━☆")
    print("              Café Bistro Management System")
    print("         ☆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━☆")
    while OptMenu!=8:
        print("1. Show Café Menu.")
        print("2. Apply Filters to the Café Menu.")
        print("3. Add a new beverage item into the Menu. ")
        print("4. Delete a beverage item from the Café Menu")
        print("5. Add a new offer into the Discounts Menu")
        print("6. Analyse Café Stats with bar graphs")
        print("7. Analyse Café Stats with pie charts")
        print("8. Exit Management System.")
        OptMenu=int(input("Enter the option number of your choice:"))
        if OptMenu==1:
            ShowCafe()
        elif OptMenu==2:
            MenuFilter()
        elif OptMenu==3:
            EditMenu()
        elif OptMenu==4:
            DelMenuItem()
        elif OptMenu==5:
            DiscountsMenu()
        elif OptMenu==6:
            BarGraph()
        elif OptMenu==7:
            PieChart()
        elif OptMenu==8:
            print("Now closing the Café Bistro Management System. Thanks for visiting.")
            break
management_system()
