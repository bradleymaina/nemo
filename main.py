import os

command = input("Enter command: ").lower()

if command == "nemo" : #nemo is the wake up call for the AI assistant
    print("Hello Engineer Bradley")

elif command == "nemo browser" :
    os.system("brave")

else: 
    print("Unknown command")