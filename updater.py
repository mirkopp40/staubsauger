import sys
import time
import shutil
import os
import subprocess

def main():
    if len(sys.argv) != 3:
        print("Usage: updater.py <new_exe_path> <old_exe_path>")
        sys.exit(1)

    # Nutze absolute Pfade
    new_exe = os.path.abspath(sys.argv[1])
    old_exe = os.path.abspath(sys.argv[2])

    time.sleep(2)  # Warte, bis das alte Programm sicher beendet ist

    # Sichere die alte Datei
    if os.path.exists(old_exe):
        try:
            os.rename(old_exe, old_exe + ".bak")
        except OSError:
            print(f"Fehler: Die Datei {old_exe} ist möglicherweise noch in Benutzung.")
            time.sleep(10)
            sys.exit(1)

    try:
        # Verschiebe die neue EXE an die Stelle der alten
        shutil.move(new_exe, old_exe)
        print("Update abgeschlossen. Starte das Programm neu...")
        time.sleep(1)
        
        # Debug-Ausgaben
        print(f"Starte die aktualisierte EXE: {old_exe}")

        # Nutze den Windows-Befehl "start" über shell=True, um die EXE zu starten.
        # Das hilft, wenn Pfade mit Leerzeichen Probleme bereiten.
        subprocess.Popen(f'start "" "{old_exe}"', shell=True)
    except Exception as e:
        print("Fehler beim Aktualisieren:", e)
        time.sleep(10)
        if os.path.exists(old_exe + ".bak"):
            shutil.move(old_exe + ".bak", old_exe)
        sys.exit(1)

if __name__ == "__main__":
    main()

