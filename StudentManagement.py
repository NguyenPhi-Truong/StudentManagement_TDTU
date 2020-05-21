class StudentManagement():
    def readStudent(self, fileName):
        try:
            with open(fileName, 'r') as f:
                pass
        except FileNotFoundError:
            print("File {} Not Found or Not Created.".format(fileName))
        return

    def getDsSinhVien(self):
        return
    
    def setDsSinhVien(self):
        return

    def addStudent(self, student):
        return

    def addStudentByIndex(self, student, index):
        return

    def delStudentByIndex(self,index):
        return

    def searchStudent(self, term):
        return

    def sortDs(self, DsSinhVien):
        return

    def writeStudent(self):
        return
    
    def writeFile(self):
        return
