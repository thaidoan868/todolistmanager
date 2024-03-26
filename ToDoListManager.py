"""
!To DO LIST MANAGER DOCUMENTAION!
This program is used to manage daily tasks using priority queue, heap, queue data structures 
You can add new tasks, extract highest priority tasks after finishing, display waiting tasks, and much more.
We use first-in-first-out machanism to handle tasks with the same priority.
The application provides command-line user interface to hide complicated operations. This program can easly be done by implemening the link list data structure but we prefer hard ways.
Enjoy your work! 
----------------------
Interpret the meanning of commands:
ins: insert a new task. This command takes two arguments, the priority level and the task name. 
ext: extract the highest priority task.
imp: show the highest priority task name.
shw: show indexes, priority levels, task names of all tasks.
inc: increase the priority of the index-th task to a new priority level, three arguments are given, the index and priority of the wantted increase task sepreateed by a colon and a new priority level value.
qit: Quit the program.
"""
import sys, copy
def Parent(i):
    return int((i+1)/2) -1
def Left(i):
    return 2*i + 1
def Right(i):
    return 2*i + 2
def MaxHeapify(A, i):
    l,r = Left(i), Right(i)
    if (l <= len(A)-1) and (A[l]['priority'] < A[i]['priority']): smallest = l
    else: smallest = i
    if (r <= len(A)-1) and (A[r]['priority'] < A[smallest]['priority']): smallest = r
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        MaxHeapify(A, smallest)
def BuilMaxHeap(A):
    for i in range(int(len(A)/2)-1,-1,-1): MaxHeapify(A, i)
def HeapMaximumKey(A):
    return A[0]
def HeapExtractMax(A):
    max = copy.deepcopy(A[0])
    A[0]['task_names'].pop(0)
    if not A[0]['task_names']:
        A[0] = A[len(A)-1]
        A.pop()
        MaxHeapify(A, 0)
    return max
def HeapIncreaseKey(A, index, old_priority, new_priority):
    i =  CheckValidKey(A, old_priority, 0)
    updated_task = dict(priority=new_priority, task_names=[A[i]['task_names'][index]])
    if len(A[i]['task_names'])-1:
        A[i]['task_names'].pop(index)
        MaxheapInsert(A, updated_task)
    else: 
        A.pop(i)
        BuilMaxHeap(A)
        MaxheapInsert(A, updated_task)
def MaxheapInsert(A, new_task):
    i = -1
    if A: #Them 1 task da co priority
        i = CheckValidKey(A, new_task['priority'], 0)
        if i != -1:
            A[i]['task_names'].append(new_task['task_names'][0])
    if i == -1:
        A.append(new_task)
        i = len(A)-1
        while i > 0 and A[Parent(i)]['priority'] > A[i]['priority']:
            A[Parent(i)], A[i] = A[i], A[Parent(i)]
            i = Parent(i)
def CheckValidKey(A, key, i):
    #Có 2 cơ hội function = i: Chính bản thân nó = key hoặc con của nó = key
    #Một đứa con = True kết thúc tìm kiếm
    if key == A[i]['priority']: return i
    l,r = Left(i), Right(i)
    if (l <= len(A)-1) and A[i]['priority'] < key and A[l]['priority'] <= key:
        _ = CheckValidKey(A, key, l)
        if _ != -1: return _
    if (r <= len(A)-1) and A[i]['priority'] < key and A[r]['priority'] <= key:
        _ = CheckValidKey(A, key, r)
        if _ != -1: return _
    return -1
def ToDoListMangager():
    queue = []
    while True:
        request = input('Command: ').split(maxsplit=2)
        if len(request) == 1:
            if request[0] == 'ext': 
                if queue: print("Removed task: %s" % (HeapExtractMax(queue)['task_names'][0]))
                else: print('ERROR: Heap underflows', file=sys.stderr)
            elif request[0] == 'shw': 
                if queue:
                    print('--------------------------------------')
                    print('Index | Priority | Task name')
                    print('--------------------------------------')
                    for task_class in queue: 
                        i = 0
                        for task in task_class['task_names']:
                            print('|%2d   | %02d       | %s' % (i, task_class['priority'], task))
                            i += 1
                    print('--------------------------------------')
                else: print('The list is empty')
            elif request[0] == 'imp': 
                if queue: print('The hightest priority task: %2d - %s' % (queue[0]['priority'], queue[0]['task_names'][0])) 
                else: print('The list is empty')
            elif request[0] == 'qit': break
            elif request[0] in ['ins', 'inc']: print('ERROR: No arguments', file=sys.stderr)
            else: print('ERROR: invalid syntax', file=sys.stderr)
        elif len(request) == 3:
            if  request[0] == 'ins' and request[1].isnumeric(): 
                new_task = dict(priority=int(request[1]), task_names=[request[2]])
                MaxheapInsert(queue, new_task)
            elif len(request[1].split(':')) == 2:
                index, old_priority = request[1].split(':')
                if request[0] == 'inc' and index.isnumeric() and old_priority.isnumeric and request[2].isnumeric():
                    index, old_priority, new_priority = int(index), int(old_priority), int(request[2])
                    if queue: 
                        i = CheckValidKey(queue, old_priority, 0)
                        if i != -1:
                            if 0<= index <=len(queue[i]['task_names'])-1:
                                if new_priority >= queue[i]['priority']: print('ERROR: New priority is lower than or equal to the current priority', file=sys.stderr)
                                else: HeapIncreaseKey(queue, index, old_priority, new_priority)
                            else: print('ERROR: Invalid index', file=sys.stderr)
                        else: print('ERROR: Invalid priority value', file=sys.stderr)
                    else: print('The list is empty')
                else: print('ERROR: invalid syntax', file=sys.stderr)
            else: print('ERROR: invalid syntax', file=sys.stderr)
        else: print('ERROR: invalid syntax', file=sys.stderr)
print("""
##################################
      TO DO LIST MANAGAGER
##################################
Synax: ins|ext|imp|shw|inc|qit ... [priority|index:old_priority] ... [new task name|new priority]
Consult the documentation for more details
----------------------------------
""")
ToDoListMangager()

