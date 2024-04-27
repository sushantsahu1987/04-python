import datetime

def hello_world():
    print("Hello, World!")
    daily=datetime.datetime.now().strftime("%A")
    print(f"Today is {daily}")

if __name__ == "__main__":
    hello_world()
