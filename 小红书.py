while True:
    try:
        school_number = int(input())
        print(school_number)
        human_number = list(map(int, input().strip().split(" ")))
        print(human_number)
        if len(human_number) == 0:
            print(0)
        elif len(human_number) == 1:
            print(human_number[0])
        else:
            i = 1
            human_number = sorted(human_number, reverse=True)
            result = human_number[0]
            while i < len(human_number):
                if human_number[i] == human_number[i - 1] or human_number[i] > human_number[
                    i - 1]:  # 这题真烂，只是要求相邻的数量不一致。
                    human_number[i] = human_number[i - 1] - 1
                    result += human_number[i]
                else:
                    result += human_number[i]
                i += 1
            print(result)
    except:
        break
