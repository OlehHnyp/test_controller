from controller import Controller
from functions import functions

if __name__ == "__main__":
    session = Controller(functions)
    print("Hello.")

    while not session.done:
        entered_command = input(
            "Enter the task name to execute it, " +
            "\"display tasks\" to display all task\'s names or \"exit\" to quit: ")
        if not entered_command:
            continue
        elif entered_command == "exit":
            print("Program closed")
            session.done = True
        elif entered_command == "display tasks":
            print(session.display_tasks())
        else:
            result = session.run_function(entered_command)
            if result is False:
                print("Wrong input")
