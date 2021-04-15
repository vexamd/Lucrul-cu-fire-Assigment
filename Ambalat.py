from queue import Queue
from threading import Thread

class Cube():
    
    def __init__(self, lat):
        self.lat = lat

    def calcul_volum(self):
        return self.lat ** 3
        
        
    def calcul_suma_laturi(self):
        return self.lat * 12


if __name__ == "__main__": 

    que = Queue()     # în coadă se vor stoca în ordine valorile obtinute in urma executiei thread-urilor
    
    cube1 = Cube(3)
    cube2 = Cube(5)
    
    cube_list = list()
    cube_list.extend([cube1, cube2])
    
    threads_list = list()
    
    for cube_elem in cube_list:
         t1 = Thread(target=lambda q, cube: q.put(cube.calcul_suma_laturi()), args=(que, cube_elem))
         t2 = Thread(target=lambda q, cube: q.put(cube.calcul_volum()), args=(que, cube_elem))
         t1.start()
         t2.start()

    for t in threads_list:
         t.join()
    
    while not que.empty():
        print(que.get())









