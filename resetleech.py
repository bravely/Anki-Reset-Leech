'''
Created on Oct 31, 2011

@author: quaunaut
'''

# Adds a button to reset the 'Leech' status to a card.

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ankiqt import mw
from anki.hooks import addHook
from anki.cards import Card
#from anki.utils import hasTag, delTag
    

def setupMenu(editor):
    resetl = QAction("Reset Leeches zomg", editor)
    resetl.setEnabled(True)
    resetl.setText("Reset Leech")
    editor.connect(resetl, SIGNAL("triggered()"), lambda e=editor: resetLeech(e))
    editor.dialog.menuActions.addSeparator()
    editor.dialog.menuActions.addAction(resetl)
    

def resetLeech(editor):
    n = "Reset Leech b"
   # if mw.currentCard.hasTag("leech")
    editor.currentCard.reps = 1
    editor.deck.refresh()
       # mw.currentCard.delTag("leech")

addHook("editor.setupMenus", setupMenu)
    
mw.registerPlugin("Reset Leech!", 18)