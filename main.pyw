import tkinter as tk
import customtkinter as ctk
import base64

ctk.set_appearance_mode("Dark")  
ctk.set_default_color_theme("blue") 


class Base64App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Live Base64 Encoder/Decoder")
        self.geometry("700x400")
        self.minsize(width=700, height=400)
        self.resizable(False, True)

        self.encoding_var = tk.StringVar(value="UTF-8")
        self.input_text = tk.StringVar()
        self.output_text = tk.StringVar()

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.create_widgets()

    def create_widgets(self):
        settings_frame = ctk.CTkFrame(self)
        settings_frame.grid(row=0, column=0, sticky="nsew", pady=10)

        encoding_label = ctk.CTkLabel(settings_frame, text="Select Encoding:")
        encoding_label.grid(row=0, column=0, padx=10)

        self.encoding_option_menu = ctk.CTkOptionMenu(settings_frame, values=["UTF-8", "UTF-16", "UTF-16LE"], variable=self.encoding_var, command=self.update_output)
        self.encoding_option_menu.grid(row=0, column=1, padx=10)

        self.mode_var = tk.StringVar(value="encode")
        encode_radio = ctk.CTkRadioButton(settings_frame, text="Encode", variable=self.mode_var, value="encode", command=self.update_output)
        decode_radio = ctk.CTkRadioButton(settings_frame, text="Decode", variable=self.mode_var, value="decode", command=self.update_output)
        encode_radio.grid(row=0, column=2, padx=10)
        decode_radio.grid(row=0, column=3, padx=10)

        text_frame = ctk.CTkFrame(self)
        text_frame.grid(row=1, column=0, sticky="nsew", pady=10, padx=10)

        text_frame.grid_rowconfigure(1, weight=1)
        text_frame.grid_columnconfigure(0, weight=1)
        text_frame.grid_columnconfigure(1, weight=1)

        input_label = ctk.CTkLabel(text_frame, text="Input:")
        input_label.grid(row=0, column=0, padx=10, sticky="w")

        self.input_textbox = ctk.CTkTextbox(text_frame, height=200)
        self.input_textbox.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.input_textbox.bind("<KeyRelease>", self.update_output)

        output_label = ctk.CTkLabel(text_frame, text="Output:")
        output_label.grid(row=0, column=1, padx=10, sticky="w")

        self.output_textbox = ctk.CTkTextbox(text_frame, height=200)
        self.output_textbox.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

    def get_encoding(self):
        return self.encoding_var.get()

    def update_output(self, event=None):
        input_data = self.input_textbox.get("1.0", tk.END).strip()
        if input_data:
            try:
                if self.mode_var.get() == "encode":
                    self.encode_text(input_data)
                else:
                    self.decode_text(input_data)
            except Exception as e:
                self.output_textbox.delete("1.0", tk.END)
                self.output_textbox.insert(tk.END, str(e))

    def encode_text(self, input_data):
        try:
            encoding = self.get_encoding()
            encoded_data = base64.b64encode(input_data.encode(encoding)).decode('utf-8')
            self.output_textbox.delete("1.0", tk.END)
            self.output_textbox.insert(tk.END, encoded_data)
        except Exception as e:
            self.output_textbox.delete("1.0", tk.END)
            self.output_textbox.insert(tk.END, f"Error: {str(e)}")

    def decode_text(self, input_data):
        try:
            encoding = self.get_encoding()
            decoded_data = base64.b64decode(input_data).decode(encoding)
            self.output_textbox.delete("1.0", tk.END)
            self.output_textbox.insert(tk.END, decoded_data)
        except Exception as e:
            self.output_textbox.delete("1.0", tk.END)
            self.output_textbox.insert(tk.END, f"Error: {str(e)}")


if __name__ == "__main__":
    app = Base64App()
    app.mainloop()
