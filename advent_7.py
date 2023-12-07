from functools import cmp_to_key

# Part 1
# Each hand wins an amount equal to its bid multiplied by its rank
# , where the weakest hand gets rank 1, the second-weakest hand gets rank 2, ...
# Find the rank of every hand in your set. What are the total winnings?

# Part 2
# Now 'J's act as Jokers that can be used to improve any hand.
# Also 'J's are now the lowest-value card, so the new card_values="J23456789TQKA"

if __name__ == "__main__":
    data = list(open('input_7.txt'))
    data = [hand.strip() for hand in data]

    def count_chars(string : str):
        char_counts = {char: string[:5].count(char) for char in string[:5]}
        return char_counts

    def is_poker(char_counts : dict):
        return len(char_counts) == 1 and max(char_counts.values()) == 5
    def is_four_of_a_kind(char_counts : dict):
        return len(char_counts) == 2 and max(char_counts.values()) == 4
    def is_full_house(char_counts : dict):
        return len(char_counts) == 2 and max(char_counts.values()) == 3
    def is_three_of_a_kind(char_counts : dict):
        return len(char_counts) == 3 and max(char_counts.values()) == 3
    def is_two_pair(char_counts : dict):
        return len(char_counts) == 3 and max(char_counts.values()) == 2
    def is_one_pair(char_counts : dict):
        return len(char_counts) == 4 and max(char_counts.values()) == 2
    def is_high_card(char_counts : dict):
        return len(char_counts) == 5 and max(char_counts.values()) == 1

    def get_hand_rank(char_counts : dict):
        if is_poker(char_counts):
            return 9
        elif is_four_of_a_kind(char_counts):
            return 8
        elif is_full_house(char_counts):
            return 7
        elif is_three_of_a_kind(char_counts):
            return 6
        elif is_two_pair(char_counts):
            return 5
        elif is_one_pair(char_counts):
            return 4
        elif is_high_card(char_counts):
            return 3
        else:
            return 1

    def bump_rank(rank : int, jacks : int):
        # print(f"bumping rank {rank} with {jacks} jacks")
        if rank == 1:
            print("bumping rank 1")
        if rank == 3 and jacks > 0: # high card 1234J
            return 4 # one pair
        elif rank == 4 and jacks > 0: # one pair JJ12A or AAJ12
            return 6 # three of a kind
        elif rank == 5 and jacks > 0: # two pair AAJJ2 or AAQQJ
            if jacks == 2:
                return 8 # four of a kind
            else:
                return 7 # full house
        elif rank == 6 and jacks > 0: # three of a kind AAAJ2 or JJJ23
            return 8 # four of a kind
        elif rank >= 7 and jacks > 0: # full house : AAAJJ or JJJAA , four of a kind : AAAAJ or JJJJA, poker : JJJJJ
            return 9 # poker
        return rank

    def compare_two_hands(hand_1, hand_2, card_values="23456789TJQKA"):
        compare_result = 0
        hand1_strength = [card_values.index(c) for c in hand_1[:5]]
        hand2_strength = [card_values.index(c) for c in hand_2[:5]]
        caret = 0
        while not compare_result and caret < 5:
            compare_result = hand1_strength[caret] - hand2_strength[caret]
            caret += 1
        return compare_result

    def get_compare_hands(card_values="23456789TJQKA", bump=False):
        def compare_hands(hand1 : str, hand2 : str):
            count1, count2 = count_chars(hand1[:5]), count_chars(hand2[:5])
            rank1, rank2 = get_hand_rank(count1), get_hand_rank(count2)
            if bump:
                rank1, rank2 = bump_rank(rank1, count1.get('J', 0)), bump_rank(rank2, count2.get('J', 0))
            r = rank1 - rank2
            if r:
                return r
            else:
                return compare_two_hands(hand1, hand2, card_values)
        return compare_hands

    def calc_prizes(cmp):
        part = sorted(data, key=cmp_to_key(cmp), reverse=False)
        # hand, index, prize
        part = [[hand, i, (i+1)*int(hand.split(' ')[1])] for i, (hand) in enumerate(part)]
        prizes = [prize for hand, i, prize in part]
        return sum(prizes)

    # Part 1
    compare_hands = get_compare_hands()
    print(f"Part 1: {calc_prizes(compare_hands)}")

    # Part 2
    compare_hands = get_compare_hands(card_values="J23456789TQKA", bump=True)
    print(f"Part 2: {calc_prizes(compare_hands)}")