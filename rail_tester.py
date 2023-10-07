from rail_lib import Rail
file = "grey_mine_route.txt"
r = Rail(file, False)
while r.advance():
    pass