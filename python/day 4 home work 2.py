def main():
    hour1 = input("add time.1: ")
    hour2 = input("add time 2: ")
    if int(hour1[0]+hour1[1]) < int(hour2[0]+hour2[1]):
        print("time 1 comes first")
    elif int(hour1[0]+hour1[1]) == int(hour2[0]+hour2[1]):
        print("hours are the same")
        if int(hour1[3] + hour1[4]) < int(hour2[3] + hour2[4]):
            print("time 1 comes first")
        elif int(hour1[3]+hour1[4]) == int(hour2[3]+hour2[4]):
            print("minute 1 and 2 are the same")
        else:
            print("time 2 comes first")
    else:
        print("time 2 comes first")


main()
input("press enter to end")
