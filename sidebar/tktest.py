''' tk_clipboard_action.py
use Tkinter to get access to the clipboard/pasteboard
tested with Python27/33
'''
import tkinter as tk
root = tk.Tk()
# keep the window from showing
root.withdraw()
text = "Donnerwetter"
root.clipboard_clear()
# text to clipboard
root.clipboard_append(text)

root.mainloop()
root.destroy()
# text from clipboard
clip_text = root.clipboard_get()
print(clip_text)  # --> Donnerwetter