class Time:
    def printTime(time):
        # time = Time()
        print "%.2d : %.2d : %.2d" % (time.hour, time.minute, time.second)

    def increment(self,second):
        self.second += second
        while self.second >= 60:
            self.second -= 60
            self.minute += 1
        while self.minute >= 60:
            self.minutes -= 60
            self.hour += 1
    def to_secs(t):
        in_secs = (t.hour * 3600) + (t.minute * 60) + t.second
        return in_secs
    def after(self, time2):
        if self.hour >= time2.hour:
            return 1
        if self.hour < time2.hour:
            return 0

        if self.minute >= time2.hour:
            return 1
        if self.minute < time2.minute:
            return 0

        if self.second >= time2.second:
            return 1
        return 0


now = Time()
now.hour = 02
now.minute = 00
now.second = 00

done = Time()
done.hour = 2
done.minute = 00
done.second = 00

# now.printTime()
# now.increment(200)
# now.printTime()
# print now.to_secs()

if done.after(now):
    print 'Not yet done'

if now.after(done):
    print 'Burnt'