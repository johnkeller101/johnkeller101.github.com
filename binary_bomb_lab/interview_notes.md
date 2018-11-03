---
layout: page
current: about
title: Interview Questions
navigation: true
class: page-template
subclass: 'post page'
cover: /assets/images/2018season/IMG_1329.jpg
cover-height: 600
permalink: /cs-interview/
---
<style type="text/css">
        width: 1500px;
        left: -220px
        font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Oxygen, Ubuntu, Cantarell, Open Sans, Helvetica Neue, sans-serif !important;
        font-size: 1.8rem;
    }
</style>

## iOS Questions

 `@property (assign) float hisAge;`
 Note that his automatically generates the following code:
 ````
 @implementation DateCalculator{
     float _hisAge; // note the underscore
 }
// SETTER
 - (void)setHisAge:(float)hisAge {
     _hisAge = hisAge;
 }
// GETTER
 -(float)hisAge {
     return _hisAge;
 }
 ````
 
 other notes:
 - a **public property** is one which is included in your header file
 - a **private property** is one which is included in your m file
 
### Property Attributes

|variable|description|
|--------|-----------|
|`strong`|adds reference to keep object alive|
|`weak` | objects can disappear and become nil|
|`assign` | normal assign, no reference (default)|
|`copy`|make copy on assign|
|`atomic`|thread safety code, so all getting and setting can be performed in one operation|
|`nonatomic`|make not threadsafe and increase performance (most code is only run on one thread which means threadsafe does not matter)|
|`readwrite`|create getter and setter (default)|
|`readonly`|create just getter|
|`getter=<name>`|specify name of getter (typical for booleans, instead of getVar, its better to say isVar)|
|`setter=<name>`|specify name of setter (typical for booleans)|

### Dot Notation
- a shortcut which allows the compiler rewrites the dot-notation to the normal notation
- only good to use on getter/setters and not regular methods

||Getter|Setter|
|-|-----|------|
|Normal| `[calc hisName]`|`[calc setHisName:@"John"]`|
|Dot Notation|`calc.hisName`|`calc.hisName = @"John"`|

### Protocols and Delegates
- **Protocol**: an interface (a promise that everything which implements this uses specific methods)
- **Delegate**: an object that implements a protocol
- **The benefit**: reduced dependencies between objects
- 


### other various key questions
- The **bounds** of an UIView is the rectangle, expressed as a location (x,y) and size (width,height) relative to its own coordinate system (0,0).
- The **frame** of an UIView is the rectangle, expressed as a location (x,y) and size (width,height) relative to the superview it is contained within.
- **Modal View Controller Design Pattern**: !(link for more info)[https://medium.com/ios-os-x-development/modern-mvc-39042a9097ca]
<img src="https://cdn-images-1.medium.com/max/2000/1*la8KCs0AKSzVGShoLQo2oQ.png" width="80%">


## Data Structures
### Big-O Notation
Let's say you're making dinner for your family. O is the process of following a recipe, and n is the number of times you follow a recipe.
- `O` - you make one dish that everyone eats whether they like it or not. You follow one recipe from top to bottom, then serve (1 recipe). <-- How I grew up
- `O(n)` - you make individual dishes for each person. You follow a recipe from top to bottom for each person in your family (recipe times the number of people in your family).
- `O(n^2)` - you make individual dishes redundantly for every person. You follow all recipes for each person in your family (recipe times the number of people squared).
- `O(log n)` - you break people into groups according to what they want and make larger portions. You make one dish for each group (recipe times request)


### Graphs
#### Graph Search
- **Depth First Search**: Goes **deep** into each child before moving to neighbors<img src="https://upload.wikimedia.org/wikipedia/commons/7/7f/Depth-First-Search.gif">
    - recursive with a flag to stop the loop
- **Breadth First Search**: Goes **broad** (to neighbors) before going deep<img src="https://www.codingame.com/servlet/fileservlet?id=7768503315394">
    - you need to use a queue
- **Binary Search** `O(log(n))` 
<img src="https://www.mathwarehouse.com/programming/images/binary-search-tree/binary-search-tree-sorted-array-animation.gif">
<img src="https://blog.penjee.com/wp-content/uploads/2015/04/binary-and-linear-search-animations.gif">

### Searches
#### Binary Search





