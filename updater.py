import os
import sys
import urllib.request
import shutil
import time
import psutil  # Zum Überprüfen, ob die Anwendung noch läuft
import subprocess  # Zum Starten der neuen Version

def update_program():
    update_url = "https://github.com/mirkopp40/staubsauger/raw/refs/heads/main/new.exe"  # Hier den tatsächlichen Download-Link einfügen
    download_path = "new.exe"  # Hier wird die neue EXE-Datei gespeichert
    old_version_path = "old_version.exe"  # Der Name der alten Version, nachdem sie umbenannt wurde

    # Überprüfen, ob das Programm noch läuft
    def is_program_running(exe_name):
        for proc in psutil.process_iter(['pid', 'name']):
            if exe_name.lower() in proc.info['name'].lower():
                return True
        return False

    # Wenn das Programm läuft, warten, bis es geschlossen wurde
    while is_program_running("new_version.exe"):
        print("Das Programm läuft noch. Warten auf Beendigung...")
        time.sleep(1)

    # Überprüfen, ob die Datei 'new_version.exe' existiert und umbenennen, falls sie existiert
    if os.path.exists("new_version.exe"):
        print("Die alte Version wurde geschlossen. Benenne sie um in 'old_version.exe'...")
        os.rename("new_version.exe", old_version_path)

        # Löschen der alten Version (wenn sie existiert)
        if os.path.exists(old_version_path):
            print("Lösche die alte Version (old_version.exe)...")
            os.remove(old_version_path)
    
    else:
        print("Keine alte Version gefunden. Fahre fort mit dem Herunterladen der neuen Version.")

    # Die neue Version herunterladen
    print("Lade die neue Version herunter...")
    try:
        urllib.request.urlretrieve(update_url, download_path)
        print("Neue Version heruntergeladen.")
    except Exception as e:
        print(f"Fehler beim Herunterladen der neuen Version: {e}")
        return

    # Sicherstellen, dass die neue Version korrekt heruntergeladen wurde
    if os.path.exists(download_path):
        print("Die neue Version wird installiert...")
        # Löschen der 'old_version.exe', falls sie existiert
        if os.path.exists(old_version_path):
            os.remove(old_version_path)
        
        # Die heruntergeladene Datei wird jetzt als 'new_version.exe' installiert
        os.rename(download_path, "new_version.exe")
        print("Die neue Version wurde erfolgreich installiert.")
        
        # Starte die neue Version im Hintergrund und schließe das Skript
        try:
            print("Starte die neue Version...")
            subprocess.Popen(["new_version.exe"])  # Startet die neue Version im Hintergrund
            print("Die neue Version wurde gestartet.")

            # Schließe den Updater
            sys.exit()  # Das Skript wird beendet

        except Exception as e:
            print(f"Fehler beim Starten der neuen Version: {e}")
    else:
        print("Fehler: Die neue Version konnte nicht heruntergeladen werden.")
        return

if __name__ == "__main__":
    update_program()
