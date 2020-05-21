from Student import Student
class MathStudent(Student):
    
    def __init__(self, MSSV, hoLot, ten, lop, namVaoHoc, diemTB):
        self.MSSV = MSSV
        super().__init__(hoLot, ten, lop, namVaoHoc, diemTB)

    def getMSSV(self):
        return self.MSSV

    def setMSSV(self, MSSV):
        self.MSSV = MSSV
        return