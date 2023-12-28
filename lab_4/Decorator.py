from abc import ABC, abstractmethod
class Component(ABC):
  @abstractmethod
  def do_work(self):
      pass
class Window(Component):
  def do_work(self):
      return('Empty Window')
class Decorator(Component):
  def __init__(self, component=''):
      self.component = component
  @abstractmethod
  def do_work(self):
      pass
class Border(Decorator):
  def do_work(self):
      return(f"<Border>{self.component.do_work()}</Border>")
class Thick(Decorator):
  def do_work(self):
      return(f"<Thick>{self.component.do_work()}</Thick>")

if __name__ == "__main__":
    a=Window()
    print(Thick(Border(a)).do_work())