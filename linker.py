import sys

file_name = "script.auiabsbhhhhhtlircpuimldoioeppppppp"
interpreter_cmd = "mono Program.exe"

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} [files]")
    quit()



print("#!/bin/sh")
i = 1
while i < len(sys.argv):
    print(f"mv {sys.argv[i]} {file_name}")
    print(interpreter_cmd)
    print(f"mv {file_name} {sys.argv[i]}")
    i += 1

