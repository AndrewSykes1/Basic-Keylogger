import os
import sys
import time
import subprocess

def rename_and_restart(new_name):
    if not getattr(sys, 'frozen', False):
        print("This only works when frozen to exe")
        return

    current_path = sys.executable
    dir_path = os.path.dirname(current_path)
    new_path = os.path.join(dir_path, new_name)

    # Create a helper batch file to do rename + restart
    helper_path = os.path.join(dir_path, "helper.bat")

    # The batch script content
    # 1. Wait for the original exe to close
    # 2. Rename the exe
    # 3. Restart the exe with new name
    batch_script = f"""
    @echo off
    :loop
    tasklist | findstr /i "{os.path.basename(current_path)}"
    if not errorlevel 1 (
        timeout /t 1 /nobreak > nul
        goto loop
    )
    rename "{os.path.basename(current_path)}" "{new_name}"
    start "" "{new_name}"
    del "%~f0"
    """

    # Write batch file
    with open(helper_path, "w") as f:
        f.write(batch_script)

    # Launch batch file and exit
    subprocess.Popen(['cmd', '/c', helper_path], shell=True)
    sys.exit()

if __name__ == "__main__":
    print("Running original exe")
    time.sleep(2)  # Do your main work here or just delay for demo
    rename_and_restart("renamed_program.exe")
