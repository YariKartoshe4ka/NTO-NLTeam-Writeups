from sage.all import *

data = [277, 92, 775, 480, 160, 92, 31, 586, 277, 801, 355, 489, 801, 31, 62, 926, 725, 489, 160, 92, 31, 586, 277, 801, 355, 489, 1281, 62, 801, 489, 1175, 277, 453, 489, 453, 348, 725, 31, 348, 864, 864, 348, 453, 489, 737, 288, 453, 489, 889, 804, 96, 489, 801, 721, 775, 926, 1281, 631]

class DihedralCrypto:
    def __init__(self, order: int) -> None:
        self.__G = DihedralGroup(order)
        self.__order = order
        self.__gen = self.__G.gens()[0]
        self.__list = self.__G.list()
        self.__padder = 31337
        print(self.__G,
        self.__order, 
        self.__gen,
        self.__list,
        self.__padder )
        
    def __pow(self, element, exponent: int):
        print("powwwwwww")
        try:
            element = self.__G(element)
        except:
            raise Exception("Not Dihedral rotation element")
        answer = self.__G(())
        aggregator = element
        for bit in bin(int(exponent))[2:][::-1]:
            if bit == '1':
                answer *= aggregator
            aggregator *= aggregator
        return answer        
    
    def __byte_to_dihedral(self, byte: int):
        return self.__pow(self.__gen, byte * self.__padder)
    
    def __map(self, element):
        return self.__list.index(element)
    
    def __unmap(self, index):
        return self.__list[index]
    def unhash(self, hashh):
        restore = []
        for i in hashh:
            restore.append(self.__unmap(i))
        return restore
    
    def hash(self, msg):
        answer = []
        for byte in msg:
            answer.append(self.__map(self.__byte_to_dihedral(byte)))
        return answer
    def unpow(self, dataaa):
        element = self.__gen
        pass


if __name__ == "__main__":
    dihedral = DihedralCrypto(1337)
    flag = b"nto{"
    while True:
        for i in b'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_':
            print(flag, i)
            temp_flag = flag + i.to_bytes(1)
            temp = dihedral.hash(temp_flag)
            if data[:len(temp)] == temp:
                flag = flag + i
                break
            print(temp, temp_flag, flag)

        if len(flag) == len(data):
            break
        
    print(flag)
    print(answer, data)
    rev = dihedral.unhash(data)
    print(len(rev))
