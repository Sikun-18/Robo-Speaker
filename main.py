import pyttsx3

if __name__ == "__main__":
    print("This script is created by Srikrushna")
    while True:
        x = input("Enter what you want to say: ")
        if x== 'q':
            break
        engine = pyttsx3.init()
        engine.say(x)
        engine.runAndWait()