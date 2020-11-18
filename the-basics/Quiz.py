# print the string I am super excited for this course! 
# 5 times with a space after each iteration
class Quiz:
    def show_excitement():
        i = 0
        msg = "I am super excited for this course! "
        sum = ""
        while i < 5:
            sum += msg
            i += 1
        return sum
    print show_excitement()
