class Item():
    def __init__(self, name, time, priority):
        self.name = name
        self.time = time
        self.priority = priority
    def tell_name(self):
        return self.name
    def tell_time(self):
        return self.time
    def high_priority(self):
        if self.priority == 'high':
            return self.name
        else:
            return ''
    def change_name(self, newname):
        self.name = newname
    def change_time(self, newtime):
        self.time = newtime
    def change_priority(self, newpriority):
        self.priority = newpriority


a = Item('cleaning', 10, 'high')
b = Item('walking', 20, 'low')
c = Item('washing', 15, 'medium')

items = [a, b, c]

def highpr():
    for i in items():
        if i.tell_priority() == 'high':
            print(i.tell_name())