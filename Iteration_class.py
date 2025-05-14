# custom iterable or iteration
class myrange:
    def __init__(self,start,stop,step):
        self.start=start
        self.stop=stop
        self.step=step

    def __iter__(self):
        return myrange_iterator(self)

class myrange_iterator:
    def __init__(self,iterable_obj):
        self.iterable_obj=iterable_obj

    def __iter__(self):
        return self
    
    def __next__(self):
        result=self.iterable_obj.start
        if self.iterable_obj.start<self.iterable_obj.stop:
            self.iterable_obj.start=self.iterable_obj.start+self.iterable_obj.step
            return result
        else:
            raise StopIteration
        
for i in myrange(4,41,5):
    print(i)
