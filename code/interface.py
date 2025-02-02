import tkinter as tk
from tkinter import messagebox


class MainMenu(tk.Tk):
    def __init__(self):
        super().__init__()

        # Window settings
        self.title("iSignTalk")
        self.geometry("450x650")
        self.config(bg="#F1F2F6")  # Light gray background for a clean look

        # Font & color palette
        self.primary_color = "#3498DB"  # Blue shade (professional and modern)
        self.accent_color = "#E67E22"   # Orange accent color
        self.button_color = "#2980B9"   # Slightly darker blue
        self.secondary_color = "#95A5A6"  # Subtle light gray for secondary buttons
        self.button_font = ("Helvetica Neue", 14, "bold")
        self.title_font = ("Montserrat", 26, "bold")

        # Main title
        self.title_label = tk.Label(self, text="iSignTalk", font=self.title_font, fg="#2C3E50", bg="#F1F2F6")
        self.title_label.pack(pady=50)

        # Main buttons
        self.quiz_button = self.create_button("Play Quiz", self.play_quiz, self.primary_color)
        self.quiz_button.pack(pady=20)

        self.dictionary_button = self.create_button("Dictionary", self.dictionary, self.secondary_color)
        self.dictionary_button.pack(pady=20)

        self.search_sign_button = self.create_button("Search Sign", self.show_sub_menu, self.accent_color)
        self.search_sign_button.pack(pady=20)

        # Submenu flag
        self.is_sub_menu = False
        self.submenu = None

    def create_button(self, text, command, bg_color):
        """Helper function to create buttons with modern design and hover effect."""
        button = tk.Button(self, text=text, command=command, width=20, height=2,
                           bg=bg_color, fg="white", font=self.button_font, relief="flat", bd=0,
                           padx=30, pady=10, activebackground=bg_color, activeforeground="white",
                           highlightthickness=0, borderwidth=0, cursor="hand2", 
                           relief="raised", highlightcolor=bg_color)
        button.bind("<Enter>", lambda event, btn=button: self.on_hover_in(btn))
        button.bind("<Leave>", lambda event, btn=button: self.on_hover_out(btn))
        return button

    def on_hover_in(self, button):
        """On hover, lighten the button color."""
        button.config(bg="#1ABC9C")

    def on_hover_out(self, button):
        """On hover out, return to the original button color."""
        button.config(bg=self.primary_color)

    def play_quiz(self):
        messagebox.showinfo("Play Quiz", "Quiz feature is not implemented yet.")

    def dictionary(self):
        messagebox.showinfo("Dictionary", "Dictionary feature is not implemented yet.")

    def show_sub_menu(self):
        if not self.is_sub_menu:
            self.is_sub_menu = True
            self.submenu = tk.Toplevel(self)
            self.submenu.title("Select an Option")
            self.submenu.geometry("350x350")
            self.submenu.config(bg="#F1F2F6")

            # Submenu Title
            submenu_title = tk.Label(self.submenu, text="Select an Option", font=("Montserrat", 18, "bold"), fg="#2C3E50", bg="#F1F2F6")
            submenu_title.pack(pady=30)

            # Submenu buttons
            self.text_to_sign_button = self.create_button("Text to Sign", self.text_to_sign, self.primary_color)
            self.text_to_sign_button.pack(pady=15)

            self.sign_to_text_button = self.create_button("Sign to Text", self.sign_to_text, self.accent_color)
            self.sign_to_text_button.pack(pady=15)

            # Close button for submenu
            self.close_button = self.create_button("Close", self.close_sub_menu, "#E74C3C")
            self.close_button.pack(pady=20)

    def close_sub_menu(self):
        self.is_sub_menu = False
        self.submenu.destroy()

    def text_to_sign(self):
        messagebox.showinfo("Text to Sign", "Text to Sign feature is not implemented yet.")

    def sign_to_text(self):
        messagebox.showinfo("Sign to Text", "Sign to Text feature is not implemented yet.")


if __name__ == "__main__":
    app = MainMenu()
    app.mainloop()
