import random
from dorfperfekt.tile import string2tile, terrains2tile, tile2string
from dorfperfekt.tilemap import InvalidTilePlacementError, TileMap

# Fonction pour tester le placement aléatoire des tuiles avec rotation
def test_random_placement(tiles):
    tilemap = TileMap() 

    for tile in tiles:
        # Trouver les positions disponibles sur le TileMap
        available_positions = list(tilemap.open)
        print(f"Positions disponibles : {available_positions}")
        
        if not available_positions:
            print("Aucune position disponible sur le TileMap.")
            break

        # Choisir une position aléatoire parmi les positions disponibles
        pos = random.choice(available_positions)
        print(f"Position choisie : {pos}")

        for ori in range(6):  
            rotated_tile = terrains2tile(tile.terrains[ori: ] + tile.terrains[: ori])

            try:
                tilemap.__setitem__(pos,rotated_tile)
                print(f"Pièce placée {tile2string(rotated_tile)}, position {pos}, ori {ori}")
                t = tilemap.__getitem__(pos)
                # (tile2string(t))
            except InvalidTilePlacementError:
                print(f"Plac. Invalide pour {tile2string(rotated_tile)}, position {pos}, ori {ori}.")
                continue 

    return 0

tiles_example = [
    string2tile("wwwgww"),
]

score = test_random_placement(tiles_example)
