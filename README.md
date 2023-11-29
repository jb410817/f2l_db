# f2l_db - Jakob Burkett

## Database/Hosting Information
- Database is currently not hosted.
- Using SQLite3 for now
    - Would like to use MongoDB, but I'm not learning about clusters and hosting right now
## Cube Information in db

The CubeState table stores the position of each of the f2l pieces. 0 means the
piece is in its solved position. Otherwise, the position of the bottom
sticker for corners and the front or back sticker for edges, is a number.
Starting on the UBL and UB positions for 1, then clockwise increasing by
one. Then, the front face starts at 5 on the FUL and FU positions. The right
side then starts at 9, the back at 13, the left at 17, and the bottom at 21.

The cube_id attribute is determined by starting at the solved position, then
FDR corner rotates, then the FR edge, then each slot clockwise from the top.

The next_id in the Solutions table points to another cases cube_id if the first
case has multiple slots being solved for and the initial solution only solved
one.

## Milestones + Progress
 - Task 1 (100%): Create diagrams and the database
 - Task 2: Make Python command line interface for inserting into the database (I expect to be done with this by the midterm report)
 - Task 3: Insert cases I know into the database
 - Task 4: Make the Python interface able to “search” for cases based on if they contain a similarity or number of F2L slots
 - Task 5: Work on generation of cases and solutions OR create a visualization of the cube faces (possibly using Roofpig https://github.com/larspetrus/Roofpig or generating the images with Python and then storing them in the database) 
