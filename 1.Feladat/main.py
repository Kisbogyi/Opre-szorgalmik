import sys

waiting_for_time = []
data = sys.stdin.readlines()
for line in data:
    line = line.strip().split(",")
    if line[0] != "":
        line[1] = int(line[1])
        line[2] = int(line[2])
        line[3] = int(line[3])
        waiting_for_time.append(line)

for i in range(len(waiting_for_time)):
    waiting_for_time[i].append(0)
rr_ready = []
fsrt_que = []
finished = []
time = 0
rr_time = 2
prevtask = None

waiting_for_time.sort(key=lambda age: age[2])
while len(waiting_for_time) != 0 or len(rr_ready) != 0 or len(fsrt_que) != 0:
    if len(waiting_for_time) != 0 and waiting_for_time[0][2] == time:
        while len(waiting_for_time) != 0 and waiting_for_time[0][2] == time:
            if waiting_for_time[0][1] == 1:
                rr_ready.append(waiting_for_time.pop(0))
            elif waiting_for_time[0][1] == 0:
                fsrt_que.append(waiting_for_time.pop(0))
                fsrt_que.sort(key=lambda process_time: process_time[3])

    if len(rr_ready) != 0:
        if prevtask != rr_ready[0]:
            print(rr_ready[0][0], end="")
        rr_time -= 1
        rr_ready[0][3] -= 1
        rr_ready[0][4] -= 1
        prevtask = rr_ready[0]
        if rr_ready[0][3] != 0:
            if rr_time == 0:
                tsk = rr_ready.pop(0)
                rr_ready.append(tsk)
                rr_time = 2
        else:
            temp = rr_ready.pop(0)
            finished.append(temp)

    elif len(fsrt_que) > 0:
        if prevtask != fsrt_que[0]:
            print(fsrt_que[0][0], end="")
        fsrt_que[0][3] -= 1
        fsrt_que[0][4] -= 1
        prevtask = fsrt_que[0]
        if fsrt_que[0][3] == 0:
            temp = fsrt_que.pop(0)
            finished.append(temp)

    time = time + 1
    for task in rr_ready:
        task[4] += 1
    for task in fsrt_que:
        task[4] += 1

print("")
finished.sort(key=lambda x: (x[2], x[0]))
for i, task in enumerate(finished):
    print(f"{task[0]}:{task[4] + 1}", end="")
    if i < len(finished) - 1:
        print(",", end="")
