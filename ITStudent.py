from Student import Student
class ITStudent(Student):
    
    def __init__(self, MSSV, hoLot, ten, lop, namVaoHoc, diemTB):
        try:
            self.MSSV = int(MSSV)
            super().__init__(hoLot, ten, lop, namVaoHoc, diemTB)
            return
        except ValueError:
            print("MSSV must be an integer.")
            return
    
    def getMSSV(self):
        return self.MSSV

    def setMSSV(self, MSSV):
        self.MSSV = MSSV
        return
    
