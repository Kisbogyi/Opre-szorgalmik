import sys

page_input = sys.stdin.readlines()
page_input = page_input[0].strip().split(",")

processed_input = [[3, abs(int(inp)), False, ""] for inp in page_input]  # processes input
# 1st element is the lock timer
# 2nd the page in memory
# 3rd is the second chance indicator
all = len(processed_input)

fifo_size = 3
fifo = []
available = ["A", "B", "C"]


def where_in_fifo(it, sc):
    for i in range(len(sc)):
        if it[1] == sc[i][1]:
            return i
    return -1


def find_raplaceable(newitem):  # TODO: redo
    i = 0
    while i < len(fifo):
        if fifo[i][0] >= 0:
            i += 1
        elif fifo[i][2]:
            temp = fifo.pop(i)
            temp[2] = False
            fifo.append(temp)
        else:
            available.append(fifo.pop(i)[3])
            newitem[3] = available[0]
            print(available.pop(0), end="")
            fifo.append(newitem)
            return
    print("*", end="")


for item in processed_input:
    for page in fifo:  # makes the pages in FIFO older
        page[0] -= 1

    idx = where_in_fifo(item, fifo)  # if page is in FIFO unlock it and give a second chance
    if idx >= 0:
        fifo[idx][0] = 0
        fifo[idx][2] = True
        all -= 1
        print("-", end="")


    else:  # if item is not in FIFO
        if len(fifo) < 3:  # checks if FIFO is full or not.
            item[3] = available[0]
            print(available.pop(0), end="")
            fifo.append(item)  # if the FIFO is empty just add the next item to it
        else:
            find_raplaceable(item)
print(f"\n{all}")
