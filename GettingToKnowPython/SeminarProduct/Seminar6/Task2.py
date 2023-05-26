
#Решение 1:
def find_farthest_orbit(arr):
    max = 0
    for a, b in arr:
        if a != b:
            s = a*b
            if max < s:
                max = s
                lst = [a, b]
    
    return lst
       
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))

#Решение 2:
def find_farthest_orbit_2 (arr):
    return max(arr, key=lambda x: (x[0] != x[1]) * x[0] * x[1])

print(*find_farthest_orbit_2(orbits))