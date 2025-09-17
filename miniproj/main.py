from checkmate import checkmate
# success = K โดนกิน
def main():
    # Example 1 (จากภาพ)
    board = """\
            R...
            .K..
            ..P.
            ....\
            """
    checkmate(board)
    
    board2 = """\
            ..
            .K\
            """
    checkmate(board2)  # คาดว่า "Fail"
    
    print("# 1) Rook ตรงคอลัมน์ (Success)")
    board = """\
            .R.
            .K.
            ...\
            """
    checkmate(board)

    print("# 2) Rook มี Pawn ขวาง (Fail)")
    board = """\
            RPK
            ...
            ...\
            """
    checkmate(board)

    print("# 3) Bishop ทแยงไม่ถูกบล็อก (Success)")
    board = """\
            B..
            .K.
            ...\
            """
    checkmate(board)

    print("# 4) Bishop ถูกบล็อกโดย Pawn (Fail)")
    board = """\
            B..
            .P.
            ..K\
            """
    checkmate(board)

    print("# 5) Queen โจมตีทแยง (Success)")
    board = """\
            Q..
            .K.
            ...\
            """
    checkmate(board)

    print("# 6) Knight โจมตี (Success)")
    board = """\
            N..
            ...
            .K.\
            """
    checkmate(board)

    print("# 7) Pawn โจมตีขึ้น (Success)")
    board = """\
            ...
            .K.
            ..P\
            """
    checkmate(board)

    print("# 8) Pawn ใต้คิงแต่ไม่ทแยง (Fail)")
    board = """\
            ...
            .K.
            .P.\
            """
    checkmate(board)

    print("# 9) กระดานสี่เหลี่ยมผืนผ้า 2x3 (Success)")
    board = """\
            R.K
            ...\
            """
    checkmate(board)

    print("# 10) อักขระแปลกถือเป็นช่องว่าง (Success)")
    board = """\
            R\K\
            """
    checkmate(board)

    print("# 11) Queen ชนมุมคิง (Success)")
    board = """\
            K...
            .Q..\
            """
    checkmate(board)

    print("# 12) ไม่มีศัตรู (Fail)")
    board = """\
            ...
            .K.
            ...\
            """
    checkmate(board)

    print("# 13) Bishop หลัง Pawn (Fail – กฎ “ชนชิ้นแรก”)")
    board = """\
            ....
            .K..
            ..P.
            ...B\
            """
    checkmate(board)

    print("# 14) Queen แต่มี Pawn ขวางในคอลัมน์ (Fail)")
    board = """\
            .Q.
            .P.
            .K.\
            """
    checkmate(board)

    print("# 15) Knight ใกล้ขอบ บอร์ด 3x2 (Success)")
    board = """\
            K.
            ..
            .N\
            """
    checkmate(board)
    
    print("tin")
    board = """\
        Q...
        .R..
        ..K.\
        """
    checkmate(board)

    
if __name__ == "__main__":
    main()