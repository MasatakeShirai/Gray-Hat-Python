from ctypes import *

kerne32 = windll.kernel32

pid = input("pid : ")

if kerne32.DebugActiveProcess(int(pid)):
    print "attached:", pid
    kerne32.DebugActiveProcessStop(int(pid))
    print "detached:", pid
else:
    print("error:",pid)
    print(WinError(GetLastError()))
