
from abc import ABC, abstractmethod
import copy
import time


class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name, **attr):
        obj = self._objects.get(name)
        if not obj:
            raise ValueError('Incorrect object name: {}'.format(name))
        obj = copy.deepcopy(obj)
        obj.__dict__.update(attr)
        return obj


class Monster:
    def __init__(self, name, health, damage):
        time.sleep(1)
        self.name = name
        self.health = health
        self.damage = damage

    def __eq__(self, other):
        return self.name == other.name and self.health == other.health and self.damage == other.damage


if __name__ == '__main__':
    
        orc = Monster('Orc', 100, 10)
        orc2 = Monster('Orc', 100, 10)

        prototype = Prototype()
        prototype.register_object('orc', orc)
        prototype.register_object('orc2', orc2)

        prototype.clone('orc')
        prototype.clone('orc2')
