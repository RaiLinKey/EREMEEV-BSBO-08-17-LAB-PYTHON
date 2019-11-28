def find_farthest_orbit(orb):
    s = 0
    k = 0
    for i in orb:
        s = 3.14 * i[0] * i[1]
        if (s > k) and (i[0] != i[1]):
            maxi = orb.index(i)
            k = s
    return maxi


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
b = find_farthest_orbit(orbits)
print(orbits[b])
