import random, pygame, sys

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode([20,100])

ahoy = pygame.mixer.Sound("Ahoy.wav")
tooLow = pygame.mixer.Sound("TooLow.wav")
tooHigh = pygame.mixer.Sound("TooHigh.wav")
whatGuess = pygame.mixer.Sound("WhatsYerGuess.wav")
gotIt = pygame.mixer.Sound("AvastGotIt.wav")
noMore = pygame.mixer.Sound("NoMore.wav")

ahoy.set_volume(0.4)
tooLow.set_volume(0.4)
tooHigh.set_volume(0.4)
whatGuess.set_volume(0.4)
gotIt.set_volume(0.4)
noMore.set_volume(0.4)

secret = random.randint(1,100)
guess = 0
tries = 0

print "AHOY! I'm the Dread Pirate Roberts, and I have a secret!"
print "It is a number from 1 to 99. I'll give you 6 tries."
ahoy.play()
pygame.time.delay(8500)  # wait for the sound to finish playing

while guess != secret and tries < 6:
    whatGuess.play()
    guess = input("What's yet guess?")
    if guess < secret:
        print "Too low, ye scurvy dog!"
        tooLow.play()
        pygame.time.delay(3200)
    elif guess > secret:
        print "Too high, landlubber!"
        tooHigh.play()
        pygame.time.delay(3000)
    tries = tries + 1
        
if guess == secret:
    print "Avast! yet got it! Found my secret, yet did!"
    gotIt.play()
else:
    noMore.play()
    print "No more guesses! Better luck next time, matey!"
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
