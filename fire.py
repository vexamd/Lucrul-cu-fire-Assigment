import threading
class Cub:
    def __init__(self, num):
        self.num = num
        print("Un cub cu latura de {}".format(self.num))
    def calc_volum(self):
        return "Volumul cubului = {}".format(self.num * self.num * self.num)
    def lenght_lat(self):
        self.lenght = self.num * 12
        return "Lungimea totala a tuturor laturilor = {}".format(self.lenght)
    def main(cub):
        if __name__ == "__main__":
            t1 = threading.Thread(target=calc_volum(), args=())
            t2 = threading.Thread(target=lenght_lat(), args=())

            t2.start()
            t2.join()
            t1.start()
            t1.join()
cub_1 = Cub(10)
print(cub_1.lenght_lat())
print(cub_1.calc_volum())
cub_2 = Cub(12)
print(cub_2.lenght_lat())
print(cub_2.calc_volum())
print("Finalizare!")