Overview:
This is a build of My Turn in python, done in boredom to bring it back to life because it was really fun and didn't deserve to die.
Probably rather buggy.

Update log:

7/19/2023
Summary: Preemptive bug fixes and casting work.
Changed from last update: Seperated deck creation to P1 and P2 creations so that the deck can refresh at empty without needing an extra set of functions.
CardListAttributes list created, which should make it casting cards easy once I get the interpretation code prepared.

6/27/2023
Summary: Added clear debuffs step.
Changed from last update: Cleared debuff step added. Changed () to [] in lists. I didn't know this, but apparently () is a 'tuple', whatever the heck that means, but it was causing problems and making it unchangeable for some reason. Making it [] instead let me change it around which is very important for things like health values and buff effects.

6/21/2023
Summary: Modded code to be functions for increased organization.
Changed from last update: Changed the amount of attack cards added to the deck from 3 to 2, I had misremembered the amount in the deck but found the correct amount and fixed it. Changed code to be in functions. Added break/bolster variable to heros.
Tweaks from original game: Break increases damage taken by 50% instead of normal 25%. However, this is still not implemented and has no effect yet.

6/19/2023
Summary: Repo started and code uploaded. Makes the starter lineup minus the items and equipment and is able to make the deck and hands. Turn and game logic not yet existent.
Changes from last update: None, no last update.
Tweaks from original game: Empower effect was a 1.25 multiplier to damage, but is currently set at 1.5. However, as turn and game logic doesn't exist yet, this is very ignorable since it doesn't see use.