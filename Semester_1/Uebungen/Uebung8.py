

x = input("\n Wie viele Damen soll Problem gelöst sein?")

N = int(x)
board = [-1] * N

def drucke_brett():
    print(f"\nProblem lösung mit {N} Damen:")
    for zeile in range(N):
        text = ""
        for spalte in range(N):
            if board[zeile] == spalte:
                text += " Q "
            else:
                text += " . "
        print(text)
    print("-" * (N * 3))

def ist_sicher(zeile, spalte):
    for i in range(zeile):
        if board[i] == spalte:
            return False
        if abs(board[i] - spalte) == abs(i - zeile):
            return False
    return True

def platziere_dame(zeile):
    if zeile == N:
        drucke_brett()
        return True

    for spalte in range(N):
        if ist_sicher(zeile, spalte):
            board[zeile] = spalte
            
            if platziere_dame(zeile + 1):
                return True
            
            board[zeile] = -1
            
    return False

platziere_dame(0)