import sys
import os
import time
import shutil
import subprocess

def main():
    if len(sys.argv) < 3:
        print("Usage: updater.py <new_exe_path> <target_path>")
        sys.exit(1)
    new_exe_path = sys.argv[1]
    target_path = sys.argv[2]
    print("Updater startet...")
    # Kurze Pause, damit sich das Hauptprogramm schließen kann
    time.sleep(2)
    try:
        if os.path.exists(target_path):
            os.chmod(target_path, 0o777)
            os.remove(target_path)
            print("Alte Version gelöscht:", target_path)
        # Verschiebe die neue Version in das Zielverzeichnis
        shutil.move(new_exe_path, target_path)
        print("Neue Version verschoben nach:", target_path)
        # Starte die neue Version
        subprocess.Popen(f'start "" "{target_path}"', shell=True)
    except Exception as e:
        print("Fehler während des Updates:", e)
    sys.exit(0)

if __name__ == "__main__":
    main()
