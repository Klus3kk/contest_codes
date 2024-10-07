lines = []
with open("input.txt", "r") as file:
	lines = file.read().replace("A", "E").replace("K", "D").replace("Q", "C").replace("J", "B").replace("T", "A").split("\n")[:-1]

hands_bids = []
for line in lines:
	hands_bids.append((line.split()[0], int(line.split()[1])))

#assign power to each hand
hand_bids_powers = []
for hand in hands_bids:
	card_dict = {}
	for card in hand[0]:
		occurences = hand[0].count(card)
		card_dict[card] = occurences
	hand_list = list(card_dict.values())

	#7 different powers, high card is power 0
	power = 0
	if(5 in hand_list):
		power = 6
	elif(4 in hand_list):
		power = 5
	elif(3 in hand_list and 2 in hand_list):
		power = 4
	elif(3 in hand_list):
		power = 3
	elif(2 in hand_list and len(hand_list) == 3):
		power = 2
	elif(2 in hand_list):
		power = 1
	hand_bids_powers.append((hand[0], hand[1], power))

#rank them all within the same power
hand_bids_powers = sorted(hand_bids_powers, key=lambda x: (x[2], x[0]))

score = 0
for i in range(len(hand_bids_powers)):
	score += (i+1) * int(hand_bids_powers[i][1])

print(score)


#part 2
lines = []
with open("input.txt", "r") as file:
	lines = file.read().replace("A", "D").replace("K", "C").replace("Q", "B").replace("J", "0").replace("T", "A").split("\n")[:-1]

hands_bids = []
for line in lines:
	hands_bids.append((line.split()[0], int(line.split()[1])))

#assign power to each hand
hand_bids_powers = []
for hand in hands_bids:
	card_dict = {}
	for card in hand[0]:
		occurences = hand[0].count(card)
		card_dict[card] = occurences
	hand_list = list(card_dict.values())

	#7 different powers, high card is power 0
	power = 0
	if(5 in hand_list):
		power = 6
	elif(4 in hand_list):
		power = 5
	elif(3 in hand_list and 2 in hand_list):
		power = 4
	elif(3 in hand_list):
		power = 3
	elif(2 in hand_list and len(hand_list) == 3):
		power = 2
	elif(2 in hand_list):
		power = 1

	if("0" in hand[0]):
		joker_count = card_dict["0"]
		if(joker_count == 1):
			if(power == 0 or power == 5):
				power += 1
			elif(power == 1 or power == 2 or power == 3):
				power += 2
		elif(joker_count == 2):
			if(power == 1 or power == 4):
				power += 2
			elif(power == 2):
				power = 5
		elif(joker_count == 3):
			if(power == 3 or power == 4):
				power += 2
		elif(joker_count == 4):
			power = 6
		
	hand_bids_powers.append((hand[0], hand[1], power))


#rank them all within the same power
hand_bids_powers = sorted(hand_bids_powers, key=lambda x: (x[2], x[0]))

hand_bids_powers = sorted(hand_bids_powers, key=lambda x: x[2])

score = 0
for i in range(len(hand_bids_powers)):
	score += (i+1) * int(hand_bids_powers[i][1])

print(score)