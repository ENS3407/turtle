import geometrie


while True:
  zeichnung=int(input("Dreieck (1) quadrat(2)"))
  if zeichnung==1 :
    seite=int(input("seitenlaenge="))
    farbe=input("Farbe: ")
    x=int(input("x="))
    y=int(input("y="))
    geometrie.dreieck(seite,farbe,x,y)
  if zeichnung==2 :
    seite=int(input("seitenlaenge="))
    farbe=input("Farbe: ")
    x=int(input("x="))
    y=int(input("y="))
    geometrie.quadrat(seite,farbe,x,y)