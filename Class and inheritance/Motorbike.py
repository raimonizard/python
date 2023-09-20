class Motorbike:
    
    _brand = None
    _model = None
    _hp = None
    _cc = None
    _year = None


    # class defined constructor
    def __init__(self, pbrand, pmodel, php, pcc, pyear):
        self._brand = pbrand
        self._model = pmodel
        self._hp = php
        self._cc = pcc
        self._year = pyear

    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, new_brand):
        self._brand = new_brand

    @brand.deleter
    def brand(self):
        del self._brand

    # toString method
    def __str__(self):
        return("The motorbike is the brand of " + self._brand + " and its model is " + self._model)

    # define how to print the datatype
    def __repr__(self):
      return f'Motorbike(brand={self._brand}, model = {self._model})'