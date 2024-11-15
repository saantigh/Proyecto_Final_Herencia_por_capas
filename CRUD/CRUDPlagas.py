from Modelo.producto_plagas import ControlPlagas

class CRUDPlagas:
    #Stock de 5 productos de control(plagas).
    @staticmethod
    def create():
        plaga1 = ControlPlagas("Plaga1","ICA2376",4,54000,15)
        plaga2 = ControlPlagas("Plaga2Silver","ICA296",4,134000,15)
        plaga3 = ControlPlagas("Plaga3SilverGold","ICA345",9,340000,30)
        plaga4 = ControlPlagas("Plaga4Gold","ICA789",5,540000,30)
        plaga5 = ControlPlagas("Plaga5Premium","ICA992",8,925000,90)

        return [plaga1,plaga2,plaga3,plaga4,plaga5]