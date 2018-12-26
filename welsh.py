import time
			
def ydwNacydw(cwestiwn):
	ateb = deletePunctuation(raw_input(cwestiwn).lower().split())
	if "nac" in ateb and "ydw" in ateb:
		return False
	elif "ydw" in ateb:
		return True
		
def deletePunctuation(string):
	punctuation = [',', '.', '?', '!', ';', ':']
	returnString = ""
	for letter in string:
		if not (letter in punctuation):
			returnString = returnString + letter
	return returnString
	
def say(words):
	print words
	time.sleep(3)
		
		
print "Helo, s'mae! Heddiw dan ni'n mynd i ddysgu Cymraeg!"
name = raw_input("Beth ydy dy enw di? ").lower().split()
offLimits = ["fy", "enw", "i", "ydy", "yw", "dw", "i'n", "ydw"]

for word in name:
	isName = True;
	for item in offLimits:
		if word == item:
			isName = False
	if isName:
		name = word.capitalize()
		break
		
print "Helo, " + name + "!"
if ydwNacydw("Wyt ti eisiau paned o de? "):
	say("Wel, 'na ni!")
else:
	say("Ti ddim yn dod o Gymru, ia?")
say("A dweud a gwir, dan ni ddim 'ma i yfed te.")
say("Dan ni'n mynd i weld y Ddraig Goch, draig bwysig iawn i Gymru.")
if ydwNacydw("Wyt ti'n gwypod stori y Ddraig Goch? "):
	say("Wel, wyt ti'n cymro? Da iawn!")
else:
	say("Mae'n stori pwysig, a mae'n dod o'r adeg cyn y Brenin Arthur.")
	say("Naeth y Ddraig Goch ymladd yn erbyn y Ddraig Wen o'r Sacsoniadd.")
	say("Naeth o ennill, a ers hynny mae o wedi bod symbol cenedlaethol i Gyrmu.")
	say("Mae o'n neis iawn, a mae o eisiau cwrdd a chdi.")
say("Wyt ti eisiau mynd rwan?")
say("Gad inni fynd!")

	
	
