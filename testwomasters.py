from multiprocessing.managers import BaseManager
import queue,random
task_queue=queue.Queue()
result_queue=queue.Queue()
class QueueManager(BaseManager):
    pass
def return_task_queue():
    global task_queue
    return task_queue
def return_result_queue():
    global result_queue
    return result_queue
if __name__=='__main__':    
    QueueManager.register('get_task_queue',callable=return_task_queue)
    QueueManager.register('get_result_queue',callable=return_result_queue)
    print('正在注册端口')
    manager=QueueManager(address=('127.0.0.1',9000),authkey = b'abc')
    print('--即将开始--')
    manager.start()
    print('管理器开始工作')
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    for i in range(10):
        n = random.randint(0,110)
        print('put task %d....'%n)
        task.put(n)
    print('try get result =....')
    for i in range(10):
        n=result.get(timeout=20)
        print('get result %d'%n)
    manager.shutdown()
    print('master exit')
    
