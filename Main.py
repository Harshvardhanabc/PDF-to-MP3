import pyttsx3
import PyPDF2
from tkinter.filedialog import askopenfilename

# Ask the user to open a file dialog and select a PDF file
book = askopenfilename(title="Select a PDF file", filetypes=[("PDF files", "*.pdf")])

# Create a PDF reader object
pdfreader = PyPDF2.PdfReader(book)

# Get the number of pages in the PDF
Num_Pages = len(pdfreader.pages)

# Initialize the text-to-speech engine
player = pyttsx3.init()

# Iterate over each page and extract text
for num in range(Num_Pages):
    # Access the current page
    page = pdfreader.pages[num]
    
    # Extract text from the page
    text = page.extract_text()
    
    # Use the text-to-speech engine to say the text
    player.say(text)

    # Save text file into mp3 mode
    player.save_to_file(text, 'D:/new.mp3')

# Wait for the speech to complete
player.runAndWait()
