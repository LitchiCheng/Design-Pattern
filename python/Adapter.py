class Adaptee:
    def getData(self):
        return 5

class Adapter:
    def __init__(self, adaptee):
        self._adaptee = adaptee
    
    def getData(self):
        print("old data is %d" % self._adaptee.getData())
        return self._adaptee.getData()*44

if __name__ == "__main__":
    ol_data = Adaptee()
    new_data = Adapter(ol_data)
    print("new data is %d" % new_data.getData())
    pass