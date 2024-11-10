from varasto import Varasto

def alkutilanne(mehua, olutta):
    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")

def olut_getterit(olutta):
    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")

def mehu_paivitys_lisaa(mehua):
    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}")

def mehu_paivitys_ota(mehua):
    print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")

def virhe():
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)

def olut_paivitys_lisaa(olutta):
    print(f"Olutvarasto: {olutta}")
    print("olutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}")

def mehu_paivitys_lisaa_virhe(mehua):
    print(f"Mehuvarasto: {mehua}")
    print("mehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}")

def olut_paivitys_ota(olutta):
    print(f"Olutvarasto: {olutta}")
    print("olutta.ota_varastosta(1000.0)")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {olutta}")

def mehu_paivitys_otto_virhe(mehua):
    print(f"Mehuvarasto: {mehua}")
    print("mehua.otaVarastosta(-32.9)")
    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {mehua}")

def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    alkutilanne(mehua, olutta)
    olut_getterit(olutta)
    mehu_paivitys_lisaa(mehua)
    mehu_paivitys_ota(mehua)
    virhe()
    olut_paivitys_lisaa(olutta)
    mehu_paivitys_lisaa_virhe(mehua)
    olut_paivitys_ota(olutta)
    mehu_paivitys_otto_virhe(mehua)
    print("hei")
    print("hei")
    print("hei")
    print("hei")
    print("hei")
    print("hei")
    print("hei")
    print("hei")
    print("hei")
    print("hei")
    print("hei")
    print("hei")
    print("hei")
    print("hei")
    print("hei")
    print("hei")
    print("hei")
    print("hei")
    print("hei")
    print("hei")
    print("hei")
    print("hei")
    print("hei")
    print("hei")
    print("hei")
    print("hei")
    print("hei")
    print("hei")
    print("hei")
    print("hei")
    print("hei")
    print("hei")
    print("hei")
    print("hei")
    print("hei")
    print("hei")
    print("hei")

if __name__ == "__main__":
    main()
