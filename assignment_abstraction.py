from abc import abstractmethod, ABC


class TouchScreenLaptop(ABC):
    @abstractmethod
    def scroll(self):
        pass

    @abstractmethod
    def click(self):
        pass
    

class HP(TouchScreenLaptop):
    def scroll(self):
        print("HP Scrolled!")


class HPNotebook(HP):
    def click(self):
        print("HP Clicked!")


class DELL(TouchScreenLaptop):
    def scroll(self):
        print("DELL Scrolled!")


class DELLNotebook(DELL):
    def click(self):
        print("DELL Clicked!")


hpn = HPNotebook()
dell = DELLNotebook()

hpn.scroll()
hpn.click()
dell.scroll()
dell.click()
