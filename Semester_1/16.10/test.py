import google.generativeai as genai
import os
import sys
from pathlib import Path
from datetime import datetime

# Versuche, den API-Key aus Umgebungsvariablen zu lesen

def ai():

    API_KEY = os.getenv("GEMINI_API_KEY")
    env_source = None


        
    # Wenn nicht gesetzt, suche rekursiv nach einer .env-Datei in Parent-Ordnern (python-dotenv)
    if not API_KEY:
        try:
            from dotenv import load_dotenv

            def find_env_from_start(start: Path):
                cur = start.resolve()
                while True:
                    candidate = cur / ".env"
                    if candidate.exists():
                        return candidate
                    if cur == cur.parent:
                        return None
                    cur = cur.parent

            # Suche zuerst im aktuellen Arbeitsverzeichnis (so findest du .env, wenn du von X runnst)
            found = find_env_from_start(Path.cwd())
            # Falls nicht gefunden, suche relativ zum Skriptverzeichnis (älteres Verhalten)
            if not found:
                found = find_env_from_start(Path(__file__).resolve().parent)

            if found:
                load_dotenv(found)
                API_KEY = os.getenv("GEMINI_API_KEY")
                env_source = str(found)
        except Exception:
            # python-dotenv nicht vorhanden oder Fehler beim Laden -> wir behandeln weiter unten
            pass

    if not API_KEY:
        print("Fehler: Umgebungsvariable GEMINI_API_KEY ist nicht gesetzt. Setze deinen API-Schlüssel.", file=sys.stderr)
        print("Beispiel (PowerShell): $env:GEMINI_API_KEY=\"<dein_schluessel>\"", file=sys.stderr)
        # Schreibe eine .env.example falls noch nicht vorhanden
        try:
            ex = Path(__file__).with_name(".env.example")
            if not ex.exists():
                ex.write_text("# Kopiere diese Datei zu .env und trage deinen Schlüssel ein\nGEMINI_API_KEY=<dein_schluessel>\n")
                print(f"Eine Beispiel-Datei '{ex.name}' wurde erstellt. Kopiere sie zu '.env' und fülle deinen Schlüssel aus.", file=sys.stderr)
        except Exception:
            pass
        sys.exit(1)

    # Wenn wir bis hierher einen Key haben, markieren, ob er aus ENV kam oder aus .env
    if API_KEY and not env_source:
        env_source = "environment variable"

    # Debug-Ausgaben (maskierter Key, Pfadinformationen)
    masked = None
    if API_KEY:
        masked = API_KEY[:4] + "..." + API_KEY[-4:] if len(API_KEY) > 8 else "****"
    print(f"[{datetime.now().isoformat()}] Python: {sys.executable}")
    print(f"[{datetime.now().isoformat()}] CWD: {Path.cwd()}")
    print(f"[{datetime.now().isoformat()}] GEMINI key source: {env_source}")
    print(f"[{datetime.now().isoformat()}] GEMINI key masked: {masked}")

    genai.configure(api_key=API_KEY)

    # Modellname optional über Umgebungsvariable überschreiben, sonst vernünftiger Default
    MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

    try:
        model = genai.GenerativeModel(MODEL_NAME)
    except Exception as e:
        print(f"Fehler beim Erstellen des Modells '{MODEL_NAME}': {e}", file=sys.stderr)
        sys.exit(2)

    try:
        response = model.generate_content("gib mir ein 5 buchstaben Wort auf deutsch, die Antwort darf nur das Wort enthalten, und muss 5 Buchstaben haben. Zähle immer nach bevor du die Antwort gibst, das es nicht mehr oder weniger als 5 Buchstaben sind. Pass auf das das Wort nicht immer das gleiche ist")
        # Antwort prüfen
        
    except Exception as e:
        print("Fehler beim Aufruf der Generative API:", file=sys.stderr)
        print(e, file=sys.stderr)
        sys.exit(3)
    return response.text 