from tkinter import *
import random
import time
import datetime

anything = Tk()   
anything.geometry('1350x50+0+0')
anything.title('Cafe Management Systems')
anything.configure(background = 'black')

#basic window created


Tops = Frame(anything, width = 1350, height = 100, bd = 14, relief = 'raise')
Tops.pack(side = TOP)

f1 = Frame(anything, width = 900, height = 650, bd = 8, relief = 'raise')
f1.pack(side = LEFT)

f2 = Frame(anything, width = 440, height = 650, bd = 8, relief = 'raise')
f2.pack(side = RIGHT)


f1a = Frame(f1, width = 90, height = 330, bd = 8, relief = 'raise')
f1a.pack(side = TOP)

f2a = Frame(f1, width = 90, height = 320, bd = 6, relief = 'raise')
f2a.pack(side = BOTTOM)

ft2 = Frame(f2, width = 440, height = 450, bd = 12, relief = 'raise')
ft2.pack(side = TOP)

fb2 = Frame(f2, width = 440, height = 200, bd = 16, relief = 'raise')
fb2.pack(side = BOTTOM)

f1aa = Frame(f1a, width = 400, height = 330, bd = 16, relief = 'raise')
f1aa.pack(side = LEFT)

f1ab = Frame(f1a, width = 400, height = 330, bd = 16, relief = 'raise')
f1ab.pack(side = RIGHT)

f2aa = Frame(f2a, width = 450, height = 330, bd = 14, relief = 'raise')
f2aa.pack(side = LEFT)

f2ab = Frame(f2a, width = 450, height = 330, bd = 6, relief = 'raise')
f2ab.pack(side = RIGHT)


#Frames are created

Tops.configure (background = 'black')
f1.configure (background = 'black')
f2.configure (background = 'black')

lblInfo = Label(Tops, font  = ('arial', 70, 'bold'), text = 'Cafe Management Systems', bd = 10)
lblInfo.grid(row = 0, column = 0)



#method for exit






var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()

DateofOrder = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofCakes = StringVar()
CostofDrinks = StringVar()
ServiceCharge = StringVar()

E_Latte = StringVar()
E_Espresso = StringVar()
E_Iced_Latte = StringVar()
E_Vale_Coffee = StringVar()
E_Cappuccino = StringVar()
E_African_Coffee = StringVar()
E_American_Coffee = StringVar()
E_Iced_Cappuccino = StringVar()

E_Coffee_Cakes = StringVar()
E_Red_Velvet_Cake = StringVar()
E_Black_Forest_Cake = StringVar()
E_Boston_Cream_Cake = StringVar()
E_Lagos_Chocolate_Cake = StringVar()
E_Kilburn_Chocolate_Cake = StringVar()
E_Carlton_Hill_Chocolate_Cake = StringVar()
E_Queen_Park_Chocolate_Cake = StringVar()


E_Latte.set('0')
E_Espresso.set('0')
E_Iced_Latte.set('0')
E_Vale_Coffee.set('0')
E_Cappuccino.set('0')
E_African_Coffee.set('0')
E_American_Coffee.set('0')
E_Iced_Cappuccino.set('0')
E_Coffee_Cakes.set('0')
E_Red_Velvet_Cake.set('0')
E_Black_Forest_Cake.set('0')
E_Boston_Cream_Cake.set('0')
E_Lagos_Chocolate_Cake.set('0')
E_Kilburn_Chocolate_Cake.set('0')
E_Carlton_Hill_Chocolate_Cake.set('0')
E_Queen_Park_Chocolate_Cake.set('0')

DateofOrder.set(time.strftime('%d/%m/%Y'))

var1.set('0')
var2.set('0')
var3.set('0')
var4.set('0')
var5.set('0')
var6.set('0')
var7.set('0')
var8.set('0')
var9.set('0')
var10.set('0')
var11.set('0')
var12.set('0')
var13.set('0')
var14.set('0')
var15.set('0')
var16.set('0')
#Widget created
# f1aa == left hand box
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>DRINKS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
Latte = Checkbutton(f1aa, text='Latte\t', variable = var1, onvalue = 1, offvalue = 0, font  = ('arial', 18, 'bold')).grid(row = 0, sticky = W)
Espresso = Checkbutton(f1aa, text='Espresso \t\t', variable = var2, onvalue = 1, offvalue = 0, font  = ('arial', 18, 'bold')).grid(row = 1, sticky = W)
Iced_Latte = Checkbutton(f1aa, text='Iced Latte \t\t', variable = var3, onvalue = 1, offvalue = 0, font  = ('arial', 18, 'bold')).grid(row = 2, sticky = W)
Vale_Coffee = Checkbutton(f1aa, text='Vale_Coffee \t\t', variable = var4, onvalue = 1, offvalue = 0, font  = ('arial', 18, 'bold')).grid(row = 3, sticky = W)
Cappuccino  = Checkbutton(f1aa, text='Cappuccino \t\t', variable = var5, onvalue = 1, offvalue = 0, font  = ('arial', 18, 'bold')).grid(row = 4, sticky = W)
African_Coffee = Checkbutton(f1aa, text='African Coffee \t\t', variable = var6, onvalue = 1, offvalue = 0, font  = ('arial', 18, 'bold')).grid(row = 5, sticky = W)
American_Coffee = Checkbutton(f1aa, text='American Coffee \t\t', variable = var7, onvalue = 1, offvalue = 0, font  = ('arial', 18, 'bold')).grid(row = 6, sticky = W)
Iced_Cappuccino = Checkbutton(f1aa, text='Iced Cappuccino \t\t', variable = var8, onvalue = 1, offvalue = 0, font  = ('arial', 18, 'bold')).grid(row = 7, sticky = W)


#f1ab == right hand box
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>CAKES<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

CoffeeCake= Checkbutton(f1ab, text='Coffee Cake\t', variable = var9, onvalue = 1, offvalue = 0, font  = ('arial', 18, 'bold')).grid(row = 0, sticky = W)
Red_Velvet_Cake = Checkbutton(f1ab, text='Red Velvet Cake\t', variable = var10, onvalue = 1, offvalue = 0, font  = ('arial', 18, 'bold')).grid(row = 1, sticky = W)
Black_Forest_Cake = Checkbutton(f1ab, text='Black Forest Cake\t', variable = var11, onvalue = 1, offvalue = 0, font  = ('arial', 18, 'bold')).grid(row = 2, sticky = W)
Boston_Cream_Cake = Checkbutton(f1ab, text='Boston Cream Cake\t', variable = var12, onvalue = 1, offvalue = 0, font  = ('arial', 18, 'bold')).grid(row = 3, sticky = W)
Lagos_Chocolate_Cake = Checkbutton(f1ab, text='Lagos Chocolate Cake\t', variable = var13, onvalue = 1, offvalue = 0, font  = ('arial', 18, 'bold')).grid(row = 4, sticky = W)
Kilburn_Chocolate_Cake = Checkbutton(f1ab, text='Kilburn Chocolatee Cake\t', variable = var14, onvalue = 1, offvalue = 0, font  = ('arial', 18, 'bold')).grid(row = 5, sticky = W)
Carlton_Hill_Cake = Checkbutton(f1ab, text='Carlton Hill Cake\t', variable = var15, onvalue = 1, offvalue = 0, font  = ('arial', 18, 'bold')).grid(row = 6, sticky = W)
Queen_park_Cake = Checkbutton(f1ab, text='Queen's Park Chocolate Cake\t', variable = var16, onvalue = 1, offvalue = 0, font  = ('arial', 18, 'bold')).grid(row = 7, sticky = W)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Enter widget for DRINKS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
txtLatte = Entry(f1aa, font=('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left', textvariable = E_Latte, state = DISABLED)
txtLatte.grid(row = 0, column = 1)
txtEspresso = Entry(f1aa, font=('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left', textvariable = E_Espresso, state = DISABLED )
txtEspresso.grid(row = 1, column = 1)
txtIced_Latte = Entry(f1aa, font=('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left', textvariable = E_Iced_Latte, state = DISABLED )
txtIced_Latte.grid(row = 2, column = 1)
txtVale_Coffee = Entry(f1aa, font=('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left', textvariable = E_Vale_Coffee, state = DISABLED )
txtVale_Coffee.grid(row = 3, column = 1)
txtCappuccino = Entry(f1aa, font=('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left', textvariable = E_Cappuccino, state = DISABLED )
txtCappuccino.grid(row = 4, column = 1)
txtAfrican_Coffee = Entry(f1aa, font=('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left', textvariable = E_African_Coffee, state = DISABLED )
txtAfrican_Coffee.grid(row = 5, column = 1)
txtAmerican_Coffee = Entry(f1aa, font=('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left', textvariable = E_American_Coffee, state = DISABLED )
txtAmerican_Coffee.grid(row = 6, column = 1)
txtIced_Cappuccino = Entry(f1aa, font=('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left', textvariable = E_Cappuccino, state = DISABLED )
txtIced_Cappuccino.grid(row = 7, column = 1)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Enter widget for CAKES<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
txtCoffeeCake = Entry(f1ab, font=('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left', textvariable = E_Coffee_Cakes, state = DISABLED )
txtCoffeeCake.grid(row = 0, column = 1)
txtRed_Velvet_Cake = Entry(f1ab, font=('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left', textvariable = E_Red_Velvet_Cake, state = DISABLED )
txtRed_Velvet_Cake.grid(row = 1, column = 1)
txtBlack_Forest_Cake = Entry(f1ab, font=('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left', textvariable = E_Black_Forest_Cake, state = DISABLED )
txtBlack_Forest_Cake.grid(row = 2, column = 1)
txtBoston_Cream_Cake = Entry(f1ab, font=('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left', textvariable = E_Boston_Cream_Cake, state = DISABLED )
txtBoston_Cream_Cake.grid(row = 3, column = 1)
txtLagos_Chocolate_Cake = Entry(f1ab, font=('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left', textvariable = E_Lagos_Chocolate_Cake, state = DISABLED )
txtLagos_Chocolate_Cake.grid(row = 4, column = 1)
txtKilburn_Chocolate_Cake = Entry(f1ab, font=('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left', textvariable = E_Kilburn_Chocolate_Cake, state = DISABLED )
txtKilburn_Chocolate_Cake.grid(row = 5, column = 1)
txtCarlton_Hill_Cake = Entry(f1ab, font=('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left', textvariable = E_Carlton_Hill_Chocolate_Cake, state = DISABLED )
txtCarlton_Hill_Cake.grid(row = 6, column = 1)
txtQueen_park_Cake = Entry(f1ab, font=('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left', textvariable = E_Queen_Park_Chocolate_Cake, state = DISABLED )
txtQueen_park_Cake.grid(row = 7, column = 1)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>RECEIPT INFO<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
lblReceipt = Label(ft2, font=('arial', 12, 'bold'), text='Receipt',bd = 2).grid(row = 0, column = 0, sticky = W)
txtReceipt = Text(ft2, font=('arial', 11, 'bold'), bd = 8, width = 59)
txtReceipt.grid(row = 1, column = 0)



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Item INFO<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
lblCostofDrinks = Label(f2aa, font=('arial', 16, 'bold'), text = 'Cost of Drinks', bd = 8)
lblCostofDrinks.grid(row = 0, column = 0, sticky = W)
txtCostofDrinks = Entry(f2aa,font=('arial', 16, 'bold'), bd = 8, justify = 'left')
txtCostofDrinks.grid(row = 0, column = 1, sticky = W)

lblCostofCakes = Label(f2aa, font=('arial', 16, 'bold'), text = 'Cost of Cakes', bd = 8)
lblCostofCakes.grid(row = 1, column = 0, sticky = W)
txtCostofCakes = Entry(f2aa,font=('arial', 16, 'bold'), bd = 8, justify = 'left')
txtCostofCakes.grid(row = 1, column = 1, sticky = W)

lblServiceCharge = Label(f2aa, font=('arial', 16, 'bold'), text = 'Sevice charge', bd = 8)
lblServiceCharge.grid(row = 2, column = 0, sticky = W)
txtServiceCharge = Entry(f2aa,font=('arial', 16, 'bold'), bd = 8, justify = 'left')
txtServiceCharge.grid(row = 2, column = 1, sticky = W)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Payment INFO<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
lblPaidTax = Label(f2ab, font=('arial', 16, 'bold'), text = 'Tax', bd = 8)
lblPaidTax.grid(row = 0, column = 0, sticky = W)
txtPaidTax = Entry(f2ab,font=('arial', 16, 'bold'), bd = 8, justify = 'left')
txtPaidTax.grid(row = 0, column = 1, sticky = W)

lblSubTotal = Label(f2ab, font=('arial', 16, 'bold'), text = 'Sub Total', bd = 8)
lblSubTotal.grid(row = 1, column = 0, sticky = W)
txtSubTotal = Entry(f2ab,font=('arial', 16, 'bold'), bd = 8, justify = 'left')
txtSubTotal.grid(row = 1, column = 1, sticky = W)

lblTotal = Label(f2ab, font=('arial', 16, 'bold'), text = 'Total', bd = 8)
lblTotal.grid(row = 2, column = 0, sticky = W)
txtTotal = Entry(f2ab,font=('arial', 16, 'bold'), bd = 8, justify = 'left')
txtTotal.grid(row = 2, column = 1, sticky = W)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>BUTTONS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
btnTotal = Button(fb2, padx = 16, pady = 1, bd = 4, fg = 'black', font = ('arial', 16, 'bold'), width = 5, text = 'Total ').grid(row = 0, column = 0)
btnReceipt = Button(fb2, padx = 16, pady = 1, bd = 4, fg = 'black', font = ('arial', 16, 'bold'), width = 5, text = 'Receipt ').grid(row = 0, column = 1)
btnReset = Button(fb2, padx = 16, pady = 1, bd = 4, fg = 'black', font = ('arial', 16, 'bold'), width = 5, text = 'Reset ').grid(row = 0, column = 2)
btnExit = Button(fb2, padx = 16, pady = 1, bd = 4, fg = 'black', font = ('arial', 16, 'bold'), width = 5, text = 'Exit ', command = qExit).grid(row = 0, column = 3)

#methods

#method to find cost of each item(ide tea,coffee,etc)

def CostofItems():
    Item1=float(E_Latta.get())
    Item2=float(E_Coke.get())
    Item3=float(E_Iced_Latta.get())
    Item4=float(E_Coffee.get())
    Item5=float(E_Cappuccin.get())
    Item6=float(E_Tea.get()) 
    Item7=float(E_Cold_coffee.get())
    Item8=float(E_Beer.get())
    
    Item9=float(E_Coffee_cake.get()) 
    Item10=float(E_Black_forest.get())
    Item11=float(E_Cream_cake.get())
    Item12=float(E_Lagoos_cake.get())
    Item13=float(E_Fruit_cake.get())
    Item14=float(E_Chocolate_cake.get())
    Item15=float(E_Chocolava.get())
    Item16=float(E_Bread_cake.get())

    PriceofDrinks = (Item1 * 1.2) + (Item2 * 1.99) + (Item3 * 4.99) + (Item4 * 1.29) + (Item5 * 3.20) + (Item6 * 1.9) + (Item7 * 2.99) + (Item8 * 3.45)

    PriceofCakes = (Item9 * 1.2) + (Item10 * 1.99) + (Item11 * 4.99) + (Item12 * 1.29) + (Item13 * 3.20) + (Item14 * 1.9) + (Item15 * 2.99) + (Item16 * 3.45)

    DrinksPrice ="Rs", str ('%.2f'%(PriceofDrinks))

    CakesPrice ="Rs", str ('%.2f'%(PriceofCakes))

    CostofCakes.set(CakesPrice)

    CostofDrinks.set(DrinksPrice)

    SC= "Rs" , str('%.2f'%(1.59))
    ServiceCharge.set(SC)

    SubTotalofITEMS = "Rs" , str('%.2f'%(PriceofDrinks + PriceofCakes + 1.59))
    SubTotal.set(SubTotalofITEMS)

    Tax= "Rs" , str('%.2f'%((PriceofDrinks + PriceofCakes + 1.59)* 0.15))
    PaidTax.set(Tax)

    TT = ((PriceofDrinks + PriceofCakes + 1.59)*0.15)
    TC = "Rs" , str('%.2f'%(PriceofDrinks + PriceofCakes + 1.59 + TT))
    TotalCost.set(TC)

def qExit():
    qExit=messagebox.askyesno("Quit System","Do you want to quit?")
    if qExit > 0:
        root.destroy()
        return
        
        
def Reset():
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofDrinks.set("")
    CostofCakes.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0",END)
    
    E_Latta.set("0")
    E_Coke.set("0")
    E_Iced_Latta.set("0")
    E_Coffee.set("0")
    E_Cappuccin.set("0")
    E_Tea.set("0")
    E_Cold_coffee.set("0")
    E_Beer.set("0")

    E_Coffee_cake.set("0")
    E_Black_forest.set("0")
    E_Cream_cake.set("0")
    E_Lagoos_cake.set("0")
    E_Fruit_cake.set("0")
    E_Chocolate_cake.set("0")
    E_Chocolava.set("0")
    E_Bread_cake.set("0")

             
    var1.set(0)    
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)

    txtLatta.configure(state=DISABLED)
    txtCoke.configure(state=DISABLED)
    txtIced_Latta.configure(state=DISABLED)
    txtCoffee.configure(state=DISABLED)
    txtCappuccin.configure(state=DISABLED)
    txtTea.configure(state=DISABLED)
    txtCold_coffee.configure(state=DISABLED)
    txtBeer.configure(state=DISABLED)
    txtCoffee_cake.configure(state=DISABLED)
    txtBlack_forest.configure(state=DISABLED)
    txtCream_cake.configure(state=DISABLED)
    txtLagoos_cake.configure(state=DISABLED)
    txtFruit_cake.configure(state=DISABLED)
    txtChocolate_cake.configure(state=DISABLED)
    txtChocolava.configure(state=DISABLED)
    txtBread_cake.configure(state=DISABLED)
#======================================================================RECEIPT============================================================================

def Receipt():
    txtReceipt.delete("1.0",END)
    x = random.randint(10908, 500876)
    randomRef = str(x)
    Receipt_Ref.set("BILL"+ randomRef)

    txtReceipt.insert(END,'Receipt Ref:\t\t\t'+Receipt_Ref.get() + '\t\t'+ DateofOrder.get()+"\n")
    txtReceipt.insert(END,'Items\t\t\t'+"Cost of Items \n")
    txtReceipt.insert(END,'Latta:\t\t\t\t'+ E_Latta.get()+"\n")
    txtReceipt.insert(END,'Coke:\t\t\t\t'+ E_Coke.get()+"\n")
    txtReceipt.insert(END,'Iced_Latta:\t\t\t\t'+ E_Iced_Latta.get()+"\n")
    txtReceipt.insert(END,'Coffee:\t\t\t\t'+ E_Coffee.get()+"\n")
    txtReceipt.insert(END,'Cappuccin:\t\t\t\t'+ E_Cappuccin.get()+"\n")
    txtReceipt.insert(END,'Tea:\t\t\t\t'+ E_Tea.get()+"\n")
    txtReceipt.insert(END,'Cold_coffee:\t\t\t\t'+ E_Cold_coffee.get()+"\n")
    txtReceipt.insert(END,'Beer:\t\t\t\t'+ E_Beer.get()+"\n")
    txtReceipt.insert(END,'Coffee_cake:\t\t\t\t'+ E_Coffee_cake.get()+"\n")
    txtReceipt.insert(END,'Black_forest:\t\t\t\t'+ E_Black_forest.get()+"\n")
    txtReceipt.insert(END,'Cream_cake:\t\t\t\t'+ E_Cream_cake.get()+"\n")
    txtReceipt.insert(END,'Lagoos_cake:\t\t\t\t'+E_Lagoos_cake.get()+"\n")
    txtReceipt.insert(END,'Fruit_cake:\t\t\t\t'+ E_Fruit_cake.get()+"\n")
    txtReceipt.insert(END,'Chocolate_cake:\t\t\t\t'+ E_Chocolate_cake.get()+"\n")
    txtReceipt.insert(END,'Chocolava:\t\t\t\t'+ E_Chocolava.get()+"\n")
    txtReceipt.insert(END,'Bread_cake:\t\t\t\t'+ E_Bread_cake.get()+"\n")
    txtReceipt.insert(END,'Cost of Drinks:\t\t'+ CostofDrinks.get()+ '\t\tTax Paid:\t' + PaidTax.get() +"\n")
    txtReceipt.insert(END,'Cost of Cakes:\t\t'+ CostofCakes.get()+ '\t\tSubTotal:\t' +SubTotal.get() +"\n")
    txtReceipt.insert(END,'Service Charge:\t\t'+ ServiceCharge.get()+ '\t\tTotal Cost:\t' + TotalCost.get() +"\n")
   
#=========================================================================CHECKBOX==========================================================================

def chkbutton_value():
    if (var1.get() == 1):
        txtLatta.configure(state= NORMAL)
    elif var1.get()== 0:
            txtLatta.configure(state= DISABLED)
            E_Latta.set("0")
    if (var2.get() == 1):
        txtCoke.configure(state=NORMAL)
    elif var2.get()== 0:
            txtCoke.configure(state=DISABLED)
            E_Coke.set("0")
    if (var3.get() == 1):
        txtIced_Latta.configure(state=NORMAL)
    elif var3.get()== 0:
            txtIced_Latta.configure(state=DISABLED)
            E_Iced_Latta.set("0")
    if (var4.get() == 1):
        txtCoffee.configure(state=NORMAL)
    elif var4.get()== 0:
            txtCoffee.configure(state=DISABLED)
            E_Coffee.set("0")
    if (var5.get() == 1):
        txtCappuccin.configure(state=NORMAL)
    elif var5.get()== 0:
            txtCappuccin.configure(state=DISABLED)
            E_Cappuccin.set("0")
    if (var6.get() == 1):
        txtTea.configure(state=NORMAL)
    elif var6.get()== 0:
            txtTea.configure(state=DISABLED)
            E_Tea.set("0")
    if (var7.get() == 1):
        txtCold_coffee.configure(state=NORMAL)
    elif var7.get()== 0:
            txtCold_coffee.configure(state=DISABLED)
            E_Cold_coffee.set("0")
    if (var8.get() == 1):
        txtBeer.configure(state=NORMAL)
    elif var8.get()==0:
            txtBeer.configure(state=DISABLED)
            E_Beer.set("0")
    if (var9.get() == 1):
        txtCoffee_cake.configure(state=NORMAL)
    elif var9.get()== 0:
            txtCoffee_cake.configure(state=DISABLED)
            E_Coffee_cake.set("0")
    if (var10.get() == 1):
        txtBlack_forest.configure(state=NORMAL)
    elif var10.get()== 0:
            txtBlack_forest.configure(state=DISABLED)
            E_Black_forest.set("0")
    if (var11.get() == 1):
        txtCream_cake.configure(state=NORMAL)
    elif var11.get()== 0:
            txtCream_cake.configure(state=DISABLED)
            E_Cream_cake.set("0")
    if (var12.get() == 1):
        txtLagoos_cake.configure(state=NORMAL)
    elif var12.get()== 0:
            txtLagoos_cake.configure(state=DISABLED)
            E_Lagoos_cake.set("0")
    if (var13.get() == 1):
        txtFruit_cake.configure(state=NORMAL)
    elif var13.get()== 0:
            txtFruit_cake.configure(state=DISABLED)
            E_Fruit_cake.set("0")
    if (var14.get() == 1):
        txtChocolate_cake.configure(state=NORMAL)
    elif var14.get()== 0:
            txtChocolate_cake.configure(state=DISABLED)
            E_Chocolate_cake.set("0")
    if (var15.get() == 1):
        txtChocolava.configure(state=NORMAL)
    elif var15.get()== 0:
            txtChocolava.configure(state=DISABLED)
            E_Chocolava.set("0")
    if (var16.get() == 1):
        txtBread_cake.configure(state=NORMAL)
    elif var16.get()== 0:
            txtBread_cake.configure(state=DISABLED)
            E_Bread_cake.set("0")




anything.mainloop()
