### ZOTS

#### This project requires the implementation of abstract classes and methods and the implementation fo interfaces.


Strategy:
#### acording to refactoring guru at: https://refactoring.guru/design-patterns/state/python/example#:~:text=State%20is%20a%20behavioral%20design,of%20acting%20on%20its%20own.
> State is a behavioral design pattern that allows an object to 
> change the behavior when its internal state changes.
> As I understand it, this pattern has the following elements:
>   1. An Abstract class, with the blueprint of the States. In this case, the State class
>   2. A Concrete Class, implementing variations of the blueprint of the abstract class. In our case, the Home(), 
>    Products() etc... This works mimicking the Interface functionality of other languages.
>   3. A Context class, which will encapsulate the many possibles states, changing behavior each time a new state is implemented. In our case 
>    this was the Dna class.


>After implementing the State Pattern, the Zots class, in another file will inherit the Dna class via the
>transition_to method. From here on, any State changes will be applied to Zot object, instantiated from the Zot class,
>not the Dna class, since this was only used to provide inheritance to Zot.
> 

> We then use the various states to give the inputs to the Zot class. The Zot class is responsible for rendering and
> Jinja2 template, so the Dna's multiple states will provide variables. In our case, two strings: filename and main_name, 
> and a list of strings that the template will loop through.
> 

> After that, we created the zot2.py file, importing Zot and creating a ZotFactory class that check the name of the 
> current script and increments in a way that zot2.py will only produce zot3.py and so on. Nothing of the Zot class is
> altered in the subclass.



 
 
