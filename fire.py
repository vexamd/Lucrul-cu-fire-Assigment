import threading
class Cube:

    def __init__(self, latura):
        self.latura = latura
        self.lungime = None
        self.volum = None
        print("Un cub cu latura de: ", self.latura, "CM este:")

    def volume(self):
        self.volum = self.latura * self. latura * self.latura

    def totalLungime(self):
        self.lungime = 12 * self.latura

if __name__ == "__main__":
    cub_1 = Cube(10)
    cub_2 = Cube(15)

    threads_list = list()

    cub_list = [cub_1, cub_2]

    for cub_elem in cub_list:
         t1 = threading.Thread(target=cub_elem.volume(), args=())
         t2 = threading.Thread(target=cub_elem.totalLungime(), args=())

         t1.start()
         t2.start()
         threads_list.append(t2)
         threads_list.append(t1)
         
    for t in threads_list:
         t.join()
     
    for cub_elem in cub_list: 
         print("Lungimea tuturor laturileor: " + str(cub_elem.lungime))
         print("Volumul cubului: " + str(cub_elem.volum))
