class Phone:
    def __init__(self,model,year,color):
        self.model = model
        self.year = year
        self.color = color
        self.is_on = False
        self.open_apps = []
        self.sleep_mode = False

    def on(self):
        self.is_on = True

    def state(self):
        self.sleep_mode = True

    def open(self,apps):
        self.open_apps.append(apps)

    def display_info(self):
        print(f"My phone model is {self.model}.")
        print(f"It came out in {self.year}.")
        print(f"It's {self.color}, because I like that color.")
        print(f"My opened apps are: ")
        for app in self.open_apps:
            print(f"{app}")
        if self.is_on:
            print(f"I am currently using my phone")
        else:
            print("I am not using my phone")
        if self.sleep_mode:
            print(f"It's in sleep mode right now because I haven't touched the screen")

def main():
    # object creation based on the Book class
    my_phone = Phone(
        "Xiaomi","2014","Black")
    my_phone.on()
    my_phone.state()
    my_phone.open("Google")
    my_phone.open("Facebook")
    my_phone.open("Youtube")
    my_phone.display_info()
    


if __name__ =="__main__":
    main()