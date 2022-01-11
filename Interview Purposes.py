#!/usr/bin/env python3

from random import randint

FrontEndList = ['ignore', '1 CSS float了解吗? --- Float is used when you required to keep your web page element pushed to the \
left or right and make all other elements cover around it', '2 Prototypal and Class inheritance区别？\
--- In JavaScript, inheritance is different from a lot of other development languages. In JavaScript \
the object system based on a prototype, not the class. Objects are only a collection of value \
pairs and name. As far as the inheritance is a concern, there is only one construct JavaScript:\
objects. Each object has a private property that comprises a link to other object known as the prototype of that object'
,'3 CSS Rule？--- CSS rules are applied by the web browsers to a file to affect the way it is displayed. \
A CSS rule is formed from: A set of properties that have values set to inform how to display HTML content.\
A selector that selects the elements you want to put on to updated values of the property.\
A CSS rule-set within a stylesheet controls the display of a webpage.','4 SASS？--- Syntactically Awesome Stylesheets\
also known as Sass is a CSS preprocessor that elegance and adds power to the basic language. It lets you use nested rules,\
variables, inline imports, mixins, etc. the syntax should be compatible with CSS. Sass supports to organized the large stylesheets,\
and keep the small stylesheets up and running. The CSS preprocessor is also a scripting language that widens CSS by permitting the \
developers to use one language to write code and then accumulate it in the CSS. What’s the difference between “normalizing” \
and “resetting” CSS? Which one you would choose? Normalizing conserves valuable default styles before “unstyling” everything. \
It fixes the errors and bugs for common browser needs.Resetting is intended to strip the styling of default browser on elements. \
For instance, paddings, margins, font-sizes of elements are rearranging to be same. For common typographic elements, you \
have to redeclare the styling. It is a nice idea to select resetting when you have a very unconventional or customized \
website design that I want to do my own designing, there is no need for any default styling to be well-maintained.', '5，\
Explain HTML meta tags --- Meta tags are passed as pairs of value/name Meta tags can comprise data about character \
description, encoding, document title, etc,Meta tags go inside HTML page’s head tag, Meta tags are not showed on \
the page but it is to be displayed on the browser', '6，div span区别？--- span is an inline element div is a block element\
For bonus points, it is illegal to put a block element in an inline element, and though div can have a ptag, and \
aptag can have awidth, for span, it is not possible to have a p or div tag inside.','7，REST web 服务的好处？--- The \
learning curve is easy as it functions on the HTTP protocol No contract clears between client and server, so roughly \
coupled application. REST approaches can be easily tested on the browser.It also supports numerous technologies \
for data transfer, for example, XML, text, image, json, etc.It is a lightweight protocol','8，Load Balancing？--- \
Load balancing is a very easy method for allocating capacities across numerous clusters or machines. The most simple \
and common algorithm of load balancing is called Round Robin. In this type of load balancing the request is divided\
 in circular order ensuring all machines get an equal number of requests and no single machine is overloaded or\
underloaded.','9，When use WebPack? --- While making a complex Front-End application with a lot of non-code static\
possessions, for example, fonts, images, CSS, etc, then yes, you should use Webpack as it a lot of great benefits.\
If your application is very small, and do not have a lot of static resources and you just require to build one file\
of JavaScript to assist the customers, then Webpack should be more overhead than required.','10，HTML DOCTYPE为什么很重要？\
--- DOCTYPE is like an instruction to web browser concerning in which markup language version the page is written. \
The declaration of DOCTYPE should be the first thing in a document of HTML, before <html> tag. The declaration of\
doctype points to a Document Type Definition. It offers rules for the markup language, so it allows the browser\
to understand the content properly.','11，Lifecycle Hooks in Vue instance? --- Each Vue instance goes through series \
of steps when they are created, mounted and destroyed. Along the way, it will also runs functions called life \
cycle hooks, giving us the opportunity to add our own code at specific stage. Below are the events, a Vue instance\
goes through. beforeCreate— The first hook in the creation hooks. They allow us to perform actions before our \
component has even been added to the DOM. We do not have access to the DOM inside of this. created— This hook can\
be used to run code after an instance is created. We can access the reactive data. But templates and Virtual DOM \
have not yet been mounted or rendered.beforeMount— The beforeMount hook runs right before the initial render happens\
and after the template or render functions have been compiled. Most likely we’ll never need to use this hook.\
mounted— We will have full access to the reactive component, templates, and rendered DOM. This is the most frequently\
used hook.beforeUpdate— This hook runs after data changes on our component and the update cycle begins. But runs \
right before the DOM is patched and re-rendered. updated— This hook runs after data changes on our component and \
the DOM re-renders. If we need to access the DOM after a property change, here is probably the safest place to do \
it.beforeDestroy— This hook will run right before tearing down the instance. If we need to clean up events or \
reactive subscriptions, this is the right place to do it.destroyed— This hook will be used to do any last minute clean\
up.','12，v-show, v-if指令的区别？--- Below are some of the main differences between between v-show and v-if directives:\
v-if only renders the element to the DOM if the expression passes whereas v-show renders all elements to the DOM \
and then uses the CSS display property to show/hide elements based on expression. v-if supports v-else and v-else-if\
directives whereas v-show doesnt support else directives. v-if has higher toggle costs since it add or remove the \
DOM every time while v-show has higher initial render costs. i.e, v-show has a performance advantage if the \
elements are switched on and off frequently, while the v-if has the advantage when it comes to initial render \
time.v-if supports tab but v-show doesnt support.','13，key in Vue.js ? --- In order to render DOM elements more \
efficiently, Vue.js reuses the elements instead of creating them from scratch every time. This default mode \
is efficient, but in some cases it may causes problems','14，Why should not use if and for directives together \
on the same element? --- It is recommended not to use v-if on the same element as v-for. Because v-for directive \
has a higher priority than v-if. There are two common cases where this can be tempting: To filter items in a \
list (e.g.v-for="user in users" v-if="user.isActive"). In these cases, replace users with a new computed property\
that returns your filtered list (e.g.activeUsers).To avoid rendering a list if it should be hidden (e.g.v-for="user\
in users" v-if="shouldShowUsers"). In these cases, move thev-if to a container element (e.g.ul,ol).', '15，What is the\
difference between computed properties and methods? --- Computed properties are getter function in Vue instance rather\
than actual methods. we can define the same function as a method instead. However, the difference is that computed\
properties are cached based on their dependencies. A computed property will only re-evaluate when some of its\
dependencies have changed. In comparison, a method invocation will always run the function whenever a re-render\
happens. When we have to compute something by doing lot of computations like looping through a large array, it is\
best to use computed properties instead of a method. Without caching, we would spend more time than necessary. \
When we do not want cache, we can use a method instead.','16，What is Mixins? --- Mixins are a flexible way to \
distribute reusable functionalities for Vue components. A mixin object can contain any component options. \
When a component uses a mixin, all options in the mixin will be “mixed” into the component’s own options', '17，How \
Vue.js track changes？--- When you pass a plain JavaScript object to a Vue instance as its data option, Vue will walk\
through all of its properties and convert them to getter/setters using Object.defineProperty. The getter/setters \
are invisible to the user, but under the hood they enable Vue to perform dependency-tracking and change-notification\
when properties are accessed or modified. Every component instance has a corresponding watcher instance, which \
records any properties “touched” during the component’s render as dependencies. Later on when a dependency’s setter\
is triggered, it notifies the watcher, which in turn causes the component to re-render.', '18，What are Async \
Components? --- In large applications, we may need to divide the app into smaller chunks and only load a component \
from the server when it’s needed. To make that easier, Vue allows you to define our component as a factory function\
that asynchronously resolves your component definition. Vue will only trigger the factory function when the \
component needs to be rendered and will cache the result for future re-renders', '19，What are filters in Vue.js?\
--- Vue.js allows us to define filters that can be used to apply common text formatting. Filters are usable in two\
places: mustache interpolations and v-bindexpressions. Filters should be appended to the end of the JavaScript \
expression, denoted by the "pipe" symbol', '20，What is Vue Router? --- Vue Router is the official router for Vue.js.\
It deeply integrates with Vue.js core to make building Single Page Applications with Vue.js easy to implement. \
Its features include: Nested route/view mapping,Modular, component-based router configuration,Route params, query, \
wildcards, View transition effects powered by Vue.js’ transition system, Fine-grained navigation control,\
Links with automatic active CSS classes, Customizable Scroll Behavior,HTML5 history mode or hash mode, \
with auto-fallback in IE9', '21，What is the virtual DOM in Vue.js? --- In Vue.js, the virtual DOM is a tree-like \
data structure or a collection of JavaScript objects that represents DOM nodes. Vue.js manage the nodes of the \
virtual DOM, and that should be rendered on the page. These objects are called "virtual nodes" or VNodes. ', '22，\
What is the main purpose of using virtual DOM in Vue.js? --- \
The virtual DOMs main purpose is to make DOM manipulation faster and more efficient. It becomes very crucial when \
you have a lot of nodes in your DOM. In this case, updating these nodes is a very expensive task for processing\
 power and resources required. Here, virtual DOM comes into action and makes JavaScript object significantly \
 faster. Vue.js automatically organizes DOM updates in batches to enhance efficiency.', '23, 什么是Vue响应式? --- 数据发\
生变化后，会重新对页面渲染，这就是Vue响应式. 过程：侦测数据的变化,收集视图依赖了哪些数据, 数据变化时，自动“通知”需要更新的视图部分，并进行更新\
「它们对应专业俗语分别是：」数据劫持 / 数据代理, 依赖收集, 发布订阅模式. 如何侦测数据变化：2种方式，使用Object.defineProperty和ES6的Proxy\
这就是进行数据劫持或数据代理；为什么要收集依赖？我们之所以要观察数据，其目的在于当数据的属性发生变化时，可以通知那些曾经使用了该数据的地方。\
比如例子中，模板中使用了location 数据，当它发生变化时，要向使用了它的地方发送通知。订阅者DEP，为什么引入DEP？ 收集依赖需要为依赖找一个\
存储依赖的地方，为此我们创建了Dep,它用来收集依赖、删除依赖和向依赖发送消息等。于是我们先来实现一个订阅者 Dep 类，用于解耦属性的依赖收集\
和派发更新操作，「说得具体点」:它的主要作用是用来存放 Watcher 观察者对象。我们可以把Watcher理解成一个中介的角色，数据发生变化时通知它，\
然后它再通知其他地方。观察者watcher，为什么要引入watcher，vue 中定义一个 Watcher 类来表示观察订阅依赖。至于为啥引入Watcher，\
《深入浅出vue.js》给出了很好的解释:当属性发生变化后，我们要通知用到数据的地方，而使用这个数据的地方有很多，而且类型还不一样，既有可能是模板，\
也有可能是用户写的一个watch,这时需要抽象出一个能集中处理这些情况的类。然后，我们在依赖收集阶段只收集这个封装好的类的实例进来，\
通知也只通知它一个，再由它负责通知其他地方.「依赖收集的目的是:」 将观察者 Watcher 对象存放到当前闭包中的订阅者 Dep 的 subs 中。\
形成如下所示的这样一个关系（图参考《剖析 Vue.js 内部运行机制》）', '24, 作用域，闭包，原型链？ --- JavaScript是门动态语言，\
跟Java不一样，JavaScript可以随意定义全局变量和局部变量，每一个函数都是一个作用域，当函数执行时会优先查找当前作用域，然后逐级向上。\
JavaScript是静态作用域，在对变量进行查询时，变量值由函数定义时的位置决定，和执行时的所处的作用域无关。ES6已经有块级作用域了，\
而且用 let 和 const 定义的变量不会提升。概念： 作用域：变量或者函数的有效作用范围, 作用域链：我们需要查找某个变量值，会先在当前作用域查找，\
如果找不到会往上一级查，如果找到的话，就返回停止查找，返回查找的值，这种向上查找的链条关系，叫作用域. 闭包，指的是能够访问另一个函数作用域的\
变量的函数。闭包就是一个函数，这个函数能够访问其他函数的作用域中的变量.  原型和原型链，一个函数可以看成一个类，\
原型是所有类都有的一个属性，原型的作用就是给这个类的每一个对象都添加一个统一的方法. 「prototype ：」每个函数都会有这个属性，这里强调，是函数，\
普通对象是没有这个属性的（这里为什么说普通对象呢，因为JS里面，一切皆为对象，所以这里的普通对象不包括函数对象）。它是构造函数的原型对象；\
「「proto」 ：」每个对象都有这个属性，这里强调，是对象，同样，因为函数也是对象，所以函数也有这个属性。它指向构造函数的原型对象；「constructor ：」\
这是原型对象上的一个指向构造函数的属性。', '25, 项目种有用到哪些ES6的特性？ --- this的指向，ES5中: this 永远指向最后调用它的那个\
对象ES6箭头函数:箭头函数的 this 始终指向函数定义时的 this，而非执行时。5-2 怎么改变this的指向: 使用 ES6 的箭头函数在函数内部使用\
_this = this使用apply、call、bindnew 实例化一个对象. 箭头函数，箭头函数的 this 始终指向函数定义时的 this，而非执行时。\
箭头函数需要记着这句话：箭头函数中没有 this 绑定，必须通过查找作用域链来决定其值（箭头函数本身没有this，但是在它声明时可以捕获别人的\
this供自己使用。），如果箭头函数被非箭头函数包含，则 this 绑定的是最近一层非箭头函数的 this，否则，this 为 undefined.','26, 性能优化，\
上个项目的性能优化是怎么做的? 代码层面怎么做性能优化? webpack怎么做性能优化? --- 初始化页面加loding图, 减少http请求和冗余数据\
 组件，路由懒加载,拆分页面。分担加载压力; 配置nginx优化; 优化wepack打包机制,精简打包代码,压缩代码,依赖按需引入 去除冗余依赖, \
代码分包, 去除非必要文件; 使用CDN; 预渲染; ssr，前端渲染和客户端渲染; 图片转base64；后台分布式部署，负载均衡 ', '27, ES6的语法？ --- ']



BackEndPythonList = ['ignore','1，REST代表什么？---REST stands for REpresentational State Transfer. REST is web standards\
based architecture and uses HTTP Protocol for data communication. It revolves around resource where every component\
is a resource and a resource is accessed by a common interface using HTTP standard methods. REST was first introduced\
by Roy Fielding in 2000. In REST architecture, a REST Server simply provides access to resources and REST client\
accesses and presents the resources. Here each resource is identified by URIs/ global IDs. REST uses various \
representations to represent a resource like text, JSON and XML. Now a days JSON is the most popular format being\
used in web services.', '2，NoSQL数据库是什么？有几种不同的NoSQL数据库？--- A NoSQL database provides a mechanism for \
storage and retrieval of data that is modeled in means other than the tabular relations used in relational \
databases (like SQL, Oracle, etc.). Types of NoSQL databases: Document Oriented,Key Value, Graph,Column Oriented',
'3，创建web API时候的架构 --- HTTP for client server communication, XML/JSON as formatting language, Simple URI as \
the address for the services, Stateless communication', '4，RDS数据库系统的ACID --- Atomicity-This property guarantees\
that if one part of the transaction fails, the entire transaction will fail, and the database state will be left \
unchanged. Consistency-This property ensures that any transaction will bring the database from one valid state to \
another.Isolation-This property ensures that the concurrent execution of transactions results in a system state \
that would be obtained if transactions were executed serially.Durable-means that once a transaction has been \
committed, it will remain so, even in the event of power loss.','5，解释一下API Gateway pattern --- An API Gateway \
is a server that is the single entry point into the system. It is similar to the Facade pattern from object‑oriented\
design. The API Gateway encapsulates the internal system architecture and provides an API that is tailored to each\
client. It might have other responsibilities such as authentication, monitoring, load balancing, caching, request\
shaping and management, and static response handling. A major benefit of using an API Gateway is that it \
encapsulates the internal structure of the application. Rather than having to invoke specific services, \
clients simply talk to the gateway.', '6，SSL/TLS如何工作？---SSL(and its successor,TLS) is a protocol that operates\
directly on top of TCP. This way, protocols on higher layers (such as HTTP) can be left unchanged while still \
providing a secure connection. Underneath the SSL layer, HTTP is identical to HTTPS. When using SSL/TLS correctly,\
all an attacker can see on the cable is which IP and port you are connected to, roughly how much data you are \
sending, and what encryption and compression is used. He can also terminate the connection, but both sides will\
know that the connection has been interrupted by a third party. 1, After building a TCP connection, the SSL \
handshake is started by the client that sends a number of specifications: which version of SSL/TLS it is running,\
what ciphersuites it wants to use, and what compression methods it wants to use; 2, The server checks what the \
highest SSL/TLS version is that is supported by them both, picks a ciphersuite from one of the clients options \
(if it supports one), and optionally picks a compression method. 3, After this the basic setup is done, the \
server sends its certificate. This certificate must be trusted by either the client itself or a party that the\
client trusts. Having verified the certificate and being certain this server really is who he claims to be \
(and not a man in the middle), a key is exchanged. The client tells the server that from now on, all communication\
will be encrypted, and sends an encrypted and authenticated message to the server.The server verifies that the MAC\
(used for authentication) is correct, and that the message can be correctly decrypted. It then returns a message, \
which the client verifies as well.The handshake is now finished, and the two hosts can communicate securely.',
'7，什么时候用Redis，或MongoDB --- Use MongoDB if you dont know yet how youre going to query your data or what \
schema to stick with.MongoDB is suited for Hackathons, startups or every time you dont know how youll query the\
data you inserted. MongoDB does not make any assumptions on your underlying schema. While MongoDB is schemaless\
and non-relational, this does not mean that there is no schema at all. It simply means that your schema needs to\
be defined in your app (e.g. using Mongoose). Besides that, MongoDB is great for prototyping or trying things out.\
Its performance is not that great and cant be compared to Redis.Use Redis in order to speed up your existing\
application.It is very uncommon to use Redis as a standalone database system (some people prefer referring to \
it as a "key-value"-store).', '8，二叉树的定义 --- A normal tree has no restrictions on the number of children\
each node can have. A binary tree is made of nodes, where each node contains a "left" pointer, a "right" pointer,\
and a data element.There are three different types of binary trees: Full binary tree: Every node other than \
leaf nodes has 2 child nodes.Complete binary tree: All levels are filled except possibly the last one, and all\
nodes are filled in as far left as possible.Perfect binary tree: All nodes have two children and all leaves are\
at the same level.', '9，定义树数据结构 --- Trees are well-known as a non-linear data structure. They don’t store \
data in a linear way. They organize data hierarchically. A tree is a collection of entities called nodes. Nodes\
are connected by edges. Each node contains a value or data or key, and it may or may not have a child node. \
The first node of the tree is called the root. Leaves are the last nodes on a tree. They are nodes without\
children.', '10，解释Stack为什么吗是递归的数据结构 --- A stack is a recursive data structure, so its: a stack is \
either empty or it consists of a top and the rest which is a stack by itself;', '11，什么是Hash Table? ---\
A hash table (hash map) is a data structure that implements an associative array abstract data type, a \
structure that can map keys to values. Hash tables implement an associative array, which is indexed by \
arbitrary objects (keys). A hash table uses a hash function to compute an index, also called a hash value, \
into an array of buckets or slots, from which the desired value can be found.', '12，Heap是什么？--- A Heap is a \
special Tree-based data structure which is an almost complete tree that satisfies the heap property: in a max \
heap, for any given node C, if P is a parent node of C, then the key (the value) of P is greater than or equal\
to the key of C. In a min heap, the key of P is less than or equal to the key of C. The node at the "top" of \
the heap (with no parents) is called the root node. A common implementation of a heap is the binary heap, in \
which the tree is a binary tree.', '13，什么是Priority Queue？--- A priority queue is a data structure that\
stores priorities (comparable values) and perhaps associated information. A priority queue is different \
from a "normal" queue, because instead of being a "first-in-first-out" data structure, values come out in \
order by priority. Think of a priority queue as a kind of bag that holds priorities. You can put one in, and\
you can take out the current highest priority.', '14，什么是Queue? --- A queue is a container of objects \
(a linear collection) that are inserted and removed according to the first-in first-out (FIFO) principle.\
The process to add an element into queue is called Enqueue and the process of removal of an element from queue\
 is called Dequeue.', '15，什么是Graph? --- A graph is a common data structure that consists of a finite set \
of nodes (or vertices) and a set of edges connecting them. A pair (x,y) is referred to as an edge, which \
communicates that the x vertex connects to the y vertex. Graphs are used to solve real-life problems that \
involve representation of the problem space as a network. Examples of networks include telephone networks, \
circuit networks, social networks (like LinkedIn, Facebook etc.).', '16，Linked List ---Linked lists are very\
useful when you need : to do a lot of insertions and removals, but not too much searching, on a list of \
arbitrary (unknown at compile-time) length. splitting and joining (bidirectionally-linked) lists is very efficient.\
You can also combine linked lists-e.g. tree structures can be implemented as "vertical" linked lists \
(parent/child relationships) connecting together horizontal linked lists (siblings). Using an array based list\
for these purposes has severe limitations: Adding a new item means the array must be reallocated \
(or you must allocate more space than you need to allow for future growth and reduce the number of reallocations)\
Removing items leaves wasted space or requires a reallocation inserting items anywhere except the end involves\
(possibly reallocating and) copying lots of the data up one position', '17，什么是Dynamic Arrays? --- A dynamic \
array is an array with a big improvement:automatic resizing.One limitation of arrays is that they re fixed size, \
meaning you need to specify the number of elements your array will hold ahead of time. A dynamic array expands \
as you add more elements. So you dont need to determine the size ahead of time.', '18，Linked List种类？--- \
A singly linked list, A doubly linked list is a list that has two references, one to the next node and another\
to previous node. A multiply linked list- each node contains two or more link fields, each field being used\
to connect the same set of data records in a different order of same set(e.g., by name, by department, \
by date of birth, etc.).A circular linked list- where last node of the list points back to the first node\
(or the head) of the list.', '19，Queue的种类都有哪些？ ---Queue can be classified into following types:\
Simple Queue- is a linear data structure in which removal of elements is done in the same order they were \
inserted i.e., the element will be removed first which is inserted first. Circular Queue- is a linear data \
structure in which the operations are performed based on FIFO (First In First Out) principle and the last \
position is connected back to the first position to make a circle. It is also calledRing Buffer. \
Circular queue avoids the wastage of space in a regular queue implementation using arrays. Priority Queue\
- is a type of queue where each element has a priority value and the deletion of the elements is depended \
upon the priority value. In case of max-priority queue, the element will be deleted first which has the largest\
priority value. In case of min-priority queue the element will be deleted first which has the minimum priority\
value.De-queue (Double ended queue)- allows insertion and deletion from both the ends i.e. elements can be \
added or removed from rear as well as front end. Input restricted deque- In input restricted double ended \
queue, the insertion operation is performed at only one end and deletion operation is performed at both the ends.\
Output restricted deque- In output restricted double ended queue, the deletion operation is performed at \
only one end and insertion operation is performed at both the ends.', '20，什么是Binary Heap？--- A Binary Heap \
is a Binary Tree with following properties: It’s a complete tree (all levels are completely filled except \
possibly the last level and the last level has all keys as left as possible). This property of Binary Heap makes\
them suitable to be stored in an array.A Binary Heap is either Min Heap or Max Heap. In a Min Binary Heap, \
the key at root must be minimum among all keys present in Binary Heap. The same property must be recursively\
true for all nodes in Binary Tree. Max Binary Heap is similar to MinHeap.', '21，什么是Binary Search Tree? ---\
Binary search tree is a data structure that quickly allows to maintain a sorted list of numbers. It is called\
a binary tree because each tree node has maximum of two children. It is called a search tree because it can be \
used to search for the presence of a number in O(log n) time. The properties that separates a binary search tree\
from a regular binary tree are: All nodes of left subtree are less than root node, All nodes of right subtree are\
more than root node. Both subtrees of each node are also BSTs i.e. they have the above two properties', '22，Complexity analysis of Queue operation? ---\
Queues offer random access to their contents by shifting the first element off the front of the queue. You have \
to do this repeatedly to access an arbitrary element somewhere in the queue. Therefore,access is O(n). Searching \
for a given value in the queue requires iterating until you find it. So search is O(n). Inserting into a\
queue, by definition, can only happen at the back of the queue, similar to someone getting in line for a delicious \
Double-Double burger at In n Out. Assuming an efficient queue implementation, queue insertion is O(1). Deleting \
from a queue happens at the front of the queue. Assuming an efficient queue implementation, queue deletion \
is `O(1).', '23，Hash Table的space complexity? ---  The space complexity of a datastructure indicates how much\
space it occupies in relation to the amount of elements it holds. For example a space complexity of O(1) ould \
mean that the datastructure alway consumes constant space no matter how many elements you put in there. O(n) \
would mean that the space consumption grows linearly with the amount of elements in it. A hashtable typically \
has a space complexity of O(n).', '24，Data structure tree 与 graph有什么区别？--- Graph: Consists of a set of vertices \
(or nodes) and a set of edges connecting some or all of them. Any edge can connect any two vertices that arent \
already connected by an identical edge (in the same direction, in the case of a directed graph) Doesnt have to be\
connected (the edges dont have to connect all vertices together): a single graph can consist of a few disconnected \
sets of vertices. Could be directed or undirected (which would apply to all edges in the graph). Tree: A type of \
graph (fit with in the category of Directed Acyclic Graphs (or a DAG)). Vertices are more commonly called "nodes"\
Edges are directed and represent an "is child of" (or "is parent of") relationship. Each node (except the root node)\
has exactly one parent (and zero or more children). Has exactly one "root" node (if the tree has at least one node),\
which is a node without a parent. Has to be connected, Is acyclic, meaning it has no cycles: "a cycle is a path \
AKA sequence of edges and vertices wherein a vertex is reachable from itself". Trees arent a recursive data \
structure', '25，什么时候用Stack or queue 数据，而不用Array/Lists ? ---  Because they help manage your data in more \
a particular way than arrays and lists. It means that when you are debugging a problem, you wont have to wonder\
if someone randomly inserted an element into the middle of your list, messing up some invariants. Arrays and lists\
are random access. They are very flexible and also easily corruptible. If you want to manage your data as FIFO or\
LIFO its best to use those, already implemented, collections.More practically you should: Use a queue when you want\
to get things out in the order that you put them in (FIFO). Use a stack when you want to get things out in the \
reverse order than you put them in (LIFO); Use a list when you want to get anything out, regardless of when you \
put them in (and when you dont want them to automatically be removed).', '26，使用Priority queue的时候对比heap和array ---\
Heap is generally preferred for priority queue implementation because heaps provide better performance compared \
arrays or linked lists: In Array: insert()operation can be implemented by adding an item at end of array inO(1) time.\
getMax()operation can be implemented by linearly searching the highest priority item in array. This operation takes\
O(n)time. deleteMax()operation can be implemented by first linearly searching an item, then removing the item by \
moving all subsequent items one position back. In a Binary Heap: getMax() can be implemented in O(1) time,\
insert() can be implemented in O(log n) time and deleteMax()can also be implemented inO(log n)time.', '27，什么是AVL Tree? ---\
AVL trees are height balancing binary search tree. It is named after Adelson-Velsky and Landis, the inventors of\
the AVL tree. AVL tree checks the height of the left and the right sub-trees and assures that the difference is \
not more than 1. This difference is called the Balance Factor. This allows us to search for an element in the AVL\
tree in O(log n), where n is the number of elements in the tree. The balance factor of a node (N) in a binary tree\
is defined as the height difference: BalanceFactor(N) = height(left_sutree(N)) − height(right_sutree(N)) // \
BalanceFactor(N) belongs to the set {-1,0,1} If the balance factor doesn’t equal -1,0, or 1 then our tree is\
unbalanced, and we need to perform certain operations (called rotations) to balance the tree. Specifically\
we need to do one or more of 4 tree rotations: Left Rotation,Right Rotation,Left Right Rotation,Right Left \
Rotation.', '28，什么是balanced tree，为什么重要？ --- A tree is said to be balanced only when all three conditions \
satisfy: The left and right subtrees height differ by at most one. The left subtree is balanced. The right \
subtree is balanced. Height-balancing requirement: A node in a tree is height-balanced if the heights of its \
subtrees differ by no more than 1. A tree is height-balanced if all of its nodes are height-balanced. In a \
balanced BST, the height of the tree is log n where n is the number of elements in the tree. In the worst case \
and in an unbalanced BST, the height of the tree can be up to n which makes it same as a linked list. In the worst\
case each of the operations (lookup, insertion and deletion) takes timeO(n) that shall be avoided.\
Balanced BST maintains h = O(log n) so all operations run inO(log n)time.', '29，Associative Array是什么？---\
In computer science, an associative array, map, symbol table, or dictionary is an abstract data type composed \
of a collection of key, value pairs, such that each possible key appears at most once in the collection. Associative\
array can be implemented as: Hash table, Self-balancing binary search tree, Unbalanced binary search tree\
Association list', '30，Hash Table的复杂度 Complexity？--- Hash tables are O(1) average and amortized time complexity\
case complexity, however it suffers from O(n) worst case time complexity (when you have only one bucket in the\
hash table, then the search complexity is O(n)). A hashtable typically has a space complexity of O(n). Hash tables\
 suffer from O(n) worst time complexity due to two reasons: 1. If too many elements were hashed into the same key: \
looking inside this key may take O(n) time (for linked lists); 2. Once a hash table has passed its load balance \
- it has to rehash (create a new bigger table, and re-insert each element to the table). However, it is said to \
be O(1) average and amortized case because: 1. It is very rare that many items will be hashed to the same key \
if you chose a good hash function and you dont have too big load balance. 2. The rehash operation, which is O(n),\
can at most happen after n/2 ops, which are all assumed O(1): Thus when you sum the average time per op, you \
get : (n*O(1) + O(n)) / n) = O(1)', '31，什么是B Tree? --- B-tree is a self-balancing tree data structure that \
maintains sorted data. B-tree stores data such that each node contains keys in ascending order. Unlike a binary\
tree, each node in a B-Tree can have more than 2 children. Each node can have up to m children, where m is called\
the tree’s “order”. Unlike self-balancing binary search trees, it is optimized for systems that read and write \
large blocks of data. It is most commonly used in database and file systems. By maximizing the number of keys \
within each internal node, the height of the tree decreases and the number of expensive node accesses is reduced. \
In addition, rebalancing of the tree occurs less often. B-trees may waste some space, since nodes are not entirely\
 full.', '32，Hash Table和Trie (Prefix Tree) 如何选择？--- Tries and hash tables are used for different things:\
If all you want is the ability to lookup a word, then a hash table will be faster. A well constructed hash table\
(i.e. a good hash function and a reasonable load factor) has O(1)lookup time. If you want to find common prefixes,\
ordered retrieval, or do similar things, then you want a trie. Lookup time in a trie is O(m): it depends on the l\
ength of the string you are looking up. And memory wise: A hash tables overhead is typically a constant multiple \
of the number of words it contains. That is, in addition to the memory required to store the strings, there is \
per-string overhead to store the mapping between hash code and string. Memory for a trie is a little more \
involved. In the worst case, there is one node per character. All those little node allocations start adding \
up. Imagine a dictionary that contains 200,000 words, and the average word length is five characters. Thats a \
million nodes of overhead.', '33，Red/Black Tree 是什么？ --- A red-black tree is a binary search tree in which\
each node has a color (red or black) associated with it (in addition to its key and left and right children). \
This can be saved in memory as a single bit (e.g. red = 1, black = 0). the following 3 properties hold:\
(root property) The root of the red-black tree is black (red property) The children of a red node are black.\
(black property) For each node with at least one null child, the number of black nodes on the path from the root\
to the null child is the same. This is sometimes known as the black-depth. The height of the red-black tree is \
at most 2*log(n + 1) Red-black trees maintain a slightly looser height invariant than AVL trees. Because the \
height of the red-black tree is slightly larger, lookup will be slower in a red-black tree. However, the looser\
 height invariant makes insertion and deletion faster. Also, red-black trees are popular due to the relative ease\
of implementation.', '34，什么时候Doubly linked list比Singly linked list更有效率？--- Short answer: Delete a node in a\
Single Linked List: O(n) You dont know which is the preceding node so you have to traverse the list until you find\
it: deleteNode(Node node){prevNode = tmpNode; tmpNode = prevNode.next; while (tmpNode != null) { if (tmpNode == \
node) {prevNode.next = tmpNode.next;}prevNode = tmpNode;tmpNode = prevNode.next;}} Delete a node in a Double Linked\
List:O(1) You can simply update the links like this:deleteNode(Node node){node.prev.next = node.next;\
node.next.prev = node.prev;}     Long Answer: Insertion is clearly less work in a singly-linked list, as long as\
you are content to always insert at the head or after some known element. (That is, you cannot insert before a \
known element, but see below.) Deletion, on the other hand, is trickier because you need to know the element \
before the element to be deleted. One way of doing this is to make the delete API work with the predecessor of\
the element to be deleted. This mirrors the insert API, which takes the element which will be the predecessor\
of the new element, but its not very convenient and its hard to document. Its usually possible, though. Generally\
speaking, you arrive at an element in a list by traversing the list.Of course, you could just search the list \
from the beginning to find the element to be deleted, so that you know what its predecessor was. That assumes that \
the delete API includes the head of the list, which is also inconvenient. Also, the search is stupidly slow.\
The way that hardly anyone uses, but which is actually pretty effective, is to define a singly-linked list iterator\
to be the pointer to the element preceding the current target of the iterator. This is simple, only one indirection \
slower than using a pointer directly to the element, and makes both insertion and deletion fast. The downside is\
 that deleting an element may invalidate other iterators to list elements, which is annoying. (It doesnt invalidate\
  the iterator to the element being deleted, which is nice for traversals which delete some elements, but thats \
not much compensation.)If deletion is not important, perhaps because the data structures are immutable, \
singly-linked lists offer another really useful property: they allow structure-sharing. A singly-linked list can\
happily be the tail of multiple heads, something which is impossible for a doubly-linked list. For this reason, \
singly-linked lists have traditionally been the simple data structure of choice for functional languages.',
'35, 字典如何删除Key，与合并两个字典？--- Del, Update', '36, 如何实现列表去重？--- Set()', '37, Func(args, kwargs) 两个参数是什么意思？---\
用于函数定义，可以将不定数量的参数传递给函数，使用这两个变量来完成函数。', '38，python内置的数据类型有哪些？--- Integer, bool, \
string, list, tuple, dictionary', '39, map() 函数使用方式？ --- 第一个参数是其他定义的函数，第二个参数可以是列表等其他数据结构', '\
40，生成随机整数，小数的方式? --- Randint(a | b), bumpy.random.randn(n)', '41, 常用Linux命令？--- ls pwd cd touch rm \
mkdir tree cp mv cat more grep echo', '42, lambda的函数使用方式？---Lambda a,b : a* b', '43, 列表的extend和append的使用区别？---\
extend是合并，append是一个一个添加', '44，任何一种统计图绘制的开源库？--- PyeCharts, MatPlotLib', '45，正则表达事匹配种，.*和*?的区别？---\
.*是贪婪匹配，会匹配尽量多；.*?是非贪婪匹配，会尽可能少匹配', '46，简单描述Django的ORM？ --- ORM，全拼Object-Relation Mapping，\
意为对象-关系映射实现了数据模型与数据库的解耦，通过简单的配置就可以轻松更换数据库，而不需要修改代码只需要面向对象编程,\
orm操作本质上会根据对接的数据库引擎，翻译成对应的sql语句,所有使用Django开发的项目无需关心程序底层使用的是MySQL、Oracle、sqlite....，\
如果数据库迁移，只需要更换Django的数据库引擎即可', '47，5条常用的SQL语句 --- show databases; show tables; desc 表名; select\
* from 表名; delete from 表名 where id=5; update students set gender=0,hometown="北京" where id=5', '48，提高python运行效率的方法 ---\
使用生成器，因为可以节约大量内存; 循环代码优化，避免过多重复代码的执行; 核心模块用Cython PyPy等，提高效率; 多进程、多线程、协程\
多个if elif条件判断，可以把最有可能先发生的条件放到前面写，这样可以减少程序判断的次数，提高效率', '49，简述cookie和session的区别 ---\
session 在服务器端，cookie 在客户端（浏览器）, session 的运行依赖 session id，而 session id 是存在 cookie 中的，也就是说，\
如果浏览器禁用了 cookie ，同时 session 也会失效，存储Session时，键与Cookie中的sessionid相同，值是开发人员设置的键值对信息，\
进行了base64编码，过期时间由开发人员设置, cookie安全性比session差', '50，Python垃圾回收机制? --- python垃圾回收主要以引用计数为主，\
标记-清除和分代清除为辅的机制，其中标记-清除和分代回收主要是为了处理循环引用的难题。', '51，HTTP请求中get和post区别? ---\
GET请求是通过URL直接请求数据，数据信息可以在URL中直接看到，比如浏览器访问；而POST请求是放在请求头中的，我们是无法直接看到的；\
GET提交有数据大小的限制，一般是不超过1024个字节，而这种说法也不完全准确，HTTP协议并没有设定URL字节长度的上限，而是浏览器做了些处理，\
所以长度依据浏览器的不同有所不同；POST请求在HTTP协议中也没有做说明，一般来说是没有设置限制的，但是实际上浏览器也有默认值。总体来说，\
少量的数据使用GET，大量的数据使用POST。GET请求因为数据参数是暴露在URL中的，所以安全性比较低，比如密码是不能暴露的，就不能使用GET请求；\
POST请求中，请求参数信息是放在请求头的，所以安全性较高，可以使用。在实际中，涉及到登录操作的时候，尽量使用HTTPS请求，安全性更好。', '52，Array数据结构的特点 ---\
Finite (fixed-size)- An array is finite because it contains only limited number of elements. Order-All the elements \
are stored one by one , in contiguous location of computer memory in a linear order and fashion. Homogenous- All\
the elements of an array are of same data types only and hence it is termed as collection of homogenous', '53, How would you \
manage Web Services API versioning? --- Versioning is a critical part of API design, as it gives developers the ability to improve \
their API without stopping the clientʼs applications whenever new updates are rolled out. The three types of API versioning are\
:URL Versioning or Route Versioning: This solution uses URI routing to point to a specific version of the API. Versioning using \
a custom header: REST APIs are versioned by providing custom headers with the version number included as an attribute. Query String \
Parameter: Considered to be the worst method, the version number is included as a query parameter', '54, How would you find the \
most expensive queries in an application? --- Expensive queries are database queries that execute very slowly or utilize large \
amounts of CPU or memory resources. These queries are the most common cause of performance issues in an application. SQL Activity \
Monitor is an easy and rich UI tool available in the SQL Server Management Studio. You can also use SQL Dynamic Management View \
(DMV) to view the most expensive queries.','55, When would you apply asynchronous communication between two systems? --- In asynchronous \
communications, the client sends a request to the server (typically requiring lengthy processing), while receiving a delivery \
acknowledgment immediately.After the client receives the acknowledgment, it carries on with other tasks and will be notified eventually \
when the server finishes processing the request. The main benefit of asynchronous communications is improved performance. Asynchronous \
communications can be applied in situations where the response is not required immediately, and the current process can continue \
without the response. Real-world examples can include email, Slack, and other messaging platforms.','56, In what situation would \
you choose RDBMS and where would you choose NoSQL? --- An RDBMS is used when you need ACID (Atomicity, Consistency, Isolation, \
Durability) compliance to reduce anomalies and protect data integrity and when the data is structured and unchanging.On the other \
hand, NoSQL is recommended for high volume environments, cloud computing & storage, and when using unstructured data. Examples of \
NoSQL databases are MongoDB, Cassandra, HBase, and CouchDB.' ,'57, Which sorting algorithm to use and when? --- Quick Sort: is one \
of the most efficient sorting algorithms. It is based on the splitting of an array or list into smaller ones and swapping values \
based on the comparison with the ‘pivot’ element selected. It is more effective for data that can fit in memory. Otherwise merge \
sort is preferred. Bubble Sort: The simplest but most inefficient sorting algorithm, it repeatedly cycles through a list, compares \
adjacent values, and swaps them if they are in the wrong order. It is mostly used when array is small or if large data which is nearly \
sorted. Selection Sort: It is a fast and simple comparison-based sorting algorithm. It sorts by finding the minimum element \
repeatedly in an array. It is mostly used when an array is small as its time complexity makes it inefficient for larger arrays. \
Merge Sort: One of the most efficient algorithms, it uses the principle of divide and conquer. It iteratively breaks down lists \
into sub-lists consisting of single elements and then merges these elements as per the requirements. Widely used in case of linked \
list or where the known data is similar.', '58, What are the qualities any good backend developer must possess? --- This is a great \
question with which to impress the interviewer, as you can tell them about your competencies and understanding of the position. \
However, many candidates make the mistake of only talking about a couple of their strengths. The ideal answer should include at \
least some of the following points: In-depth knowledge of server programming languages like Python, Ruby, Java, Perl \
Great acquaintance with NoSQL and RDBMS, Good understanding of front-end technologies (easy to work with frontend developers)\
Basic understanding of cloud deployments, Ability to develop business logic within any app, Ability to easily create functional APIs\
Design of service architecture, Ability to optimize web applications','59, Define what is a Hash Function? --- A hash function is \
any function that can be used to map data of arbitrary size to fixed-size values. The values returned by a hash function are called \
hash values, hash codes, digests, or simply hashes. The values are used to index a fixed-size table called a hash table. Use of a \
hash function to index a hash table is called hashing or scatter storage addressing.Mathematically speaking, a hash function is \
usually defined as a mapping from the universe of elements you want to store in the hash table to the range {0, 1, 2, .., \
numBuckets - 1}. Some properties of Hash Functions are: Very fast to compute (nearly constant), One way; can not be reversed \
Output does not reveal information on input, Hard to find collisions (different data with same hash), Implementation is based on \
parity-preserving bit operations (XOR and ADD), multiply, or divide.','60, Explain what is Hash Value? --- A Hash Value (also \
called as Hashes or Checksum) is a string value (of specific length), which is the result of calculation of a Hashing Algorithm. \
Hash Values have different uses: Indexing for Hash Tables. Determine the Integrity of any Data (which can be a file, folder, email, \
attachments, downloads etc).', '61, What is Hashing? --- Hashing is the practice of using an algorithm (or hash function) to \
map data of any size to a fixed length. This is called a hash value (or sometimes hash code or hash sums or even a hash digest if \
you’re feeling fancy). In hashing, keys are converted into hash values or indexes by using hash functions. Hashing is a one-way \
function.', '62, What is Hash Collision? --- There’s always a chance that two different inputs for hash function will generate \
the same hash value. This is known as a hash collision. If a collision happens, you just compare the actual objects you are hashing \
to see if they match. What is the probability of a hash collision? This question is just a general form of the birthday problem from \
mathematics: Given k randomly generated values, where each value is a non-negative integer less than N, what is the probability \
that at least two of them are equal? Take the well-known hash function CRC32, for example. If you feed this function the two strings \
“plumless” and “buckeroo”, it generates the same value. This is known as a hash collision.', '63, What is MD5? --- MD5 is a so-called \
cryptographic hash function. Although MD5 was initially designed to be used as a cryptographic hash function, it has been found to \
suffer from extensive vulnerabilities. It can still be used as a checksum to verify data integrity, but only against unintentional \
corruption. This basically means that you can give in any bitstring as input for the function, and you will get out a fixed-size \
bitstring (128-bit in the case of MD5) as output. The output is usually called "digest". The digest depends solely on the input and \
nothing else. Thus in itself it can be used as an integrity proof, but not as authenticity, if the underlying hash function has the \
necessary properties (in this case collision-resistance). This means that for two different outputs the digest itself should be \
also different. The problem is that the digests size is fixed, which in turn means that with sufficient number of messages it will \
always be possible to find a collision (i.e., two different inputs yielding the same output).One should also note that there is \
nowadays no justification to use MD5, as weaknesses have been discovered (namely post-fix collision attacks). Also using SHA-256/512 \
on modern hardware is usually faster then MD5.','64, Explain when to use Hashing on practice? --- Use a hash function when you want \
to compare a value but cant store the plain representation (for any number of reasons). Passwords should fit this use-case very well \
since you dont want to store them plain-text for security reasons (and shouldnt). But what if you wanted to check a filesystem for \
pirated music files? It would be impractical to store 3 mb per music file. So instead, take the hash of the file, and store that (md5 \
would store 16 bytes instead of 3mb). That way, you just hash each file and compare to the stored database of hashes (This doesnt \
work as well in practice because of re-encoding, changing file headers, etc, but its an example use-case).Use a hash function when \
youre checking validity of input data. Thats what they are designed for. If you have 2 pieces of input, and want to check to see if \
they are the same, run both through a hash function. The probability of a collision is astronomically low for small input sizes \
(assuming a good hash function). Thats why its recommended for passwords. For passwords up to 32 characters, md5 has 4 times the \
output space. SHA1 has 6 times the output space (approximately). SHA512 has about 16 times the output space. You dont really care \
what the password was, you care if its the same as the one that was stored. Thats why you should use hashes for passwords.Hash \
functions are also great for signing data. For example, if youre using HMAC, you sign a piece of data by taking a hash of the data \
concatenated with a known but not transmitted value (a secret value). So, you send the plain-text and the HMAC hash. Then, the \
receiver simply hashes the submitted data with the known value and checks to see if it matches the transmitted HMAC. If its the \
same, you know it wasnt tampered with by a party without the secret value. This is commonly used in secure cookie systems by HTTP \
frameworks, as well as in message transmission of data over HTTP where you want some assurance of integrity in the data.']

DevOpsEngList = ['ignore', '1, 你是如何看待DevOps在IT中的重要性？ ---', '2，你了解过的DevOps比较受欢迎的工具有哪些？你熟悉哪些？---\
Git : Version Control System tool, Jenkins : Continuous Integration tool, Selenium : Continuous Testing tool\
Puppet, Chef, Ansible : Configuration Management and Deployment tools, Nagios : Continuous Monitoring tool\
Docker : Containerization tool', '3，持续监控的重要性？---', '4，Infrastructure as code了解吗？YAML或Json? ---', '5，\
VCS版本控制熟悉吗？GitHub熟悉吗？下载Repo的方式？', '6，git fetch vs git pull? ---', '7，解释一下Branch? ---', '8，merge\
 conflict有处理的经验吗？---', '9，Jenkins的Master Slave架构工作流程？--- 1，Jenkin master pull code from. \
GitHub repo when there’s commit 2, distribute across slaves 3, Slaves carry out builds, test, and test reports','10, \
Docker的架构？--- Docker uses a client-server architecture. Docker Client is a service that runs a command. \
The command is translated using the REST API and is sent to the Docker Daemon (server). Docker Daemon accepts \
the request and interacts with the operating system to build Docker images and run Docker containers.A Docker \
image is a template of instructions, which is used to create containers.Docker container is an executable package \
of an application and its dependencies together.Docker registry is a service to host and distribute Docker \
images among users.','11，虚机和container的区别 --- memory: VM - occupies lot of memory space; Docker - occupy less\
Boot-up time: VM - long; Docker - short. Performance: VM - multiple vm unstable performance; Docker - \
better performance, hosted in single docker engine. Scaling: VM - difficult scale up; Docker - Easy;\
Efficiency: VM - low; Docker - High. Portability: VM - Compatibility issues while porting across different\
platforms. Space allocation: VM - Data volumes cannot share; Docker: Data volumes shared and used again across\
multiple containers', '12，Docker Image和Docker container的区别 --- Docker image: templates of docker containers; \
Docker containers are runtime instances of Docker image. An image is built using Dockerfile; Containers are \
created using Docker images. Docker image is stored in Docker repository or a Docker hub; Docker Container \
stored in Docker daemon. Docker image layer is a read-only filesystem; Docker container layer is a read-write\
filesystem','13，Nagios在持续监控系统，应用和服务的时候如何工作？--- Nagios enables server monitoring and the ability \
to check if they are sufficiently utilized or if any task failures need to be addressed. Verifies the status \
of the servers and services. Inspects the health of your infrastructure. Checks if applications are working\
correctly and web servers are reachable ', '14, Kubernetes是什么？---Kubernetes is an open-source system for \
automating deployment, scaling, and management of containerized applications.The purpose of Kubernetes is to \
make it easier to organize and schedule your application across a fleet of machines. At a high level it is an \
operating system for your cluster.Basically, it allows you to not worry about what specific machine in your \
datacenter each application runs on. Additionally it provides generic primitives for health checking and \
replicating your application across these machines, as well as services for wiring your application into\
 micro-services so that each layer in your application is decoupled from other layers so that you can \
 scale/update/maintain them independently. To understand what Kubernetes is good for, lets look at some \
examples: You would like to run a certain application in a container on multiple different locations. Sure, \
if its 2-3 servers/locations, you can do it by yourself but it can be challenging to scale it up to additional\
multiple location.Performing updates and changes across hundreds of containers. Handle cases where the current \
load requires to scale up (or down)','15，Pod是做什么的？---Pods represent the processes running on a cluster. By\
limiting pods to a single process, Kubernetes can report on the health of each process running in the cluster. \
Pods have: a unique IP address (which allows them to communicate with each other) persistent storage volumes\
(as required) configuration information that determine how a container should run. Although most pods contain \
a single container, many will have a few containers that work closely together to execute a desired function.','16，Pod内的container如何交互通信？---\
Containers within a pod share networking space and can reach other on localhost. For instance, if you have two \
containers within a pod, a MySQL container running on port 3306, and a PHP container running on port 80, the \
PHP container could access the MySQL one through localhost:3306.', '17，Docker, Docker Compose, Docker Swarm,\
Kubernetes --- Docker is a container engine, it makes you build and run usually no more than one container at\
most, locally on your PC for development purposes.Docker Compose is a Docker utility to run multiple containers\
and let them share volumes and networking via the docker engine features, runs locally to emulate service \
composition and remotely on clusters. Docker Compose is mostly used as a helper when you want to start multiple\
Docker containers and dont want to start each one separately using docker run .... Docker Swarm is for running and \
connecting containers on multiple hosts. It does things like scaling, starting a new container when one crashes, \
networking containers.Kubernetes is a container orchestration platform, it takes care of running containers and \
enhancing the engine features so that containers can be composed and scaled to serve complex applications (sort \
of PaaS, managed by you or cloud provider). Kubernetes goal is very similar to that for Docker Swarm but its \
developer by Google.', '18，nameSpace是什么？如果用默认的nameSpace问题是什么？--- Namespaces allow you split your cluster\
into virtual clusters where you can group your applications in a way that makes sense and is completely separated \
from the other groups (so you can for example create an app with the same name in two different namespaces).\
When using the default namespace alone, it becomes hard over time to get an overview of all the applications you \
manage in your cluster. Namespaces make it easier to organize the applications into groups that makes sense, \
like a namespace of all the monitoring applications and a namespace for all the security applications, etc.\
Namespaces can also be useful for managing Blue/Green environments where each namespace can include a different \
version of an app and also share resources that are in other namespaces (namespaces like logging, monitoring, \
etc.).Another use case for namespaces is one cluster, multiple teams. When multiple teams use the same cluster,\
they might end up stepping on each others toes. For example if they end up creating an app with the same name \
it means one of the teams overriden the app of the other team because there cant be too apps in Kubernetes with \
the same name (in the same namespace).', '19，Pod是ephemeral的吗？---Pods are ephemeral. They are not designed to \
run forever, and when a Pod is terminated it cannot be brought back. In general, Pods do not disappear until they\
are deleted by a user or by a controller.Pods do not "heal" or repair themselves. For example, if a Pod is \
scheduled on a node which later fails, the Pod is deleted. Similarly, if a Pod is evicted from a node for any\
reason, the Pod does not replace itself.', '20，StatefulSet in K8s? ---When using Kubernetes, most of the time \
you don’t care how your pods are scheduled, but sometimes you care that pods are deployed in order, that they \
have a persistent storage volume, or that they have a unique, stable network identifier across restarts and \
reschedules. In those cases,StatefulSets can help you accomplish your objective. It manages the deployment\
 and scaling of a set of Pods, and provides guarantees about the ordering and uniqueness of these Pods.\
StatefulSets are valuable for applications that require one or more of the following.Stable, unique network \
identifiers.Stable, persistent storage.Ordered, graceful deployment and scaling.Ordered, automated rolling\
updates.', '21，DaemonSet? ---DaemonSets are used in Kubernetes when you need to run one or more pods on all\
(or a subset of) the nodes in a cluster. The typical use case for a DaemonSet is logging and monitoring for \
the hosts. For example, a node needs a service (daemon) that collects health or log data and pushes them to a \
central system or database. As the name suggests you can use daemon sets for running daemons (and other tools)\
that need to run on all nodes of a cluster. These can be things like cluster storage daemons (e.g. Quobyte,\
glusterd, ceph, etc.), log collectors (e.g. fluentd or logstash), or monitoring daemons (e.g. Prometheus Node \
Exporter, collectd, New Relic agent, etc.)', '22，Docker和K8s的差别？ ---Docker and Kubernetes are complementary.\
Docker provides an open standard for packaging and distributing containerized applications, while Kubernetes \
provides for the orchestration and management of distributed, containerized applications created with Docker.\
In other words, Kubernetes provides the infrastructure needed to deploy and run applications built with \
Docker.', '23，为什么需要K8s在容器上面？---In the quality assurance (QA) environments, we can get away with running\
containers on a single host to develop and test applications. However,when we go to production, we do not have\
the same liberty, as we need to ensure that our applications: Are fault-tolerant, Can scale, and do this on-demand\
Use resources optimally, Can discover other applications automatically, and communicate with each other\
Are accessible from the external world. Can update/rollback without any downtime. Container orchestrators are \
the tools which group hosts together to form a cluster, and help us fulfill the requirements mentioned above.\
Nowadays, there are many container orchestrators available, such as: Docker Swarm: Docker Swarm is a container \
orchestrator provided by Docker, Inc. It is part of Docker Engine.Kubernetes:Kubernetes was started by Google, \
but now, it is a part of the Cloud Native Computing Foundation project.Mesos Marathon:Marathon is one of the \
frameworks to run containers at scale on Apache Mesos.Amazon ECS:Amazon EC2 Container Service (ECS) is a \
hosted service provided by AWS to run Docker containers at scale on its infrastructrue.Hashicorp Nomad:\
Nomad is the container orchestrator provided by HashiCorp.']


AlgorithmList = ['ignore', '1，Explain how Bubble Sort works ---Bubble Sort is based on the idea of repeatedly\
 comparing pairs of adjacent elements and then swapping their positions if they are in the wrong order. Bubble \
sort is a stable, in-place sort algorithm. How it works: In an unsorted array of n elements, start with the first\
 two elements and sort them in ascending order. (Compare the element to check which one is greater).Compare the\
 second and third element to check which one is greater, and sort them in ascending order.Compare the third and\
 fourth element to check which one is greater, and sort them in ascending order....Repeat steps 1–nuntil no more \
 swaps are required.Bubble sort has a worst-case and average complexity of O(n squared), where n is the number\
of items being sorted. When the list is already sorted (best-case), the complexity of bubble sort is only O(n).\
The space complexity for Bubble Sort is O(1), because only single additional memory space is required (for \
temp swap element).', '2, Classify Sorting Algorithms --- Sorting algorithms can be categorised based on the \
following parameters:Based on Number of Swaps or Inversion. This is the number of times the algorithm swaps \
elements to sort the input.Selection Sort requires the minimum number of swaps. Based on Number of Comparisons. \
This is the number of times the algorithm compares elements to sort the input. Using Big-O notation, the sorting \
algorithm examples listed above require at least O(n log n)comparisons in the best case and O(n2) comparisons in \
the worst case for most of the outputs.Based on Recursion or Non-Recursion. Some sorting algorithms, such as \
Quick Sort, use recursive techniques to sort the input. Other sorting algorithms, such as Selection Sort or \
Insertion Sort, use non-recursive techniques. Finally, some sorting algorithm, such as Merge Sort, make use of \
both recursive as well as non-recursive techniques to sort the input.Based on Stability. Sorting algorithms are \
said to be stable if the algorithm maintains the relative order of elements with equal keys. In other words, two \
equivalent elements remain in the same order in the sorted output as they were in the input. Insertion sort, \
Merge Sort, and Bubble Sort are stable. Heap Sort and Quick Sort are not stable. Based on Extra Space Requirement.\
Sorting algorithms are said to be in place if they require a constant O(1) extra space for sorting. Insertion \
sort and Quick-sort are in place sort as we move the elements about the pivot and do not actually use a separate \
array which is NOT the case in merge sort where the size of the input must be allocated beforehand to store the \
output during the sort. Merge Sort is an example of out place sort as it require extra memory space for it’s \
operations.', '3, Explain how Insertion Sort works ---Insertion Sort is an in-place, stable,comparison-based sorting\
 algorithm. The idea is to maintain a sub-list which is always sorted. An element which is to be inserted in \
 this sorted sub-list, has to find its appropriate place and then it has to be inserted there. Hence the name,\
 insertion sort.Steps on how it works: If it is the first element, it is already sorted.Pick the next element.\
Compare with all the elements in sorted sub-list. Shift all the the elements in sorted sub-list that is greater \
than the value to be sorted.Insert the value.Repeat until list is sorted. Insertion sort runs in O(n2) in its \
worst and average cases. It runs in O(n) time in its best case.Insertion sort performs two operations: it scans \
through the list, comparing each pair of elements, and it swaps elements if they are out of order. Each operation \
contributes to the running time of the algorithm. If the input array is already in sorted order, insertion sort \
compares O(n) elements and performs no swaps. Therefore, in the best case, insertion sort runs in O(n) time.\
Space complexity is O(1) because an extra variable key is used (as a temp variable for insertion).', '4, Explain \
what is ideal Sorting algorithm? The Ideal Sorting Algorithm would have the following properties: Stable: Equal \
keys aren’t reordered. Operates in place:requiring O(1) extra space.Worst-case O(n log n) key comparisons.\
Worst-case O(n) swaps.Adaptive: Speeds up to O(n) when data is nearly sorted or when there are few unique keys.\
There is no algorithm that has all of these properties, and so the choice of sorting algorithm depends on the\
 application.', '5, Explain how Heap Sort works ---Heapsort is a comparison-based sorting algorithm. Heapsort can \
 be thought of as an improved selection sort: like that algorithm, it divides its input into a sorted and an unsorted\
 region, and it iteratively shrinks the unsorted region by extracting the largest element and moving that to the \
 sorted region. The improvement consists of the use of a heap data structure rather than a linear-time search to \
find the maximum. A heap is a complete binary tree (every level filled as much as possible beginning at the left \
side of the tree) that follows this condition: the value of a parent element is always greater than the values of \
its left and right child elements. So, by taking advantage of this property, we can pop off the max of the \
heap repeatedly and establish a sorted array. In an array representation of a heap binary tree, this essentially \
means that for a parent element with an index of i, its value must be greater than its left child [2i+1] and right \
child [2i+2] (if it has one).The HeapSort steps are: Create a max heap from the unsorted list. Swap the max element, \
located at the root, with the last element. Re-heapify or rebalance the array again to establish the max heap order. \
The new root is likely not in its correct place. Repeat Steps 2–3 until complete (when the list size is 1)', '6, Explain \
how Merge Sort works --- Merge sort is a divide-and-conquer,comparison-based sorting algorithm based on the idea \
of breaking down a list into several sub-lists until each sublist consists of a single element and merging those \
sublists in a manner that results into a sorted list. Most implementations produce a stable sort, which means that \
the order of equal elements is the same in the input and output. Can be used as external sorting (when the data to \
be sorted is too large to fit into memory).There are two methods for implementing a Merge Sort algorithm: The \
Top-Down (recursive) approach. Given an array of size N, the algorithm recursively breaks the array in half and \
then merges the results together.The Bottom-Up (iterative) approach. Rather than breaking the overall array into \
distinct pieces, bottum-up mergesort loops over the array using intervals of varying sizes. Each interval is sorted \
and merged together; subsequent loops over the array have larger intervals, effectively merging our previously \
sorted (smaller) intervals together. Space complexity is always Ω(n) as you have to store the elements somewhere. \
Additional space complexity can be O(n) in an implementation using arrays and O(1) in linked list implementations. \
In practice implementations using lists need additional space for list pointers, so unless you already have the \
list in memory it shouldnt matter.','7, Sort a Stack using Recursion --- The idea of the solution is to hold all \
values in system stack until the stack becomes empty. When the stack becomes empty, insert all held items one \
by one in sorted order.', '8, Whats the difference between External vs Internal sorting? n internal sorting all \
the data to sort is stored in memory at all times while sorting is in progress.In external sorting data is stored \
outside memory (like on disk) and only loaded into memory in small chunks. External sorting is usually applied in \
cases when data cant fit into memory entirely.So in internal sorting you can do something like shell sort - just \
access whatever array elements you want at whatever moment you want. You cant do that in external sorting - the \
array is not entirely in memory, so you cant just randomly access any element in memory and accessing it randomly \
on disk is usually extremely slow. The external sorting algorithm has to deal with loading and unloading chunks of \
data in optimal manner. Divide and conquer algorithms like merge sort are commonly used for external sorting, \
because they break up the problem of sorting everything into a series of smaller sorts on chunks at a time. It \
doesn’t require random access to the the dataset and can be made to operate in chunks which fit in memory. In \
some cases the in-memory chunks maybe sorted using an in-memory (internal) sorting algorithm.','9, When is Quicksort \
better than Mergesort? They are both O(n log n) and yet most people use Quicksort instead of Mergesort. Why is \
hat? Quicksort has O(n2) worst-case runtime and O(n log n) average case runtime. However, it’s superior to merge \
sort in many scenarios because many factors influence an algorithm’s runtime, and, when taking them all together, \
quicksort wins out. Quicksort in particular requires little additional space (its in-place and MergeSort requires \
extra memory linear to number of elements to be sorted) and exhibits good cache locality (does half as many reads \
as the other algorithms), and this makes it faster than merge sort in many cases. In addition, it’s very easy to \
avoid quicksort’s worst-case run time of O(n2) almost entirely by using an appropriate choice of the pivot – such \
as picking it at random (this is an excellent strategy). The average case performance for quicksort is faster \
than mergesort. But this is only true if you are assuming constant time to access any piece of memory on demand. \
In RAM this assumption is generally not too bad (it is not always true because of caches, but it is not too bad). \
However if your data structure is big enough to live on disk, then quicksort gets killed by the fact that your \
average disk does something like 200 random seeks per second. if data has to be sorted on disk, you really, \
really want to use some variation of mergesort.', '10, Explain how QuickSort works --- Quick Sort is a divide \
and conquer,comparison,in-place algorithm. Efficient implementations of Quicksort are not a stable sort. \
When implemented well, it can be about two or three times faster than its main competitors, merge sort and \
heapsort.Quicksort determines something called a pivot, which is a somewhat arbitrary element in the collection. \
Using the pivot point, quicksort partitions(or divides) the larger unsorted collection into two, smaller lists. \
It moves all the elements smaller than the pivot to the left (before) the pivot element, and moves all the \
elements larger than the pivot to the right (after) the pivot element. Even though the list isn’t completely \
sorted yet, we know that the items are in the correct order in relation to the pivot. This means that we never \
have to compare elements on the left side of the partition to elements on the right side of the partition. We \
already know they are in their correct spots in relation to the pivot. The sub-lists are then sorted recursively. \
Ideally, partitioning would use the median of the given values (in the array), but the median can only be found by \
scanning the whole array and this would slow the algorithm down. In that case the two partitions would be of equal \
size; In the simplest versions of quick sort an arbitrary element, typically the last (rightmost) element is used \
as an estimate (guess) of the median. Overall time complexity of Quick Sort is O(n log n). In the worst case, \
it makes O(n2) comparisons (all elements are same or array is already sorted).The partition step used in quicksort \
ideally is an in-place operation (without creating any additional arrays). But since quicksort calls itself on \
the order of log(n) times (in the average case), worst case number of calls is O(n), at each recursive \
call a new stack frame of constant size must be allocated. Hence the O(log n) space complexity.', '11, Explain \
how Radix Sort works --- Radix sort is a sorting technique that sorts the elements by first grouping the individual \
digits of the same place value. Then, sort the elements according to their increasing/decreasing order. Radix sort \
uses counting sort as a subroutine to sort an array of numbers. Because integers can be used to represent \
strings (by hashing the strings to integers), radix sort works on data types other than just integers. Radix sort \
is a non-comparative sorting algorithm. It avoids comparison by creating and distributing elements into buckets \
according to their radix. For example, a binary system (using numbers 0 and 1) has a radix of 2 and a decimal \
system (using numbers 0 to 9) has a radix of 10. Radix sorts can be implemented to start at either the most \
significant digit (MSD) or least significant digit (LSD). For example, with 1234, one could start with 1(MSD) \
or 4(LSD).Radix sort will operate on n d-digit numbers where each digit can be one of at most b different values \
(since b is the base (or radix) being used). For example, in base 10, a digit can be 0,1,2,3,4,5,6,7,8 or 9.\
Radix sort uses counting sort on each digit. Each pass over n d-digit numbers will take O(n + b) time, and \
there are d passes total. Therefore, the total running time of radix sort is O(d(n+b)). When d is a constant \
and b isnt much larger than n (in other words,b=O(n)), then radix sort takes linear time.The space complexity \
comes from counting sort, which requires O(n+b) space to hold the counts, indices, and output lists.', '12, Explain \
how to find 100 largest numbers out of an array of 1 billion numbers ---The brute force solution will be to \
sort the array in O(n log n) time complexity and take the last 100 numbers but you can do better. You can keep \
a priority queue (implemented as a heap) of the 100 biggest numbers, iterate through the billion numbers, whenever \
you encounter a number greater than the smallest number in the queue (the head of the queue), remove the head of \
the queue and add the new number to the queue. In general, if you need the largest K numbers from a set of N \
numbers, the complexity is O(N log K) rather than O(N log N), this can be very significant when K is very small \
comparing to N.You can also apply problem solving process. Ask interviewer the range or meaning of these numbers \
to make the problem clear. If, for example, these numbers stands for peoples age of within a country \
(e.g. China), then its a much easier problem. With a reasonable assumption that nobody alive is older than 200, \
you can use an int array of size 200 (maybe 201) to count the number of people with the same age in just one \
iteration. Here the index means the age. After this its a piece of cake to find 100 largest number. \
By the way this also is called counting sort. Counting sort takes O(n + k) time and O(n + k) space, where n \
is the number of items we are sorting and k is the number of possible values.','13, When Merge Sort is \
preferred over Quick Sort? Mergesort advantages over Quicksort are: Mergesort is worst-case O(n log n), \
Quicksort is average case O(n log n), but has a worst case of O(n2). Mergesort is stable by design, equal \
elements keep their original order. Mergesort is well suited to be implemented parallel (multithreading) \
Mergesort uses (about 30%) less comparisons than QuickSort. This is an often overlooked advantage, because a \
comparison can be quite expensive (e.g. when comparing several fields of database rows) Mergesort is a superior \
algorithm for sorting linked lists, since it makes fewer total comparisons. Linked lists can be merged with \
only O(1) space overhead instead of O(n) space overhead. Quicksort usually is better than mergesort for two \
reasons: Quicksort has better locality of reference than mergesort, which means that the accesses performed in \
quicksort are usually faster than the corresponding accesses in mergesort. Quicksort uses worst-case O(log n) \
memory (if implemented correctly), while mergesort requires O(n) memory due to the overhead of merging.\
Scenarios when quicksort is worse than mergesort: Array is already sorted, All elements in the array are the same\
Array is sorted in reverse order', '14, Why is Merge sort preferred over Quick sort for sorting Linked Lists? ---\
Quicksort depends on being able to index (or random access) into an array or similar structure. When thats \
possible, its hard to beat Quicksort.You cant index directly into a linked list very quickly. That is, \
if myList is a linked list, then myList[x], were it possible to write such syntax, would involve starting \
at the head of the list and following the first x links. That would have to be done twice for every comparison \
that Quicksort makes, and that would get expensive real quick.Same thing on disk - Quicksort would have to \
seek and read every item it wants to compare.Merge sort is faster in these situations because it reads the \
items sequentially, typically making log(n) passes over the data. There is much less I/O involved, and much \
less time spent following links in a linked list. Quicksort is fast when the data fits into memory and can be \
addressed directly. Mergesort is faster when data wont fit into memory or when its expensive to get to an item.']

TestEngList = ['1, What is the difference between the QA and software testing? --- The role of QA (Quality \
Assurance) is to monitor the quality of the "process" used to produce the software. While the software testing, \
is the process of ensuring the functionality of final product meets the users requirement.', '2, What is the \
difference between build and release? Build: It is a number given to Installable software that is given to the \
testing team by the development team. Release: It is a number given to Installable software that is handed over \
to the customer by the tester or developer', '3, What is bug leakage and bug release? --- Bug release is when \
software or an application is handed over to the testing team knowing that the defect is present in a release. \
During this the priority and severity of bug is low, as bug can be removed before the final handover. Bug leakage \
is something, when the bug is discovered by the end users or customer, and not detected by the testing team while \
testing the software.', '4, What is data driven testing? --- Data driven testing is an automation testing \
framework, which tests the different input values on the AUT. These values are read directly from the data files. \
The data files may include csv files, excel files, data pools and many more', '5, Explain the steps for Bug Cycle? ---\
 Once the bug is identified by the tester, it is assigned to the development manager in open status. If the bug is \
a valid defect the development team will fix it. If it is not a valid defect, the defect will be ignored and \
marked as rejected. The next step will be to check whether it is in scope. If the bug is not the part of the \
current release then the defects are postponed. If the defect or bug is raised earlier then the tester will \
assign a DUPLICATE status. When bug is assigned to developer to fix, it will be given a IN-PROGRESS status\
Once the defect is repaired, the status will change to FIXED at the end the tester will give CLOSED status if \
it passes the final test', '6, Mention the different types of software testing? --- Unit testing, Integration \
testing and regression testing, Shakeout testing, Smoke testing, Functional testing, Performance testing, White \
box and Black box testing, Alpha and Beta testing, Load testing and stress testing, System testing', '7, What is \
branch testing and what is boundary testing? The testing of all the branches of the code, which is tested once, \
is known as branch testing. While the testing, that is focused on the limit conditions of the software is known as \
boundary testing', '8, What are the contents of test plans and test cases? --- Testing objectives, Testing scope\
Testing the frame, The environment, Reason for testing, The criteria for entrance and exit, Deliverables, \
Risk factors', '9, What is Agile testing and what is the importance of Agile testing? --- Agile testing is \
software testing, is testing using Agile Methodology. The importance of this testing is that, unlike normal \
testing process, this testing does not wait for the development team to complete the coding first and then doing \
testing. The coding and testing both goes simultaneously. It requires continuous customer interaction','What are \
the tools used by a tester while testing? Selenium, Firebug, OpenSTA, WinSCP, YSlow for FireBug, Web Developer \
toolbar for firebox', '10, What are the tools used by a tester while testing? --- Selenium, Firebug, OpenSTA, \
WinSCP, YSlow for FireBug, Web Developer toolbar for firebox', '11, Explain stress testing, load testing and \
volume testing? Load Testing: Testing an application under heavy but expected load is known as Load Testing. \
Here, the load refers to the large volume of users, messages, requests, data, etc.Stress Testing: When the \
load placed on the system is raised or accelerated beyond the normal range then it is known as Stress Testing. \
Volume Testing: The process of checking the system, whether the system can handle the required amounts of data, \
user requests, etc. is known as Volume Testing','12, What is the difference between functional and non-functional \
testing? --- Functional Testing: Performed before non-functional testing, Based on customer requirements, Describes \
what the product does; Non-Functional Testing: Performed after functional testing, Based on customers expectations,\
Describes how the product works', '13, What are the different methods of testing? --- There are three methods of \
software testing and they are as follows: Black-box testing: It is a testing strategy based solely on requirements \
and specifications. In this strategy, it requires no knowledge of internal paths, structures, or implementation of \
the software being tested; White box testing: It is a testing strategy based on internal paths, code structures, \
and implementation of the software being tested. White box testing generally requires detailed programming \
skills; Gray box testing: It is a strategy for software debugging in which the tester has limited knowledge \
of the internal details of the program.']





def draws():
    choice = int(input('Please choose which role you would like to interview? 1 for frontend, 2 for backend Python,'
                   '3 for DevOps Eng, 4 for Algorithm, 5 for Test Engineer :)  '))
    if choice == 1:
        while True:
            try:
                n = []
                numb = int(input('Please type a number for how many times will the draw stops for Frontend Questions:  '))
                for i in range(numb):
                    Interview_num = randint(0 + 1, len(FrontEndList) - 1)
                    n = FrontEndList[Interview_num]
                print('this is final result: ', n)
                break
            except:
                print('Only integers accepted! Please try again. ')
    elif choice == 2:
        while True:
            try:
                n = []
                numb = int(input('Please type a number for how many times will the draw stops for Python Backend Questions:  '))
                for i in range(numb):
                    Interview_num = randint(0 + 1, len(BackEndPythonList) - 1)
                    n = BackEndPythonList[Interview_num]
                print('this is final result: ', n)
                break
            except:
                print('Only integers accepted! Please try again. ')
    elif choice == 3:
        while True:
            try:
                n = []
                numb = int(input(
                    'Please type a number for how many times will the draw stops for Python Backend Questions:  '))
                for i in range(numb):
                    Interview_num = randint(0 + 1, len(DevOpsEngList) - 1)
                    n = DevOpsEngList[Interview_num]
                print('this is final result: ', n)
                break
            except:
                print('Only integers accepted! Please try again. ')
    elif choice == 4:
        while True:
            try:
                n = []
                numb = int(input(
                    'Please type a number for how many times will the draw stops for Algorithm Questions:  '))
                for i in range(numb):
                    Interview_num = randint(0 + 1, len(AlgorithmList) - 1)
                    n = AlgorithmList[Interview_num]
                print('this is final result: ', n)
                break
            except:
                print('Only integers accepted! Please try again. ')

    elif choice == 5:
        while True:
            try:
                n = []
                numb = int(input(
                    'Please type a number for how many times will the draw stops for Test Eng Questions:  '))
                for i in range(numb):
                    Interview_num = randint(0 + 1, len(TestEngList) - 1)
                    n = TestEngList[Interview_num]
                print('this is final result: ', n)
                break
            except:
                print('Only integers accepted! Please try again. ')

draws()


'''
aa = {'1':'asdfasdf','2':'fdsafads','3':'32113qwdasd'}
print(aa['1'])'''