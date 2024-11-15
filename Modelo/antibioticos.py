class Antibiotico:
    def __init__(self, nombre_antibiotico: str, dosis: float, tipo_animal: str, precio_antibiotico: float):
        self.__nombre_antibiotico = nombre_antibiotico  
        self.__dosis = dosis  
        self.__tipo_animal = tipo_animal  
        self.__precio_antibiotico = precio_antibiotico  

    # Getter y Setter para nombre_antibiotico
    @property
    def nombre_antibiotico(self):
        return self.__nombre_antibiotico

    @nombre_antibiotico.setter
    def nombre_antibiotico(self, nombre_antibiotico):
        if not nombre_antibiotico.strip():
            raise ValueError("El nombre del antibiótico no puede estar vacío.")
        if not all(char.isalpha() or char.isspace() for char in nombre_antibiotico):
            raise ValueError("El nombre del antibiótico solo puede contener letras y espacios.")
        self.__nombre_antibiotico = nombre_antibiotico

    # Getter y Setter para dosis
    @property
    def dosis(self):
        return self.__dosis

    @dosis.setter
    def dosis(self, dosis):
        if 400 <= dosis <= 600:
            self.__dosis = dosis
        else:
            raise ValueError("La dosis debe estar entre 400Kg y 600Kg.")

    # Getter y Setter para tipo_animal
    @property
    def tipo_animal(self):
        return self.__tipo_animal

    @tipo_animal.setter
    def tipo_animal(self, tipo_animal):
        if tipo_animal.lower() in ['bovinos', 'caprinos', 'porcinos']:
            self.__tipo_animal = tipo_animal
        else:
            raise ValueError("El tipo de animal debe ser 'bovinos', 'caprinos' o 'porcinos'.")

    # Getter y Setter para precio_antibiotico
    @property
    def precio_antibiotico(self):
        return self.__precio_antibiotico

    @precio_antibiotico.setter
    def precio_antibiotico(self, precio_antibiotico):
        if precio_antibiotico <= 0:
            raise ValueError("El precio del antibiótico debe ser un valor positivo.")
        self.__precio_antibiotico = precio_antibiotico

