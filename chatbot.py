import tkinter as tk
from tkinter import scrolledtext, END
from nltk.chat.util import Chat, reflections

class HRChatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("HR Chatbot")

        self.chat_area = scrolledtext.ScrolledText(root, width=50, height=20)
        self.chat_area.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.input_label = tk.Label(root, text="You:")
        self.input_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.input_entry = tk.Entry(root, width=40)
        self.input_entry.grid(row=1, column=1, padx=10, pady=10)

        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.bot = Chat(self.pairs, reflections)

    def send_message(self):
        user_input = self.input_entry.get()
        self.input_entry.delete(0, tk.END)
        self.chat_area.insert(tk.END, "You: " + user_input + "\n")

        response = self.bot.respond(user_input)
        self.chat_area.insert(tk.END, "HR Bot: " + response + "\n")
        self.chat_area.see(tk.END)

  
    pairs = [
        [
            r"(.*) your name?",
            ["My name is HR Bot.",]
        ],
        [
            r"(.*) (interview|job)?",
            ["We have various job openings. Please visit our careers page for more information.",]
        ],
        [
            r"(.*) (resume|CV)?",
            ["You can submit your resume through our online application portal.",]
        ],
        [
            r"(.*) (benefits|perks)?",
            ["We offer competitive benefits including health insurance, retirement plans, and flexible work hours.",]
        ],
        [
            r"(.*) (contact|reach)?",
            ["You can contact HR at hr@example.com or call us at +1234567890.",]
        ],
        [
            r"quit",
            ["Goodbye! Have a great day.",]
        ],
    ]

if __name__ == "__main__":
    root = tk.Tk()
    app = HRChatbot(root)
    root.mainloop()
      
