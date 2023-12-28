from abc import ABC, abstractmethod

class WidowSystemNotification:

    def __init__(self):
        self.observers = []

    def add(self, observer):
        self.observers.append(observer)
        print(f'add window {observer.number}')

    def delete(self, observer):
        self.observers.remove(observer)
        print(f'add window {observer.number}')

    def notification(self):
        for observer in self.observers:
            observer.get_notification()
class AbstractObserver(ABC):
    @abstractmethod
    def get_notification(self):
        pass

class Window_web(AbstractObserver):
    def __init__(self, number):
        self.number = number

    def get_notification(self):
        print(f'web-window {self.number} get notification')
class Window_mobile(AbstractObserver):
    def __init__(self, number):
        self.number = number

    def get_notification(self):
        print(f'mobile-window {self.number} get notification')


if __name__ == "__main__":
    window_web_1 = Window_web(1)
    window_web_2 = Window_web(2)
    window_web_3 = Window_web(3)

    window_mobile_1 = Window_mobile(1)
    window_mobile_2 = Window_mobile(2)

    system = WidowSystemNotification()
    system.add(window_web_1)
    system.add(window_web_2)
    system.add(window_web_3)

    system.add(window_mobile_1)
    system.add(window_mobile_2)
    system.notification()
