import sqlite3

# Connect to the database
con = sqlite3.connect('f2l.db')
cursor = con.cursor()

# rotates the cube clockwise 90 degrees some number of times using Speffz notation
def rotate_cube(times, state):
    # Speffz notation dictionary
    corner_map = {
        "a": "b", "b": "c", "c": "d", "d": "a",
        "e": "q", "f": "r", "g": "s", "h": "t",
        "i": "e", "j": "f", "k": "g", "l": "h",
        "m": "i", "n": "j", "o": "k", "p": "l",
        "q": "m", "r": "n", "s": "o", "t": "p",
        "u": "x", "v": "u", "w": "v", "x": "w",
    }
    edge_map = {
        "a": "m", "b": "i", "c": "e", "d": "q",
        "e": "a", "f": "h", "g": "w", "h": "n",
        "i": "d", "j": "l", "k": "x", "l": "r",
        "m": "c", "n": "p", "o": "u", "p": "f",
        "q": "b", "r": "t", "s": "v", "t": "j",
        "u": "g", "v": "k", "w": "o", "x": "s",
    }

    aux = ""
    result = state

    # rotate the cube
    for i in range(times):
        aux = ""
        # for each position, set the result to the rotated position
        for pos in range(0, len(result), 2):
            aux += corner_map[result[pos]] + edge_map[result[(pos + 1)]]
        result = aux[6:8] + aux[0:6]
    return result

# mirrors the cube (left and right swap)
def mirror_cube(state):
    # Speffz notation mirroring arrays
    # corners and edges are mirrored separately - corner b -> corner a, edge b -> edge d
    # corners
    corner_map = {
        "a": "b", "b": "a", "c": "d", "d": "c",
        "e": "n", "f": "m", "g": "p", "h": "o",
        "i": "j", "j": "i", "k": "l", "l": "k",
        "m": "f", "n": "e", "o": "h", "p": "g",
        "q": "r", "r": "q", "s": "t", "t": "s",
        "u": "v", "v": "u", "w": "x", "x": "w",
    }

    edge_map = {
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
        result += corner_map[current]
        
        # now edges
        pos += 1
        pos = pos % len(edge_map)
        current = state[pos]
        result += edge_map[current]
        
    return result[2:4] + result[0:2] + result[6:8] + result[4:6]

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
    cursor.execute("PRAGMA foreign_keys = ON")

    # Create a table in the database
    cursor.execute("CREATE TABLE IF NOT EXISTS cube_state (\
                    cube_id TEXT primary key ON CONFLICT IGNORE NOT NULL, \
                    fr_corner text, fr_edge text, fl_corner text, fl_edge text, \
                    bl_corner text, bl_edge text, br_corner text, br_edge text, y text, y_prime text, y2 text, mirror text)")
    cursor.execute("CREATE TABLE IF NOT EXISTS related_states(\
                    cube_id text, ref text, \
                    UNIQUE (cube_id, ref), \
                    FOREIGN KEY (cube_id) REFERENCES cube_state(cube_id))")
    cursor.execute("CREATE TABLE IF NOT EXISTS solutions (\
                    cube_id text NOT NULL REFERENCES cube_state(cube_id), solution text, move_count int, weight int, \
                    PRIMARY KEY (cube_id, solution))")
    cursor.execute("CREATE TABLE IF NOT EXISTS cube_tags (\
                    cube_id text NOT NULL, one_slot boolean, adj_slots boolean, diag_slots boolean, \
                    three_slots boolean, all_slots boolean, \
                    FOREIGN KEY (cube_id) REFERENCES cube_state(cube_id), \
                    PRIMARY KEY (cube_id) ON CONFLICT IGNORE)")

# insert a solution into the solutions table
def insert_solution(cube_pos, solution):
    valid_chars = ["F", "L", "B", "R", "U", "D", "X", "Y", "Z", "E", "M", "S", "f", "l", "b", "r", "u", "d", "'", " ", "2"]
    cube_id = cube_pos
    state_solutions = {
        cube_id: solution,
        rotate_cube(1, cube_id): rotate_solution(1, solution),
        rotate_cube(2, cube_id): rotate_solution(2, solution),
        rotate_cube(3, cube_id): rotate_solution(3, solution),
        mirror_cube(cube_id): mirror_solution(solution),
        rotate_cube(1, mirror_cube(cube_id)): rotate_solution(1, mirror_solution(solution)),
        rotate_cube(2, mirror_cube(cube_id)): rotate_solution(2, mirror_solution(solution)),
        rotate_cube(3, mirror_cube(cube_id)): rotate_solution(3, mirror_solution(solution)),
    }
    
    for state, sol in state_solutions.items():
        valid_move_check = [i for i in sol if i not in valid_chars]
        if len(valid_move_check) > 0:
            print("Solution " + sol + " for state " + state + " is invalid. Please check the solution and try again.")
            continue
        move_count = len(sol.split())
        weight = 1
        if sol == "":
            sol = "SOLVED"
        try:
            cursor.execute("INSERT INTO solutions VALUES (?, ?, ?, ?)", (state, sol, move_count, weight))
        except sqlite3.IntegrityError:
            print("Solution " + sol + " is already in the database for state " + state + ". Weight increased by 1.")
            cursor.execute("UPDATE solutions SET weight = weight + 1 WHERE cube_id = ? AND solution = ?", (state, sol))
        except:
            print("Error inserting solution " + sol + " for state " + state + ". Please check the solution and try again.")
            continue
    con.commit()

# insert a cube state into the cube_state table
def insert_cube_state(cube_pos):
    cube_id = cube_pos

    cube_y = rotate_cube(1, cube_id)
    cube_y_prime = rotate_cube(3, cube_id)
    cube_y2 = rotate_cube(2, cube_id)
    cube_mirror = mirror_cube(cube_id)
    cube_mirror_y = rotate_cube(1, cube_mirror)
    cube_mirror_y_prime = rotate_cube(3, cube_mirror)
    cube_mirror_y2 = rotate_cube(2, cube_mirror)
    cubes_list = [cube_id, cube_y, cube_y_prime, cube_y2, cube_mirror, cube_mirror_y, cube_mirror_y_prime, cube_mirror_y2]

    data = []
    for cube in cubes_list:
        data.append(
            (
                cube, cube[0], cube[1], cube[2], cube[3], cube[4], cube[5], cube[6], cube[7],
                rotate_cube(1, cube), rotate_cube(3, cube), rotate_cube(2, cube), mirror_cube(cube)
            )
            )
    try:
        cursor.executemany("INSERT INTO cube_state VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
    except sqlite3.IntegrityError:
        print("At least one of the cube states already exists in the database: ") 
        print([cube[0] for cube in data])
    except:
        print("Error inserting state " + [cube[0] for cube in data] + ". Please check the solution and try again.")
    
    # insert related states
    for cube in cubes_list:
        try:
            cursor.executemany("INSERT INTO related_states VALUES (?, ?)", [(cube, other_cube) for other_cube in cubes_list if other_cube != cube])
        except sqlite3.IntegrityError:
            continue
        except:
            print("Error inserting related states for state " + cube + ". Please check the input and try again.")
            continue

    for i in cubes_list:
        insert_cube_tags(i)
    
    con.commit()

# insert cube tags into the cube_tags table
def insert_cube_tags(cube_pos):
    cube_id = cube_pos
    # vjulxrwt
    # which states are unsolved?
    pair1 = not(cube_id[0:2] == "vj")
    pair2 = not(cube_id[2:4] == "ul")
    pair3 = not(cube_id[4:6] == "xr")
    pair4 = not(cube_id[6:8] == "wt")
    one_slot = (pair1 + pair2 + pair3 + pair4) == 1
    # checks if 1 and 2, 2 and 3, 3 and 4, or 4 and 1 are unsolved
    adj_slots = (pair1 and pair2) ^ (pair2 and pair3) ^ (pair3 and pair4) ^ (pair4 and pair1)
    diag_slots = (pair1 and pair3) ^ (pair2 and pair4)
    three_slots = (pair1 + pair2 + pair3 + pair4) == 3
    all_slots = (pair1 + pair2 + pair3 + pair4) == 4
    
    try:
        cursor.execute("INSERT INTO cube_tags VALUES (?, ?, ?, ?, ?, ?)", (cube_id, one_slot, adj_slots, diag_slots, three_slots, all_slots))
    except sqlite3.IntegrityError:
        print("Cube tags for state " + cube_id + " already exist in the database.")
    except:
        print("Error inserting cube tags for state " + cube_id + ". Please check input and try again.")

def retrieve_data():
    # Retrieve data from the table
    # cursor.execute("SELECT * FROM your_table")
    # rows = cursor.fetchall()
    # for row in rows:
    print("Retrieving data...")

def print_menu():
    print("\n\n~ ~ ~ Main Menu ~ ~ ~")
    print("1. Insert F2L Case")
    print("2. Retrieve Solutions")
    print("3. Exit")
    choice = input("Enter your choice: ")
    return choice

def clean_state(state):
    solved = "vjulxrwt"
    cube_id = state
    # replace placeholders with solved values
    for i in range(0, len(cube_id)):
        if cube_id[i] == "z" or cube_id[i] == "Z" or cube_id[i] == " ":
            cube_id = cube_id[:i] + solved[i] + cube_id[i+1:]
    return cube_id

# Run your command line interface
if __name__ == "__main__":
    create_tables()
    print ("Welcome to the F2L database!")
    choice = "CONTINUE"
    while(choice.lower() != "exit" and choice != "3"):
        choice = print_menu()
        if choice == '1':
            cube_pos = clean_state(input("Enter cube position: "))
            solution = input("Enter solution: ")
            insert_cube_state(cube_pos)
            insert_solution(cube_pos, solution)
        elif choice == '2':
            retrieve_data()

# Close the database connection
con.close()
