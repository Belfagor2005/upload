# ChessBoard

This plugin is a frontend to let you play a game of chess against your Enigma2 box. Your opponent on the box is gnuchess.

## Requirements:
* a full HD skin
* gnuchess-6 (https://www.gnu.org/software/chess/) or stockfish (https://github.com/official-stockfish/Stockfish)
* python-chess-0.23.11 (last supported version for python-2, https://github.com/niklasf/python-chess/releases/tag/v0.23.11)

![image](https://user-images.githubusercontent.com/15088943/80862960-3e289580-8c79-11ea-97f3-9ce8b053700f.png)

## Operation
* move the focus field with the arrow keys or number keys
* mark a piece with the ok key or number "5" key
* move to the target field and make your move with the ok key or number "5" key
* channel up and channel down keys change gnuchess movetime within one to ten seconds
* blue key switches the color you play, even in a running game
* yellow key rotates the board
* green key shows the move that gnuchess is expecting
* red key undos moves
* menu key opens settings menu; if installed you may use stockfish as chess engine

## Ideas
* Spielzeit/Uhr als Alternative zur Spielstärke
* Remis anbieten (möglich?)
* Info-Handler aus python-chess
* Absichern, dass gnuchess installiert ist
* Absichern, dass python-chess installiert ist
* Ohne Computer spielen
* Stellung eingeben
* Spiel abbrechen/resetten
* Spiel speichern, laden, fortsetzen
* Bedienung vereinfachen: ausgewählte Figur nur auf erlaubten Bahnen bewegen

## Acknowledgements
Chess pieces font is taken from https://github.com/xeyownt/chess_merida_unicode

