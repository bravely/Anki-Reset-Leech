ResetLeech is a plugin for Anki under commission by kfdm.

Often in Anki, a card will be suspended and marked as a Leech
when you would actually like to be able to go back and review
the card again. However, even if you take away its Leech
status, the card still has a high base count of times missed,
meaning that the next time you miss it, it immediately is 
leeched again.

This aims to fix that, without adjusting any of your other stats.

Side note: Because of a generic error in Anki that is recieved
when trying to reset the counter to 0, I just had to shortcut
around the problem and set it to 1. When it's out of 15, I figure
that it isn't that big of a deal. Might go back and fix that
later if I figure out the bug.