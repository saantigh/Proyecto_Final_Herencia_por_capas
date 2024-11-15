from Modelo.cliente import Cliente

class CRUDCLiente:
    #Lista de clientes predefinidos
    @staticmethod
    def create():
        cliente1 = Cliente("Alexandra Ocampo Ruiz","1234556789")
        cliente2 = Cliente("Juana Valentina Martinez Sanchez", "987654321")
        cliente3 = Cliente("Manuela Marin Rojo","1027200500")
        cliente4 = Cliente("Sebastian Perdomo Rengifo","100000000")
        cliente5 = Cliente("Alejandro Castrillon Rivera","000000001")

        return [cliente1,cliente2,cliente3,cliente4,cliente5]
