import customtkinter as ctk
import random
import time

main = ctk.CTk()
main.title("Should I do it?")
main.geometry("800x600")
left_frame = None
right_frame = None

def initialize_main_window():
    first_frame_color = random.choice(["darkblue", "darkred"])
    global left_frame
    left_frame = ctk.CTkFrame(main, width=400, height=600, fg_color=first_frame_color, corner_radius=0)
    left_frame.pack(side="left", fill="both", expand=True)
    left_frame.bind("<Button-1>", lambda event: show_random_answer())
    left_frame.bind("<Enter>", lambda event: hover_color(left_frame))
    left_frame.bind("<Leave>", lambda event: hover_color(left_frame))
    global right_frame
    right_frame = ctk.CTkFrame(main, width=400, height=600, corner_radius=0,
                               fg_color="darkred" if first_frame_color == "darkblue" else "darkblue")
    right_frame.pack(side="right", fill="both", expand=True)
    right_frame.bind("<Button-1>", lambda event: show_random_answer())
    right_frame.bind("<Enter>", lambda event: hover_color(right_frame))
    right_frame.bind("<Leave>", lambda event: hover_color(right_frame))

def show_random_answer():
    def switch_colors():
        if not left_frame.winfo_exists() or not right_frame.winfo_exists():
            return
        hover_color(left_frame)
        hover_color(right_frame)
        main.update()
        if time.time() - start_time < 2:
            main.after(200, switch_colors)
        else:
            display_answer()

    def display_answer():
        left_frame.destroy()
        right_frame.destroy()
        answer = random.choice(["Yes", "No"])
        answer_label = ctk.CTkLabel(main, text=answer, font=("Arial", 250), fg_color="black")
        answer_label.pack(side="top", fill="both", expand=True)
        answer_label.bind("<Button-1>", lambda event: reset_main_window(answer_label))

    left_frame.unbind("<Button-1>")
    left_frame.unbind("<Enter>")
    left_frame.unbind("<Leave>")
    right_frame.unbind("<Button-1>")
    right_frame.unbind("<Enter>")
    right_frame.unbind("<Leave>")
    left_frame.bind("<Button-1>", lambda event: display_answer())
    right_frame.bind("<Button-1>", lambda event: display_answer())

    start_time = time.time()
    switch_colors()

def reset_main_window(answer_label):
    answer_label.destroy()
    initialize_main_window()

def hover_color(frame):
    current_color = frame.cget("fg_color")
    color_map = {
        "darkred": "red",
        "red": "darkred",
        "darkblue": "blue",
        "blue": "darkblue"
    }
    new_color = color_map.get(current_color, current_color)
    frame.configure(fg_color=new_color)
    frame.update()

initialize_main_window()
main.mainloop()
