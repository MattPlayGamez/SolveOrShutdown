import time
import random
import subprocess
import tkinter as tk
from tkinter import font as tkfont
from threading import Timer
teken = ""
def is_process_running(process_name):
    try:
        # Check for the process in the list of running processes
        output = subprocess.check_output('tasklist', shell=True).decode()
        return process_name in output
    except Exception as e:
        print(e)
        return False

def shutdown_pc():
    print("Shutting down")
    #subprocess.run(["shutdown", "/s", "/t", "0"])

def run_gui(teken):
    def on_check_question():
        try:
            if teken=="+":
                split_question = question_label['text'].split('+')
                print(f"First part: {split_question[0]}, second: {split_question[1]}")
                correct_answer = int(split_question[0]) + int(split_question[1])
                answer_from_form = int(input_answer.get())
            elif teken=="-":
                split_question = question_label['text'].split('-')
                print(f"First part: {split_question[0]}, second: {split_question[1]}")
                correct_answer = int(split_question[0]) - int(split_question[1])
                answer_from_form = int(input_answer.get())
            elif teken=="*":
                split_question = question_label['text'].split('*')
                print(f"First part: {split_question[0]}, second: {split_question[1]}")
                correct_answer = int(split_question[0]) * int(split_question[1])
                answer_from_form = int(input_answer.get())
            if correct_answer != answer_from_form:
                shutdown_pc()
            else:
                if shutdown_timer.is_alive():
                    shutdown_timer.cancel()  # Cancel the shutdown if the answer is correct
                root.destroy()  # Close the GUI window
        except Exception as e:
            print(e)

    def update_timer():
        nonlocal time_left
        if time_left > 0:
            time_left -= 1
            timer_label.config(text=f"Time left: {time_left // 60}:{time_left % 60:02d}")
            root.after(1000, update_timer)  # Schedule the function to run again after 1 second
        else:
            shutdown_pc()  # Shutdown if time runs out

    root = tk.Tk()
    root.title("Solve Or Shutdown")
    root.geometry("450x300")
    root.resizable(False, False)

    lbl_new_label = tk.Label(root, text="Solve Or Shutdown", font=tkfont.Font(family="Times New Roman", size=25))
    lbl_new_label.pack(pady=10)

    random_number1 = 0
    random_number2 = 0
    if teken =="+":
        random_number1 = random.randint(0, 1000)
        random_number2 = random.randint(0, 1000)
    elif teken =="-":
        random_number2 = random.randint(0, 1000)
        random_number1 = random.randint(random_number2, 2000)
    elif teken =="*":
        random_number1 = random.randint(0, 100)
        random_number2 = random.randint(0, 100)
    question_label = tk.Label(root, text=f"{random_number1}{teken}{random_number2}", font=tkfont.Font(family="Times New Roman", size=15))
    question_label.pack(pady=10)

    input_answer = tk.Entry(root, justify="center", font=tkfont.Font(size=15))
    input_answer.pack(pady=10)

    check_question_button = tk.Button(root, text="Verzend", command=on_check_question)
    check_question_button.pack(pady=20)

    time_left = 5 * 60  # 5 minutes in seconds
    timer_label = tk.Label(root, text=f"Time left: {time_left // 60}:{time_left % 60:02d}", font=tkfont.Font(family="Times New Roman", size=15))
    timer_label.pack(pady=10)

    update_timer()  # Start the countdown

    # Schedule shutdown in 1 hour
    shutdown_timer = Timer(1 * 60 * 60, shutdown_pc)
    shutdown_timer.start()

    root.mainloop()

if __name__ == "__main__":
    random.seed()

    while True:
        print("Running loop")
        time.sleep(1)  # Sleep for 1 minute
        random_number = random.randint(0, 10)  # Generate random number between 0 and 10
        print(f"Generated Random Number: {random_number}")

        if random_number >= 5:
            teken=""

            if random_number==6:
                teken="*"
            if random_number==7:
                teken="-"
            if random_number>7:
                teken="+"
            if not is_process_running("FlightSimulator.exe"):
                print("MSFS is not running. Running the GUI check...")
                run_gui(teken)
