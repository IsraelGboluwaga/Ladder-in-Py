import random
class Cards:
	def __init__(self, ranks = 0, suits = 2):
		self.ranks = ranks
		self.suits = suits

	suitList = ["Clubs", "Diamonds", "Hearts", "Spades"]
	rankList = ["narf", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

	def __str__(self):
		return self.rankList[self.ranks] + " of " + self.suitList[self.suits]
	def __cmp__(self, other):
		if self.suits > other.suits:
			return 1
		if self.suits < other.suits:
			return -1
		if self.ranks > other.ranks:
			return 1
		if self.ranks < other.ranks:
			return -1
		return 0


# print Cards(1,2)
# print Cards.suitList[3]
# print Cards.rankList[11]
# print Cards(1,2) > Cards(2,2)

class Deck:
	def __init__(self):
		self.cards = []
		for suit in range(4):
			for rank in range(1, 14):
				self.cards.append(Cards(rank, suit))

	def printDeck(self):
		for card in self.cards:
			print card

	def __str__(self):
		s = ""
		for i in range(len(self.cards)):
			s = s + " "*i +str(self.cards[i]) + "\n"
		return s
	def shuffle(self):
		nCards = len(self.cards)
		for i in range(nCards):
			j = random.randrange(nCards)
			self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
			# s = self.cards[i]
			# self.cards[i] = self.cards[j]
			# self.cards[j] = s
	def removeCard(self, card):
		if card in self.cards:
			self.cards.remove(card)
			return True
		else:
			return False
	def popCard(self):
		return self.cards.pop()
	def isEmpty(self):
		return len(self.cards) == 0

deck = Deck()
deck.printDeck()
# print deck
# print random.randrange(0, len(deck.cards))
deck.popCard()
deck.printDeck()