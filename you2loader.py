import tkinter
import customtkinter
from pytube import YouTube


def clear_loading_elements():
    finish_download_label.pack_forget()
    progress_bar.pack_forget()
    progress_percent.pack_forget()

def start_download():
    try:
        clear_loading_elements()
        dw_button.configure(state="disabled", text="Searching video...")
        link.configure(state="disabled")
        dw_button.update()
        finish_download_label.pack(padx=10, pady=10)
        progress_bar.pack(padx=10, pady=10)
        progress_percent.pack(padx=5, pady=5)
        finish_download_label.configure(text="")
        yt_url = url_var.get()
        yt_obj = YouTube(yt_url, on_progress_callback=on_progress)
        finish_download_label.configure(text=f"Video: {yt_obj.title}", text_color="white", font=("Arial", 20))
        dw_button.configure(text="Downloading...")
        video = yt_obj.streams.get_highest_resolution()
        video.download()
        progress_percent.configure(text="Video downloaded successfully!", text_color="green")
        dw_button.configure(state="normal", text="Download")
        link.configure(state="normal")
    except Exception as e:
        print(e)
        
        progress_percent.configure(text="Error while downloading the video!", text_color="red")

def on_progress(stream, chunk, bytes_remaining):
    size = stream.filesize
    bytes_downloaded = size - bytes_remaining
    percent = (100 * bytes_downloaded) / size
    percent = int(percent)
    progress_percent.configure(text=f"{percent} %")
    progress_percent.update()
    progress_bar.set(float(percent) / 100)
    progress_bar.update()

# System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Define app frame
app = customtkinter.CTk()
app.geometry("1000x600")
app.title("you2loader | Download YouTube videos")

# adding UI elements
title = customtkinter.CTkLabel(app, text="Insert the link of the video you want to download:")
title.pack(padx=10, pady=10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=400, height=30, textvariable=url_var)
link.pack()

finish_download_label = customtkinter.CTkLabel(app, text="")

progress_percent = customtkinter.CTkLabel(app, text="")
progress_bar = customtkinter.CTkProgressBar(app, width=400, fg_color="white", progress_color="green")
progress_bar.set(0)

dw_button = customtkinter.CTkButton(app, text="Download", width=200, height=40, command=start_download)
dw_button.pack(padx=10, pady=10)



if __name__ == "__main__":
    app.mainloop()