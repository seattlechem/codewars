# Closest Left In a Binary Tree
[github.com/kamyu104/LeetCode/blob/master/Python/closest-leaf-in-a-binary-tree.py](https://github.com/kamyu104/LeetCode/blob/master/Python/closest-leaf-in-a-binary-tree.py)
[www.geeksforgeeks.org/find-closest-leaf-binary-tree/](https://www.geeksforgeeks.org/find-closest-leaf-binary-tree/

Given a Binary Tree and a key ‘k’, find distance of the closest leaf from ‘k’.
```
Examples:

              A
            /    \    
           B       C
                 /   \  
                E     F   
               /       \
              G         H
             / \       /
            I   J     K
```
Closest leaf to 'H' is 'K', so distance is 1 for 'H'
Closest leaf to 'C' is 'B', so distance is 2 for 'C'
Closest leaf to 'E' is either 'I' or 'J', so distance is 2 for 'E' 
Closest leaf to 'B' is 'B' itself, so distance is 0 for 'B' 
