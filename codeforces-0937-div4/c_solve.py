def solve(s):
    sl = s.split(':')
    hour = int(sl[0])
    minute = int(sl[1])

    if hour < 12:
        if hour == 0:
            hour += 12
        return "%02d:%02d AM" % (hour, minute)

    hour -= 12
    if hour == 0:
        hour += 12
    return "%02d:%02d PM" % (hour, minute)
    

def main():
    import io,os,sys
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    tc = int(input())
    while tc:
        s = input().strip().decode()
        sys.stdout.write(str(solve(s)) + "\n")
        tc -= 1

main()