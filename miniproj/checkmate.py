# checkmate.py

def _normalize_board(board_str):
    """
    แปลงสตริงหลายบรรทัดเป็นกระดานสี่เหลี่ยมผืนผ้า
    - อักขระที่ไม่ใช่ตัวหมากจะถูกแทนด้วย '.'
    - pad ให้ทุกแถวกว้างเท่ากัน
    """
    raw_rows = [row for row in board_str.splitlines() if row is not None]
    if not raw_rows:
        return None  # undefined: ไม่มีข้อมูล

    valid = set("PBRQNK")
    rows = []
    width = 0
    for r in raw_rows:
        cleaned = ''.join(ch if ch in valid else '.' for ch in r)
        rows.append(cleaned)
        width = max(width, len(cleaned))

    if width == 0:
        return None

    # pad ให้เป็นผืนผ้า
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

    pawn_attacks_up=True  -> Pawn โจมตี 'ขึ้น' (จากมุมมองกระดาน): ตำแหน่ง Pawn ที่โจมตี K จะอยู่ที่ (kr+1, kc±1)
    pawn_attacks_up=False -> Pawn โจมตี 'ลง' : ตำแหน่ง Pawn ที่โจมตี K จะอยู่ที่ (kr-1, kc±1)
    """
    rows = _normalize_board(board_str)
    if rows is None:
        return  # undefined: ไม่พิมพ์อะไร

    pos = _find_king(rows)
    if pos is None:
        return  # undefined: ไม่พบ K

    kr, kc = pos
    h, w = len(rows), len(rows[0])

    # --- Knight ---
    knight_moves = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
    for dr, dc in knight_moves:
        r, c = kr + dr, kc + dc
        if _inside(r, c, h, w) and rows[r][c] == 'N':
            print("Success")
            return

    # --- Pawn (แก้ทิศให้ถูกต้อง) ---
    # ถ้าโจมตีขึ้น: P ที่จะกิน K ต้องอยู่ "แถวถัดลงมา" จาก K = kr+1
    # ถ้าโจมตีลง:   P ต้องอยู่ "แถวถัดขึ้นไป" จาก K = kr-1
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

    # --- Rook / Queen (ตรงแนว) ---
    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        if _ray_hits(rows, kr, kc, {'R', 'Q'}, dr, dc):
            print("Success")
            return

    print("Fail")
