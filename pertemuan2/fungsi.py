def greeting (jam = 6 ):
    if jam  < 12:
        return "selamat pagi!"
    elif jam < 18:
        return "selamat sore!"
    else:
        return " selamat malam!"

print(greeting(125))