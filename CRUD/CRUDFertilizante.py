from Modelo.producto_fertilizante import ControlFertilizantes

class CRUDFertilizantes:
    #Stock de 5 productos de control(fertilizantes). 
    @staticmethod
    def create():
        fertilizante1 = ControlFertilizantes("Fertilizante1","ICA237",4,54000,"2024-02-14")
        fertilizante2 = ControlFertilizantes("Fertilizante2Silver","ICA2968",4,134000,"2024-03-30")
        fertilizante3 = ControlFertilizantes("Fertilizante3SilverGold","ICA3457",9,340000,"2024-05-07")
        fertilizante4 = ControlFertilizantes("Fertilizante4Gold","ICA652",5,640000,"2024-03-15")
        fertilizante5 = ControlFertilizantes("Fertilizante5Premium","ICA960",8,1025000,"2024-01-12")

        return [fertilizante1,fertilizante2,fertilizante3,fertilizante4,fertilizante5] 