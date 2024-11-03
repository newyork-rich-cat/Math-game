import random
import threading

def make_question(stage):
    a = random.randint(1, 5 * stage)
    q = str(a)
    for i in range(stage // 2 + 1):
        b = random.randint(1, 5 * stage)
        op = random.randint(1, 3)
        if op == 1:
            q += "+"
        elif op == 2:
            q += "-"
        elif op == 3:
            q += "*"
        q += str(b)
    return q

def timeout_input(prompt, timeout):
    print(prompt, end=': ', flush=True)
    ans = [None]  # Using a list to modify within the inner function
    
    def get_input():
        ans[0] = input()
    
    thread = threading.Thread(target=get_input)
    thread.start()
    thread.join(timeout)
    
    if thread.is_alive():
        print("\n시간 초과!")
        return None
    return ans[0]

score = 0
skip_limit = 4
for stage in range(1, 100):
    sc1 = 0
    sc2 = 0
    print("******************************************************")
    print("스테이지", stage, "   스킵:skip   남은 스킵 횟수:", skip_limit)
    print("******************************************************")
    
    for x in range(3):
        q = make_question(stage)
        print("******************************************************")
        print("남은 문제 수:",3 - x )
        print("******************************************************")
        
        print(q)
        print("******************************************************")
        ans = timeout_input("답을 입력하세요", timeout=5)  # 5 seconds to answer
        
        if ans is None:  # If the answer is None, it means timeout occurred
            print("******************************************************")
            sc2 += 1
            break
        
        if ans == "skip":
            if skip_limit > 0:
                skip_limit -= 1
                print("******************************************************")
                print("스킵하였습니다.      남은 스킵 횟수:", skip_limit)
                print("******************************************************")
                continue
            else:
                while ans == "skip":
                    print("남은 스킵 횟수가 없습니다.")
                    ans = timeout_input("답을 입력하세요", timeout=60)
        
        try:
            r = int(ans)
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력하세요.")
            sc2 += 1
            continue
        
        if eval(q) == r:
            print("정답!")
            sc1 += 1
            score += stage
        else:
            print("오답!")
            sc2 += 1
            
    print("정답 :", sc1, "오답 :", sc2)
    if sc2 == 0:
        print("다음 스테이지로")
    else:
        print("게임 오버")
        print("******************************************************")
        print("스코어:", score)
        print("******************************************************")
        break
