# ------------------------------------------------------------------------ #
# Title: Assignment 06
# Description: Working with functions in a class,
# When the program starts, load each "row" of data
# in "ToDoToDoList.txt" into a python Dictionary.
# Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2022,Created started script
# NDaharia,05.25.2022,Modified code to complete assignment 6

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strToDoFile = "ToDoFile.txt"  # Name of data file
objFile = None  # Object that represents a file
dicRow = {}  # Row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # List that acts as a 'table' of rows
strChoice = ""  # Captures the selection of user options
strPriority = ""  # Captures the user priority data
strStatus = ""  # Captures the status of processing functions
strTask = ""  # Captures the user task data



# Processing  --------------------------------------------------------------- #

class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # to clear current data
        file = open(file_name, "r")
        for line in file:
            task, priority = line.split(",")
            row = {"Task": task.strip(), "Priority": priority.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows, 'Success'

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """
        :param task: inputted task that user wants to add to list
        :param priority: inputted priority user wants to add to list
        :param list_of_rows: the list of dictionary rows tasks and priorities are appended to
        :return: the updated list of rows with the added tasks
        """
        list_of_rows.append({"Task": task, "Priority": priority})
        return list_of_rows, 'Success'

    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        """
        :param task: inputted task the user wants to delete the task/priority pair for
        :param list_of_rows: the list of dictionary rows tasks and priorities are saved in
        :return: the updated list_of_rows with the inputted task row removed (if it was in it),
                whether the entered task was successfully removed or whether it was not found
        """
        Present = False
        for row in list_of_rows:
            if row["Task"].lower() == task.lower():
                list_of_rows.remove(row)
                Present = True
        if Present == True:
            return list_of_rows, 'Success'
        else:
            return list_of_rows, 'Task not found. See available current tasks.'

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """
        :param file_name: the name of the file that the data will be written to
        :param list_of_rows: the list of dictionaries the data is saved in
        :return: list_of_rows that has just been written to the file
        """
        file = open(file_name, "w")
        for row in list_of_rows:
            file.write(row["Task"] + "," + row["Priority"] + "\n")
        file.close()
        return list_of_rows, 'Success'


# Presentation (Input/Output)  -------------------------------------------- #

class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user
        :return:
        """
        print(
            '''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
        print()

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user
        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()
        return choice

    @staticmethod
    def print_current_Tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows
        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user
        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing
        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority():
        pass
        """
        :return: returns user inputted task, priority data
        """
        task = input("Enter task you wish to be added: ")
        priority = input("Enter priority of the added task [Low, Medium, High]: ")
        return task, priority  # to print in format: return task, priority

    @staticmethod
    def input_task_to_remove():
        pass
        """
        :return: returns the task that user wants to remove the row of
        """
        task = input("Enter task to be removed: ")
        return task

        # return task


# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
strToDoFile: str = "ToDoFile.txt"  # read file data

# Step 2 - Display a menu of choices to the user

while True:
    # Step 3 To see current data
    IO.print_current_Tasks_in_list(lstTable)  # To see the current data in the list/table
    IO.print_menu_Tasks()  # to see menu
    strChoice = IO.input_menu_choice()  # to see menu option

    # Step 4 - Process menu choice
    if strChoice.strip() == '1':  # Add a new Task
        strTask, strPriority = IO.input_new_task_and_priority()  # Capture the returned values from the function in variables
        lstTable, strStatus = Processor.add_data_to_list(
            strTask, strPriority, lstTable)  # Add captured data to the list
        IO.print_current_Tasks_in_list(lstTable)  # To see the updated list
        IO.input_press_to_continue(strStatus)  # Ask the User to press enter to continue after displaying 'Success'
        continue  # to see the menu

    elif strChoice == '2':  # Remove an existing Task
        strTask = IO.input_task_to_remove()  # user inputs task to remove
        lstTable, strStatus = Processor.remove_data_from_list(
            strTask, lstTable)  # row of entered task is removed
        IO.print_current_Tasks_in_list(lstTable)  # displays updated list of current tasks
        IO.input_press_to_continue(strStatus)
        continue  # to see the menu

    elif strChoice == '3':  # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            lstTable, strStatus = Processor.write_data_to_file(
                strToDoFile, lstTable)  # write data to file & save return variables
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to see the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            lstTable, strStatus = Processor.read_data_from_file(strToDoFile, lstTable)
            IO.print_current_Tasks_in_list(lstTable)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("File Reload Cancelled!")
        continue  # to see the menu

    elif strChoice == '5':  # Exit Program
        print("Goodbye!")
        break  # and Exit
