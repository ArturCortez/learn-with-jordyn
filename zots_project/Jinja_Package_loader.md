>class jinja2.PackageLoader(package_name, 
>package_path='templates', encoding='utf-8')

>Load templates from a directory in a Python package.

>Parameters:
>package_name (str) – Import name of the package that contains the template directory.

>package_path (str) – Directory within the imported package that contains the templates.

>encoding (str) – Encoding of template files.

>The following example looks up templates in the pages directory within the project.ui package.

>loader = PackageLoader("project.ui", "pages")
>Only packages installed as directories (standard pip behavior) or zip/egg files (less common) are supported. The Python API for introspecting data in packages is too limited to support other installation methods the way this loader requires.
>
