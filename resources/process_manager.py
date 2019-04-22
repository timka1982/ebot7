
import time
from multiprocessing import Process, Pipe


def process_func(connection, idx):
    while True:
        instruction = connection.recv()
        if instruction['idx'] != idx:
            continue
        if instruction['type'] == 'fetch':
            print('Process %s is fetching' % idx)
            time.sleep(3)
            print('Process %s done fetching' % idx)
        if instruction['type'] == 'answer':
            print('Process %s is answering' % idx)
            time.sleep(0.2)
            print('Process %s is done answering' % idx)


def manager_func(main_conn, child_conn):
    p1 = Process(target=process_func, args=(child_conn, 1))
    print('starting up child processes')
    p1.start()
    p2.start()
    while True:
        if not p1.is_alive():
            print('p1 has died')
            break
        if not p2.is_alive():
            print('p2 has died')
            break
        time.sleep(0.1)
    print('EXITING LOOP :(')


class ProcessManager:
    def __init__(self):
        main_conn, child_conn = Pipe()
        process_manager = Process(target=manager_func, args=(main_conn,
                                                             child_conn))
        print('starting up process_manager')
        process_manager.start()
        main_conn.send({'type': 'fetch', 'idx': 0})
        time.sleep(5)
        main_conn.send({'type': 'answer', 'idx': 0})
        main_conn.send({'type': 'fetch', 'idx': 1})
        time.sleep(5)
        main_conn.send({'type': 'answer', 'idx': 1})
        main_conn.send({'type': 'fetch', 'idx': 0})
        main_conn.send({'type': 'answer', 'idx': 1})
        time.sleep(5)
        print('Seems to be working')


process_manager = ProcessManager()
