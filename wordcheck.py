words = ["paladin", "batman"]

class Language:
	def __init__(self):
		self.characters = {}
	
	def AddWord(self, word):
		index = 0
		for ch in word:
			if ch in self.characters:
				if word in self.characters[ch]:
					self.characters[ch][word].append(index)
				else:
					self.characters[ch][word] = [index]
			else:
				self.characters[ch] = {word : [index]}
			index += 1
	
lang = Language()
	
for word in words:
	lang.AddWord(word)
	
for ch in lang.characters:
	print ch + ": ",
	print lang.characters[ch]