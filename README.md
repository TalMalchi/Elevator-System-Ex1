## ObjectOriented_2021_Ex1


# Object-Oriented Programming-Task Number 1- Part 1:

![Elevator1](https://user-images.githubusercontent.com/93086649/141957290-3393d480-9653-4597-814c-770febf18583.jpg)

***The Most Relevant Links we saw during our work:***
- https://www.youtube.com/watch?v=xOayymoIl8U
- https://www.youtube.com/watch?v=siqiJAJWUVg
- https://thinksoftware.medium.com/elevator-system-design-a-tricky-technical-interviewquestion-116f396f2b1c
- https://elevation.fandom.com/wiki/Destination_dispatch#System_principle
- https://everythingwhat.com/what-is-a-destination-oriented-elevator
- https://peters-research.com/index.php/papers/understanding-the-benefits-and-limitations-of-
 /destination-control

***what is the problem?***  
we have 2 files:  
- json file- represnt a building 
- csv file with new calls      
for each new call, we have to choose the eleavtor with the minmum time to complete the call .   
The output will be the same input file, but with the allocate elevator.

***How we face it?***   
  *in the beginning* - we created a building from each json file.
we read the csv file and add each call to list of calls of the building.  
*Next* - we create new out put file, and for each call, we allocate the best elevator with the shortest time


***Off-line Algoritem:***   
*before each call:*   
  we go throw all the elevators in the building:
  - calculate the time with all the stops the elevator already have
  - add the new call to temp_list_calls
  - calculate the whole route time include the new stops
  - allocate the elevator with the shorest time
 - Each elevator move over all the floors in the ‘calls’ list.  



![image](https://user-images.githubusercontent.com/93086649/142676721-20abad35-64aa-4c2d-a753-ee223a2e6d94.png)
