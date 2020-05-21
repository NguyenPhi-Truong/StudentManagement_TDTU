class Student():

    def __init__(self, hoLot, ten, lop, namVaoHoc, diemTB):
        self.hoLot = hoLot
        self.ten = ten
        self.lop = lop
        self.namVaoHoc = namVaoHoc
        self.diemTB = diemTB

    def getHoLot(self):
        return self.hoLot
    
    def setHoLot(self, hoLot):
        self.hoLot = hoLot

    def getTen(self):
        return self.ten

    def setTen(self, ten):
        self.ten = ten
    
    def getLop(self):
        return self.lop

    def setLop(self, lop):
        self.lop = lop

    def getNamVaoHoc(self):
        return self.namVaoHoc
    
    def getDiemTB(self):
        return self.diemTB
    
    def toString(self):
        return self.hoLot + ' ' + self.ten + ' - ' + self.lop + ' - ' + str(self.namVaoHoc) + ' - ' + str(self.diemTB)

    