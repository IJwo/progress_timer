from time import sleep
from tkinter import Y

class Tea():
    def __init__(self, brew_time, firstindiv, indiv, fix_time):
        self.brew_time = brew_time
        self.firstindiv = firstindiv
        self.indiv = indiv
        self.brewes = 1
        self.fix_time = bool(fix_time)

    def get_start_time(self, start_time):
        self.brew_time = start_time
    
    def get_progress_time(self, indiv):
        self.indiv = indiv

    def get_firstindiv(self, firstindiv):
        self.brew_time = firstindiv
    
    def after_first_brew(self):
        self.brew_time -= self.firstindiv

    def brews(self):
        if self.fix_time is True:
            if self.brew_time < 105:
                self.brew_time += self.indiv
            else:
                pass
        else:
            self.brew_time += self.indiv
        self.brewes += 1

    def print_remaining_time(self):
        print("NO. ", self.brewes, " brews")
        for i in range(self.brew_time):
            print(self.brew_time - i)
            #sleep(1)

    def print_first_brew_time(self):
        print("NO. ", self.brewes, " brews")
        self.brewes += 1
        for i in range(self.brew_time):
            print(self.brew_time - i)
        self.after_first_brew()
            #sleep(1)
def main():
    winter = Tea(90, 25, 5, True)
    next_brew = True
    winter.print_first_brew_time()

    while next_brew:
        flag = input("Do you want to brew?")
        flag.lower()
        if flag == "y":
            next_brew = True
        elif flag == "n":
            next_brew = False
            break
        elif flag != "y" and flag != "n":
            print("not valid")
            continue
        winter.print_remaining_time()
        winter.brews()

if __name__ == '__main__':
    main()