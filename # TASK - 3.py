from tkinter import *
import tkinter.messagebox as alert
import random
import re
from termcolor import colored

class CyberPasswordForge(Tk):

    def __init__(self):
        super().__init__()
        # Window positioning and styling
        monitor_width = self.winfo_screenwidth()
        monitor_height = self.winfo_screenheight()
        window_width = 520
        window_height = 320
        pos_x = int((monitor_width / 2) - (window_width / 2))
        pos_y = int((monitor_height / 2) - (window_height / 2))
        self.geometry(f'{window_width}x{window_height}+{pos_x}+{pos_y}')
        self.title("🔐 Cyber Password Forge")
        self.resizable(False, False)
        self.configure(bg="#0a0a0a")
        
        # Interface construction
        self.title_section = self.build_title_section()
        self.setup_main_title()
        self.length_section = self.build_length_section()
        self.setup_length_controls()
        self.length_input_box = self.create_length_input()
        self.security_section = self.build_security_section()
        self.setup_security_controls()
        self.security_level = StringVar()
        self.security_level.set("high")
        self.setup_security_options()
        self.action_section = self.build_action_section()
        self.setup_forge_button()

    def build_title_section(self):
        section = Frame(self, height=60, bg="#1a1a2e")
        section.pack(fill=X, pady=(0, 5))
        return section

    def setup_main_title(self):
        title = Label(self.title_section, text="⚡ CYBER PASSWORD FORGE ⚡", 
                     font=("Courier New", 20, "bold"), fg="#00ff41", bg="#1a1a2e")
        title.pack(pady=10)

    def build_length_section(self):
        section = Frame(self, bg="#16213e", height=80, padx=25, pady=15)
        section.pack(fill=BOTH, padx=10, pady=5)
        return section

    def setup_length_controls(self):
        label = Label(self.length_section, text="◈ PASSWORD LENGTH", 
                     font=("Consolas", 14, "bold"), bg="#16213e", fg="#0ff0fc")
        label.pack(side=LEFT, padx=(0, 15))

    def create_length_input(self):
        entry = Entry(self.length_section, width=4, fg="#00ff41", bg="#0a0a0a",
                     font=("Courier New", 12, "bold"), insertbackground="#00ff41",
                     bd=2, relief="solid")
        entry.pack(side=LEFT, ipady=3, ipadx=3)
        return entry

    def build_security_section(self):
        section = Frame(self, bg="#16213e", height=90, padx=25, pady=15)
        section.pack(fill=BOTH, padx=10, pady=5)
        return section

    def setup_security_controls(self):
        label = Label(self.security_section, text="◈ SECURITY PROTOCOL", 
                     font=("Consolas", 14, "bold"), bg="#16213e", fg="#0ff0fc")
        label.pack(anchor=W, pady=(0, 5))

    def setup_security_options(self):
        basic = Radiobutton(self.security_section, text="BASIC", value="low", 
                          variable=self.security_level, font=("Consolas", 11, "bold"), 
                          bg="#16213e", fg="#ff6b6b", selectcolor="#0a0a0a",
                          activebackground="#16213e", activeforeground="#ff6b6b")
        standard = Radiobutton(self.security_section, text="STANDARD", value="medium",
                             variable=self.security_level, font=("Consolas", 11, "bold"),
                             bg="#16213e", fg="#ffd93d", selectcolor="#0a0a0a",
                             activebackground="#16213e", activeforeground="#ffd93d")
        advanced = Radiobutton(self.security_section, text="ADVANCED", value="high",
                             variable=self.security_level, font=("Consolas", 11, "bold"),
                             bg="#16213e", fg="#00ff41", selectcolor="#0a0a0a",
                             activebackground="#16213e", activeforeground="#00ff41")
        
        basic.pack(side=LEFT, padx=(20, 0))
        standard.pack(side=LEFT, padx=(40, 0))
        advanced.pack(side=LEFT, padx=(40, 0))

    def build_action_section(self):
        section = Frame(self, bg="#16213e", height=80, padx=25, pady=20)
        section.pack(fill=BOTH, padx=10, pady=5)
        return section

    def setup_forge_button(self):
        button = Button(self.action_section, text="⚡ FORGE PASSWORD ⚡", 
                       bg="#00ff41", fg="#0a0a0a", borderwidth=0, cursor="target",
                       padx=25, pady=8, font=("Courier New", 12, "bold"),
                       activebackground="#0ff0fc", activeforeground="#0a0a0a",
                       command=lambda: self.initiate_forging(self.length_input_box.get(), self.security_level.get()))
        button.pack()

    def display_forged_password(self, length, security, password):
        forge_result_window = Toplevel(self)
        forge_result_window.geometry("750x250")
        forge_result_window.resizable(False, False)
        forge_result_window.title("🔐 Password Forged Successfully")
        forge_result_window.configure(bg="#0a0a0a")
        
        header = Label(forge_result_window, 
                      text=f"⚡ PASSWORD SUCCESSFULLY FORGED ⚡\nLENGTH: {length} | SECURITY: {security.upper()}", 
                      fg="#00ff41", bg="#0a0a0a", font=("Courier New", 14, "bold"))
        header.pack(pady=10)
        
        password_display = Text(forge_result_window, height=4, width=80, 
                              fg="#0ff0fc", bg="#1a1a2e", font=("Courier New", 11, "bold"),
                              bd=2, relief="solid", insertbackground="#00ff41")
        password_display.insert(END, password)
        password_display.config(state=DISABLED)
        password_display.pack(pady=10)
        
        close_button = Button(forge_result_window, text="◈ CLOSE ◈", width=15, bd=0,
                            bg="#ff6b6b", fg="#ffffff", font=("Consolas", 11, "bold"),
                            command=forge_result_window.destroy, cursor="target")
        close_button.pack(side=RIGHT, padx=(0, 25), pady=10)
        
        forge_result_window.mainloop()

    def forge_basic_password(self, length):
        character_pool = list()
        for upper in range(65, 90):
            character_pool.append(chr(upper))
        for lower in range(97, 122):
            character_pool.append(chr(lower))
        
        counter = 1
        forged_password = ""
        while counter <= length:
            selected_char = random.choice(character_pool)
            forged_password += selected_char
            counter += 1
        
        print(colored(f"Forged password: {forged_password}", "light_green"))
        return forged_password

    def forge_standard_password(self, length):
        character_pool = list()
        for upper in range(65, 91):
            character_pool.append(chr(upper))
        for digit in range(48, 58):
            character_pool.append(chr(digit))
        for lower in range(97, 123):
            character_pool.append(chr(lower))
        
        counter = 1
        forged_password = ""
        while counter <= length:
            selected_char = random.choice(character_pool)
            forged_password += selected_char
            counter += 1
        
        # Ensure password contains digits
        digit_check = re.compile('[0123456789]')
        if digit_check.search(forged_password) is None:
            forged_password = self.forge_standard_password(length)
        elif digit_check.search(forged_password) is not None:
            print(colored(f"Forged password: {forged_password}", "light_green"))
        return forged_password

    def forge_advanced_password(self, length):
        character_pool = list()
        special_chars = ['!', '@', '#', '$', '%', '^', '&', '*']
        
        for upper in range(65, 91):
            character_pool.append(chr(upper))
        for digit in range(48, 58):
            character_pool.append(str(digit))
        for special in special_chars:
            character_pool.append(special)
        for lower in range(97, 123):
            character_pool.append(chr(lower))
        
        counter = 1
        forged_password = ""
        while counter <= length:
            selected_char = random.choice(character_pool)
            forged_password += selected_char
            counter += 1
        
        # Ensure password contains both digits and special characters
        special_check = re.compile('[!@#$^&*]')
        digit_check = re.compile('[0123456789]')
        
        if special_check.search(forged_password) is None and digit_check.search(forged_password) is None:
            forged_password = self.forge_advanced_password(length)
        elif special_check.search(forged_password) is None and digit_check.search(forged_password) is not None:
            forged_password = self.forge_advanced_password(length)
        elif special_check.search(forged_password) is not None and digit_check.search(forged_password) is None:
            forged_password = self.forge_advanced_password(length)
        elif special_check.search(forged_password) is not None and digit_check.search(forged_password) is not None:
            print(colored(f"Forged password: {forged_password}", "light_green"))
        return forged_password

    def initiate_forging(self, length, security):
        try:
            length = int(length)
            if length > 80 or length < 4:
                alert.showwarning(title="⚠️ FORGE ERROR", 
                                message="Password length must be between 4 and 80 characters")
            elif length <= 80 or length >= 4:
                print(colored(f"Initiating password forge:\nLength = {length} Security = {security}", "light_blue"))
                
                if security == "low":
                    password = self.forge_basic_password(int(length))
                    self.display_forged_password(length, security, password)
                elif security == "medium":
                    password = self.forge_standard_password(int(length))
                    self.display_forged_password(length, security, password)
                elif security == "high":
                    password = self.forge_advanced_password(int(length))
                    self.display_forged_password(length, security, password)
        except Exception as error:
            print(colored(f"Forge Exception: {error}", "red"))
            alert.showwarning(title="⚠️ FORGE ERROR", 
                            message="Invalid password length\n(minimum 4 | maximum 80)")

    def activate(self):
        self.mainloop()

if __name__ == '__main__':
    forge = CyberPasswordForge()
    forge.activate()