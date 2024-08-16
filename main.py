from tkinter import *


#Calculator class
class Calculator:


        #__init__ method
        def __init__(self, master):
                """

                method that initializes the object's atributes
                """

                #assign reference to the main window of the application
                self.master = master

                #add a name to the application
                master.title("Calculator dyal 3li")

                #create line where we display the equation
                self.equation = Entry(master, width=36, borderwidth=5)

                #assign a position for the equation line in the main application window
                self.equation.grid(row=0, column=4, padx=10, pady=10)

                #execute the .createButton() method
                self.createButton()            

        def createButton(self):
                """
                method that creates buttons
                """

                #create each button object
                b0 = self.addButton(0)
                b1 = self.addButton(1)
                b2 = self.addButton(2)
                b3 = self.addButton(3)
                b4 = self.addButton(4)
                b5 = self.addButton(5)
                b6 = self.addButton(6)
                b7 = self.addButton(7)
                b8 = self.addButton(8)
                b9 = self.addButton(9)
                b_add = self.addButton('+')
                b_sub = self.addButton('-')
                b_mult = self.addButton('*')
                b_div = self.addButton('/')
                b_clear = self.addButton('c')
                b_equal = self.addButton('=')

                #arrange the buttons into rows
                row1 = [b7, b8, b9, b_add]
                row2 = [b4, b5, b6, b_sub]
                row3 = [b1, b2, b3, b_mult]
                row4 = [b_clear, b0, b_equal, b_div]

                #assign each button to the main screen of the application
                r = 1
                for row in [row1, row2, row3, row4]:
                        c = 0
                        for b in row:
                            b.grid(row=r, column=c, columnspan=1)
                            c += 1
                        r += 1


        def addButton(self, value):
            """
            Method that adds the buttons to the main screen of the application
            """

            return Button(
                self.master,
                text=value,
                width=9,
                command=lambda: self.clickButton(str(value)))

        def clickButton(self, value):
            """
            method that adds actions to the buttons of the calculator app
            """

            #get the equation entered by the user
            current_equation = str(self.equation.get())

            #if a user clicks "c", clear the quatin line
            if value == "c":
                self.equation.delete(-1, END)

            #if a user clicks "=", compute the answer and display in the equation line
            elif value == "=":
                answer = str(eval(current_equation))
                self.equation.delete(-1, END)
                self.equation.insert(0, answer)

            #if user clicks any other button, add the value to the equation line
            else:
                self.equation.delete(0, END)
                self.equation.insert(0, current_equation + value)

if __name__ == "__main__":
        
        #create the main window of the application
        root = Tk()

        #tell the calculator class to use this main window
        my_gui = Calculator(root)

        #executable look on the application
        root.mainloop()