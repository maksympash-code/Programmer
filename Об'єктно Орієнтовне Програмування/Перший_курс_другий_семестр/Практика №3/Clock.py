from time import *
from turtle import *
from datetime import *

class Clock:
    def __init__(self, size):
        self.size = size
        self.time = self.get_world_time()

    def Digital_Blood(self):
        radius = self.size
        up()
        goto(0, -radius)
        down()
        circle(radius)
        left(90)
        up()
        goto(0,(radius-radius/5))
        for i in range(1,13):
            penup()
            goto(0, -20)
            setheading(90)
            right(30*i)
            forward(radius-radius/8)
            down()
            write(str(i), align="center", font=("Times New Roman",32, "normal"))

    def arrow_second(self):
        pencolor("Red")
        pensize(1)
        size = self.size - self.size / 3
        up()
        goto(0,0)
        down()
        forward(size)
        backward(size + size / 5)
        goto(0,0)

    def arrow_minute(self):
        pencolor("Black")
        pensize(3)
        size = self.size - self.size / 4
        up()
        goto(0,0)
        down()
        forward(size)
        backward(size + self.size / 5)
        goto(0,0)



    def arrow_hour(self):
        pencolor("Black")
        pensize(6)
        size = self.size - self.size / 2
        up()
        goto(0,0)
        down()
        forward(size)
        backward(self.size - self.size / 6)
        goto(0,0)


    def get_world_time(self):
        current_time = datetime.now(timezone.utc)

        kyiv_timezone = timezone(timedelta(hours=2))  # UTC+2
        local_time = current_time.astimezone(kyiv_timezone)

        hour = local_time.hour
        minute = local_time.minute
        second = local_time.second

        return [hour, minute, second]


    def run_clock(self):
        second = self.time[2]
        minute = self.time[1]
        hour = self.time[0]
        pencolor("Black")
        self.Digital_Blood()
        color("Black")
        up()
        goto(0,0)
        setheading(90)
        right(6*minute)
        down()
        self.arrow_minute()
        color("Black")
        up()
        goto(0,0)
        setheading(90)
        right(30 * hour)
        down()
        self.arrow_hour()
        down()
        while True:
            self.arrow_second()
            sleep(1)
            for i in range(3):
                undo()
            second += 1
            if second == 60:
                second = 1
                minute += 1
                setheading(90)
                right(6 * (minute - 1))
                color ("White")
                self.arrow_minute()
                setheading(90)
                right(6 * minute)
                color("Black")
                self.arrow_minute()
                up()
                goto(0,0)
                setheading(90)
                right(30 * hour)
                down()
                self.arrow_hour()
                if minute == 60:
                    minute = 0
                    hour += 1
                    setheading(90)
                    right(6 * (hour - 1))
                    color("White")
                    self.arrow_hour()
                    setheading(90)
                    right(30 * hour)
                    color("Black")
                    self.arrow_hour()
            setheading(90)
            right(6 * second)

if __name__ == "__main__":
    speed(0)
    hideturtle()
    clock = Clock(300)
    clock.run_clock()
    mainloop()
