# f2l_db - Jakob Burkett

## Installation
- I used python 3.10.12
- Clone repo
- ```pip3 install sqlite3 ```
  - I think that's the only package requirement
- python3 f2l_db.py

## Usage
- Currently, usage is very strict
- Menus allow most inputs, I think
- Cube states must use Speffz notation (8 lowercase letters a-x)
- Solutions must use capital letters for all rotations and slice turns
- Solutions can not use 2' moves (ex. R2') - use R2 instead. They're equivalent, don't be fancy.
- Solution moves must have spaces between moves.
- Breaking these "rules" may result in the program closing with an error.
- Use Roofpig by Lars Petrus to display solutions (https://jsfiddle.net/dc2xvsrm/63/)

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
 - Task 2 (100%): Make Python command line interface for inserting into the database (I expect to be done with this by the midterm report)
 - Task 3 (100%): Insert cases I know into the database
 - Task 4 (100%): Make the Python interface able to “search” for cases based on if they contain a similarity or number of F2L slots
 - Task 5 (100%): Work on generation of cases and solutions OR create a visualization of the cube faces (possibly using Roofpig https://github.com/larspetrus/Roofpig or generating the images with Python and then storing them in the database)
   - I chose the generation. Generation occurs when manual entries are made.
