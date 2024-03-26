!To DO LIST MANAGER DOCUMENTAION!
This program is used to manage daily tasks using priority queue, heap, queue data structures 
You can add new tasks, extract highest priority tasks after finishing, display waiting tasks, and much more.
We use first-in-first-out machanism to handle tasks with the same priority.
The application provides command-line user interface to hide complicated operations. This program can easly be done by implemening the link list data structure but we prefer hard ways.
Enjoy your work! 
----------------------
Interpret the meanning of commands:
[O(n + lgn)]    ins: insert a new task. This command takes two arguments, the priority level and the task name.
[Θ(lgn)]        ext: extract the highest priority task. 
[Θ(1)]          imp: show the highest priority task name. 
[Θ(n)]          shw: show indexes, priority levels, task names of all tasks. 
[O(nlgn + lgn)] inc: increase the priority of the index-th task to a new priority level, three arguments are given, the index and priority of the wantted increase task sepreateed by a colon and a new priority level value. 
                qit: Quit the program.
The running time is terrible though. If this program implements the link list the running of all operations would take only O(n)