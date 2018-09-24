{'application':{'type':'Application',
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------


          'name':'Template',
    'backgrounds': [
    {'type':'Background',
          'name':'bgTemplate',
          'title':u'Hangman',
          'size':(560, 373),
          

        'menubar': {'type':'MenuBar',
         'menus': [
             {'type':'Menu',
             'name':'menuFile',
             'label':'&File',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuFileNewGame',
                   'label':'&New Game',
                   'command':'cmdNewGame',
                  },
                  {'type':'MenuItem',
                   'name':'menuFileExit',
                   'label':'E&xit',
                   'command':'exit',
                  },
              ]
             },
         ]
     },
         'components': [

{'type':'StaticText', 
    'name':'stYourGuesses', 
    'position':(28, 236), 
    'font':{'faceName': u'Tahoma', 'family': 'sansSerif', 'size': 10}, 
    'text':u'', 
    },

{'type':'StaticText', 
    'name':'StaticText1', 
    'position':(26, 200), 
    'font':{'faceName': u'Tahoma', 'family': 'sansSerif', 'size': 10}, 
    'text':u'Your Guesses:', 
    },

{'type':'StaticLine', 
    'name':'StaticLine2Copy', 
    'position':(86, 11), 
    'size':(4, 34), 
    'layout':'vertical', 
    },

{'type':'StaticLine', 
    'name':'StaticLine3', 
    'position':(87, 10), 
    'size':(69, 4), 
    'layout':'horizontal', 
    },

{'type':'StaticLine', 
    'name':'StaticLine2', 
    'position':(157, 10), 
    'size':(4, 160), 
    'layout':'vertical', 
    },

{'type':'StaticLine', 
    'name':'StaticLine1', 
    'position':(133, 171), 
    'size':(50, 4), 
    'layout':'horizontal', 
    },

{'type':'StaticText', 
    'name':'stDisplayWord', 
    'position':(247, 87), 
    'font':{'style': 'bold', 'faceName': u'Courier New', 'family': 'sansSerif', 'size': 14}, 
    'text':u'----------', 
    },

{'type':'Button', 
    'name':'btnGuessWord', 
    'position':(252, 128), 
    'size':(120, -1), 
    'label':u'Guess the word', 
    },

{'type':'Button', 
    'name':'btnGuessLetter', 
    'position':(250, 32), 
    'size':(120, -1), 
    'label':u'Guess a letter', 
    },

{'type':'StaticText', 
    'name':'foot2', 
    'position':(88, 115), 
    'enabled':False, 
    'font':{'faceName': 'Tahoma', 'family': 'sansSerif', 'size': 22}, 
    'text':u'\\', 
    },

{'type':'StaticText', 
    'name':'foot1', 
    'position':(69, 115), 
    'enabled':False, 
    'font':{'faceName': 'Tahoma', 'family': 'sansSerif', 'size': 22}, 
    'text':u'/', 
    },

{'type':'StaticLine', 
    'name':'body', 
    'position':(85, 65), 
    'size':(4, 55), 
    'font':{'style': 'bold', 'faceName': 'Tahoma', 'family': 'sansSerif', 'size': 8}, 
    'layout':'vertical', 
    },

{'type':'StaticLine', 
    'name':'arm2', 
    'position':(94, 79), 
    'size':(36, 4), 
    'layout':'horizontal', 
    },

{'type':'StaticLine', 
    'name':'arm1', 
    'position':(45, 79), 
    'size':(36, 4), 
    'layout':'horizontal', 
    },

{'type':'StaticText', 
    'name':'head', 
    'position':(75, 29), 
    'enabled':False, 
    'font':{'faceName': 'Tahoma', 'family': 'sansSerif', 'size': 20}, 
    'text':u'O', 
    },

] # end components
} # end background
] # end backgrounds
} }