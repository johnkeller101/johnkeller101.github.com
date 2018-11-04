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
    - The main goal of MVC pattern is separate data/logic, view and controller. There are 3 layers.
        1. **Model**: Models are representation of your app's data. There is user class or struct. So it has fields like name, birthdate, etc. It is data reside in Model layer.
        2. **View**: It is object which user can see and interact with. UILabel showing text is one kind of view.
        3. **Controller**: Controller mediates between Model and View. It takes data from model and show on views and also update model when user interacts with view.



### Runtime
- **Introspection**: allows you to get information about methods and classes at runtime in your code
    - **Class**: Object representing class
        - Get with `[object class]` or `NSClassFromString`
    - **Selector** (SEL): Internal id for method name
        - Get with `@selector` or `NSSelectorFromString`
    - **Method**: Object representing method
        - Get with `class_getInstanceMethod`
    - `isMemberOfClass`: Is it an instance of the class?
    - `isKindOfClass`: Is it an instance of the class (or an inherited class)?
    - `respondsToSelector`: Does it have a method?
    - `performSelector`: Call the method

### View Life Cycles
- Begin Life
    - `viewDidLoad` gets called once when the view gets loaded into memory
    - `viewWillAppear` gets called every time the view appears, can be called many times
    - `viewWillLayoutSubviews` and `viewDidLayoutSubviews` lays out constraints and sizing
    - `ViewDidAppear` view is completely loaded
- End Life
    - `viewWillDisappear` you can do stuff before the view disappears
    - `ViewDidDisappear` lets you know the view is gone



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
         <a data-toggle="collapse" href="#moreBinary" role="button" aria-expanded="false" aria-controls="moreBinary"> show more info below</a>
    </div>
</div>

<div class="collapse" id="moreBinary">
  <div class="card card-body">
    <img src="https://www.mathwarehouse.com/programming/images/binary-search-tree/optimal-binary-search-tree-from-sorted-array.gif" style="max-width: 40%">
    <img src="https://blog.penjee.com/wp-content/uploads/2015/04/binary-and-linear-search-animations.gif">
  </div>
</div>

<small>learn about searches in [python](https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/)</small>

### Sorting Methods
<style type="text/css">.sort-methods img { max-width:150px; }</style>
<div class="row sort-methods">
    <div class="col-md-2">
        <h4>Selection</h4>
        <img src="https://thumbs.gfycat.com/WavyImaginaryLangur-small.gif">
        <img src="https://codingconnect.net/wp-content/uploads/2016/09/Selection-Sort.gif">
    </div>
    <div class="col-md-2">
        <h4>Bubble</h4>
        <img src="https://upload.wikimedia.org/wikipedia/commons/5/54/Sorting_bubblesort_anim.gif">
        <img src="https://codepumpkin.com/wp-content/uploads/2017/10/BubbleSort_Avg_case.gif">
    </div>
    <div class="col-md-2">
        <h4>Insertion</h4>
        <img src="https://thumbs.gfycat.com/CornyThickGordonsetter-small.gif">
        <img src="https://cdn-images-1.medium.com/max/1600/1*krA0OFxEDgi8hVHJffCi4w.gif">
    </div>
        <div class="col-md-2">
        <h4>Merge</h4>
        <img src="https://www.codeproject.com/KB/recipes/SortVisualization/Merge_Sort.gif">
        <img src="https://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif">
    </div>
        <div class="col-md-2">
        <h4>Heap</h4>
        <img src="https://upload.wikimedia.org/wikipedia/commons/1/1b/Sorting_heapsort_anim.gif">
        <img src="https://upload.wikimedia.org/wikipedia/commons/f/fe/Heap_sort_example.gif">
    </div>
</div>

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
    - **Synchronous**: waits until the task has completed, multiple tasks will be completed in order.
    - **Asynchronous**: completes a task in the background, multiple tasks can be completed out of order
2. Difference between thread-safe and non-thread-safe in iOS
    - Thread-Unsafe:
2. What is the difference between `atomic` and `nonatomic` properties?
    - Suppose, you are using a string with nonatomic property and you are using two threads in your app. when the two threads are trying to change/access the string at the same time, the result will be unpredictable. because we don't know which process will run at which time.
    - So, at that time, we have to set the string with property atomic. so that one process/thread will handle the string at a time. Like that, we are making it thread safe.
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
7. What is *posing* in Objective-C?
8. What are the differences between `copy` and `retain`? 

-------

1. What is your favorite Apple framework to work with?
    - `UIKit` why?
2. When would you use a `class` or a `struct`?
    - Classes are a reference type so if you change a property in the class you are changing the reference (think one instance when called more than once)
        + Subclass inherits everything from the parent class which can add bloat
    - A struct is a value type which creates many copies of the object without overwriting others (think more than one instance when called many times, ex an array)
        - lightweight and clean
3. What third party libraries do you use? What are the pros and cons?
    - `cocoapods`

----
Coding Questions:
- Gesture recognizers
- networking: authenticating
- merge sort, shuffle array
- debugging just by looking at code
    - ui must be on main thread, memory leaks using two strong variables
- modulo operator `%` which gives remainder
    - ex converting seconds to minutes: `64 % 60 = 4` which gives you 1 minute 4 seconds
- 

[more good ones here to trip people up](http://andras.palfi.hu/iosobjc-interview-questions/)

## Actual Interview Topics

1. String manipulation
2. Binary search
3. Systems design
4. Some question on detecting elevation changes in a user's run/bike. The interviewer wanted me to discuss what possible things we could return and I gave some ideas. Overall it was unclear what exactly I had to implement. So I just implemented a method that returns the number of elevation climbs the user did.  
5. They gave an array of numbers(elevations) and wanted to determine the first "climb". 
6. Fill in blank obj-c methods

## Interview Simulation Structure

|Time|Description|
|-----------|-----|
|   0-30m   | Tell me about your past projects and education in school |
|   30-45m  | open that xcode: show me how you would parse a [json file](https://jsonplaceholder.typicode.com/albums) |
|   45-60m  | Do you have any questions for me? |

Random Question Generator:
<script type="text/javascript">
var myArray = [
  "Apples",
  "Bananas",
  "Pears"
];
var randomItem = myArray[Math.floor(Math.random()*myArray.length)];
var obj = document.getElementById('random-question');
document.getElementById("random-question").innerHTML = randomItem;
</script>
<a href="#" id="random-question">text url</a>


## My Background

- I have always had a passion for design and experiences.
- Started when I was a kid working at my family's business producing live theater and musical performances, ingratiating software as much as possible
    + Used Keynote, Final Cut Pro, Quartz Composer (may it rip)
- Shifted to computer science later in high school and developed a passion for it
- In college, my experience has shifted beyond objective-c, and into many other languages like python, php, swift, and a number of others

1. DSA and High School Apps
    - Mostly server-side written in PHP
    - Uses HTML parsing to determine contents of page and display them
    - Uses Regex to extract essential information from web pages like phone numbers, emails, and names
2. Colorado Scholarships
    - Back-end written in PHP with both web and iOS clients
    - iOS features list filtering 
3. desire2learn Gradebook App
    - Built for more of a personal tool for quicker mobile access to the gradebook. Published on github so others can utilize it if they want
    - Using `locksmith`, which integrates secure keychain storage of the username and password
    - desire2learn API was largely undocumented and reverse-engineered from their web js requests
    - `alamofire` allows the proper proper requests to be made in a light-weight way
    - also dealt with cookie management in `WKWebViews` to display authenticated file URLs
4. BallzClone
    - Built as a fun project to show that the content I was learning in Calculus 2 was applicable to my career
    - Utilizes Pythagorean Theorem on every collision to calculate the proper bounce angle
    - My first app using both `Swift` and `SceneKit`


   
