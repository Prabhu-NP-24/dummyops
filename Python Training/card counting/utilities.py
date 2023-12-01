import random

class BlackJack():
    
    def generate_deck(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]
        return deck
    
    def draw_cards(self, deck, num_cards):
        return random.sample(deck, num_cards)
    
    def play_memory_game(self, num_turns):
        
        util = BlackJack()
        deck = util.generate_deck()

        for turn in range(1, num_turns + 1):
            print(f"\nTurn {turn}:")
            current_set = util.draw_cards(deck, 3)

            # Display the current set of cards
            print("Current set of cards:")
            for card in current_set:
                print(f"{card['rank']} of {card['suit']}")

            # Prompt the user to input their card count
            user_count = int(input("How many cards of the same rank did you see? "))

            # Check if the user's count matches the actual count
            actual_count = len(set(card['rank'] for card in current_set))
            if user_count == actual_count:
                print("Correct! You have a good memory.")
            else:
                print(f"Wrong! The actual count was {actual_count}.")