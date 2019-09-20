from ctypes import *

msvcrt = cdll.msvcrt
message = "hello\n"
msvcrt.printf("test:%s",message)