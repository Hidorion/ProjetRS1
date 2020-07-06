import re
import string

#variables
posavatar = "A"
Faim = 100
Soif = 100
Fatigue = 0
#while Faim > 0 or Soif > 0 or Fatigue < 100 :
print("Bonjour jeune âme. Tu es içi sur une île à priori vierge et déserte.Mais l'est-elle vraiment ?")
print("Ce sera à TOI et TOI seul(e) de le découvrir !")
print("Ah oui, j'en oublie les manière, je m'appelle Hidorion et je serais la petite voix qui t'accompagnera et toi, et toi tu es...")
avatar = str(input("Ah oui voilà c'est... "))
while not re.match("^[A-Za-z]*$", avatar) or avatar == "":
    avatar = str(input("C'est un drôle de nom... Non tu as du te tromper, recommence je t'en pris. (Utilisez juste des lettres s.v.p.) "))
avatar = avatar.capitalize()
print("Parfait et bien je te souhaite la bienvenue " + avatar + " !")
print()
print("Sur la carte tu te verras par ce symbole =>", posavatar)
print()
print("Tu devras gérer ta Faim, ta Soif et ta Fatigue.")
print(" Si ta Faim ou Soif descend en dessous de 0 ou si ta Fatigue atteint 100, tu as perdu.")
print()
print("Voici ton niveau actuel de Faim :  ", Faim,"/ 100")
print("Voici ton niveau actuel de Soif :  ", Soif,"/ 100")
print("Voici ton niveau actuel de Fatigue : ", Fatigue,"/ 100")
#print("Tu as perdu")
