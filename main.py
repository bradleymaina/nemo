import os

while True : 

    command = input("Enter command: ").lower()

    if command == "nemo" : #nemo is the wake up call for the AI assistant
        print("Hello Engineer Bradley")

    elif command == "nemo browser" :
        os.system("brave")

# specific for my file manager 
# replace with appropriate file manager eg thunar , nautilus
    elif command == "nemo files" : 
        os.system("dolphin")

#specific for my zsh
#replace with appropriate shell manager 
    elif command == "nemo shell":
        os.system("kitty") 

    elif command == "nemo code" :
        os.system("antigravity")
 
    elif command == "nemo spotify" :
        os.system("spotify")

    else: 
        print("Unknown command")