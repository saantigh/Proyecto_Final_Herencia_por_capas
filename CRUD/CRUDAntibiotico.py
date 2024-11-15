from Modelo.antibioticos import Antibiotico

class CRUDAntibiotico:
    # Stock de 5 productos antibióticos
    @staticmethod
    def create():
        antibiotico1=Antibiotico("antibiotico1",300,"caprinos",87000)
        antibiotico2=Antibiotico("antibiotico2Silver",500,"porcinos",256000)
        antibiotico3=Antibiotico("antibiotico3SilverGold",500,"porcinos",340000)
        antibiotico4=Antibiotico("antibiotico4Gold",300,"bovinos",540000)
        antibiotico5=Antibiotico("antibiotico5GoldPremium",800,"bovinos",750000)
        
        return [antibiotico1,antibiotico2,antibiotico3,antibiotico4,antibiotico5]