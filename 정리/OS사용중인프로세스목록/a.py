import psutil

def def_A():
    # 코드 내용 입력
   
    # 현재 실행 중인 프로세스의 정보를 가져옵니다.
    processes = []

    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            # 프로세스 이름, PID, CPU 사용량을 가져옵니다.
            
            process = {
                'name': proc.info['name'],
                'pid': proc.info['pid'],
                'cpu_percent': proc.info['cpu_percent']
            }

            # 프로세스 정보를 리스트에 추가합니다.
            processes.append(process)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    # CPU 사용량이 높은 순으로 프로세스를 정렬합니다.
    processes = sorted(processes, key=lambda x: x['cpu_percent'], reverse=True)

    # 정렬된 프로세스 정보를 출력합니다.
    for p in processes:
        print(f"{p['name']} ({p['pid']}): {p['cpu_percent']}%")

    # CPU 사용량 측정
    cpu_percent = psutil.cpu_percent(interval=0.1)

    # 측정한 CPU 사용량 출력
    print(f"CPU 사용량: {cpu_percent}%")
    
    # 문자열로 변환하여 반환합니다.
    return str(processes) + "\nCPU 사용량: " + str(cpu_percent) + "%\n"

    # 파일에 결과를 저장합니다.
with open("C:/doit/result.txt", "w", encoding="utf-8", newline="\r\n") as f:
        f.write(def_A())
