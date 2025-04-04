import sys
import os
import subprocess
import requests
import time

def download_new_version(url, target_path):
    try:
        print(f"Lade neue Version herunter von deiner mudda {url}...")
        response = requests.get(url)
        response.raise_for_status()  # Überprüft auf HTTP-Fehler
        with open(target_path, 'wb') as f:
            f.write(response.content)
        print(f"Neue Version erfolgreich heruntergeladen: {target_path}")
    except requests.exceptions.RequestException as e:
        print(f"Fehler beim Herunterladen der neuen Version: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 3:
        print("Usage: updater.py <exe_path> <download_url>")
        sys.exit(1)

    exe_path = os.path.abspath(sys.argv[1])
    download_url = sys.argv[2]
    
    # Überprüfen, ob der Update-Skript (updater.py) im gleichen Verzeichnis ist
    updater_path = os.path.join(os.path.dirname(exe_path), "updater.py")
    if not os.path.exists(updater_path):
        print("Fehler: Die Datei updater.py wurde nicht gefunden.")
        sys.exit(1)

    print("Update vorbereitet. Starte mit dem Umbenennen der alten Version...")
    
    # Bennen die alte .exe-Datei um
    old_exe_path = os.path.join(os.path.dirname(exe_path), "old_exe.exe")
    try:
        os.rename(exe_path, old_exe_path)
        print(f"Alte Version umbenannt zu {old_exe_path}")
    except Exception as e:
        print(f"Fehler beim Umbenennen der alten Datei: {e}")
        sys.exit(1)

    # Neue Version herunterladen
    new_exe_path = os.path.join(os.path.dirname(exe_path), "new_version.exe")
    download_new_version(download_url, new_exe_path)
    
    # Starte die neue Version
    print("Starte die neue Version...")
    try:
        subprocess.Popen(f'start "" "{new_exe_path}"', shell=True)
    except Exception as e:
        print(f"Fehler beim Starten der neuen Version: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
