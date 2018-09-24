# TIO_CH24_3.rsrc.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# Resource file for Virtual Pet program with pause button

{'application':{'type':'Application',
          'name':'Template',
    'backgrounds': [
    {'type':'Background',
          'name':'bgTemplate',
          'title':'Virtual Pet',
          'size':(325, 369),
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
    'name':'stPaused', 
    'position':(70, 199), 
    'size':(156, 38), 
    'alignment':u'center', 
    'font':{'style': 'bold', 'faceName': u'Tahoma', 'family': 'sansSerif', 'size': 20}, 
    'text':u'StaticText1', 
    },

{'type':'Button', 
    'name':'btnPause', 
    'position':(112, 288), 
    'label':u'Pause', 
    },

{'type':'ImageButton', 
    'name':'stop', 
    'position':(10, 17), 
    'size':(40, 40), 
    'border':'transparent', 
    'file':'stopbutton.GIF', 
    'font':{'faceName': u'Trebuchet MS', 'family': 'sansSerif', 'size': 12}, 
    'toolTip':u'Do Nothing', 
    },

{'type':'ImageButton', 
    'name':'doctor', 
    'position':(250, 17), 
    'size':(40, 40), 
    'border':'transparent', 
    'file':'docbutton.GIF', 
    'font':{'faceName': u'Trebuchet MS', 'family': 'sansSerif', 'size': 12}, 
    'toolTip':u'Go to Doctor', 
    },

{'type':'ImageButton', 
    'name':'play', 
    'position':(190, 17), 
    'size':(40, 40), 
    'border':'transparent', 
    'file':'playbutton.GIF', 
    'toolTip':u'Play', 
    },

{'type':'ImageButton', 
    'name':'walk', 
    'position':(130, 17), 
    'size':(40, 40), 
    'border':'transparent', 
    'file':'walkbutton.GIF', 
    'toolTip':u'Go for a walk', 
    },

{'type':'StaticText', 
    'name':'Health', 
    'position':(9, 271), 
    'text':u'Health', 
    },

{'type':'Gauge', 
    'name':'HealthGauge', 
    'position':(73, 270), 
    'size':(199, 14), 
    'layout':'horizontal', 
    'max':8, 
    'toolTip':u"Your pet's Health", 
    'value':8, 
    },

{'type':'ImageButton', 
    'name':'feed', 
    'position':(70, 17), 
    'size':(40, 40), 
    'border':'transparent', 
    'file':'eatbutton.GIF', 
    'toolTip':u'Feed', 
    },

{'type':'Image', 
    'name':'petwindow', 
    'position':(66, 63), 
    'size':(160, 134), 
    'file':'pet1.GIF', 
    },

{'type':'StaticText', 
    'name':'Happiness', 
    'position':(9, 258), 
    'text':u'Happiness', 
    },

{'type':'Gauge', 
    'name':'HappyGauge', 
    'position':(73, 256), 
    'size':(199, 14), 
    'layout':'horizontal', 
    'max':8, 
    'toolTip':u"Your pet's Happiness", 
    'value':8, 
    },

{'type':'StaticText', 
    'name':'Hunger', 
    'position':(8, 245), 
    'text':u'Hunger', 
    },

{'type':'Gauge', 
    'name':'HungerGauge', 
    'position':(73, 242), 
    'size':(199, 14), 
    'foregroundColor':(255, 0, 0, 255), 
    'layout':'horizontal', 
    'max':8, 
    'toolTip':u"Your pet's Hunger", 
    'value':8, 
    },

] # end components
} # end background
] # end backgrounds
} }
