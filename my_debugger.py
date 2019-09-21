from ctypes import *
from my_debugger_defines import *

kernel32 = windll.kernel32

class debugger():
    def __init__(self):
        pass

    def load(self, pass_to_exe):

        #dwCreateFlags determines how the process creates
        #If you want to see the calculator GUI
        #creation_flags = CREATE_NEW_CONSOLE
        creation_flags = DEBUG_PROSESS

        #Instantiate structure
        startupinfo = STARTUPINFO()
        process_information = PROCESS_INFORMATION()

        #Processes launched by the following two options are displayed in a separate window
        #Example in which the setting in the STARTUPINFO structure affects the debug target
        startupinfo.dwFlags     = 0x1
        startupinfo.wShowWindow = 0x0

        #Initialize variable cb indicating the size of startupinfo
        startupinfo.cb = sizeof(startupinfo)

        if kernel32.CreateProcessA(  
                                pass_to_exe,
                                None,
                                None,
                                None,
                                None,
                                creation_flags,
                                None,
                                None,
                                byref(startupinfo),
                                byref(process_information)
        ):
            print("[*] We have successfully launched the process!")
            print("[*] PID: %d" % process_information.dwProcessId)

        else:
            print("Error: 0x%08x." % kernel32.GetLastError)
