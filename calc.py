# Calculator coded with Python with Tkinter and customtkinter used for GUI. Comments are detailed as much as
# possible by me.

import customtkinter
from tkinter import * 
from tkinter import messagebox

# Used to store each number chosen to type in the input
inserted_numbers = []

# Used to store the full numbers in the input with the defined operation
saved_number = []

# Used for identifying how many times equal was clicked and preventing multiple clicks and errors.
equal_launched = 0
equal = None


# The main function where the operations are done in
def operation(operation_chosen):
    # Globalizing these two variables to use them
    global equal
    global equal_launched

    # If the operation chosen is not a valid operation, then it's most probably just a number to display...
    if operation_chosen not in ["clear", "clearall", "subtract", "multiply", "equal", "add", "divide"]:
        # If the length of saved_number is greater than 0 and length of inserted_numbers less than one...
        if len(saved_number) > 0 and len(inserted_numbers) < 1:
            # Put 0 as the default number in the label
            user_label.configure(text="0")

        # So the user can start a new operation after doing one with equal button, it empties the label
        # if equal_launched is 1.
        if equal_launched == 1:
            # Empty the label
            #print(len(saved_number))
            user_label.configure(text="")  
            equal_launched = 0          
        
        # If the text in the label is 0 then change it to empty 
        # This is to prevent 0 being shown on top of new numbers, as in:
        # If default 0 and you typed 123, without the following condition this will be shown: 0123
        if str(user_label.cget("text")) == '0':
            user_label.configure(text="")
        
        # Append the chosen number to inserted_numbers so it would be displayed afterwards.
        inserted_numbers.append(operation_chosen) 

        # As long as the length of the label is under 8, display it by adding the operation chosen
        # above whatever is already in the label.
        if len(str(user_label.cget("text"))) < 8:
            user_label.configure(text=str(user_label.cget("text")) + str(operation_chosen))
        
        # If it exists 8, show an error messagebox
        else:
            messagebox.showerror("ERR", "Maximum 8 numbers allowed.")
    
    # If the operation chosen is clear...
    elif operation_chosen == "clear":
        # Only if the number in the label isn't the same as the previous saved_number...
        if str(user_label.cget("text")) != str(saved_number):
            # And if the length of the inserted numbers isn't 0...
            if len(inserted_numbers) != 0:
                # Delete the last number from the list
                del inserted_numbers[-1]
        
            # Asign the full_sum variable used to add (string) the inserted numbers
            full_sum = ''

            # For each number in inserted_numbers...
            for i in inserted_numbers:
                # Append to each own next to each other as string.
                full_sum = full_sum + str(i)

            # If the length of inserted_numbers is 0, then asign full_sum to 0 as well
            if len(inserted_numbers) == 0:
                full_sum = 0
        
            # print(full_sum)

            # If the last saved number is 0, then put the label as the previous full_number.
            if len(saved_number) == 0:
                user_label.configure(text=str(full_sum))
            # If it's not 0, then asign the label the first saved number
            else:
                user_label.configure(text=str(saved_number[0][0]))

    # If the operation chosen is clearall...
    elif operation_chosen == "clearall": 
        # Clear the inserted numbers AND the last saved number, with changing the label to 0
        inserted_numbers.clear()
        saved_number.clear()
        user_label.configure(text="0")

    # If it's none of the above, then it's an operation
    else:

        # If the operation chosen is [add/subtract/multiply/divide/equal]...
        if operation_chosen == "add":
            # Append to the saved_number the inserted text with the operation chosen [+/-/x/ / /=]
            saved_number.append((str(user_label.cget("text")), "+"))
        elif operation_chosen == "subtract":
            saved_number.append((str(user_label.cget("text")), "-"))
        elif operation_chosen == "multiply":
            saved_number.append((str(user_label.cget("text")), "x"))
        elif operation_chosen == "divide":
            saved_number.append((str(user_label.cget("text")), "/"))
        elif operation_chosen == "equal" and equal_launched == 0:
            saved_number.append((str(user_label.cget("text")), "="))

        # Clear the inserted numbers.
        inserted_numbers.clear()

        # If equal isn't None, meaning the user clicked the equal button, then
        # asign sum equal to the result you got previously. That way it would show
        # and calculate upon that amount.
        if equal != None:
            sum = equal
        # If the operation chosen is add then asign sum to 0 so it would just add up on it
        # In case of add this won't change anything but the other functions are set to None
        elif operation_chosen == "add":
            sum = 0
        # Other functions set to None so it won't operate with 0, for example if you do 
        # x 2 with sum=0 it will give 0, but in this case the operation will change as seen later
        else:
            sum = None

        # print("\n\nBefore saved number: ", saved_number)

        # to_consider_amount is used if you, for example, chose 2 + 1 and then directly clicked
        # x, it will first do 2+1 =3 then it will allow you to do the multiplication with another number.
        # This process is done at the end of else in the for i loop, code to identify: TCA
        to_consider_amount = None

        # If the length of the last saved_number is greater than 1, then proceed with the operation
        if len(saved_number) > 1:
            # For each saved number in saved_number...
            for i in saved_number:

                # If the operation is add, and the i[1] is +
                if operation_chosen == "add" and i[1] == "+":
                    #print("\nAdd")
                    
                    # And if there isn't a to_consider amount, simply add the last sum with the current
                    # number from the loop
                    if to_consider_amount == None:
                        sum = float(sum) + float(i[0])

                    # If there is a to_consider amount, operate on it first
                    else:
                        #print("To consider amount: ", to_consider_amount[0])
                        #print("To do operation: ", to_consider_amount[1])
                        # According to the operation in to_consider_amount[1], do the operation
                        # by adding/subtracting/multiplying/dividing on the current number in the loop
                        if to_consider_amount[1] == "-":
                            sum = to_consider_amount[0] - float(i[0])
                        elif to_consider_amount[1] == "x":
                            sum = to_consider_amount[0] * float(i[0])                        
                        elif to_consider_amount[1] == "/":
                            sum = to_consider_amount[0] / float(i[0])  
                        elif to_consider_amount[1] == "+":
                            sum = to_consider_amount[0] + float(i[0])  

                    # Restart equal_launched to 0 so you would be able to click Enter again.
                    equal_launched = 0


                # If the operation chosen is Subtracting...
                elif operation_chosen == "subtract" and i[1] == "-":
                    #print("\nSubtract")
                    # If the to_consider_amount is None...
                    if to_consider_amount == None:
                        # If the sum is None, then asign the current number from the loop
                        # as sum. That way it won't be 0. If this was removed, same with
                        # asigning sum above on line 116, then it will do the operation
                        # as if there is 0. This happens on the first number
                        # you insert.
                        if sum == None:
                            #print("Pre-action Normal")
                            sum = float(i[0])
                            #print(sum)
                        # If it isn't None, then normally subtract the sum asigned on line 170
                        # with the one from the loop which is what the user wanted to subtract it with.
                        else:
                            #print("Normal")
                            sum = float(sum) - float(i[0])
                            #print(sum)
                    
                    # The below is the same as the addition.
                    else:
                        #print("To consider amount: ", to_consider_amount[0])
                        #print("To do operation: ", to_consider_amount[1])
                        if to_consider_amount[1] == "-":
                            sum = to_consider_amount[0] - float(i[0])
                        elif to_consider_amount[1] == "x":
                            sum = to_consider_amount[0] * float(i[0])                        
                        elif to_consider_amount[1] == "/":
                            sum = to_consider_amount[0] / float(i[0])  
                        elif to_consider_amount[1] == "+":
                            sum = to_consider_amount[0] + float(i[0]) 

                    equal_launched = 0

                # Same as subtract
                elif operation_chosen == "multiply" and i[1] == "x":
                    #print("\nMultiply")
                    if to_consider_amount == None:
                        if sum == None:
                            #print("Pre-action Normal")
                            sum = float(i[0])
                            #print(sum)
                        else:
                            #print("Normal")
                            sum = float(sum) * float(i[0])
                            #print(sum)
                    else:
                        #print("To consider amount: ", to_consider_amount[0])
                        #print("To do operation: ", to_consider_amount[1])
                        if to_consider_amount[1] == "-":
                            sum = to_consider_amount[0] - float(i[0])
                        elif to_consider_amount[1] == "x":
                            sum = to_consider_amount[0] * float(i[0])                        
                        elif to_consider_amount[1] == "/":
                            sum = to_consider_amount[0] / float(i[0])  
                        elif to_consider_amount[1] == "+":
                            sum = to_consider_amount[0] + float(i[0]) 

                    equal_launched = 0

                # Same as subtract/multiply
                elif operation_chosen == "divide" and i[1] == "/":
                    #print("\nDivide")
                    if to_consider_amount == None:
                        if sum == None:
                            #print("Pre-action Normal")
                            sum = float(i[0])
                            #print(sum)
                        else:
                            #print("Normal")
                            sum = float(sum) / float(i[0])
                            #print(sum)
                    else:
                        #print("To consider amount: ", to_consider_amount[0])
                        #print("To do operation: ", to_consider_amount[1])
                        if to_consider_amount[1] == "-":
                            sum = to_consider_amount[0] - float(i[0])
                        elif to_consider_amount[1] == "x":
                            sum = to_consider_amount[0] * float(i[0])                        
                        elif to_consider_amount[1] == "/":
                            sum = to_consider_amount[0] / float(i[0])  
                        elif to_consider_amount[1] == "+":
                            sum = to_consider_amount[0] + float(i[0]) 

                    equal_launched = 0

                # If the operation chosen is equal, and the i[1] is =, AND to_consider_amount isn't None,
                # with equal_launched being 0 (to prevent couple of equal clicks)...
                elif operation_chosen == "equal" and i[1] == "=" and to_consider_amount != None and equal_launched == 0:
                        # Do calculation according to the sign chosen.
                        if to_consider_amount[1] == "-":
                            equal = to_consider_amount[0] - float(i[0])
                        elif to_consider_amount[1] == "x":
                            equal = to_consider_amount[0] * float(i[0])                        
                        elif to_consider_amount[1] == "/":
                            equal = to_consider_amount[0] / float(i[0])  
                        elif to_consider_amount[1] == "+":
                            equal = to_consider_amount[0] + float(i[0])  

                        # Trigger equal_launched to 1
                        equal_launched = 1
                        
                # Code to identify TCA, sets to_consider_amount the 
                # float of the integer from the loop and its operation to be calculated 
                # afterwards.
                else:
                    to_consider_amount = (float(i[0]), i[1])
                    # print("Empty")


            saved_number.clear()
            if operation_chosen == "add":
                saved_number.append((str(sum), "+"))
            elif operation_chosen == "subtract": 
                saved_number.append((str(sum), "-"))
            elif operation_chosen == "multiply":
                saved_number.append((str(sum), "x"))
            elif operation_chosen == "divide":
                saved_number.append((str(sum), "/"))
            elif operation_chosen == "equal" and equal_launched == 0:
                saved_number.append((str(equal), "="))

            if operation_chosen == "equal":
                if len(str(equal)) < 9:
                    print(equal)
                    # Split the result. We have to identify if it's a float or not, and my way
                    # to do that is to first split the result. Then if the result of [1] 
                    # is 0 then it can be an integer safely, so we can safely display it as an 
                    # integer. Or else, display it as a float normally.
                    split = str(equal).split(".")
                    #print(split)

                    if split[1] == '0':
                        user_label.configure(text=str(int(equal)))
                    else:
                        user_label.configure(text=str(equal))
                else:
                    messagebox.showerror("ERR", "Result exceeds limit 8.")
            else:
                if len(str(sum)) < 9:
                    print(sum)
                    split = str(sum).split(".")
                    #print(split)

                    if split[1] == '0':
                        user_label.configure(text=str(int(sum)))
                    else:
                        user_label.configure(text=str(sum))
                else:
                    messagebox.showerror("ERR", "Result exceeds limit 8.")

    
    #print("Inserted numbers: ", inserted_numbers)
    #print("Saved number: ", saved_number)
        

# Primary root of Tkinter GUI with its window title
root = customtkinter.CTk()
root.title("Python Calculator Project")

# The label by which the inserted/calculated amounts will be displayed on
user_label = customtkinter.CTkLabel(root, text='0', width=120, height=40, font=customtkinter.CTkFont(size=16), fg_color=("lightgray", "#343638"), corner_radius=50)
user_label.pack(pady=10)

# The first/primary frame where the C (Clear) and AC (Clear All) buttons are disabled
primary_num_frame = customtkinter.CTkFrame(root, fg_color='transparent')
primary_num_frame.pack()
clear = customtkinter.CTkButton(primary_num_frame, text="C", width=40, height=40, cursor="hand2", command=lambda: operation("clear")).pack(side=LEFT, padx=5, pady=10)
clearall = customtkinter.CTkButton(primary_num_frame, text="AC", width=40,  height=40,cursor="hand2", command=lambda: operation("clearall")).pack(side=LEFT, padx=5)

# Binding the keyboard buttons to its functions, c for clear and the ESC button for clearall
root.bind("<c>", lambda e: operation("clear"))
root.bind("<Escape>", lambda e: operation("clearall"))

# The second frame where the numbers 7-9 are displayed, and the dividing button /
first_num_frame = customtkinter.CTkFrame(root, fg_color='transparent')
first_num_frame.pack()
seven = customtkinter.CTkButton(first_num_frame, text="7", width=40, height=40, cursor="hand2", command=lambda: operation("7")).pack(side=LEFT, padx=5)
eight = customtkinter.CTkButton(first_num_frame, text="8", width=40, height=40, cursor="hand2", command=lambda: operation("8")).pack(side=LEFT, padx=5)
nine = customtkinter.CTkButton(first_num_frame, text="9", width=40, height=40, cursor="hand2", command=lambda: operation("9")).pack(side=LEFT, padx=5)
divide = customtkinter.CTkButton(first_num_frame, text="/", width=40, height=40, cursor="hand2", command=lambda: operation("divide")).pack(side=LEFT, padx=5)

# Binding the keyboard buttons to its functions
root.bind("<Key-7>", lambda e: operation("7"))
root.bind("<Key-8>", lambda e: operation("8"))
root.bind("<Key-9>", lambda e: operation("9"))
root.bind("</>", lambda e: operation("divide"))

# The third frame where numbers 4-6 are displayed, and the multiplying button x
second_num_frame = customtkinter.CTkFrame(root, fg_color='transparent')
second_num_frame.pack()
four = customtkinter.CTkButton(second_num_frame, text="4", width=40, height=40, cursor="hand2", command=lambda: operation("4")).pack(side=LEFT, padx=5, pady=10)
five = customtkinter.CTkButton(second_num_frame, text="5", width=40, height=40, cursor="hand2", command=lambda: operation("5")).pack(side=LEFT, padx=5)
six = customtkinter.CTkButton(second_num_frame, text="6", width=40, height=40, cursor="hand2", command=lambda: operation("6")).pack(side=LEFT, padx=5)
multiply = customtkinter.CTkButton(second_num_frame, text="x", width=40, height=40, cursor="hand2", command=lambda: operation("multiply")).pack(side=LEFT, padx=5)

# Binding the keyboard buttons to its functions
root.bind("<Key-4>", lambda e: operation("4"))
root.bind("<Key-5>", lambda e: operation("5"))
root.bind("<Key-6>", lambda e: operation("6"))
root.bind("<*>", lambda e: operation("multiply"))

# The fourth frame where the numbers 1-3 are displayed, and the equal button =
third_num_frame = customtkinter.CTkFrame(root, fg_color='transparent')
third_num_frame.pack()
one = customtkinter.CTkButton(third_num_frame, text="1", width=40, height=40, cursor="hand2", command=lambda: operation("1")).pack(side=LEFT, padx=5)
two = customtkinter.CTkButton(third_num_frame, text="2", width=40, height=40, cursor="hand2", command=lambda: operation("2")).pack(side=LEFT, padx=5)
three = customtkinter.CTkButton(third_num_frame, text="3", width=40, height=40, cursor="hand2", command=lambda: operation("3")).pack(side=LEFT, padx=5)
equal = customtkinter.CTkButton(third_num_frame, text="=", width=40, height=40, cursor="hand2", command=lambda: operation("equal")).pack(side=LEFT, padx=5)

# Binding the keyboard buttons to its functions
root.bind("<Key-1>", lambda e: operation("1"))
root.bind("<Key-2>", lambda e: operation("2"))
root.bind("<Key-3>", lambda e: operation("3"))
root.bind("<Return>", lambda e: operation("equal"))

# The fifth frame where the number 0, plus sign +, and minus sign - are displayed
fourth_num_frame = customtkinter.CTkFrame(root, fg_color='transparent')
fourth_num_frame.pack()
zero = customtkinter.CTkButton(fourth_num_frame, text="0", width=90, height=40, cursor="hand2", command=lambda: operation("0")).pack(side=LEFT, padx=5, pady=10)
plus = customtkinter.CTkButton(fourth_num_frame, text="+", width=40, height=40, cursor="hand2", command=lambda: operation("add")).pack(side=LEFT, padx=5)
minus = customtkinter.CTkButton(fourth_num_frame, text="-", width=40, height=40, cursor="hand2", command=lambda: operation("subtract")).pack(side=LEFT, padx=5)

# Binding the keyboard buttons to its functions
root.bind("<Key-0>", lambda e: operation("0"))
root.bind("<+>", lambda e: operation("add"))
root.bind("<minus>", lambda e: operation("subtract"))

# The loop by which the root is running in
root.mainloop()