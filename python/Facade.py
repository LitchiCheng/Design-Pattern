class InterFaceA:
    def method(self):
        print("i am a")

class InterFaceB:
    def method(self):
        print("i am b")

class InterFaceC:
    def method(self):
        print("i am c")

class Facade:
    def methodComboAB(self):
        a = InterFaceA()
        b = InterFaceB()
        a.method()
        b.method()
    
    def methodComboBC(self):
        b = InterFaceB()
        c = InterFaceC()
        b.method()
        c.method()
    
if __name__ == "__main__":
    client = Facade()
    if 0:
        client.methodComboAB()
    else:
        client.methodComboBC()
