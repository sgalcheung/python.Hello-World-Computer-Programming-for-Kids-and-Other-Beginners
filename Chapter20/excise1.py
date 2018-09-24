from PythonCard import model
import random

guess = 0
secret = random.randint(1,100)
done = False
tries = 6

class NumGuess(model.Background):

    def on_initialize(self, event):
        self.guess = self.components.tfGuessNum.text
        self.components.StaticText4.text = ""
        self.components.StaticText5.text = "You have " + str(tries) + " left."

    def on_btnGuess_mouseClick(self, event):
    	global done, guess, tries
    	if not done:
            guess = int(self.components.tfGuessNum.text)
            if tries > 1:
                if guess != secret:
                    if guess < secret:
                        self.components.StaticText4.text = "Too low, ye scurvy dog!"
                    elif guess > secret:
                        self.components.StaticText4.text = "Too high, landlubber!"
                    tries = tries - 1                         # used up one try    
                    self.components.StaticText5.text = "You have " + str(tries) + " left."

                elif guess == secret:
                    self.components.StaticText4.text = "Avast! Ye got it!  Found my secret, ye did!"
                    self.components.StaticText5.text = ""
                    done = True
            elif tries == 1:
                if guess != secret:
                    self.components.StaticText4.text ="No more guesses!  Better luck next time, matey!"
                    self.components.StaticText5.text =  "The secret number was " + str(secret)
                    done = True
                else:
                    self.components.StaticText4.text = "Avast! Ye got it!  Found my secret, ye did!"
                    self.components.StaticText5.text = ""
                    done = True   
                

app = model.Application(NumGuess)
app.MainLoop()
