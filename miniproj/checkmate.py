# checkmate.py

def _normalize_board(board_str):
    """
    แปลงสตริงหลายบรรทัดเป็น 'กระดานสี่เหลี่ยมจัตุรัส'
    - อักขระที่ไม่ใช่ตัวหมาก (P,B,R,Q,N,K) จะถูกแทนด้วย '.'
    - ตัดช่องว่างหัว/ท้ายของแต่ละบรรทัด เพื่อกันกรณี indent จาก triple-quote
    - ถ้าไม่ใช่สี่เหลี่ยมจัตุรัส ให้คืนค่า "invalid"
    - ถ้าไม่มีข้อมูล ให้คืนค่า None
    """
    if board_str is None:
        return None

    lines = board_str.strip("\n").splitlines()
    if not lines:
        return None

    valid = set("PBRQNK")
    rows = []
    width = 0
    for line in lines:
        line = line.strip()  # กัน indent
        cleaned = ''.join(ch if ch in valid else '.' for ch in line)
        rows.append(cleaned)
        width = max(width, len(cleaned))

    # check ขนาดของ board
    height = len(rows)
    if width != height or width == 0:
        return "invalid"

    # pad ให้แต่ละแถวกว้างเท่ากัน (ความยาวเท่ากับ width)
    rows = [r.ljust(width, '.') for r in rows]
    return rows


def _find_king(rows):
    for r, line in enumerate(rows):
        c = line.find('K')
        if c != -1:
            return r, c
    return None


def _inside(r, c, h, w):
    return 0 <= r < h and 0 <= c < w


def _ray_hits(rows, kr, kc, attackers, dr, dc):
    h, w = len(rows), len(rows[0])
    r, c = kr + dr, kc + dc
    while _inside(r, c, h, w):
        ch = rows[r][c]
        if ch != '.':                  # ชนชิ้นแรก = ตัวบล็อก
            return ch in attackers     # ใช่ตัวโจมตีที่ยิงตามแกนนี้หรือไม่
        r += dr
        c += dc
    return False


def checkmate(board_str, pawn_attacks_up=True):
    """
    พิมพ์ "Success" ถ้า King ('K') ถูกเช็คโดยศัตรู (P,B,R,Q,N)
    ไม่เช่นนั้นพิมพ์ "Fail"

    เคสพิเศษ:
      - ถ้าบอร์ดไม่ใช่สี่เหลี่ยมจัตุรัส: พิมพ์ "invalid board" แล้ว return
      - ถ้าไม่มีข้อมูล/ไม่พบ K: เงียบ ๆ return

    หมายเหตุ Pawn:
      - pawn_attacks_up=True  : Pawn โจมตี 'ขึ้น' จากมุมมองตำแหน่ง K
                                => Pawn ที่จะกิน K ต้องอยู่ที่ (kr+1, kc±1)
      - pawn_attacks_up=False : Pawn โจมตี 'ลง'
                                => Pawn ที่จะกิน K ต้องอยู่ที่ (kr-1, kc±1)
    """
    rows = _normalize_board(board_str)
    if rows is None:
        return
    # return invalid board เมื่อ invalid
    if rows == "invalid":
        print("invalid board")
        return

    pos = _find_king(rows)
    if pos is None:
        return

    kr, kc = pos
    h, w = len(rows), len(rows[0])

    # --- Knight ---
    knight_moves = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
    for dr, dc in knight_moves:
        r, c = kr + dr, kc + dc
        if _inside(r, c, h, w) and rows[r][c] == 'N':
            print("Success")
            return

    # --- Pawn ---
    step = 1 if pawn_attacks_up else -1
    for dc in (-1, 1):
        r, c = kr + step, kc + dc
        if _inside(r, c, h, w) and rows[r][c] == 'P':
            print("Success")
            return

    # --- Bishop / Queen (ทแยง) ---
    for dr, dc in [(-1,-1),(-1,1),(1,-1),(1,1)]:
        if _ray_hits(rows, kr, kc, {'B', 'Q'}, dr, dc):
            print("Success")
            return

    # --- Rook / Queen (แนวตรง) ---
    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        if _ray_hits(rows, kr, kc, {'R', 'Q'}, dr, dc):
            print("Success")
            return

    print("Fail")
