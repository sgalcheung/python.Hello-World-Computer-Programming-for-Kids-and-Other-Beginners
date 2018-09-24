init_cards()
while not game_done:
    blocked = 0
    player_turn()                                                   
    if len(p_hand) == 0:     # player has no cards left, so he wins                                         
        game_done = True                                            
        print                                                       
        print "You won!"                                            
    if not game_done:                                               
        computer_turn()                                             
    if len(c_hand) == 0:     # computer has no cards left, so it wins                                       
        game_done = True                                            
        print                                                       
        print "Computer won!"                                       
    if blocked >= 2:         # both players are blocked, so game ends                                   
        game_done = True
        print "Both players blocked.  GAME OVER."

print "\nYour hand: ",
for card in p_hand:
    print card.short_name,
print "   Up card: ", up_card.short_name
if up_card.rank == '8':
    print"   Suit is", active_suit 

print "What would you like to do? ",
response = raw_input ("Type a card to play or 'Draw' to take a card: " )

# keep trying untile the player enters something valid
while not valid_play:                                                     
    selected_card = None               # get a card the player holds, or "draw"
    while selected_card == None:                                          
        if response.lower() == 'draw':
            # if choice is "draw" get a card from the deck and add it
            #   to the player's hand
            valid_play = True
            if len(deck) > 0:   
                card = random.choice(deck)                                
                p_hand.append(card)                                       
                deck.remove(card)                                         
                print "You drew", card.short_name                         
            else:                                                         
                print "There are no cards left in the deck"               
                blocked += 1                                              
            return                                                      
        else:
            for card in p_hand:       # check if the selected card is in the player's hand
                if response.upper() == card.short_name:                   
                    selected_card = card
            if selected_card == None:
                response = raw_input("You don't have that card. Try again:")

    if selected_card.rank == '8':     # playing an 8 is always legal                                  
        valid_play = True
        is_eight = True
    elif selected_card.suit  == active_suit:                              
        valid_play = True
    elif selected_card.rank  == up_card.rank:                             
        valid_play = True
                                
    if not valid_play:
        response = raw_input("That's not a legal play.  Try again: ")

def get_new_suit():
    global active_suit
    got_suit = False
    while not got_suit:                   # keep trying until the player enters a valid suit                                      
        suit = raw_input("Pick a suit: ")
        if suit.lower() == 'd':
            active_suit = "Diamonds"
            got_suit = True
        elif suit.lower() == 's':
            active_suit = "Spades"
            got_suit = True
        elif suit.lower() == 'h':
            active_suit = "Hearts"
            got_suit = True
        elif suit.lower() == 'c':
            active_suit = "Clubs"
            got_suit = True
        else:
            print"Not a valid suit.  Try again. ",  
    print "You picked", active_suit

def computer_turn():
    global c_hand, deck, up_card, active_suit, blocked
    options = []
    for card in c_hand:
        if card.rank == '8':           # computer plays an 8                                     
            c_hand.remove(card)
            up_card  = card
            print "  Computer played ", card.short_name
            #suit totals:  [diamonds, hearts, spades, clubs]     
            suit_totals = [0, 0, 0, 0]     # count how many cards of each suit are held                             
            for suit in range(1, 5): 
                for card in c_hand:
                    if card.suit_id == suit:
                        suit_totals[suit-1] += 1
            long_suit = 0                  # the suit with the most cards is the "long suit"
            for i in range (4):
                if suit_totals[i] > long_suit:
                    long_suit = i
            
            # make the long suit the active suit
            if long_suit == 0:                                            
                active_suit = "Diamonds"                                  
            if long_suit == 1:                                            
                active_suit = "Hearts"                                    
            if long_suit == 2:                                            
                active_suit = "Spades"                                    
            if long_suit == 3:                                            
                active_suit = "Clubs"                                     
            print "  Computer changed suit to ", active_suit
            return         # done computer's hand - back to main loop                                               
        else:                                                     
            if card.suit == active_suit:       # see what cards are possible plays                           
                options.append(card)                                      
            elif card.rank == up_card.rank:                               
                options.append(card)                                      
                    
    if len(options) > 0:
        best_play = options[0]                # see which play optio is best (highest value)
        for card in options:                                              
            if card.value > best_play.value:                              
                best_play = card                                          
        c_hand.remove(best_play)              # play computer's card                                 
        up_card = best_play                                               
        active_suit = up_card.suit                                        
        print "  Computer played ", best_play.short_name                  
            
    else:                                # no possible plays, so draw 
        if len(deck) >0:                 # (if there are any cards in the deck)
            next_card = random.choice(deck)                               
            c_hand.append(next_card)                                      
            deck.remove(next_card)                                        
            print "  Computer drew a card"                                  
        else:                            # no cards left in deck, so computer is blocked
            print"  Computer is blocked"                                  
            blocked += 1                                                  
    print "Computer has %i cards left" % (len(c_hand))

done = False
p_total = c_total = 0
while not done:    
    game_done = False
    blocked = 0
    init_cards()        # set up deck and create player's and computer's hands                                                    
    while not game_done:
        player_turn() 
        if len(p_hand) == 0:     # player won                                         
            game_done = True
            print
            print "You won!"
            # display game score here
            p_points = 0
            for card in c_hand:                                           
                p_points += card.value     # add up points from computer's remaining cards                     
            p_total += p_points            # add points from this game to the total                               
            print"You got %i points for computer's hand" % p_points
        if not game_done: 
            computer_turn()
        if len(c_hand) == 0:        # computer won                                      
            game_done = True
            print
            print "Computer won!"
            # display game score here
            c_points = 0
            for card in p_hand:                                           
                c_points += card.value      # add up points from player's remaining cards                             
            c_total += c_points             # add points from this game to the total                              
            print"Computer got %i points for your hand" % c_points
        if blocked >= 2:                    # both player and computer blocked, so both get points
            game_done = True                                              
            print "Both players blocked.  GAME OVER."                     
            player_points = 0                                             
            for card in c_hand:                                           
                p_points += card.value                                    
            p_total += p_points                                           
            c_points = 0                                                  
            for card in p_hand:                                           
                c_points += card.value                                    
            c_total += c_points                                           
            print"You got %i points for computer's hand" % p_points       
            print"Computer got %i points for your hand" % c_points        
    play_again = raw_input("Play again (Y/N)? ")
    if play_again.lower().startswith('y'):
        done = False
        print "\nSo far, you have %i points" % p_total                    
        print  "and the computer has %i points.\n" % c_total                   
    else:
        done = True
            
print "\n Final Score:"                                                   
print "You: %i     Computer: %i" % (p_total, c_total)                     