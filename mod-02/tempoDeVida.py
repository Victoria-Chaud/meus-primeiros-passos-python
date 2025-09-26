# Nesta atividade vamos escrever um programa que irá calcular em média quantas semanas de vida lhe resta aqui na Terra.
#O objetivo é considerar a entrada de acorco dom a sua idade.
# Por exemplo, aqui tenho alguém de 15 anos, e presumimos que ele viverá até os 90, seremos otimistas.
# E então vamos calcular quantas semanas ainda restam em sua vida.

age = int(input("\nQuantos anos você tem: "))

years = 90 - age
weeks = years * 52
#print("\nVocê tem " + str(weeks) + " semanas de vida.")
print(f"\nVocê ainda tem {weeks} semanas de vida.")