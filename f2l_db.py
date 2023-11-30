import sqlite3

# Connect to the database
con = sqlite3.connect('f2l.db')
cursor = con.cursor()

# rotates the cube clockwise 90 degrees some number of times using Speffz notation
def rotate_cube(times, state):
    print("Rotating state (" + state + ") " + str(times) + " times...")
    # Speffz notation dictionary
    rotate_map = {
        "a": "b", "b": "c", "c": "d", "d": "a",
        "e": "q", "f": "r", "g": "s", "h": "t",
        "i": "e", "j": "f", "k": "g", "l": "h",
        "m": "i", "n": "j", "o": "k", "p": "l",
        "q": "m", "r": "n", "s": "o", "t": "p",
        "u": "x", "v": "u", "w": "v", "x": "w",
    }

    aux = ""
    result = state

    # rotate the cube
    for i in range(times):
        aux = ""
        # for each position, set the result to the rotated position
        for pos in result:
            aux += rotate_map[pos]
        result = aux
    print("Result: " + result)
    return result

# mirrors the cube (left and right swap)
def mirror_cube(state):
    # Speffz notation mirroring arrays
    # corners and edges are mirrored separately - corner b -> corner a, edge b -> edge d
    # corners
    corners_map = {
        "a": "b", "b": "a", "c": "d", "d": "c",
        "e": "n", "f": "m", "g": "p", "h": "o",
        "i": "j", "j": "i", "k": "l", "l": "k",
        "m": "f", "n": "e", "o": "h", "p": "g",
        "q": "r", "r": "q", "s": "t", "t": "s",
        "u": "v", "v": "u", "w": "x", "x": "w",
    }

    edges_map = {
        "a": "a", "b": "d", "c": "c", "d": "b",
        "e": "m", "f": "p", "g": "o", "h": "n",
        "i": "i", "j": "l", "k": "k", "l": "j",
        "m": "e", "n": "h", "o": "g", "p": "f",
        "q": "q", "r": "t", "s": "s", "t": "r",
        "u": "u", "v": "x", "w": "w", "x": "v",
    }
    
    result = ""

    # for each position, set the result to the mirror position
    for pos in range(0, len(state), 2):
        # corner first
        current = state[pos]
        result += corners_map[current]
        
        # now edges
        pos += 1
        current = state[pos]
        result += edges_map[current]
        
    return result

# rotates the solution 90 degrees some number of times using standard FBRLUD notation
def rotate_solution(times, solution):
    # map for rotation
    move_map = {
        # normal turns
        # F -> L, L -> B, B -> R, R -> F, U -> U, D -> D
        # F
        "F": "L", "F'": "L'", "F2": "L2",
        # L
        "L": "B", "L'": "B'", "L2": "B2",
        # B
        "B": "R", "B'": "R'", "B2": "R2",
        # R
        "R": "F", "R'": "F'", "R2": "F2",
        # U
        "U": "U", "U'": "U'", "U2": "U2",
        # D
        "D": "D", "D'": "D'", "D2": "D2",

        # rotations
        # X -> Z, Y -> Y, Z -> X'
        "X": "Z", "X'": "Z'", "X2": "Z2",
        "Y": "Y", "Y'": "Y'", "Y2": "Y2",
        "Z": "X'", "Z'": "X", "Z2": "X2",

        # slice turns
        # E -> E, M -> S', S -> M
        "E": "E", "E'": "E'", "E2": "E2",
        "M": "S'", "M2": "S2", "M'": "S",
        "S": "M", "S'": "M'", "S2": "M2",

        # wide turns
        # f -> l, l -> b, b -> r, r -> f, u -> u, d -> d
        "f": "l", "f'": "l'", "f2": "l2",
        "l": "b", "l'": "b'", "l2": "b2",
        "b": "r", "b'": "r'", "b2": "r2",
        "r": "f", "r'": "f'", "r2": "f2",
        "u": "u", "u'": "u'", "u2": "u2",
        "d": "d", "d'": "d'", "d2": "d2",
    }

    aux = ""
    result = solution
    for i in range(times):
        aux = ""
        for turn in result.split():
            aux += move_map[turn] + " "
        result = aux
    return result.strip()

# mirrors the solution horizontally
def mirror_solution(solution):
    mirror_map = {
        # normal turns
        "F": "F'", "F'": "F", "F2": "F2",
        "L": "R'", "L'": "R", "L2": "R2",
        "B": "B'", "B'": "B", "B2": "B2",
        "R": "L'", "R'": "L", "R2": "L2",
        "U": "U'", "U'": "U", "U2": "U2",
        "D": "D'", "D'": "D", "D2": "D2",
        # rotations
        "X": "X'", "X'": "X", "X2": "X2",
        "Y": "Y'", "Y'": "Y", "Y2": "Y2",
        "Z": "Z'", "Z'": "Z", "Z2": "Z2",
        # slice turns
        "E": "E'", "E'": "E", "E2": "E2",
        "M": "M", "M'": "M'", "M2": "M2",
        "S": "S'", "S'": "S", "S2": "S2",
        # wide turns
        "f": "f'", "f'": "f", "f2": "f2",
        "l": "r'", "l'": "r", "l2": "r2",
        "b": "b'", "b'": "b", "b2": "b2",
        "r": "l'", "r'": "l", "r2": "l2",
        "u": "u'", "u'": "u", "u2": "u2",
        "d": "d'", "d'": "d", "d2": "d2",
    }
    
    result = ""
    for turn in solution.split():
        result += mirror_map[turn] + " "
    
    return result.strip()

# Define your command line interface functions
def create_tables():
    # Print the status of pragma foreign_keys
    cursor.execute("PRAGMA foreign_keys")
    status = cursor.fetchone()[0]
    print("Foreign keys status: ", status)

    # Create a table in the database
    cursor.execute("CREATE TABLE IF NOT EXISTS "
                   "cube_state(cube_id primary key, fr_corner, fr_edge, fl_corner, fl_edge, "
                   "bl_corner, bl_edge, br_corner, br_edge, y, y_prime, y2, mirror)")
    cursor.execute("CREATE TABLE IF NOT EXISTS " 
                   "related_states(cube_id, ref, "
                   "FOREIGN KEY (cube_id) REFERENCES cube_state(cube_id))")
    cursor.execute("CREATE TABLE IF NOT EXISTS solutions "
                   " (cube_id REFERENCES cube_state(cube_id), solution, solution_id primary key, move_count, next_id)")
    cursor.execute("CREATE TABLE IF NOT EXISTS solution_tags "
                   "(solution_id REFERENCES solutions(solution_id), one_slot, adj_slots, diag_slots, three_slots, all_slots, weight)")

# insert a cube state into the cube_state table
def insert_cube_state(cube_pos):
    cube_id = cube_pos
    cube_y = rotate_cube(1, cube_pos)
    cube_y_prime = rotate_cube(3, cube_pos)
    cube_y2 = rotate_cube(2, cube_pos)
    cube_mirror = mirror_cube(cube_pos)
    cube_mirror_y = rotate_cube(1, cube_mirror)
    cube_mirror_y_prime = rotate_cube(3, cube_mirror)
    cube_mirror_y2 = rotate_cube(2, cube_mirror)
    cubes_list = [cube_pos, cube_y, cube_y_prime, cube_y2, cube_mirror, cube_mirror_y, cube_mirror_y_prime, cube_mirror_y2]

    data = []
    for cube in cubes_list:
        data.append(
            (
                cube, cube[0], cube[1], cube[2], cube[3], cube[4], cube[5], cube[6], cube[7],
                rotate_cube(1, cube), rotate_cube(3, cube), rotate_cube(2, cube), mirror_cube(cube)
            )
            )
        
    cursor.executemany("INSERT INTO cube_state VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
    con.commit()

def retrieve_data():
    # Retrieve data from the table
    # cursor.execute("SELECT * FROM your_table")
    # rows = cursor.fetchall()
    # for row in rows:
    print("Retrieving data...")

def print_menu():
    print("~ ~ ~ Main Menu ~ ~ ~")
    print("1. Insert F2L Case")
    print("2. Retrieve Solutions")
    print("3. Exit")
    choice = input("Enter your choice: ")
    return choice

# Run your command line interface
if __name__ == '__main__':
    create_tables()
    print ("Welcome to the F2L database!")
    choice = "CONTINUE"
    while(choice.lower() != "exit" and choice != "3"):
        choice = print_menu()
        if choice == '1':
            cube_pos = input("Enter cube position: ")
            solution = input("Enter solution: ")
            insert_cube_state(cube_pos)
        elif choice == '2':
            retrieve_data()

# Close the database connection
con.close()
