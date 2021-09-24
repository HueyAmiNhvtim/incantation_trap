from tkinter import *
from word_management_spell_bound import sorted_all, sorted_three, sorted_four, search_words, sort_words_list

import random
import string


# Be careful of the ipadx and ipady
# TO-DO: Make the shuffle algo...
#        DISPLAY THE SUCCESSFUL STUFF
#          CHECK SUBMITTED WORDS
#           SOCRING SYSTEMS


class RipOffSpellBound:
    def __init__(self):
        """Initialize the frame. Am I doing sth wrong or is it supposed to be that long? """

        # Main Frame
        self.window = Tk()
        self.window.title("Spellbound Rip-off")
        self.window.geometry("1920x1080")
        self.window.columnconfigure((0, 1, 2, 3), weight=1)
        self.window.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), weight=1)

        # For cancelling the after loop:
        self.after_id = None

        # Status Frame for checking words:
        self.status_fr = Frame(self.window, bg="#301394", relief=GROOVE, borderwidth=2)
        self.status_fr.grid_propagate(False)
        self.status_fr.columnconfigure(0, weight=1)
        self.status_fr.columnconfigure(1, weight=2)
        self.status_fr.rowconfigure(0, weight=1)

        self.status_label = Label(self.status_fr, bg="#023d5e", fg="#bfbd97", text="WORDS CHECKER", borderwidth=4)
        self.status_label.config(font=("Courier", 16))
        self.status_label.grid(column=0, row=0, sticky="NSEW")
        self.status_fr.grid(column=0, columnspan=4, row=0, sticky="NSEW")

        self.displayed_submitted = StringVar()
        self.words_display = Label(self.status_fr, bg="#136594", textvariable=self.displayed_submitted,
                                   borderwidth=4, width=2, fg="#e3db46")
        self.words_display.config(font=("Courier", 20))
        self.displayed_submitted.set("Nothing has been submitted")
        self.words_display.grid(column=1, row=0, sticky="NSEW")

        # Display_Frame
        self.frame_display_words = Frame(self.window, bg="#2a2a35", relief=GROOVE, borderwidth=2)
        self.frame_display_words.grid(column=0, columnspan=4, row=1, rowspan=6, padx=20, pady=20, sticky="NSEW")
        self.frame_display_words.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.frame_display_words.columnconfigure((0, 1), weight=1)
        self.frame_display_words.grid_propagate(False)
        self.display_strvar = []
        for i in range(12):
            label = StringVar()
            self.display_strvar.append(label)
        # Python 3.8 and above.
        # self.display_strvar = [label := StringVar() for i in range(12)]
        self.display_index = 0
        self.labels_display = []

        # Create columns and rows
        for i in range(2):
            for j in range(6):
                self.label_word = Label(self.frame_display_words, textvariable=self.display_strvar[self.display_index],
                                        font=("Courier", 20), bg="#424261", fg="#dcd9cd", borderwidth=2)
                self.display_strvar[self.display_index].set("Valid words appear here")
                self.label_word.grid(row=j, column=i, sticky="NSEW", padx=2)
                self.labels_display.append(self.label_word)
                self.display_index += 1
        self.display_index = 0  # Restart to make it also work for label traversal
        # Round (Optional), Score(), Time
        self.rou_sco_tim_fr = Frame(self.window, bg="#301394", relief=GROOVE, borderwidth=2)
        self.rou_sco_tim_fr.grid_propagate(False)
        self.score = 0
        self.rou_sco_tim_fr.columnconfigure((1, 3), weight=1)
        self.rou_sco_tim_fr.columnconfigure((0, 2, 4), weight=2)
        self.rou_sco_tim_fr.rowconfigure(0, weight=1)
        self.rou_sco_tim_fr.grid(column=0, columnspan=4, row=7, sticky="NSEW")

        # Round Label
        self.round_indicator = StringVar()
        self.round_num = 1
        self.round_label = Label(self.rou_sco_tim_fr, bg="#136594", fg="#e3db46", font=("Courier", 20),
                                 textvariable=self.round_indicator, borderwidth=4, width=2)
        self.round_indicator.set(f"ROUND {self.round_num}")
        self.round_label.grid(column=0, row=0, sticky="NSEW")
        # Score_Label + Score Display_here...
        self.score_label = Label(self.rou_sco_tim_fr, bg="#023d5e", text="SCORE", borderwidth=4, fg="#bfbd97")
        self.score_label.config(font=("Courier", 16))
        self.score_label.grid(column=1, row=0, sticky="NSEW")

        self.score = StringVar()
        self.score_display = Label(self.rou_sco_tim_fr, bg="#136594", fg="#e3db46",
                                   textvariable=self.score, borderwidth=4, width=2)
        self.score_display.config(font=("Courier", 20))
        self.score.set("0")
        self.score_display.grid(column=2, row=0, sticky="NSEW")

        # Timer label + Time_Left:
        self.timer_label = Label(self.rou_sco_tim_fr, bg="#023d5e", text="TIME LEFT", borderwidth=4, fg="#bfbd97")
        self.timer_label.config(font=("Courier", 16))
        self.timer_label.grid(column=3, row=0, sticky="NSEW")

        self.timer_display = Label(self.rou_sco_tim_fr, bg="#136594", fg="#e3db46", text="0", borderwidth=4, width=2)
        self.timer_display.config(font=("Courier", 20))
        self.timer_display.grid(column=4, row=0, sticky="NSEW")

        # Display the shuffle lists and the space to enter...
        self.input_output_fr = Frame(self.window, bg="#1a0d1c", relief=GROOVE, borderwidth=2)
        self.input_output_fr.grid(column=0, columnspan=3, row=8, rowspan=4, ipadx=20, ipady=20, sticky="NSEW")
        self.input_output_fr.rowconfigure((0, 1), weight=1)
        self.input_output_fr.columnconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        self.input_output_fr.grid_propagate(False)
        # Trying to create a list of string var here. Requires Python 3.8 for the walrus operator.
        self.letters_strvar = []
        self.labels_strvar = []
        for i in range(7):
            button = StringVar()
            display = StringVar()
            self.letters_strvar.append(button)
            self.labels_strvar.append(display)
        # Python 3.8 and above
        # self.letters_strvar = [button := StringVar() for i in range(7)]
        # self.labels_strvar = [display := StringVar() for i in range(7)]
        self.entered_list = []
        self.buttons_list = []

        for first_row in range(7):  # Be sure to check this....
            # Lambda trick to cause the function to store the current value at the time the lambda is defined/
            # instead of looking up the value AFTER the loop is done (a closure), which would be the last value.
            self.letter_button = Button(self.input_output_fr, textvariable=self.letters_strvar[first_row],
                                        command=lambda index=first_row: self.__button_to_boxes(index),
                                        font=("Courier", 20), bg="#38263b", fg="#f9d71c")
            self.letters_strvar[first_row].set("Press\nShuffle!")
            self.letter_button.grid(row=0, column=first_row, sticky="NSEW", padx=2)
            self.buttons_list.append(self.letter_button)

        for second_row in range(7):
            self.letter_label = Label(self.input_output_fr, textvariable=self.labels_strvar[second_row],
                                      font=("Courier", 20), bg="#301934", fg="#fafdec", borderwidth=2)
            self.labels_strvar[second_row].set("")
            self.letter_label.grid(row=1, column=second_row, sticky="NSEW", padx=2)

        # Shuffle, Clear, Backspace, Submit, Quit
        self.shu_cle_back_sub_qui_fr = Frame(self.window, bg="#ffdea7", relief=GROOVE, borderwidth=2)
        self.shu_cle_back_sub_qui_fr.grid(column=3, row=8, rowspan=5, sticky="NSEW")
        self.shu_cle_back_sub_qui_fr.rowconfigure((0, 1, 2, 3, 4), weight=1)
        self.shu_cle_back_sub_qui_fr.columnconfigure(0, weight=1)
        self.shu_cle_back_sub_qui_fr.grid_propagate(False)

        # The buttons! Since the buttons are static, that means that I don't have to type them out individually.
        name_buttons_commands = {"SHUFFLE": self.__shuffle, "CLEAR": self.__clear, "BACKSPACE": self.__backspace,
                                 "SUBMIT": self.__submit, "GIVE UP": self.__give_up}
        self.options_list = []
        for name, command in name_buttons_commands.items():
            self.options = Button(self.shu_cle_back_sub_qui_fr, text=f"{name}", command=command, font=("Courier", 20))
            self.options.grid(row=list(name_buttons_commands.keys()).index(name), sticky="NSEW")
            self.options_list.append(self.options)

        # For the shuffle method class:
        self.sorted_all = sorted_all
        self.sorted_three = sorted_three
        self.sorted_four = sorted_four
        self.already_there = []

        # For the score method and the round_winning_one...
        self.score_letter = 0
        self.unfilled_left = len(self.display_strvar)

    def timer_countdown(self, timer_seconds: int):
        if 0 <= timer_seconds:
            self.timer_display.configure(text=f"{timer_seconds}")
            timer_seconds -= 1
            self.after_id = self.window.after(1000, lambda: self.timer_countdown(timer_seconds))
        elif timer_seconds < 0:
            self.disable_buttons()
            self.__popup_fail(fail_reason="Time's up!")

    def __shuffle(self):
        # I need to make the shuffle algo
        # Also unfreeze the buttons while at it.
        list_letters = []
        alphabet_list = list(string.ascii_uppercase)
        vowels_list = ["A", "E", "I", "O", "U"]
        consonants_list = [letter for letter in alphabet_list if letter not in vowels_list]
        rng = random.randint(0, 100)
        if rng >= 34:
            # Choose with repitions
            num_vowels = random.randint(2, 3)
            list_letters += random.choices(vowels_list, k=num_vowels)
            list_letters += random.choices(consonants_list, k=7-num_vowels)
        elif rng <= 34:
            print("LOL")
            # Choose one word out of the list along with other, then shuffle their letters around.
            three_letter = random.choice(sorted_three)
            four_letter = random.choice(sorted_four)
            list_letters = list(three_letter + four_letter)
        random.shuffle(list_letters)
        for i in range(len(list_letters)):
            self.letters_strvar[i].set(list_letters[i])
            self.labels_strvar[i].set("")
            if self.buttons_list[i]["state"] == DISABLED:
                self.buttons_list[i]["state"] = NORMAL
        self.entered_list = []
        return

    def __clear(self):
        """ Empty all of the output labels.
            Empty the list string too."""
        for i in range(len(self.buttons_list)):
            self.labels_strvar[i].set("")
            if self.buttons_list[i]["state"] == DISABLED:
                self.buttons_list[i]["state"] = NORMAL
        self.entered_list = []
        return

    def __backspace(self):
        # Check if the entered list is 0 length.
        # Unfreeze the button associated with that letter.
        if len(self.entered_list) > 0:
            last_letter_pos = len(self.entered_list) - 1
            last_letter_value = self.labels_strvar[last_letter_pos].get()
            letters = list(map(lambda x: x.get(), self.letters_strvar))
            if last_letter_value in letters:
                index_last_letter_button = letters.index(last_letter_value)
                self.buttons_list[index_last_letter_button]["state"] = NORMAL
            self.labels_strvar[last_letter_pos].set("")
            self.entered_list.pop(last_letter_pos)
        return

    def __submit(self):
        # Compare the string to the sorted list and then empty it.
        # Also unfreeze the button too. Also, remove the valid word away from the
        # sorted one and put it in the already entered words_list. The result is a tuple containing
        # a boolean and the index. That was unnecessary...
        word = "".join(self.entered_list)
        result = search_words(word, self.sorted_all)
        self.already_there = sort_words_list(self.already_there)
        result_if_entered_twice = search_words(word, self.already_there)
        if result[0] is True:
            if result_if_entered_twice[0] is False:
                self.displayed_submitted.set(f"{word} is VALID!")
                self.already_there.append(word)
                # This does not work across multiple rounds
                self.display_strvar[self.display_index].set(word)
                # This is for the shuffling algo.
                if len(word) == 3:
                    self.sorted_three.remove(word)
                elif len(word) == 4:
                    self.sorted_four.remove(word)
                self.__scoring(self.entered_list)
                self.unfilled_left -= 1
                self.display_index += 1
            else:
                self.displayed_submitted.set(f"{word} has already been entered!")
        else:
            if len(word) > 0:
                self.displayed_submitted.set(f"{word} is NOT VALID!")
            else:
                self.displayed_submitted.set("Nothing?")
        self.__clear()
        self.__check_if_win()
        return

    def __give_up(self):
        # Make sure that the countdown is stopped when pressed the button
        self.window.after_cancel(self.after_id)
        self.after_id = None
        self.timer_display.configure(text="0")
        self.disable_buttons()
        self.__popup_fail(fail_reason="Oh well, the game ends here.")
        return

    def __button_to_boxes(self, index):
        letter = self.letters_strvar[index].get()
        self.entered_list.append(letter)
        self.labels_strvar[len(self.entered_list) - 1].set(letter)
        self.buttons_list[index]["state"] = DISABLED
        return

    def __scoring(self, entered: list):
        # I have to hard code this. Sorry!
        # Based on letter frequency in English dictionaries. The more common, the less points
        scoring_points = {"E": 1, "S": 2, "I": 3, "A": 4, "R": 5, "N": 6, "T": 7, "O": 8, "L": 9,
                          "C": 10, "D": 11, "U": 12, "G": 13, "P": 14, "M": 15, "H": 16,
                          "B": 17, "Y": 18, "F": 19,  "V": 20, "K": 21, "W": 22, "Z": 23, "X": 24,
                          "J": 25, "Q": 26}
        for letter in entered:
            self.score_letter += scoring_points[letter]
        # Display the score on the board...
        self.score.set(f"{self.score_letter}")
        return

    def __check_if_win(self):
        if self.unfilled_left == 0:
            self.disable_buttons()
            self.window.after_cancel(self.after_id)
            self.after_id = None
            popup = Toplevel(bg="grey")
            popup.geometry("480x360")
            popup_msg = Label(popup, fg="red", text=f"You've won ROUND {self.round_num}!", font=("Courier", 17))
            popup_stat = Label(popup, fg="red", text=f"Your score is {self.score_letter}\nafter "
                                                     f"{self.round_num} ROUNDS(S)",
                               font=("Courier", 17))
            self.round_num += 1
            popup_continue = Button(popup, fg="red", relief=RAISED, text=f"CONTINUE TO ROUND{self.round_num}?\n"
                                                                         f"You will not be able to reenter words\n"
                                                                         f"from the previous round(s).",
                                    command=lambda: self.restart_continue(popup), font=("Courier", 15))
            popup_restart = Button(popup, fg="red", relief=RAISED, text="RESTART?",
                                   command=lambda: self.restart_everything(popup), font=("Courier", 15))
            popup_destroy = Button(popup, fg="red", relief=RAISED, text="QUIT?", command=self.window.destroy,
                                   font=("Courier", 15))
            popup_msg.pack()
            popup_continue.pack()
            popup_stat.pack()
            popup_restart.pack()
            popup_destroy.pack()
        return

    def restart_everything(self, popup: Toplevel):
        for i in range(len(self.options_list)):
            self.options_list[i]["state"] = NORMAL
        self.displayed_submitted.set("Nothing has been submitted yet.")
        self.score.set("0")
        self.score_letter = 0
        self.unfilled_left = len(self.display_strvar)
        self.sorted_all = sorted_all
        self.sorted_three = sorted_three
        self.sorted_four = sorted_four
        self.already_there = []
        self.entered_list = []
        self.round_num = 1
        self.round_indicator.set(f"ROUND {self.round_num}")
        self.display_index = 0
        for word in self.display_strvar:
            word.set("Valid words appear here")
        for i in range(len(self.letters_strvar)):
            self.letters_strvar[i].set("Press\nShuffle!")
            self.labels_strvar[i].set("")
        self.__clear()
        popup.destroy()
        self.timer_countdown(240)

    def restart_continue(self, popup: Toplevel):
        for i in range(len(self.options_list)):
            self.options_list[i]["state"] = NORMAL
        self.displayed_submitted.set("Nothing has been submitted yet.")
        self.unfilled_left = len(self.display_strvar)
        self.round_indicator.set(f"ROUND {self.round_num}")
        self.display_index = 0
        self.entered_list = []
        for word in self.display_strvar:
            word.set("Valid words appear here")
        for i in range(len(self.letters_strvar)):
            self.letters_strvar[i].set("Press\nShuffle!")
            self.labels_strvar[i].set("")
        self.__clear()
        popup.destroy()
        self.timer_countdown(200)
        return

    def __popup_fail(self, fail_reason):
        popup = Toplevel(bg="grey")
        popup.geometry("480x360")
        popup_msg = Label(popup, fg="red", text=f"{fail_reason}", font=("Courier", 17))
        popup_stat = Label(popup, fg="red", text=f"Your score is {self.score_letter}\nafter {self.round_num} "
                                                 f"ROUND(S)", font=("Courier", 17))
        popup_restart = Button(popup, fg="red", relief=RAISED, text="RESTART?",
                               command=lambda: self.restart_everything(popup), font=("Courier", 15))
        popup_destroy = Button(popup, fg="red", relief=RAISED, text="QUIT?", command=self.window.destroy,
                               font=("Courier", 15))
        popup_msg.pack()
        popup_stat.pack()
        popup_restart.pack()
        popup_destroy.pack()
        return

    def disable_buttons(self):
        for i in range(len(self.options_list)):
            self.options_list[i]["state"] = DISABLED
        return


if __name__ == "__main__":
    ripoff = RipOffSpellBound()
    ripoff.timer_countdown(240)
    ripoff.window.mainloop()
