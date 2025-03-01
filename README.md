# FEN Legal Moves by Piece

This repository contains a Python script that calculates and displays all legal chess moves for a given board position (specified using a FEN string). The moves are grouped by the piece making the move in the order: **King, Queen, Rook, Bishop, Knight, Pawn**. Captures are represented in Standard Algebraic Notation (SAN) using an "x" (for example, "Nxf3" or "exd5").

## Features

- **FEN Input:** Reads a FEN string from the command line using `argparse`.
- **Legal Move Generation:** Uses the [python‑chess](https://pypi.org/project/python-chess/) library to compute all legal moves for the current board position.
- **Grouping by Piece:** Moves are grouped by the piece that makes the move in the following order:
  - King
  - Queen
  - Rook
  - Bishop
  - Knight
  - Pawn
- **SAN Representation:** Each move is converted into Standard Algebraic Notation, with captures clearly indicated.
- **Total Count:** Displays the total number of legal moves available.

## Requirements

- Python 3.6 or later
- [python‑chess](https://pypi.org/project/python-chess/)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ssmythe/fen_legal_moves.git
   cd fen_legal_moves
   ```

2. **(Optional) Create and activate a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required library:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script by passing a FEN string as a command-line argument. For example:

```bash
python fen_legal_moves.py "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
```

This command will display all legal moves for the side to move (in this example, White) grouped by piece type in the following order: **King, Queen, Rook, Bishop, Knight, Pawn**. It will also print the total number of legal moves.

## Usage Example

Suppose you want to view the legal moves from the starting position of a chess game. You can run:

```bash
python fen_legal_moves.py "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
```

A sample output might look like this:

```
King moves:
  O-O
  O-O-O

Queen moves:
  Qd2

Rook moves:
  Ra1
  Rh1

Bishop moves:
  Bc1
  Bf1

Knight moves:
  Nf3
  Nc3

Pawn moves:
  a3
  b3
  c3
  d3
  e3
  f3
  g3
  h3

Total legal moves: 20
```

> **Note:** The output will vary depending on the board position provided by the FEN string.

## License

This project has no license.
