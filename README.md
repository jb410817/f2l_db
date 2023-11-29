 # f2l_db - Jakob Burkett

## Database/Hosting Information
- Database is currently not hosted.
- Using SQLite3 for now
    - Would like to use MongoDB, but I'm not learning about clusters and hosting right now
## Cube Information in db

The CubeState table stores the position of each of the f2l pieces. This table uses the Speffz blind notation for labeling.

The corners location is indicated by the location of the bottom colors sticker. The edges locations are indicated by the front and back colors stickers.

The cube_id attribute is a string of all the positions of the pieces in the order:

DRF + FR + DFL + FL + DLB + BL + DBR + BR

Solved id: vjulxrwt

The next_id in the Solutions table points to another cases cube_id if the first
case can be transformed into another. Ex: case jbulxrwt = U + fculxrwt = R U R'

The y, y_prime, and y2 attributes have the id of the cube when that rotation is performed. Ex: vjfixrwt = Y' + jbulxrwt

The mirror attribute stores the id of the cube in the mirror position

## Milestones + Progress
 - Task 1 (100%): Create diagrams and the database
 - Task 2: Make Python command line interface for inserting into the database (I expect to be done with this by the midterm report)
 - Task 3: Insert cases I know into the database
 - Task 4: Make the Python interface able to “search” for cases based on if they contain a similarity or number of F2L slots
 - Task 5: Work on generation of cases and solutions OR create a visualization of the cube faces (possibly using Roofpig https://github.com/larspetrus/Roofpig or generating the images with Python and then storing them in the database) 
