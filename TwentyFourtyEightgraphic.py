# 2048 front-end (graphics)
import time
from assets import graphics
import TwentyFourtyEightgameLogic as game


"""
GameStates (update);

1. in-game
2. menu popup rectangle
    a. new game
    b. help [popup rectangle same size as list-of-options one]
    c. settings
    d. quit
3. help (2b)
    a. how-to-play
4. settings (2c)
    a. TBD!
"""

# GLOBAL VARIABLES
version = "summer2022Graphics"



def createBoard(win, x1, y1, x2, y2):
    """
    Draw the initial gameboard.
        1. lines start & end coords: (5, 5), (35, 35)
        2. game logo (rectangle based on win coords): (x1+2.5, ), (x2/2 - 2.5, )
    """
    # draw game background
    game_rect = graphics.Rectangle(graphics.Point(5, 5), graphics.Point(35, 35))
    game_rect.setFill("darkgoldenrod1")
    game_rect.draw(win)

    hLines = []
    vLines = []
    board = [hLines, vLines]
    lineDistance = (x2 - x1)/4

    # draw horizontal lines
    for i in range(5):
        hLines.append(graphics.Line(graphics.Point(x1, y1 + i*lineDistance), graphics.Point(x2, y1 + i*lineDistance)))
        hLines[i].setFill("white")
        hLines[i].setOutline("black")
        hLines[i].draw(win)
    
    # draw vertical lines
    for i in range(5):
        vLines.append(graphics.Line(graphics.Point(x1 + i*lineDistance, y1), graphics.Point(x1 + i*lineDistance, y2)))
        vLines[i].setFill("white")
        vLines[i].setOutline("black")
        vLines[i].draw(win)

    # draw 2048 logo: win coords -> Point(x1+2.5, ), Point(x2/2 - 2.5, )
    logo = graphics.Rectangle(graphics.Point(2.5, 40), graphics.Point(17.5, 55))
    logo.setFill("darkgoldenrod1")
    logo.setOutline("black")
    logo.draw(win)

    logo_text = graphics.Text(graphics.Point(10, 47.5), "2048")
    logo_text.setFill("black")
    logo_text.setStyle("bold")
    logo_text.setSize(36)
    logo_text.draw(win)

# draw score & best rectangles
    # score
    score = graphics.Rectangle(graphics.Point(22.5, 51.25), graphics.Point(28.75, 53.75))
    score.setFill("darkgoldenrod1")
    score.setOutline("black")
    score.draw(win)

    score_text = graphics.Text(graphics.Point(25.625, 52.5), "Score")
    score_text.setFill("black")
    score_text.setStyle("bold")
    score_text.setSize(12)
    score_text.draw(win)

    # best
    best = graphics.Rectangle(graphics.Point(31.25, 51.25), graphics.Point(37.5, 53.75))
    best.setFill("darkgoldenrod1")
    best.setOutline("black")
    best.draw(win)

    best_text = graphics.Text(graphics.Point(34.375, 52.5), "Best")
    best_text.setFill("black")
    best_text.setStyle("bold")
    best_text.setSize(12)
    best_text.draw(win)


def createInGameButton(win):
    """
    Create the in-game buttons (MENU).
    :return a tuple of rectangles and texts.
    """
    # create menu elements rectangle
    menu_rect = graphics.Rectangle(graphics.Point(22.5, 37.5), graphics.Point(37.5, 42.5))
    menu_rect.setFill("darkgoldenrod1")
    menu_rect.draw(win)

    # create menu elements text
    menu_text = graphics.Text(graphics.Point(30, 40), "Menu")
    menu_text.setFill("black")
    menu_text.setStyle("bold")
    menu_text.setSize(24)
    menu_text.draw(win)

    return (menu_rect, menu_text)


def createInGameRectangles():
    """
    Create the in-game rectangles.
    :return a list of the rectangles created.
    """
    rectangles = []

    # create the last 2 elements rectangles in labels
    for i in range(2):
        rectangles.append(graphics.Rectangle(graphics.Point(22.5 + (i)*8.75, 45), graphics.Point(28.75 + (i)*8.75, 51.25)))
        rectangles[i].setFill("white")
        rectangles[i].setOutline("black")

    return rectangles


def createInGameTexts():
    """
    Create the in-game texts.
    :return a list of the texts created.
    """
    texts = []
    # 0: score, 1: best
    labels = ["0", "0"]

    # creating the last 2 elements text in labels
    for i in range(2):
        texts.append(graphics.Text(graphics.Point(25.625 + (i)*8.75, 48.125), labels[i]))
        texts[i].setFill("gray")
        texts[i].setStyle("bold")
        texts[i].setSize(18)

    return texts


def updateInGameTexts(game_board, texts, win):
    """Update score and best."""
    highest = -1
    for row in game_board:
        for element in row:
            if element > highest:
                highest = element
    temp_score = texts[0]
    texts[0].setText(str(highest))
    temp_score.undraw()
    texts[0].draw(win)
    if int(texts[0].getText()) > int(texts[1].getText()):
        temp_best = texts[1]
        texts[1].setText(str(highest))
        temp_best.undraw()
        texts[1].draw(win)


def createInGameWidgets(win):
    """
    Create and Draw the in-game widgets (SCORE & BEST VALUES).
    :return as a tuple of rectangle and text.
    """
    rect = createInGameRectangles()
    for element in rect:
        element.draw(win)
    
    text = createInGameTexts()
    for element in text:
        element.draw(win)

    return (rect, text)


def createMenuRectangles():
    """Create a list of buttons (all we need to do is draw them)."""
    rectangles = []

    # main rectangle
    rectangles.append(graphics.Rectangle(graphics.Point(0, 0), graphics.Point(40, 60)))
    rectangles[0].setFill("white")

    # range of len(labels)
    for i in range(1, 5):
        rectangles.append(graphics.Rectangle(graphics.Point(12.5, 13.75 + (i - 1)*8), graphics.Point(27.5, 18.75 + (i - 1)*8)))
        rectangles[i].setFill("darkgoldenrod1")
        rectangles[i].setOutline("black")
    
    return rectangles


def createMenuTexts():
    """Create a list of texts for buttons (all we need to do is draw them)."""
    texts = []
    labels = ["Quit", "Settings", "New Game", "Resume"]

    for i in range(len(labels)):
        texts.append(graphics.Text(graphics.Point(20, 16.25 + i*8), labels[i]))
        texts[i].setFill("gray")
        texts[i].setStyle("bold")
        texts[i].setSize(16)

    return texts


def createMenuButtons(win):
    """Create and Draw buttons when menu button is pressed."""
    rectangles = createMenuRectangles()
    texts = createMenuTexts()

    return (rectangles, texts)


def drawMenuButtons(menu, win):
    """Draw menu buttons."""
    for rect_text in menu:
        for element in rect_text:
            element.draw(win)



def undrawMenuButtons(menu):
    """Undraw menu buttons."""
    for rect_text in menu:
        for element in rect_text:
            element.undraw()


def drawMenuButtonsLoss(menu, win):
    """Draw menu buttons for a loss (no resume button)."""
    # 5 rectangles (minus the resume one)
    for i in range(4):
        if i != 4:
            menu[0][i].draw(win)
    # 4 texts (minus the resume one)
    for i in range(3):
        if i != 3:
            menu[1][i].draw(win)



def undrawMenuButtonsLoss(menu):
    """Undraw menu buttons for a loss (no resume button)."""
    # 5 rectangles
    for i in range(5):
        if i != 4:
            menu[0][i].undraw()
    # 4 texts
    for i in range(4):
        if i != 3:
            menu[1][i].undraw()


def createSettingsButtons(win):
    """TBD!"""
    pass


def checkButtonClick(point, rectangle):
    """Check for a button click."""
    if point != None:
        if(rectangle.getP1().getX() <= point.x <= rectangle.getP2().getX() and rectangle.getP1().getY() <= point.y <= rectangle.getP2().getY()):
            return True


def checkKeyPress(key):
    """Check for a key press."""
    if key != "":
        return True


def createBoardPieceRectangles():
    """
    Create rectangles for every piece (helps for changing colors of new pieces).
    :return a list of rectangles starting from the top left, ending at bottom right

    Note: iteration: for x in ___: for y in ___: (i.e. goes through all y's first)
    """
    rectangles = []

    for y in range(4):
        startCoordY = 35 - 7.5*(y + 1)
        endCoordY = 35 - 7.5*y
        for x in range(4):
            startCoordX = 5 + 7.5*x
            endCoordX = 12.5 + 7.5*x
            rectangles.append(graphics.Rectangle(graphics.Point(startCoordX, startCoordY), graphics.Point(endCoordX, endCoordY)))
            rectangles[y*4 + x].setFill("darkgoldenrod1")
            rectangles[y*4 + x].setOutline("black")

    return rectangles


def createBoardPieceTexts(game_board):
    """
    Create text positions for every piece (numerical values for squares).
    :return a list of texts starting from the top left, ending at bottom right

    Note: iteration: for x in ___: for y in ___: (i.e. goes through all y's first)
    """
    texts = []

    for y in range(4):
        coordY = 31.25 - 7.5*y
        for x in range(4):
            coordX = 8.75 + 7.5*x
            texts.append(graphics.Text(graphics.Point(coordX, coordY), str(game_board[y][x])))
            texts[y*4 + x].setFill("black")
            texts[y*4 + x].setStyle("bold")
            texts[y*4 + x].setSize(20)

    return texts


def createBoardPieces(game_board):
    """
    Create the 2048 game pieces. (Note: not drawing anything, just creating).
    :return a tuple of rectangles and texts.
    """
    rectangles = createBoardPieceRectangles()
    texts = createBoardPieceTexts(game_board)

    return (rectangles, texts)


def updateBoardPieceTexts(texts, game_board):
    """
    Update text values based on new updated board.
    We update after 2 possibilities: computer move OR user move
    :return a list of texts.
    """
    for i in range(4):
        for j in range(4):
            texts[i*4 + j].setText(str(game_board[i][j]))


def drawBoard(pieces, win):
    """
    Draw updated board.

    sizeof piece rectangle: 7.5 x 7.5
    position of bottom left (start): (5, 5), (12.5, 12.5)
    position of top right (start): (27.5, 27.5), (35, 35)
    """
    # lst consists of (rectangle, texts)
    for lst in pieces:
        for element in lst:
            if type(element) is graphics.Text:
                if element.getText() == '0':
                    element.setTextColor("darkgoldenrod1")
                else:
                    element.setTextColor("black")
            element.draw(win)


def undrawBoard(pieces):
    for lst in pieces:
        for element in lst:
            element.undraw()


def drawComputerMove(row, col, val, pieces, game_board, win):
    """
    Draw board once, denoting the piece which has appeared from computer.
    Create "animation" of piece getting bigger from a reduced size.
    Call drawBoard(), restoring the color of the new piece to the default.
    """
    for i in range(4):
        for j in range(4):
            if row == i and col == j:
                # get rectangle size
                p1X = pieces[0][i*4 + j].getP1().getX()
                p1Y = pieces[0][i*4 + j].getP1().getY()
                p2X = pieces[0][i*4 + j].getP2().getX()
                p2Y = pieces[0][i*4 + j].getP2().getY()
                # modify both rectangle and text size to create the illusion of a piece getting bigger
                for animation in range(3):
                    if animation > 0:
                        rect.undraw()
                        text.undraw()
                    rect = graphics.Rectangle(graphics.Point(p1X + (2 - animation), p1Y + (2 - animation)), graphics.Point(p2X - (2 - animation), p2Y - (2 - animation)))
                    rect.setFill("pink")
                    rect.setOutline("black")
                    rect.draw(win)
                    text = graphics.Text(pieces[0][i*4 + j].getCenter(), str(val))
                    text.setTextColor("black")
                    text.setStyle("bold")
                    text.setSize(animation*4 + 12)
                    text.draw(win)
                    # DELAY TIME FOR "ANIMATION"
                    time.sleep(0.05)
                rect.undraw()
                text.undraw()
                break


def drawUserMove(game_board, win):
    """
    Draw board multiple times, depending on furthest distance of piece move.
    Create "animation" of pieces moving from original position.
    Call drawBoard(), displaying the updated board.
    """
    pass



def main():
    win = graphics.GraphWin("2048 - 88vch", 400, 600)
    win.setCoords(0, 0, 40, 60)

# draw colored background
    background = graphics.Rectangle(graphics.Point(0, 0), graphics.Point(40, 60))
    # color
    background.setFill("burlywood3")
    background.draw(win)
    createBoard(win, 5, 5, 35, 35)
    # a tuple of (rectangle, texts)
    #       Note: need to create an updateInGameValues() function
    #               takes in some param and updates the value in score/best
    #               (undraw then redraw) 
    in_game_widgets = createInGameWidgets(win)

    # menu_button is a tuple (rect, text)
    menu_button = createInGameButton(win)

    # Initialize game state trackers
    loss = 0
    winners_mode = 0
    
    if version == "ics31":
        valid_inputs = ["w", "a", "s", "d", "q"]
    if version == "summer2022":
        # arrow keys follow wasd placement (ex. w = \x1b[A)
        valid_inputs = ["w", "a", "s", "d", "\x1b[A", "\x1b[D", "\x1b[B", "\x1b[C", "q"]
    if version == "summer2022Graphics":
        # arrow keys follow wasd placement (ex. w = \x1b[A)
        valid_inputs = ["w", "a", "s", "d", "Up", "Left", "Down", "Right", "q"]
    
    
    # main gamestate (in-game)
    # create substates (but don't draw them yet!)
        # 1: menu
    menu = createMenuButtons(win)
            # 5: resume     (from #2)
            # 4: new game   (from #2)
            # 3: settings   (from #2)
    settings = createSettingsButtons(win)
            # 2: quit       (from #2)


    INGAME = 1

    while INGAME == 1:
        game_board = [[0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]]
        # initalize graphical pieces
        pieces = createBoardPieces(game_board)
        drawBoard(pieces, win)

        # initialize board's first cell
        # generate 2 random pieces and locations using the generate_piece function
        # place the piece at the specified location
        for i in range(2):
            # Note: generate_piece function is within the computer_move function
            row, col, val = game.computer_move(game_board)
            undrawBoard(pieces)
            updateBoardPieceTexts(pieces[1], game_board)
            drawComputerMove(row, col, val, pieces, game_board, win)
            drawBoard(pieces, win)
        # for drawComputerMove() and drawUserMove() we need functions (used repeatedly)
        # print console game
        updateInGameTexts(game_board, in_game_widgets[1], win)
        game.print_board(game_board)
        print()


        # main loop
        # first print initial game board
        gamestate = 0
        z = True
        while z:
            # in-game (GAME LOOP)
            if gamestate == 0:
                click = win.checkMouse()
                press = win.checkKey()
                if checkButtonClick(click, menu_button[0]):
                    drawMenuButtons(menu, win)
                    gamestate = 1
                    continue
                elif checkKeyPress(press):
                    if press in valid_inputs:
                        # (FINAL PORTION -- ACTUAL GAME IMPLEMENTATION!!): update game then print updated game board
                        # convert arrow keys -> wasd (preserve code)
                        if version == "summer2022Graphics":
                            for i in range(4):
                                # assigment of arrow key value to wasd value
                                if press == valid_inputs[i + 4]:
                                    press = valid_inputs[i]
                                    break
                        elif version == "summer2022":
                            if user_input[0:2] == "\x1b[":
                                for i in range(4):
                                    # assigment of arrow key value to wasd value
                                    if user_input[2] == valid_inputs[i + 4][2]:
                                        user_input = valid_inputs[i]
                                        break
                        elif version == "ics31":
                            pass
                        
                        # Check if board position changed
                        if game.check_board_moved(game_board, press) == False:
                            print("Board hasn't changed. Please enter another move...")
                            press = win.checkKey()
                            continue
                        # else, execute the user's move
                        else:
                            game_board = game.move_board(game_board, press)
                            updateInGameTexts(game_board, in_game_widgets[1], win)
                            # NEED TO DISPLAY MOVEMENT OF PLAYER PIECE HERE...
                        # Check if the user wins (NEED TO MODIFY)
                        if game.check_user_win(game_board) and winners_mode == 0:
                            game.print_board(game_board)
                            print("Congratulations! You have won 2048!")
                            z = 1
                            while z:
                                end_game_input = input("Would you like to continue playing? (Enter yes or no) ")
                                if end_game_input == 'yes':
                                    print("you have chosen to continue, Please enter a move...")
                                    user_input = input()
                                    z = 0
                                elif end_game_input == 'no':
                                    user_input = 'q'
                                    z = 0
                                else:
                                    print("Please enter a proper choice")
                            winners_mode = 1
                            continue
                        # place a random piece on the board
                        row, col, val = game.computer_move(game_board)
                        undrawBoard(pieces)
                        updateBoardPieceTexts(pieces[1], game_board)
                        drawComputerMove(row, col, val, pieces, game_board, win)
                        drawBoard(pieces, win)
                        # check to see if the game is over using the game_over function
                        if game.game_over(game_board):
                            print("Game Over! You have lost!")
                            loss = 1
                            drawMenuButtonsLoss(menu, win)
                            gamestate = 1
                            continue
                        # show updated board using the print_board function
                        game.print_board(game_board)
                        print()
                        # take user's turn
                        press = win.checkKey()
                    else:
                        press = win.checkKey()
            # menu
            if gamestate == 1:
                click = win.checkMouse()
                # quit
                if checkButtonClick(click, menu[0][1]):
                    z = False
                    INGAME = 0
                # settings (TBD!)
                if checkButtonClick(click, menu[0][2]):
                    pass
                    #gamestate = 3
                # new game
                if checkButtonClick(click, menu[0][3]):
                    undrawMenuButtons(menu)
                    undrawBoard(pieces)
                    in_game_widgets[1][0].setText("0")
                    gamestate = 2
                    continue
                # we only display resume if it's not a loss
                if loss != 1:
                    # resume
                    if checkButtonClick(click, menu[0][4]):
                        undrawMenuButtons(menu)
                        gamestate = 0
            # settings (from #2)
            if gamestate == 3:
                pass
            # new game (from #3)
            if gamestate == 2:
                z = False
    print("Goodbye")
    win.close()

    # console game
    #game.main(game_board)



if __name__ == "__main__":
    main()
