---
layout: page
current: about
title: Interview Notes
navigation: true
class: page-template
subclass: 'post page'
cover: /assets/images/2018season/IMG_1329.jpg
cover-height: 600
permalink: /cs-interview/
include_bootstrap: yes
sitemap: false
---
<style type="text/css">
@media (min-width: 1300px) {
    .post-full-content {
        width: 1300px;
        left: -120px;

    }
}
    .post-full-content {
        font-size: 1.8rem;
        font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Oxygen, Ubuntu, Cantarell, Open Sans, Helvetica Neue, sans-serif !important;
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
 
 - a **public property** is one which is included in your header file
 - a **private property** is one which is included in your m file
 
### Property Attributes

|variable|description|
|--------|-----------|
|`strong`  **   |adds reference to keep object alive|
|`weak`  **     | objects can disappear and become nil|
|`assign`       | normal assign, no reference (default)|
|`copy`         |make copy on assign|
|`atomic` **    |thread safety code, so all getting and setting can be performed in one operation|
|`nonatomic` ** |make not threadsafe and increase performance (most code is only run on one thread which means threadsafe does not matter)|
|`readwrite`    |create getter and setter (default)|
|`readonly`     |create just getter|
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


### Other Questions
- The **bounds** of an UIView is the rectangle, expressed as a location (x,y) and size (width,height) relative to its own coordinate system (0,0).
- The **frame** of an UIView is the rectangle, expressed as a location (x,y) and size (width,height) relative to the superview it is contained within.
- **Modal View Controller Design Pattern**: [link with more info](https://medium.com/ios-os-x-development/modern-mvc-39042a9097ca)
<img src="https://cdn-images-1.medium.com/max/2000/1*la8KCs0AKSzVGShoLQo2oQ.png" width="80%">


## Data Structures
### Big-O Notation
Let's say you're making dinner for your family. O is the process of following a recipe, and n is the number of times you follow a recipe.
- `O` - you make one dish that everyone eats whether they like it or not. You follow one recipe from top to bottom, then serve (1 recipe).
- `O(n)` - you make individual dishes for each person. You follow a recipe from top to bottom for each person in your family (recipe times the number of people in your family).
- `O(n^2)` - you make individual dishes redundantly for every person. You follow all recipes for each person in your family (recipe times the number of people squared).
- `O(log n)` - you break people into groups according to what they want and make larger portions. You make one dish for each group (recipe times request)

### Hash Tables
- for any problem given, first assume it is using a hash table
- A hash table is in elementary terms a `key` `value` pair which gives you very quick lookups (think dictionary)
- The `key` and `value` can be any type of object
- What happens when you have a **collision** (two values for the same key)? You can store the two values in a linked list
- **Runtime**: 
    - depends on the content and implementation
    - assuming we have an ideal hashtable, the time complexity is constant or `O(1)`
    - in a worst-case hashtable, the time complexity is `O(n)`

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Hash_table_5_0_1_1_1_1_1_LL.svg/450px-Hash_table_5_0_1_1_1_1_1_LL.svg.png" style="max-width: 80%">

```
class Hashtable {
    linkedList[] data
    boolean put(String key, Person value){
        int hashcode = getHashCode(key)
        int index = convertToIndex(hashcode)
        linkedList list = data[index]
        list.insert(key,value)
    }
}
```

### Min Heap
The smallest element is at the root of the tree, with larger elements as children
<img src="http://www.algolist.net/img/nearly-complete-binary-tree-correct.png" style="max-width: 50%">


### Graphs

<div class="row">
    <div class="col-md-4">
        <h4>Depth First Search</h4>
        Goes deep into each child before moving to neighbors<img src="https://upload.wikimedia.org/wikipedia/commons/7/7f/Depth-First-Search.gif" style="max-width: 80%">
    </div>
    <div class="col-md-4">
        <h4>Depth First Search</h4>
        Goes broad (to neighbors) before going deep<img src="https://www.codingame.com/servlet/fileservlet?id=7768503315394" style="max-width: 80%">
    </div>
    <div class="col-md-4">
        <h4>Binary Search</h4>
        <code>O(log(n))</code> cut in half and see if the value is less than or greater than
        <img src="https://www.mathwarehouse.com/programming/images/binary-search-tree/binary-search-tree-sorted-array-animation.gif" style="max-width: 80%">
         <a data-toggle="collapse" href="#moreBinary" role="button" aria-expanded="false" aria-controls="moreBinary"> Show more binary search examples below</a>
    </div>
</div>

<div class="collapse" id="moreBinary">
  <div class="card card-body">
    <img src="https://www.mathwarehouse.com/programming/images/binary-search-tree/optimal-binary-search-tree-from-sorted-array.gif" style="max-width: 40%">
    <img src="https://blog.penjee.com/wp-content/uploads/2015/04/binary-and-linear-search-animations.gif">
  </div>
</div>

<small>learn about searches in [python](https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/)</small>

## My Questions for you

1. Who is your ideal candidate for a summer intern? 
    - How much do you value a quick and dedicated learner?
2. How long does internal code review normally take? 
    - What systematic steps are taken to be nimble and release features quickly?
    - How are new features thought up? Do developers have input on features they feel should be added?
3. How do you employ Strava’s value of *Balance*? 
    - What does the average work week look like for you? What is the organizational structure like at Strava? 
    - What is the office environment and culture like?
    - How many meetings do you have per week?
4. How closely do the iOS and web teams work together? 
    - What are the steps taken internally to promote feature parity?
5. Is the common structure to have smaller teams work on features independently? 
    - I saw that through the watchOS development cycle only a few engineers were involved with building and testing for release.
6. How much of your position solely relies on Objective-C? 
    - I looked up your background and saw you are well-versed on more server-side software. Do you think that helps you in your position?
    - Do the back-end and client developers work closely together?
    - I know the public Strava API has been heavily handicapped in the past few years. Does the iOS app use a similar, but more complex API?
    - How quickly is your team integrating Swift into your codebase? Is it a priority that new features be built using it?
12. What is the **testing suite** like? 
    - How important is previous knowledge of testing frameworks like `__________`?
    - What about literal testing of bluetooth devices in workout mode?


## Sample Interview Questions
Sources: [50 iOS Interview Questions And Answers
](https://medium.com/@duruldalkanat/ios-interview-questions-13840247a57a); [toptal](https://www.toptal.com/ios/interview-questions); [raywenderlich](https://www.raywenderlich.com/2616-ios-interview-questions)

1. What is the difference between Synchronous & Asynchronous task? 
    - Synchronous: waits until the task has completed
    - Asynchronous: completes a task in the background
2. What is the difference between `atomic` and `nonatomic` properties?
    - Properties specified as `atomic` are guaranteed to always return a fully initialized object. This also happens to be the default state for synthesized properties so, while it’s a good practice to specify `atomic` to remove the potential for confusion, if you leave it off, your properties will still be `atomic`. This guarantee of `atomic` properties comes at a cost to performance, however. If you have a property for which you know that retrieving an uninitialized value is not a risk (e.g. if all access to the property is already synchronized via other means), then setting it to `nonatomic` can gain you a bit of performance.
3. Explain method swizzling. When you would use it?
4. What happens when the following code executes? `Ball *ball = [[[[Ball alloc] init] autorelease] autorelease];`
    - the `autorelease` occurs twice, which causes the item to crash
5. List the five iOS app states:
    1. Not running
    2. Suspended
    3. Background
    4. Inactive
    5. Active
6. Which is faster: to iterate through an `NSArray` or an `NSSet`?
    - `NSArray` as the order is retained and specified
7. What is posing in Objective-C?
8. What are the differences between `copy` and `retain`? 



