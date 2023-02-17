import pygame, random
import easygui
width = int(input("Enter the width of the window: "))
height = int(input("Enter the height of the window: "))

# Set the window size
window_size = (width, height)

# Create the window
screen = pygame.display.set_mode(window_size)


easygui.msgbox("LOADING SOUTH PARK STICK OF TRUTH ", "CopyrightTM", "PLAY") 

 
 
# --------- Globale variabelen ----------
#coordinaten van de vakjes:
vakjes = [[20,18], [234,13], [451,15], [660,15], [879,15], [1099,15], [1309,15], [1534,14], [1743,16], [1725,229], [1731,446], [1724,671], [1740,885], [1529,884], [1317,882], [1102,885], [876,885], [663,881], [449,882], [227,880], [14,878], [9,653], [8,436], [10,222]

]

#Pion posities
posities = [0,0]

beurt = 0

worp = 0
bord = pygame.image.load("Petra.png")
pion1 = pygame.image.load("avatar7.png")
pion2 = pygame.image.load("avatar1.png")
defaultImageSize = (100, 128)

pion2 = pygame.transform.scale(pion2, defaultImageSize)
pion1 = pygame.transform.scale(pion1, defaultImageSize) 


# --------- Pygame initialisatie ----------
pygame.init()
pygame.mixer.init()
Kiki = pygame.mixer.Sound("intro.mp3")
Kiki.play()
import time
time.sleep(27)
Kiki.stop()
pygame.mixer.music.load("muziek.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)
#Menu






#Naam:
pygame.display.set_caption("South Park The Stick of Truth")

#Afsluiting spel
done = False

#Framerate
clock = pygame.time.Clock()





# --------- Hoofdloop van het programma ----------
while not done:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            done = True
        
        elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("Knop: Spatie")
                    
                    worp = random.randint(1,6)
                    posities[beurt] += worp      
                    
                    
                    
                    if posities[beurt] >= 63:
                        posities[beurt] = 63
                        
                    else:
                            
                            if beurt == 0:
                                beurt = 1
                                
                                
                            else:
                                beurt = 0
                                
                elif event.key == pygame.K_BACKSPACE:
                    print("Knop: Backspace")
                    posities = [0,0]
                    beurt = 0
                    
                elif event.key == pygame.K_ESCAPE:
                    done == True
                                    
           
                                    
                        
                   
                                                  
                

                        
                     
                    
                    
                    
    
    clock.tick(60) # Zet de limiet op 60 frames per seconde
    pygame.display.flip() # ververs het beeldscherm met de nieuwe versie van het scherm
    screen.fill((255,255,255)) # begin met een witte achtergrond
    bordrect = bord.get_rect()
    screen.blit (bord,bordrect) # teken het bord op het volgende screen:
    
    speler0_x = vakjes[posities[0]][0]
    speler0_y = vakjes[posities[0]][1]
    screen.blit(pion1, (speler0_x, speler0_y))
    
    
    
    
    speler1_x = vakjes[posities[1]][0] + 5
    speler1_y = vakjes[posities[1]][1] + 5
    screen.blit(pion2, (speler1_x, speler1_y))
    
    
    
    myfont = pygame.font.Font("Downtown Elegance Bold.ttf", 30)
    
    text ="Laatste worp: " + str(worp)
    label = myfont.render(text, 1, (0, 0, 0))
    screen.blit(label, (350, 470))#1400-709
    
    text = "Aan de beurt: " + str(beurt + 1)
    label = myfont.render(text, 1, (0, 0, 0))
    screen.blit(label, (350, 495))
    
    










    


# --------- Afsluiting ----------
pygame.quit() #dit sluit pygame netjes af en sluit het gamevenster


