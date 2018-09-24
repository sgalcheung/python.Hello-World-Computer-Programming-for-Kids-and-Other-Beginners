{'application':{'type':'Application',
          'name':'Template',
    'backgrounds': [
    {'type':'Background',
          'name':'bgTemplate',
          'title':'Standard Template with File->Exit menu',
          'size':(400, 300),
          'style':['resizeable'],

        'menubar': {'type':'MenuBar',
         'menus': [
             {'type':'Menu',
             'name':'menuFile',
             'label':'&File',
             'items': [
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
    'name':'StaticText5', 
    'position':(53, 203), 
    'text':u'StaticText5', 
    },

{'type':'StaticText', 
    'name':'StaticText4', 
    'position':(51, 175), 
    'font':{'style': 'bold', 'family': 'sansSerif', 'size': 9}, 
    'text':u'StaticText4', 
    },

{'type':'StaticText', 
    'name':'StaticText3', 
    'position':(31, 94), 
    'text':u'Type in your guess, then click the Guess button.', 
    },

{'type':'StaticText', 
    'name':'StaticText2', 
    'position':(20, 31), 
    'text':u"It is a number from 1 to 99.  I'll give you 6 tries.", 
    },

{'type':'StaticText', 
    'name':'StaticText1', 
    'position':(15, 9), 
    'text':u"AHOY!  I'm the Dread Pirate Roberts, and I have a secret!", 
    },

{'type':'Button', 
    'name':'btnGuess', 
    'position':(146, 125), 
    'label':u'Guess', 
    },

{'type':'TextField', 
    'name':'tfGuessNum', 
    'position':(30, 125), 
    'text':u'0', 
    },

] # end components
} # end background
] # end backgrounds
} }
