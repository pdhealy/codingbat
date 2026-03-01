# Version 1
def parrot_trouble(talking, hour):
    if talking and (hour < 7 or hour > 20):
        return True
    else:
        return False

# Version 2
def parrot_trouble(talking, hour):
    return (talking and (hour < 7 or hour > 20))

if __name__ == "__main__":
    parrot_trouble(True, 6)  #True
    parrot_trouble(True, 7)  #False
    parrot_trouble(False, 6)  #False
    parrot_trouble(True, 21)  #True
    parrot_trouble(False, 21)  #False
    parrot_trouble(False, 20)  #False
    parrot_trouble(True, 23)  #True
    parrot_trouble(False, 23)  #False
    parrot_trouble(True, 20)  #False
    parrot_trouble(False, 12)  #False
