import my_debugger

debugger = my_debugger.debugger()

debugger.load("C:\\Windows\\System32\\notepad.exe")

pid = raw_input("Enter the PID of the process to attach to : ");
debugger.attach(int(pid))
debugger.run()
debugger.detach()
