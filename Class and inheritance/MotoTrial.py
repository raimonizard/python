from Motorbike import *

class MotoTrial(Motorbike):
    __wheelsize = None

    def __init__(self,pbrand,pmodel,php,pcc,pyear,pwheelsize):
        super().__init__(pbrand,pmodel,php,pcc,pyear)
        self.__wheelsize = pwheelsize

    # toString method
    def __str__(self):
        return("The mototrial is the brand of " + self._brand + " and its model is " + self._model + " and its wheelsize is " + str(self.__wheelsize))