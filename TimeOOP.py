class Time:
    pass

time = Time()
time.hour = 11
time.minute = 59
time.second = 30

time2 = Time()
time2.hour = 10
time2.minute = 34
time2.second = 12

def print_time(time):
    form = "%.2d : %.2d : %.2d" %(time.hour, time.minute, time.second)
    return form

def to_secs(t):
    in_secs = (t.hour * 3600) + (t.minute * 60) + t.second
    return in_secs

def is_after(t1, t2):
    return to_secs(t1) < to_secs(t2)

def makeTime(seconds):
    t = Time()
    t.hour = seconds // 3600
    t.minute = seconds % 3600 // 60
    t.second = seconds % 60
    return t

def add_time(t1, t2):
    seconds = to_secs(t1) + to_secs(t2)
    return makeTime(seconds)

start = Time()
start.hour = 5
start.minute = 0
start.second = 0

duration = Time()
duration.hour = 1
duration.minute = 45
duration.second = 58

# done = add_time(start, duration)
# print print_time(done)

# Write a correct version of increment that doesn't contain any loops
def increment(time, seconds):
    # newTime = Time()
    added_time = to_secs(time) + seconds
    return makeTime(added_time)

incr_time = increment(start, 90)
print print_time(incr_time)
print print_time(start)