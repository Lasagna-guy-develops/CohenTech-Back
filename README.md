Hey! Welcome to my technical work for the position as full-stack

I wasn't sure if there was a need to build something in the front end. Sorry if I missed it

The code in here works as follows:

1. Everything was structured as a tree, a single root for all the hierarchy
   and nodes which can handle n children

2. In the node Employee class (Structure/node.py) there's a definition for the variables the object
   contains and the functions required to "recursively" get information about the hierarchy.
   (the class was defined to work as a dict in order to facilitate conversion to json)
    
3. In the Tree class (Structure/tree.py) there's a list of all the nodes included in the hierarchy,
   a secondary list to store unsupervised nodes and a root node variable to store the head of the
   hierarchy. The functions defined in there help to workout needs around the tree.

4. In the ExportImport folder there's a class to store the tree as a json file to facilitate data
   recovery if necessary. (to be stored in Static/Data.json)

5. In the Service folder there's a small bit of code built with fastApi to manipulate the data
   structure via http requests. 
