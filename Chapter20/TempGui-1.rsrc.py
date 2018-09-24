{'application':{'type':'Application',
          'name':'Template',
    'backgrounds': [
    {'type':'Background',
          'name':'bgTemplate',
          'title':'Standard Template with File->Exit menu',
          'size':(451, 362),
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
             {'type':'Menu',
             'name':'menuConvert',
             'label':u'&Convert',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuConvertCtoF',
                   'label':u'&Celsius to Fahrenheit',
                  },
                  {'type':'MenuItem',
                   'name':'menuConvertFtoC',
                   'label':u'&Fahrenheit to Celsius',
                  },
              ]
             },
         ]
     },
         'components': [

{'type':'StaticText', 
    'name':'StaticText2', 
    'position':(313, 173), 
    'text':u'Fahrenheit', 
    },

{'type':'StaticText', 
    'name':'StaticText1', 
    'position':(49, 173), 
    'text':u'Celsius', 
    },

{'type':'Spinner', 
    'name':'spinFahr', 
    'position':(297, 140), 
    'size':(105, -1), 
    'max':1000, 
    'min':-1000, 
    'value':100, 
    },

{'type':'TextField', 
    'name':'tfCel', 
    'position':(17, 140), 
    },

{'type':'Button', 
    'name':'btnFtoC', 
    'position':(126, 171), 
    'label':u'<<<Fahrenheit to Celsius', 
    },

{'type':'Button', 
    'name':'btnCtoF', 
    'position':(126, 123), 
    'label':u'Celsius to Fahrenheit>>>', 
    },

] # end components
} # end background
] # end backgrounds
} }
