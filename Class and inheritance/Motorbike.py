class Motorbike:
    _brand: str = None
    _model: str = None
    _hp: int = None
    _cc: int = None
    _year: int = None


    # class defined constructor
    def __init__(self, pbrand: str, pmodel: str, php: int, pcc: int, pyear: int):
        self._brand = pbrand
        self._model = pmodel
        self._hp = php
        self._cc = pcc
        self._year = pyear

    @property
    def brand(self) -> str:
        return self._brand
    
    @brand.setter
    def brand(self, new_brand):
        self._brand = new_brand

    @brand.deleter
    def brand(self):
        del self._brand

    # toString method
    def __str__(self) -> str:
        return("The motorbike is the brand of " + self._brand + " and its model is " + self._model)

    # define how to print the datatype
    def __repr__(self) -> str:
      return f'Motorbike(brand={self._brand}, model = {self._model})'