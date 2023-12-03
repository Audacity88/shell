def d1_p1():
    with open("input/d1.txt") as f:
        lines = f.readlines()
        total = 0
        for line in lines:
            line = line.strip("\n")
            nums = [int(s) for s in list(line) if s.isdigit()]
            val = 10 * nums[0] + 1 * nums[-1]
            print(line, nums, val)
            total += val
        print(total)

def d1_p2():
    with open("input/d1.txt") as f:
        lines = f.readlines()
        total = 0
        digits = 'one,two,three,four,five,six,seven,eight,nine'.split(',')
        repl = 'o1e,t2o,t3ree,f4ur,f5ve,s6x,s7ven,e8ght,n9ne'.split(',')
        for line in lines:
            line = line.strip("\n")
            for i in range(9):
                if digits[i] in line:
                    # print(line)
                    line = line.replace(digits[i], repl[i])
                    # print(line)
            nums = [int(s) for s in list(line) if s.isdigit()]
            val = 10 * nums[0] + 1 * nums[-1]
            print(line, nums, val)
            total += val
        print(total)

R_MAX = 12
G_MAX = 13
B_MAX = 14

def d2_p1():
    max_dic = {"red": R_MAX, "green": G_MAX, "blue": B_MAX}
    rv = 0
    with open("input/d2.txt") as f:
        for line in f.readlines():
            good = True
            game, score = line.strip("\n").split(": ")
            id = game.split(" ")[1]
            print(id)
            for event in score.split(";"):
                for balls in event.split(","):
                    num, color = balls.split()
                    print(num, color)
                    if int(num) > max_dic[color]:
                        good = False
                        print("no good")
                        break
            if good:
                rv += int(id)
                print("+", id, "=", rv)
            print("="*90)
    return rv

def d2_p2():
    with open("input/d2.txt") as f:
        total = 0
        for line in f.readlines():
            max_dic = {"red": 0, "green": 0, "blue": 0}
            game, score = line.strip("\n").split(": ")
            id = game.split(" ")[1]
            print(id)
            for event in score.split(";"):
                for balls in event.split(","):
                    num, color = balls.split()
                    print(num, color)
                    if int(num) > max_dic[color]:
                        max_dic[color] = int(num)
                        print(max_dic)
            power = max_dic["red"] * max_dic["green"] * max_dic["blue"]
            total += power
            print(power, total)
            print("="*90)
    return total