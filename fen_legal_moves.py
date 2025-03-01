#!/usr/bin/env python3
import argparse
import chess


def main():
    # Set up argument parser for FEN input
    parser = argparse.ArgumentParser(
        description="Calculate and display legal chess moves grouped by piece from a given FEN string."
    )
    parser.add_argument("fen", help="FEN string representing the chess board position.")
    args = parser.parse_args()

    # Create a board using the provided FEN
    try:
        board = chess.Board(args.fen)
    except ValueError as e:
        print("Error: Invalid FEN string provided.", e)
        exit(1)

    legal_moves = list(board.legal_moves)

    # Dictionary to group moves by piece type
    moves_by_piece = {
        chess.KING: [],
        chess.QUEEN: [],
        chess.ROOK: [],
        chess.BISHOP: [],
        chess.KNIGHT: [],
        chess.PAWN: [],
    }

    # Group each move by the piece on the from_square
    for move in legal_moves:
        piece = board.piece_at(move.from_square)
        if piece is not None:
            moves_by_piece[piece.piece_type].append(move)

    # Define piece type names for display
    piece_names = {
        chess.KING: "King",
        chess.QUEEN: "Queen",
        chess.ROOK: "Rook",
        chess.BISHOP: "Bishop",
        chess.KNIGHT: "Knight",
        chess.PAWN: "Pawn",
    }

    total_moves = 0
    # Order pieces: King, Queen, Rook, Bishop, Knight, Pawn.
    piece_order = [
        chess.KING,
        chess.QUEEN,
        chess.ROOK,
        chess.BISHOP,
        chess.KNIGHT,
        chess.PAWN,
    ]

    # Display moves grouped by piece type
    for piece_type in piece_order:
        moves = moves_by_piece[piece_type]
        if moves:
            print(f"{piece_names[piece_type]} moves:")
            for move in moves:
                # Convert move to SAN notation (captures include an "x")
                print("  " + board.san(move))
            total_moves += len(moves)
            print()  # Blank line for readability

    print(f"Total legal moves: {total_moves}")


if __name__ == "__main__":
    main()
