import os 
import subprocess
import psutil

def control_app(action : str, app_name : str) :
    # Open and Close App
    if action == "open" :
        os.system(f"start {app_name}")
        return f"Open {app_name}"
    
    elif action == "close" :
        found = False
        for proc in psutil.process_iter(["name"]) :
            if app_name.lower() in proc.info['name'].lower():
                proc.kill ()
                found = True
        return f"{app_name} has closed" if found else f"{app_name} tidak ditemukan."
