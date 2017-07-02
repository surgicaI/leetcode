num_silver = 180
num_gold = 52
num_gaint = 4
num_magical = 4 

gold_silver = (65 + 91) / 2
gold_gold = (205 + 287) / 2
gold_gaint = (1640 + 2296) / 2
gold_magical = (615 + 861) / 2

cards_silver = 13
cards_gold = 41
cards_gaint = 123
cards_magical = 328

tot_gold = gold_silver * num_silver + gold_gold * num_gold + gold_magical * num_magical + gold_gaint * num_gaint

tot_cards = cards_silver * num_silver + cards_gold * num_gold + cards_magical * num_magical + cards_gaint * num_gaint

print('total gold : {0}'.format(int(tot_gold)))
print('total cards: {0}'.format(tot_cards))