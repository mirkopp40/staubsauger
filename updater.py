import sys
import time
import shutil
import os
import subprocess

def main():
    if len(sys.argv) != 3:
        print("Usage: updater.py <new_exe_path> <old_exe_path>")
        sys.exit(1)

    new_exe = sys.argv[1]
    old_exe = "new.exe"

    time.sleep(2)  # Warte, bis das alte Programm sicher beendet ist

    # Überprüfen, ob die alte Datei noch existiert und nicht gesperrt ist
    if os.path.exists(old_exe):
        try:
            os.rename(old_exe, old_exe + ".bak")  # Alte Datei sichern
        except OSError:
            print(f"Fehler: Die Datei {old_exe} ist möglicherweise noch in Benutzung.")
            time.sleep(10)
            sys.exit(1)

    try:
        shutil.move(new_exe, old_exe)  # Verschieben statt kopieren + löschen
        print("Update abgeschlossen. Starte das Programm neu...")
        time.sleep(1)  # Sicherheitswartezeit
        subprocess.Popen([old_exe])
    except Exception as e:
        print("Fehler beim Aktualisieren:", e)
        time.sleep(10)
        if os.path.exists(old_exe + ".bak"):
            shutil.move(old_exe + ".bak", old_exe)  # Backup wiederherstellen
        sys.exit(1)

if __name__ == "__main__":
    main()
