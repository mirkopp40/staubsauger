import sys
import time
import os
import subprocess

def main():
    if len(sys.argv) != 2:
        print("Usage: updater.py <new_exe_path>")
        sys.exit(1)

    # Absoluten Pfad der neuen Datei ermitteln
    new_exe = os.path.abspath(sys.argv[1])
    time.sleep(2)  # Warte, bis das alte Programm beendet ist

    if not os.path.exists(new_exe):
        print("Fehler: Die neue Datei wurde nicht gefunden:", new_exe)
        sys.exit(1)

    # Zielpfad: Datei umbenennen zu "updatetversion.exe" im selben Verzeichnis
    target_exe = os.path.join(os.path.dirname(new_exe), "updatetversion.exe")
    try:
        os.rename(new_exe, target_exe)
    except Exception as e:
        print("Fehler beim Umbennen der Datei:", e)
        sys.exit(1)

    print("Update abgeschlossen. Starte die neue Version:", target_exe)
    # Starte die neue Version über den Windows "start"-Befehl
    subprocess.Popen(f'start "" "{target_exe}"', shell=True)

if __name__ == "__main__":
    main()



