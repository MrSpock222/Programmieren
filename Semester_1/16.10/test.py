import google.generativeai as genai
import os

# Der Client erhält den API-Schlüssel aus der Umgebungsvariable `GEMINI_API_KEY`.
# Stelle sicher, dass die Umgebungsvariable gesetzt ist.
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Erstelle das generative Modell
model = genai.GenerativeModel("gemini-1.5-flash")

response = model.generate_content("gib mir ein 5 buchstaben Wort auf deutsch")
print(response.text)