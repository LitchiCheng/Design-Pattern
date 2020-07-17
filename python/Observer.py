class Observer:
    def __init__(self):
        pass
    
    def update(self):
        pass

class ConcretObserver1(Observer):
    def update(self):
        print("i am 1")

class ConcretObserver2(Observer):
    def update(self):
        print("i am 2")
    
class Subject:
    def __init__(self):
        self._observer_list = []

    def attachObserver(self, ob):
        if len(self._observer_list) == 0:
            self._observer_list.append(ob)
            return
        for i in self._observer_list:
            if(i != ob):
                self._observer_list.append(ob)
    
    def dettachObserver(self, ob):
        if len(self._observer_list) == 0:
            return
        for i in self._observer_list:
            if(i == ob):
                self._observer_list.remove(ob)
    
    def notifyObserver(self):
        for i in self._observer_list:
            i.update()
    
class ConcretSubject(Subject):
    def run(self):
        self.notifyObserver()

if __name__ == "__main__":
    c1 = ConcretObserver1()
    c2 = ConcretObserver2()
    s = ConcretSubject()
    s.attachObserver(c1)
    s.attachObserver(c2)
    s.run()