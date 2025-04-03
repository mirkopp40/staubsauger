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
    old_exe = sys.argv[2]
    time.sleep(2)  # Warte, bis das Hauptprogramm beendet ist
    try:
        shutil.copy(new_exe, old_exe)
        print("Update abgeschlossen. Starte das Programm neu...")
        os.remove(new_exe)
        subprocess.Popen([old_exe])
    except Exception as e:
        print("Fehler beim Aktualisieren:", e)

if __name__ == "__main__":
    main()
