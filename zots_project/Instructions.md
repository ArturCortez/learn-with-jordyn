>>Create a file called zot.py which defines the following classes:
> 
    1.Zot;
    2.TemplateRenderer; 
    3.DNA
>
> Such that all of the following are true:
>
> A Zot is a self rendering Jinja template
> A Zot has DNA
> DNA has a property template_name and a state
> The state of the DNA is used to create the inputs to the render_template method of the template_renderer
> Each Zot has a render method which renders self.dna.template_name
> Each Zot has a write method which writes the Zot to a file
>
> Create a file called zot2.py , the first line of which is import zot. 
>
> You may not redefine anything from zot in zot2. 
>
> When run, zot2.py must create zot3.py, and zot3.py must create zot4.py (Which in turns creates zot5.py, and so on ad infinitum)
> 
> You may not directly edit zots3.py
>
>
>