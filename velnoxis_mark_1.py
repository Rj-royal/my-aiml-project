import pypdf
import time
from google.genai import types
from google import genai
client= genai.Client(api_key="PASTE_YOUR_KEY_HERE")
def definition_pyq(pdf_path):
    print("Reading scanned PDF using Gemini Vision...")
    
    try:
        # 2. Load the actual file as bytes
        with open(pdf_path, "rb") as f:
            pdf_bytes = f.read()
            print(f"Step 2: File loaded ({len(pdf_bytes)} bytes). Sending to Gemini...")
        prompt=f"""
        you are an expert academic analyst. I am providing you with text from a previous year question (pyq) paper.

        task:
        1. identify the top 5 most important topics mentioned.
        2. group question by marks(e.g., 2-mark question,3-mark question,12-mark question)
        3. predict which topic is most likely to repeat based on this paper.
        """
        response = client.models.generate_content(model='gemini-3.1-flash-lite-preview',contents=[types.Part.from_bytes(data=pdf_bytes,mime_type='application/pdf'),prompt])
        print("Step 3: Response received!")
        print("--- Velnoxis Smart Summary ---")
        if response.text:
            print(response.text)
        else:
            print("Gemini returned an empty response. Check if the PDF is password protected.")
    except FileNotFoundError:
        print(f"Error: The file at {pdf_path} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

definition_pyq(r"C:\Users\ANKIT SHAW\Downloads\pyq.pdf")
time.sleep(10)
