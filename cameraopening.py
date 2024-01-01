import subprocess,os,time
subprocess.run('start microsoft.windows.camera:', shell=True)
time.sleep(10)
subprocess.run('Taskkill /IM WindowsCamera.exe /F', shell=True)