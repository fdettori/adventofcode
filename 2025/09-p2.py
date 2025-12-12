"""
--- Part Two ---

The Elves just remembered: they can only switch out tiles that are red or green. So, your rectangle can only include red or green tiles.

In your list, every red tile is connected to the red tile before and after it by a straight line of green tiles. The list wraps, so the first red tile is also connected to the last red tile. Tiles that are adjacent in your list will always be on either the same row or the same column.

Using the same example as before, the tiles marked X would be green:

..............
.......#XXX#..
.......X...X..
..#XXXX#...X..
..X........X..
..#XXXXXX#.X..
.........X.X..
.........#X#..
..............

In addition, all of the tiles inside this loop of red and green tiles are also green. So, in this example, these are the green tiles:

..............
.......#XXX#..
.......XXXXX..
..#XXXX#XXXX..
..XXXXXXXXXX..
..#XXXXXX#XX..
.........XXX..
.........#X#..
..............

The remaining tiles are never red nor green.

The rectangle you choose still must have red tiles in opposite corners, but any other tiles it includes must now be red or green. This significantly limits your options.

For example, you could make a rectangle out of red and green tiles with an area of 15 between 7,3 and 11,1:

..............
.......OOOOO..
.......OOOOO..
..#XXXXOOOOO..
..XXXXXXXXXX..
..#XXXXXX#XX..
.........XXX..
.........#X#..
..............

Or, you could make a thin rectangle with an area of 3 between 9,7 and 9,5:

..............
.......#XXX#..
.......XXXXX..
..#XXXX#XXXX..
..XXXXXXXXXX..
..#XXXXXXOXX..
.........OXX..
.........OX#..
..............

The largest rectangle you can make in this example using only red and green tiles has area 24. One way to do this is between 9,5 and 2,3:

..............
.......#XXX#..
.......XXXXX..
..OOOOOOOOXX..
..OOOOOOOOXX..
..OOOOOOOOXX..
.........XXX..
.........#X#..
..............

Using two red tiles as opposite corners, what is the largest area of any rectangle you can make using only red and green tiles?
"""

import itertools

def solve_part_two_optimized():
    # Leggi il file
    with open('2025/09.txt', 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    # Parsing delle coordinate (lista ordinata che forma il poligono)
    poly_points = []
    for line in lines:
        x, y = map(int, line.split(','))
        poly_points.append((x, y))

    # Creiamo una lista di segmenti del poligono per controlli veloci
    # Ogni segmento è ((x1, y1), (x2, y2), is_vertical)
    segments = []
    num_points = len(poly_points)
    for i in range(num_points):
        p1 = poly_points[i]
        p2 = poly_points[(i + 1) % num_points] # Collega l'ultimo al primo
        
        is_vert = (p1[0] == p2[0])
        # Normalizziamo il segmento (dal minore al maggiore) per facilitare i calcoli
        if is_vert:
            seg = (p1[0], min(p1[1], p2[1]), max(p1[1], p2[1]), True)
        else:
            seg = (min(p1[0], p2[0]), max(p1[0], p2[0]), p1[1], False)
        segments.append(seg)

    max_area = 0

    # Funzione per verificare se un rettangolo è valido
    def is_valid_rect(rx1, rx2, ry1, ry2):
        # Normalizza coordinate rettangolo
        rmin_x, rmax_x = min(rx1, rx2), max(rx1, rx2)
        rmin_y, rmax_y = min(ry1, ry2), max(ry1, ry2)

        # 1. CONTROLLO INTERSEZIONI (Il poligono taglia il rettangolo?)
        for (s1, s2, s3, is_vert) in segments:
            if is_vert: # Segmento Poligono Verticale: x fisso = s1, y da s2 a s3
                vx, vy_min, vy_max = s1, s2, s3
                # Se la linea verticale è STRETTAMENTE dentro la X del rettangolo
                if rmin_x < vx < rmax_x:
                    # E se le Y si sovrappongono
                    if max(rmin_y, vy_min) < min(rmax_y, vy_max): 
                        return False
            else: # Segmento Poligono Orizzontale: x da s1 a s2, y fisso = s3
                hx_min, hx_max, hy = s1, s2, s3
                # Se la linea orizzontale è STRETTAMENTE dentro la Y del rettangolo
                if rmin_y < hy < rmax_y:
                    # E se le X si sovrappongono
                    if max(rmin_x, hx_min) < min(rmax_x, hx_max):
                        return False

        # 2. CONTROLLO PUNTO INTERNO (Ray Casting)
        # Prendiamo il punto centrale esatto del rettangolo
        cx = (rmin_x + rmax_x) / 2.0
        cy = (rmin_y + rmax_y) / 2.0

        # Prima controlliamo se il centro è esattamente SU un bordo (caso rettangoli sottili)
        on_boundary = False
        for (s1, s2, s3, is_vert) in segments:
            if is_vert:
                # x coincide e y è nel range
                if abs(cx - s1) < 0.0001 and s2 <= cy <= s3:
                    on_boundary = True; break
            else:
                # y coincide e x è nel range
                if abs(cy - s3) < 0.0001 and s1 <= cx <= s2:
                    on_boundary = True; break
        
        if on_boundary:
            return True

        # Se non è sul bordo, facciamo Ray Casting verso destra
        # Contiamo quanti segmenti verticali attraversiamo
        intersections = 0
        for (vx, vy_min, vy_max, is_vert) in segments:
            if is_vert:
                # Il segmento è a destra del punto E copre la Y del punto
                if vx > cx and vy_min <= cy < vy_max:
                    intersections += 1
        
        # Dispari = Dentro, Pari = Fuori
        return (intersections % 2 == 1)

    # Iteriamo tutte le coppie
    for p1, p2 in itertools.combinations(poly_points, 2):
        x1, y1 = p1
        x2, y2 = p2

        # Calcolo Area (Inclusiva)
        width = abs(x1 - x2) + 1
        height = abs(y1 - y2) + 1
        area = width * height

        # Ottimizzazione: Se l'area è minore del record attuale, inutile controllare
        if area <= max_area:
            continue

        # Verifica geometrica
        if is_valid_rect(x1, x2, y1, y2):
            max_area = area

    print("Largest rectangle area (Part 2):", max_area)

if __name__ == "__main__":
    solve_part_two_optimized()