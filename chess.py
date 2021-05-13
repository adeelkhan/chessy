
class Piece:
    def __init__(self, repr, board, pos, color):
        self.color = color
        self.board = board
        self.position = pos
        self.repr = repr

    def move(self, to, player):
        pass

    def get_valid_moves(self, row, col):
        pass

    def __str__(self):
      return self.repr

    def get_color(self):
        return self.color

    def set_position(self, pos):
        self.position = pos

class Queen(Piece):
    def __init__(self, repr, board, pos, color):
        super().__init__(repr, board, pos, color)

    def move(self, to, player):
        frow, fcol = self.board.get_position(self.position)
        trow, tcol = self.board.get_position(to)
        valid_moves = self.get_valid_moves(frow, fcol)
        is_check = self.is_check(trow, tcol)
        self.board.checkmate_status = is_check

        if is_check:
            print('Check!')

        if (trow, tcol) in valid_moves:
            piece = self.board.get_box(frow, fcol).get_piece()
            captured_piece = self.board.get_box(trow, tcol).get_piece()
            if captured_piece: # captured piece
                player.captured_pieces.append(str(captured_piece))

            piece.set_position(to)
            self.board.get_box(frow, fcol).set_piece(None)
            self.board.get_box(trow, tcol).set_piece(piece)
            return True
        else:
            print("Can't move there.")
            return False


    def get_valid_moves(self, row, col):
        positions = {}

        # right
        j = col + 1
        while j < 8:
            piece = self.board.get_box(row, j).get_piece()
            if not piece or piece.get_color() != self.color:
                positions[(row, j)] = (row, j)
                j+=1
            else:
                break

        # left
        j = col - 1
        while j >=0 :
            piece = self.board.get_box(row, j).get_piece()
            if not piece or piece.get_color() != self.color:
                positions[(row, j)] = (row, j)
                j-=1
            else:
                break

        # down
        i = row + 1
        while i < 8:
            piece = self.board.get_box(i, col).get_piece()
            if not piece or piece.get_color() != self.color:
                positions[(i, col)] = (i, col)
                i+=1
            else:
                break

        # up
        i = row - 1
        while i >=0:
            piece = self.board.get_box(i, col).get_piece()
            if not piece or piece.get_color() != self.color:
                positions[(i, col)] = (i, col)
                i-=1
            else:
                break

        # diagonal right down
        i =  row + 1
        j =  col + 1
        while i < 8 and j < 8:
            piece = self.board.get_box(i, j).get_piece()
            if not piece or piece.get_color() != self.color:
                positions[(i,j)] = (i, j)
                i+=1
                j+=1
            else:
                break

        # diagonal right up
        i = row - 1
        j = col + 1
        while i >= 0 and j < 8:
            piece = self.board.get_box(i, j).get_piece()
            if not piece or piece.get_color() != self.color:
                positions[(i, j)] = (i, j)
                i -= 1
                j += 1
            else:
                break

        # diagonal left down
        i = row + 1
        j = col - 1
        while i < 8 and j >= 0:
            piece = self.board.get_box(i, j).get_piece()
            if not piece or piece.get_color() != self.color:
                positions[(i, j)] = (i, j)
                i += 1
                j -= 1
            else:
                break

        # diagonal left up
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            piece = self.board.get_box(i, j).get_piece()
            if not piece or piece.get_color() != self.color:
                positions[(i, j)] = (i, j)
                i -= 1
                j -= 1
            else:
                break

        return positions

    def get_all_moves(self, row, col):
        positions = {}

        # right
        j = col + 1
        while j < 8:
            piece = self.board.get_box(row, j).get_piece()
            if not piece or piece.get_color() == self.color:
                positions[(row, j)] = (row, j)

            if piece and piece.get_color() == self.color:
                break
            j += 1

        # left
        j = col - 1
        while j >= 0:
            piece = self.board.get_box(row, j).get_piece()
            if not piece or piece.get_color() == self.color:
                positions[(row, j)] = (row, j)

            if piece and piece.get_color() == self.color:
                break

            j -= 1

        # down
        i = row + 1
        while i < 8:
            piece = self.board.get_box(i, col).get_piece()
            if not piece or piece.get_color() == self.color:
                positions[(i, col)] = (i, col)

            if piece and piece.get_color() == self.color:
                break

            i += 1

        # up
        i = row - 1
        while i >= 0:
            piece = self.board.get_box(i, col).get_piece()
            if not piece or piece.get_color() == self.color:
                positions[(i, col)] = (i, col)

            if piece and piece.get_color() == self.color:
                break

            i -= 1

        # diagonal right down
        i = row + 1
        j = col + 1
        while i < 8 and j < 8:
            piece = self.board.get_box(i, j).get_piece()
            if not piece or piece.get_color() == self.color:
                positions[(i, j)] = (i, j)

            if piece and piece.get_color() == self.color:
                break

            i += 1
            j += 1

        # diagonal right up
        i = row - 1
        j = col + 1
        while i >= 0 and j < 8:
            piece = self.board.get_box(i, j).get_piece()
            if not piece or piece.get_color() == self.color:
                positions[(i, j)] = (i, j)

            if piece and piece.get_color() == self.color:
                break

            i -= 1
            j += 1

        # diagonal left down
        i = row + 1
        j = col - 1
        while i < 8 and j >= 0:
            piece = self.board.get_box(i, j).get_piece()
            if not piece or piece.get_color() == self.color:
                positions[(i, j)] = (i, j)

            if piece and piece.get_color() == self.color:
                break

            i += 1
            j -= 1

        # diagonal left up
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            piece = self.board.get_box(i, j).get_piece()
            if not piece or piece.get_color() == self.color:
                positions[(i, j)] = (i, j)

            if piece and piece.get_color() == self.color:
                break
            i -= 1
            j -= 1

        return positions


    def is_check(self, row, col):
        # right
        j = col + 1
        while j < 8:
            piece = self.board.get_box(row, j).get_piece()
            if not piece:
                j += 1
                continue

            if piece and piece.get_color() != self.color and str(piece)[0] == 'G':
                return True
            else:
                break


        # left
        j = col - 1
        while j >= 0:
            piece = self.board.get_box(row, j).get_piece()
            if not piece:
                j -= 1
                continue

            if piece and piece.get_color() != self.color and str(piece)[0] == 'G':
                return True
            else:
                break

        # down
        i = row + 1
        while i < 8:
            piece = self.board.get_box(i, col).get_piece()
            if not piece:
                i += 1
                continue

            if piece and piece.get_color() != self.color and str(piece)[0] == 'G':
                return True
            else:
                break

        # up
        i = row - 1
        while i >= 0:
            piece = self.board.get_box(i, col).get_piece()
            if not piece:
                i -= 1
                continue

            if piece and piece.get_color() != self.color and str(piece)[0] == 'G':
                return True
            else:
                break

        # diagonal right down
        i = row + 1
        j = col + 1
        while i < 8 and j < 8:
            piece = self.board.get_box(i, j).get_piece()
            if not piece:
                i += 1
                j += 1
                continue

            if piece and piece.get_color() != self.color and str(piece)[0] == 'G':
                return True
            else:
                break

        # diagonal right up
        i = row - 1
        j = col + 1
        while i >= 0 and j < 8:
            piece = self.board.get_box(i, j).get_piece()
            if not piece:
                i -= 1
                j += 1
                continue

            if piece and piece.get_color() != self.color and str(piece)[0] == 'G':
                return True
            else:
                break

        # diagonal left down
        i = row + 1
        j = col - 1
        while i < 8 and j >= 0:
            piece = self.board.get_box(i, j).get_piece()
            if not piece:
                i += 1
                j -= 1
                continue

            if piece and piece.get_color() != self.color and str(piece)[0] == 'G':
                return True
            else:
                break


        # diagonal left up
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            piece = self.board.get_box(i, j).get_piece()
            if not piece:
                i -= 1
                j -= 1
                continue

            if piece and piece.get_color() != self.color and str(piece)[0] == 'G':
                return True
            else:
                break


class Rook(Piece):
    def __init__(self, repr, board, pos, color):
        super().__init__(repr, board, pos, color)

    def move(self, to, player):
        frow, fcol = self.board.get_position(self.position)
        trow, tcol = self.board.get_position(to)
        valid_moves = self.get_valid_moves(frow, fcol)
        is_check = self.is_check(trow, tcol)
        self.board.checkmate_status = is_check

        if is_check:
            print('Check!')

        if (trow, tcol) in valid_moves:
            piece = self.board.get_box(frow, fcol).get_piece()
            captured_piece = self.board.get_box(trow, tcol).get_piece()
            if captured_piece: # captured piece
                player.captured_pieces.append(str(captured_piece))

            piece.set_position(to)
            self.board.get_box(frow, fcol).set_piece(None)
            self.board.get_box(trow, tcol).set_piece(piece)
            return True
        else:
            return False


    def get_valid_moves(self, row, col):
        positions = {}

        # move right
        j = col + 1
        while j < 8:
            piece = self.board.get_box(row, j).get_piece()
            if not piece or piece.get_color() != self.color:
                positions[(row, j)] = (row, j)
                j += 1
            else:
                break

        # move left
        j = col - 1
        while j >= 0:
            piece = self.board.get_box(row, j).get_piece()
            if not piece or piece.get_color() != self.color:
                positions[(row, j)] = (row, j)
                j -= 1
            else:
                break

        # move down
        i = row + 1
        while i < 8:
            piece = self.board.get_box(i, col).get_piece()
            if not piece or piece.get_color() != self.color:
                positions[(i, col)] = (i, col)
                i += 1
            else:
                break

        # move up
        i = row - 1
        while i >= 0:
            piece = self.board.get_box(i, col).get_piece()
            if not piece or piece.get_color() != self.color:
                positions[(i, col)] = (i, col)
                i -= 1
            else:
                break

        return positions

    def get_all_moves(self, row, col):
        positions = {}

        # move right
        j = col + 1
        while j < 8:
            piece = self.board.get_box(row, j).get_piece()
            if not piece or piece.get_color() == self.color:
                positions[(row, j)] = (row, j)

            if piece and piece.get_color() == self.color:
                break
            j += 1

        # move left
        j = col - 1
        while j >= 0:
            piece = self.board.get_box(row, j).get_piece()
            if not piece or piece.get_color() == self.color:
                positions[(row, j)] = (row, j)

            if piece and piece.get_color() == self.color:
                break

            j -= 1

        # move down
        i = row + 1
        while i < 8:
            piece = self.board.get_box(i, col).get_piece()
            if not piece or piece.get_color() == self.color:
                positions[(i, col)] = (i, col)

            if piece and piece.get_color() == self.color:
                break

            i += 1

        # move up
        i = row - 1
        while i >= 0:
            piece = self.board.get_box(i, col).get_piece()
            if not piece or piece.get_color() == self.color:
                positions[(i, col)] = (i, col)

            if piece and piece.get_color() == self.color:
                break

            i -= 1

        return positions

    def is_check(self, row, col):
        # move right
        j = col + 1
        while j < 8:
            piece = self.board.get_box(row, j).get_piece()
            if not piece:
                j += 1
                continue

            if piece or piece.get_color() != self.color and str(piece)[0] == 'G':
                return True
            else:
                break


        # move left
        j = col - 1
        while j >= 0:
            piece = self.board.get_box(row, j).get_piece()
            if not piece:
                j -= 1
                continue

            if piece or piece.get_color() != self.color and str(piece)[0] == 'G':
                return True
            else:
                break


        # move down
        i = row + 1
        while i < 8:
            piece = self.board.get_box(i, col).get_piece()
            if not piece:
                i += 1
                continue

            if piece or piece.get_color() != self.color and str(piece)[0] == 'G':
                return True
            else:
                break


        # move up
        i = row - 1
        while i >= 0:
            piece = self.board.get_box(i, col).get_piece()
            if not piece:
                i -= 1
                continue

            if piece or piece.get_color() != self.color and str(piece)[0] == 'G':
                return True
            else:
                break

        return False



class Bishop(Piece):
    def __init__(self, repr, board, pos, color):
        super().__init__(repr, board, pos, color)

    def move(self, to, player):
        frow, fcol = self.board.get_position(self.position)
        trow, tcol = self.board.get_position(to)
        valid_moves = self.get_valid_moves(frow, fcol)
        is_check = self.is_check(trow, tcol)
        self.board.checkmate_status = is_check

        if is_check:
            print('Check!')
        if (trow, tcol) in valid_moves:
            piece = self.board.get_box(frow, fcol).get_piece()
            captured_piece = self.board.get_box(trow, tcol).get_piece()
            if captured_piece: # captured piece
                player.captured_pieces.append(str(captured_piece))

            piece.set_position(to)
            self.board.get_box(frow, fcol).set_piece(None)
            self.board.get_box(trow, tcol).set_piece(piece)
            return True
        else:
            print("Cant move there.")
            return False



    def get_valid_moves(self, row, col):
        positions = {}

        # diagonal right down
        i = row + 1
        j = col + 1
        while i < 8 and j < 8:
            piece = self.board.get_box(i, j).get_piece()
            if not piece or piece.get_color() != self.color:
                positions[(i, j)] = (i, j)
                i += 1
                j += 1
            else:
                break

        # diagonal right up
        i = row - 1
        j = col + 1
        while i >= 0 and j < 8:
            piece = self.board.get_box(i, j).get_piece()
            if not piece or piece.get_color() != self.color:
                positions[(i, j)] = (i, j)
                i -= 1
                j += 1
            else:
                break

        # diagonal left down
        i = row + 1
        j = col - 1
        while i < 8 and j >= 0:
            piece = self.board.get_box(i, j).get_piece()
            if not piece or piece.get_color() != self.color:
                positions[(i, j)] = (i, j)
                i += 1
                j -= 1
            else:
                break

        # diagonal left up
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            piece = self.board.get_box(i, j).get_piece()
            if not piece or piece.get_color() != self.color:
                positions[(i, j)] = (i, j)
                i -= 1
                j -= 1
            else:
                break

        return positions

    def get_all_moves(self, row, col):
        positions = {}

        # diagonal right down
        i = row + 1
        j = col + 1
        while i < 8 and j < 8:
            piece = self.board.get_box(i, j).get_piece()
            if not piece or piece.get_color() == self.color:
                positions[(i, j)] = (i, j)

            if piece and piece.get_color() == self.color:
                break

            i += 1
            j += 1

        # diagonal right up
        i = row - 1
        j = col + 1
        while i >= 0 and j < 8:
            if not piece or piece.get_color() == self.color:
                positions[(i, j)] = (i, j)

            if piece and piece.get_color() == self.color:
                break

            i -= 1
            j += 1

        # diagonal left down
        i = row + 1
        j = col - 1
        while i < 8 and j >= 0:
            if not piece or piece.get_color() == self.color:
                positions[(i, j)] = (i, j)

            if piece and piece.get_color() == self.color:
                break
            i += 1
            j -= 1

        # diagonal left up
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if not piece or piece.get_color() == self.color:
                positions[(i, j)] = (i, j)

            if piece and piece.get_color() == self.color:
                break
            i -= 1
            j -= 1

        return positions

    def is_check(self, row, col):
        # diagonal right down
        i = row + 1
        j = col + 1
        while i < 8 and j < 8:
            piece = self.board.get_box(i, j).get_piece()
            if not piece:
                i += 1
                j += 1
                continue

            if piece and piece.get_color() != self.color and str(piece)[0] == 'G':  # check case
                return True
            else:
                break


        # diagonal right up
        i = row - 1
        j = col + 1
        while i >= 0 and j < 8:
            piece = self.board.get_box(i, j).get_piece()
            if not piece:
                i -= 1
                j += 1
                continue

            if piece and piece.get_color() != self.color and str(piece)[0] == 'G':  # check case
                return True
            else:
                break


        # diagonal left down
        i = row + 1
        j = col - 1
        while i < 8 and j >= 0:
            piece = self.board.get_box(i, j).get_piece()
            if not piece:
                i += 1
                j -= 1
                continue

            if piece and piece.get_color() != self.color and str(piece)[0] == 'G':  # check case
                return True
            else:
                break


        # diagonal left up
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            piece = self.board.get_box(i, j).get_piece()
            if not piece:
                i -= 1
                j -= 1
                continue

            if piece and piece.get_color() != self.color and str(piece)[0] == 'G':  # check case
                return True
            else:
                break

        return False


class King(Piece):
    def __init__(self, repr, board, pos, color):
        super().__init__(repr, board, pos, color)

    def move(self, to, player):
        frow, fcol = self.board.get_position(self.position)
        trow, tcol = self.board.get_position(to)
        valid_moves = self.get_valid_moves(frow, fcol)
        is_check = self.is_check(trow, tcol)
        if is_check:
            print("Can't move there, Check!!")

        self.board.checkmate_status = is_check

        if not is_check and (trow, tcol) in valid_moves:
            piece = self.board.get_box(frow, fcol).get_piece()
            captured_piece = self.board.get_box(trow, tcol).get_piece()
            if captured_piece:  # captured piece
                player.captured_pieces.append(str(captured_piece))

            piece.set_position(to)
            self.board.get_box(frow, fcol).set_piece(None)
            self.board.get_box(trow, tcol).set_piece(piece)
            return True
        else:
            return False

    def get_valid_moves(self, row, col):
        positions = {}

        # down
        i = row + 1
        if i < 8:
            piece = self.board.get_box(i, col).get_piece()
            if not piece or (piece and piece.get_color() != self.color):
                positions[(i, col)] = (i, col)

        # up
        i = row - 1
        if i >= 0:
            piece = self.board.get_box(i, col).get_piece()
            if not piece or (piece and piece.get_color() != self.color):
                positions[(i, col)] = (i, col)

        # right
        j = col + 1
        if j < 8:
            piece = self.board.get_box(row, j).get_piece()
            if not piece or (piece and piece.get_color() != self.color):
                positions[(row, j)] = (row, j)

        # left
        j = col - 1
        if j >= 0:
            piece = self.board.get_box(row, j).get_piece()
            if not piece or (piece and piece.get_color() != self.color):
                positions[(row, j)] = (row, j)

        # rightdown diag
        i = row + 1
        j = col + 1
        if i < 8 and j < 8:
            piece = self.board.get_box(i, j).get_piece()
            if not piece or (piece and piece.get_color() != self.color):
                positions[(i, j)] = (i, j)

        # leftdown diag
        i = row + 1
        j = col - 1
        if i < 8 and j >= 0:
            piece = self.board.get_box(i, j).get_piece()
            if not piece or (piece and piece.get_color() != self.color):
                positions[(i, j)] = (i, j)

        # rightup diag
        i = row - 1
        j = col + 1
        if i >= 0 and j < 8:
            piece = self.board.get_box(i, j).get_piece()
            if not piece or (piece and piece != self.color):
                positions[(i, j)] = (i, j)

        # leftup diag
        i = row - 1
        j = col - 1
        if i >= 0 and j >= 0:
            piece = self.board.get_box(i, j).get_piece()
            if not piece or (piece and piece != self.color):
                positions[(i, j)] = (i, j)

        return positions

    def is_check(self, trow, tcol):
        #brute force way
        valid_moves = {}
        for i in range(8):
            for j in range(8):
                piece = self.board.get_box(i,j).get_piece()
                if piece and piece.get_color() != self.color:
                    frow, fcol = self.board.get_position(piece.position)
                    valid_moves.update(piece.get_all_moves(frow, fcol))

        return True if (trow, tcol) in valid_moves else False


    def get_all_moves(self, row, col):
        positions = {}

        # down
        i = row + 1
        if i < 8:
            positions[(i, col)] = (i, col)

        # up
        i = row - 1
        if i >= 0:
            positions[(i, col)] = (i, col)

        # right
        j = col + 1
        if j < 8:
            positions[(row, j)] = (row, j)

        # left
        j = col - 1
        if j >= 0:
            positions[(row, j)] = (row, j)

        # rightdown diag
        i = row + 1
        j = col + 1
        if i < 8 and j < 8:
            positions[(i, j)] = (i, j)

        # leftdown diag
        i = row + 1
        j = col - 1
        if i < 8 and j >= 0:
            positions[(i, j)] = (i, j)

        # rightup diag
        i = row - 1
        j = col + 1
        if i >= 0 and j < 8:
            positions[(i, j)] = (i, j)

        # leftup diag
        i = row - 1
        j = col - 1
        if i >= 0 and j >= 0:
            positions[(i, j)] = (i, j)

        return positions



class Knight(Piece):
    def __init__(self, repr, board, pos, color):
        super().__init__(repr, board, pos, color)

    def move(self, to, player):
        frow, fcol = self.board.get_position(self.position)
        trow, tcol = self.board.get_position(to)
        valid_moves = self.get_valid_moves(frow, fcol)
        is_check = self.is_check(trow, tcol)
        self.board.checkmate_status = is_check

        if is_check:
            print('Check!')

        if (trow, tcol) in valid_moves:
            piece = self.board.get_box(frow, fcol).get_piece()
            captured_piece = self.board.get_box(trow, tcol).get_piece()
            if captured_piece: # captured piece
                player.captured_pieces.append(str(captured_piece))

            piece.set_position(to)
            self.board.get_box(frow, fcol).set_piece(None)
            self.board.get_box(trow, tcol).set_piece(piece)
            return True
        else:
            print("Can't move there")
            return False


    def get_valid_moves(self, row, col):
        positions = {}

        # up right   |->
        i = row - 2
        j = col + 1
        if i >=0 and j < 8:
            self.populate_positions(i, j, positions)

        # up left    <-|
        i = row - 2
        j = col - 1
        if i >= 0 and j >= 0:
            self.populate_positions(i, j, positions)

        # left up    /\__
        i = row - 1
        j = col - 2
        if i >= 0 and j >=0:
            self.populate_positions(i, j, positions)

        # left down  \/--
        i = row + 1
        j = col - 2
        if i < 8 and j >= 0:
            self.populate_positions(i, j, positions)

        # right up   __/\
        i = row - 1
        j = col + 2
        if i >= 0 and j < 8:
            self.populate_positions(i, j, positions)

        # right down --\/
        i = row + 1
        j = col + 2
        if i < 8 and j < 8:
            self.populate_positions(i, j, positions)

        # down right |->
        i = row + 2
        j = col + 1
        if i < 8 and j < 8:
            self.populate_positions(i, j, positions)

        # down left  <-|
        i = row + 2
        j = col - 1
        if i < 8 and j >= 0:
            self.populate_positions(i, j, positions)

        return positions

    def populate_positions(self, i, j, positions):
        piece = self.board.get_box(i, j).get_piece()
        if not piece or piece.get_color() != self.color:
            positions[(i, j)] = (i, j)


    def get_all_moves(self, row, col):
        positions = {}

        # up right   |->
        i = row - 2
        j = col + 1
        if i >= 0 and j < 8:
            piece = self.board.get_box(i, j).get_piece()
            if not piece or piece.get_color() == self.color:
                positions[(i, j)] = (i, j)

        # up left    <-|
        i = row - 2
        j = col - 1
        if i >= 0 and j >= 0:
            piece = self.board.get_box(i, j).get_piece()
            if not piece or piece.get_color() == self.color:
                positions[(i, j)] = (i, j)


        # left up    /\__
        i = row - 1
        j = col - 2
        if i >= 0 and j >= 0:
            piece = self.board.get_box(i, j).get_piece()
            if not piece or piece.get_color() == self.color:
                positions[(i, j)] = (i, j)


        # left down  \/--
        i = row + 1
        j = col - 2
        if i < 8 and j >= 0:
            piece = self.board.get_box(i, j).get_piece()
            if not piece or piece.get_color() == self.color:
                positions[(i, j)] = (i, j)


        # right up   __/\
        i = row - 1
        j = col + 2
        if i >= 0 and j < 8:
            piece = self.board.get_box(i, j).get_piece()
            if not piece or piece.get_color() == self.color:
                positions[(i, j)] = (i, j)


        # right down --\/
        i = row + 1
        j = col + 2
        if i < 8 and j < 8:
            piece = self.board.get_box(i, j).get_piece()
            if not piece or piece.get_color() == self.color:
                positions[(i, j)] = (i, j)


        # down right |->
        i = row + 2
        j = col + 1
        if i < 8 and j < 8:
            piece = self.board.get_box(i, j).get_piece()
            if not piece or piece.get_color() == self.color:
                positions[(i, j)] = (i, j)


        # down left  <-|
        i = row + 2
        j = col - 1
        if i < 8 and j >= 0:
            piece = self.board.get_box(i, j).get_piece()
            if not piece or piece.get_color() == self.color:
                positions[(i, j)] = (i, j)


        return positions

    def is_check(self, row, col):
        # up right   |->
        i = row - 2
        j = col + 1
        if i >= 0 and j < 8:
            piece = self.board.get_box(i, j).get_piece()
            if piece and piece.get_color() != self.color and str(piece)[0]=='G':
                return True

        # up left    <-|
        i = row - 2
        j = col - 1
        if i >= 0 and j >= 0:
            piece = self.board.get_box(i, j).get_piece()
            if piece and piece.get_color() != self.color and str(piece)[0] == 'G':
                return True

        # left up    /\__
        i = row - 1
        j = col - 2
        if i >= 0 and j >= 0:
            piece = self.board.get_box(i, j).get_piece()
            if piece and piece.get_color() != self.color and str(piece)[0] == 'G':
                return True

        # left down  \/--
        i = row + 1
        j = col - 2
        if i < 8 and j >= 0:
            piece = self.board.get_box(i, j).get_piece()
            if piece and piece.get_color() != self.color and str(piece)[0] == 'G':
                return True

        # right up   __/\
        i = row - 1
        j = col + 2
        if i >= 0 and j < 8:
            piece = self.board.get_box(i, j).get_piece()
            if piece and piece.get_color() != self.color and str(piece)[0] == 'G':
                return True

        # right down --\/
        i = row + 1
        j = col + 2
        if i < 8 and j < 8:
            piece = self.board.get_box(i, j).get_piece()
            if piece and piece.get_color() != self.color and str(piece)[0] == 'G':
                return True

        # down right |->
        i = row + 2
        j = col + 1
        if i < 8 and j < 8:
            piece = self.board.get_box(i, j).get_piece()
            if piece and piece.get_color() != self.color and str(piece)[0] == 'G':
                return True

        # down left  <-|
        i = row + 2
        j = col - 1
        if i < 8 and j >= 0:
            piece = self.board.get_box(i, j).get_piece()
            if piece and piece.get_color() != self.color and str(piece)[0]=='G':
                return True

class Pawn(Piece):
    def __init__(self, repr, board, pos, color):
        super().__init__(repr, board, pos, color)
        self.first_move = True

    def move(self, to, player):
        frow, fcol = self.board.get_position(self.position)
        trow, tcol = self.board.get_position(to)
        valid_moves = self.get_valid_moves(frow, fcol)
        is_check = self.is_check(trow, tcol)
        self.board.checkmate_status = is_check

        if is_check:
            print('Check!')

        if (trow, tcol) in valid_moves:
            piece = self.board.get_box(frow, fcol).get_piece()
            captured_piece = self.board.get_box(trow, tcol).get_piece()
            if captured_piece: # captured piece
                player.captured_pieces.append(str(captured_piece))

            piece.set_position(to)
            self.board.get_box(frow, fcol).set_piece(None)
            self.board.get_box(trow, tcol).set_piece(piece)

            self.first_move = False
        else:
            print("Can't move there")
            return False

        return True


    def is_check(self, row, col):

        if self.color == 'black':
            # rightdown diag
            i = row + 1
            j = col + 1
            if i < 8 and j < 8:
                piece = self.board.get_box(i, j).get_piece()
                if piece and piece.get_color() != self.color and str(piece)[0]=='G': # check case
                    return True

            # leftdown diag
            i = row + 1
            j = col - 1
            if i < 8 and j >= 0:
                piece = self.board.get_box(i, j).get_piece()
                if piece and piece.get_color() != self.color and str(piece)[0]=='G': # check case
                    return True

        else:
            # rightup diag
            i = row - 1
            j = col + 1
            if i >= 0 and j < 8:
                piece = self.board.get_box(i, j).get_piece()
                if piece and piece.get_color() != self.color and str(piece)[0] == 'G':  # check case
                    return True

            # leftup diag
            i = row - 1
            j = col - 1
            if i >= 0 and j >= 0:
                piece = self.board.get_box(i, j).get_piece()
                if piece and piece.get_color() != self.color and str(piece)[0] == 'G':  # check case
                    return True

        return False


    def get_valid_moves(self, row, col):
        positions = {}
        if self.color == 'black':
            # down
            i = row + 1
            if i < 8:
                piece = self.board.get_box(i, col).get_piece()

                if not piece:
                    positions[(i, col)] = (i, col)
                    if self.first_move:
                        positions[(i + 1, col)] = (i + 1, col)

            # rightdown diag
            i = row + 1
            j = col + 1
            if i < 8 and j < 8:
                piece = self.board.get_box(i, j).get_piece()
                if piece and piece.get_color() != self.color:
                    positions[(i, j)] = (i, j)


            # leftdown diag
            i = row + 1
            j = col - 1
            if i < 8 and j >= 0:
                piece = self.board.get_box(i, j).get_piece()
                if piece and piece.get_color() != self.color:
                    positions[(i, j)] = (i, j)

        else:
            # up
            i = row - 1
            if i >= 0:
                piece = self.board.get_box(i, col).get_piece()
                if not piece:
                    positions[(i, col)] = (i, col)
                    if self.first_move:
                        positions[(i - 1, col)] = (i - 1, col)

            # rightup diag
            i = row - 1
            j = col + 1
            if i >= 0 and j < 8:
                piece = self.board.get_box(i, j).get_piece()
                if piece and piece != self.color:
                    positions[(i, j)] = (i, j)

            # leftup diag
            i = row - 1
            j = col - 1
            if i >= 0 and j >= 0:
                piece = self.board.get_box(i, j).get_piece()
                if piece and piece != self.color:
                    positions[(i, j)] = (i, j)

        return positions

    def get_all_moves(self, row, col):
        positions = {}
        if self.color == 'black':
            # rightdown diag
            i = row + 1
            j = col + 1
            if i < 8 and j < 8:
                piece = self.board.get_box(i, j).get_piece()
                if not piece or piece.get_color() == self.color:
                    positions[(i, j)] = (i, j)

            # leftdown diag
            i = row + 1
            j = col - 1
            if i < 8 and j >= 0:
                piece = self.board.get_box(i, j).get_piece()
                if not piece or piece.get_color() == self.color:
                    positions[(i, j)] = (i, j)

        else:
            # rightup diag
            i = row - 1
            j = col + 1
            if i >= 0 and j < 8:
                piece = self.board.get_box(i, j).get_piece()
                if not piece or piece.get_color() == self.color:
                    positions[(i, j)] = (i, j)

            # leftup diag
            i = row - 1
            j = col - 1
            if i >= 0 and j >= 0:
                piece = self.board.get_box(i, j).get_piece()
                if not piece or piece.get_color() == self.color:
                    positions[(i, j)] = (i, j)

        return positions


class Box(object):
    def __init__(self, p):
        self.piece = p

    def set_piece(self, p):
        self.piece = p

    def get_piece(self):
        return self.piece if self.piece else None

    def __str__(self):
        return str(self.piece) if self.piece else '##'

class Board(object):
    def __init__(self):
        self.board = [0] * 8
        for i in range(8):
            self.board[i] = [0] * 8

        for i in range(8):
            for j in range(8):
                self.board[i][j] = Box(None)

        self.alphabet_index_map = { 'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7 }
        self.checkmate_status = False
        self.initialize()


    def get_position(self, position):
        row = int(position[1]) - 1
        col = self.alphabet_index_map[position[0]]

        return row, col

    def get_box(self, i, j):
        return self.board[i][j]


    def setup(self, col, row, piece):
        col = self.alphabet_index_map[col]
        row = row-1
        self.board[row][col].set_piece(piece)

    def initialize(self):
        # setup black pieces
        self.setup('a', 1, Rook('Rb', self, 'a1', 'black'))
        self.setup('b', 1, Knight('Kb', self, 'b1', 'black'))
        self.setup('c', 1, Bishop('Bb', self, 'c1', 'black'))
        self.setup('d', 1, Queen('Qb', self, 'd1', 'black'))

        self.setup('e', 1, King('Gb', self, 'e1', 'black'))
        self.setup('f', 1, Bishop('Bb', self, 'f1', 'black'))
        self.setup('g', 1, Knight('Kb', self, 'g1', 'black'))
        self.setup('h', 1, Rook('Rb', self, 'h1', 'black'))

        self.setup('a', 2, Pawn('Pb', self, 'a2', 'black'))
        self.setup('b', 2, Pawn('Pb', self, 'b2', 'black'))
        self.setup('c', 2, Pawn('Pb', self, 'c2', 'black'))
        self.setup('d', 2, Pawn('Pb', self, 'd2', 'black'))

        self.setup('e', 2, Pawn('Pb', self, 'e2', 'black'))
        self.setup('f', 2, Pawn('Pb', self, 'f2', 'black'))
        self.setup('g', 2, Pawn('Pb', self, 'g2', 'black'))
        self.setup('h', 2, Pawn('Pb', self, 'h2', 'black'))

        # setup white pieces
        self.setup('a', 8, Rook('Rw', self, 'a8', 'white'))
        self.setup('b', 8, Knight('Kw', self, 'b8', 'white'))
        self.setup('c', 8, Bishop('Bw', self, 'c8', 'white'))
        self.setup('d', 8, King('Gw', self, 'd8', 'white'))

        self.setup('e', 8, Queen('Qw', self, 'e8', 'white'))
        self.setup('f', 8, Bishop('Bw', self, 'f8', 'white'))
        self.setup('g', 8, Knight('Kw', self, 'g8', 'white'))
        self.setup('h', 8, Rook('Rw', self, 'h8', 'white'))

        self.setup('a', 7, Pawn('Pw', self, 'a7', 'white'))
        self.setup('b', 7, Pawn('Pw', self, 'b7', 'white'))
        self.setup('c', 7, Pawn('Pw', self, 'c7', 'white'))
        self.setup('d', 7, Pawn('Pw', self, 'd7', 'white'))

        self.setup('e', 7, Pawn('Pw', self, 'e7', 'white'))
        self.setup('f', 7, Pawn('Pw', self, 'f7', 'white'))
        self.setup('g', 7, Pawn('Pw', self, 'g7', 'white'))
        self.setup('h', 7, Pawn('Pw', self, 'h7', 'white'))



    def print_board(self):
        print('    a |b |c |d |e |f |g |h ')
        print("-" * 30)
        for i in range(8):
            print(str(i+1), end=':  ')
            for j in range(8):
                print(self.board[i][j], end='|')
            print('\n')
        print("-" * 30)

    def parse_move(self, move, player):
        fpos = move.split('->')[0]
        col = self.alphabet_index_map[fpos[0]]
        row = int(fpos[1]) - 1
        tpos = move.split('->')[1]

        piece = self.board[row][col].get_piece()

        # player should only handle its piece
        if piece and piece.get_color() == player.color:
            if self.checkmate_status == True and str(piece)[0] != 'G': # only king can be moved
                print('Invalid move, you are checked!')
                return False
            status = self.board[row][col].get_piece().move(tpos, player)

            # previous king move result in check repeat the turn
            if self.checkmate_status == True and str(piece)[0] == 'G':
                return False
        else:
            print('Invalid piece touched')
            return False

        return status

    def move(self, move, player):
        return self.parse_move(move, player)



class Player(object):
    def __init__(self, name, color, board):
        self.name = name
        self.board = board
        self.__color = color
        self.captured_pieces = []

    @property
    def color(self):
        return self.__color


    def __str__(self):
        return self.name

    def play(self):
        print(self.name, '[', ','.join(self.captured_pieces), ']', end=' ')
        move = input('{} piece move? '.format(self.color))
        valid_move = self.board.move(move, self)
        return valid_move

class Game(object):
    def __init__(self):
        self.board = Board()
        self.player1 = Player('adeel', 'black', self.board)
        self.player2 = Player('jawad', 'white', self.board)
        self.turn = 0

        # todo add timer to the game


    def start(self):
        while(True):
            if self.turn == 0:
                valid_move = self.player1.play()
                if valid_move:
                    self.turn = 1
            else:
                valid_move = self.player2.play()
                if valid_move:
                    self.turn = 0

            self.show()

    def show(self):
        self.board.print_board()


g = Game()
g.show()
g.start()

