# ♠️ BlackJack Game (Python)

A terminal-based Blackjack game written in Python featuring ASCII-rendered playing cards, betting mechanics, and basic dealer AI.

The game runs entirely in the console and simulates a traditional Blackjack flow: betting, dealing, hitting, standing, dealer turns, and payout resolution.

---

## 🎮 Features

- 🃏 ASCII-rendered playing cards
- 🎲 Cryptographically secure deck shuffling (`secrets`)
- 💰 Player balance and betting system
- 🏦 Pot handling with ante
- 🧮 Automatic Ace value adjustment (11 → 1 when busting)
- 🤖 Dealer logic (hits until hand value ≥ 17)
- 🛡️ Insurance option when dealer shows Ace
- 🔁 Multi-round gameplay loop

---

## 📁 Project Structure

```

BlackJackGame/
├── Main.py # Application entry point
├── Game.py # Game loop and gameplay logic
├── Deck.py # Deck creation and shuffling
├── Card.py # Card model + ASCII rendering
├── Player.py # Player behavior and hand logic
├── Dealer.py # Dealer AI behavior
└── README.md

```

---

## ▶️ How To Run

From the `BlackJackGame` directory:

```bash
python Main.py
```

If you have multiple Python versions installed:

```bash
python3 Main.py
```

---

## 🕹️ How To Play

1. The game starts with:

   - A starting balance of **$100**
   - A configurable **ante** (default: $10)

2. Each round:

   - You place a bet (or default to the ante).
   - Cards are dealt automatically.
   - One dealer card is hidden initially.
   - You choose to:

     - **hit** → draw another card
     - **stay** → end your turn

3. Dealer rules:

   - Dealer reveals hidden card after your turn.
   - Dealer hits until hand value ≥ 17.

4. Outcomes:

   - **Win** → you receive the pot.
   - **Draw** → ante is refunded.
   - **Lose** → bet is lost.

5. You can continue playing until you exit or run out of balance.

---

## 🧱 Core Classes

### `Card`

Represents a single playing card.

```python
Card(suit: str, rank: str)
```

- Calculates point value automatically.
- Provides ASCII rendering utilities:

  - `ascii_version_of_card(...)`
  - `ascii_version_of_hidden_card(...)`

---

### `Deck`

Manages one or more shuffled decks.

```python
Deck(num_decks=1)
```

- Uses a cryptographically secure shuffle (`secrets.choice`).
- Provides:

  - `deal_card()`

---

### `Player`

Represents the human player.

Key responsibilities:

- Tracks hand and balance
- Calculates hand value with Ace adjustment
- Prompts user for hit/stay decision
- Displays cards

---

### `Dealer (inherits Player)`

Represents the dealer AI.

Additional behavior:

- Can hide first card during display
- Automatically plays hand until value ≥ 17

---

### `Game`

Orchestrates the entire gameplay loop.

Responsibilities:

- Betting logic and pot management
- Dealing cards
- Player turns
- Dealer turns
- Determining winner
- Updating balance
- Screen rendering

Entry point:

```python
game = Game(num_decks=1, ante=10)
game.play_game()
```

---

## ⚙️ Configuration

You can tweak game behavior inside `Main.py`:

```python
game = Game(
    num_decks=1,   # Number of decks in the shoe
    ante=10        # Ante per round
)
```

---

## 🖥️ Terminal Compatibility

This game uses Unicode characters for card suits:

```
♠ ♦ ♥ ♣
```

Make sure your terminal supports UTF-8 encoding.

---

## 🚧 Known Limitations / Future Ideas

- Split logic partially implemented but not fully wired into gameplay.
- No persistent save state for balance.
- No automated tests.
- No double-down support yet.
- No multiplayer support.

These are good future expansion opportunities.

---

## 📜 License

Personal project. Free to modify and experiment.

