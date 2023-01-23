from .component_interface import *


class AlertComponent(Component):
  def __init__(self, text: str, badge: str = '', color: str = 'indigo'):    
    self.text = text
    self.badge = badge
    self.color = color

  def to_html(self):
    return '''<div class="text-center py-4 lg:px-4">
<div class="p-2 bg-''' + self.color + '''-800 items-center text-''' + self.color + '''-100 leading-none lg:rounded-full flex lg:inline-flex" role="alert">
    <span class="flex rounded-full bg-''' + self.color + '''-500 uppercase px-2 py-1 text-xs font-bold mr-3">''' + self.badge + '''</span>
    <span class="font-semibold mr-2 text-left flex-auto">''' + self.text + '''</span>            
</div>
</div>'''

class CardComponent(Component):
  def __init__(self, components: list = None, classes: str = ''):    
    # https://stackoverflow.com/questions/4841782/python-constructor-and-default-value
    self.components = components or []
    self.classes = classes

  def to_html(self):
    return '''<div class="block max-w-sm p-6 bg-white border border-gray-200 rounded-lg shadow-md hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-700 dark:hover:bg-gray-700 ''' + self.classes + '''">
    ''' + '\n'.join(map(lambda x: x.to_html(), self.components)) + ''' 
</div>'''

  def add(self, component):
    self.components.append(component)
    return self

  def add_component(self, component):
    self.components.append(component)
    return self
  def add_html(self, value: str):    
    self.components.append(HtmlComponent(value))
    return self
    

  def add_text(self, value: str):    
    self.components.append(TextComponent(value))
    return self
    

  def add_link(self, text: str, url: str):    
    self.components.append(LinkComponent(text, url))
    return self
    

  def add_plainlink(self, text: str, url: str, classes: str = ''):    
    self.components.append(PlainlinkComponent(text, url, classes))
    return self
    

  def add_image(self, url: str, alt: str):    
    self.components.append(ImageComponent(url, alt))
    return self
    

  def add_header(self, text: str, size: int = 5):    
    self.components.append(HeaderComponent(text, size))
    return self
    

  def add_card(self, components: list = None, classes: str = ''):    
    self.components.append(CardComponent(components, classes))
    return self
    

  def add_alert(self, text: str, badge: str = '', color: str = 'indigo'):    
    self.components.append(AlertComponent(text, badge, color))
    return self
    

  def add_hero(self, title: str, subtitle: str = '', image: str = '', color: str = 'indigo'):    
    self.components.append(HeroComponent(title, subtitle, image, color))
    return self
    

  def add_divider(self):    
    self.components.append(DividerComponent())
    return self
    

  def add_form(self, action: str, components: list = None, method: str = 'GET'):    
    self.components.append(FormComponent(action, components, method))
    return self
    


  def add_pandastable(self, dataframe: str):
    advanced_add_pandastable(self, dataframe)
    return self
    


  def add_emgithub(self, url: str):
    advanced_add_emgithub(self, url)
    return self
    

class CodeComponent(Component):
  def __init__(self, value: str, header: str = ''):    
    self.value = value
    self.header = header

  def to_html(self):
    return '''<div class="mx-auto my-10 max-w-3xl">
    <div class="flex h-11 w-full items-center justify-start space-x-1.5 rounded-t-lg bg-gray-900 px-3">
        <span class="h-3 w-3 rounded-full bg-red-400"></span>
        <span class="h-3 w-3 rounded-full bg-yellow-400"></span>
        <span class="h-3 w-3 rounded-full bg-green-400"></span>
        <code class="pl-5 text-lime-500">''' + self.header + '''</code>
    </div>
    <div class="w-full border-t-0 bg-gray-700 pb-5">
        <code class="text-gray-500">&gt&gt&gt</code>
        <code class="text-white">''' + self.value + '''</code>
    </div>
</div>'''

class CodeeditorComponent(Component):
  def __init__(self, value: str, language: str = 'python'):    
    self.value = value
    self.language = language

  def to_html(self):
    return '''<style type="text/css" media="screen">
#editorContainer {
    width: calc( 100vw - 40px );
    height: 500px;
    max-height: calc( 80vh - 60px );
    position: relative;
    background-color: red;
}
#editor { 
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
}
</style>

<div id="editorContainer">
    <div id="editor">''' + self.value + '''</div> 
</div>
<script src="https://cdn.jsdelivr.net/gh/ajaxorg/ace-builds/src-noconflict/ace.js" type="text/javascript" charset="utf-8"></script>
<script>
    var editor = ace.edit("editor");
    editor.setTheme("ace/theme/monokai");
    editor.session.setMode("ace/mode/''' + self.language + '''");

    const savedCode = localStorage.getItem('code');

    if (savedCode) {
        editor.setValue(savedCode);
    }
</script>'''

class DividerComponent(Component):
  def __init__(self):    
    pass

  def to_html(self):
    return '''<hr class="my-5 border-gray-300 w-full">'''

class FooterComponent(Component):
  def __init__(self, title: str, subtitle: str = '', logo: str = '', components: list = None):    
    self.title = title
    self.subtitle = subtitle
    self.logo = logo
    # https://stackoverflow.com/questions/4841782/python-constructor-and-default-value
    self.components = components or []

  def to_html(self):
    return '''<footer class="text-gray-600 body-font">
    <div class="container px-5 py-24 mx-auto flex md:items-center lg:items-start md:flex-row md:flex-nowrap flex-wrap flex-col">
        <div class="w-64 flex-shrink-0 md:mx-0 mx-auto text-center md:text-left">
            <a class="flex title-font font-medium items-center md:justify-start justify-center text-gray-900"><img class="object-scale-down h-10" src="''' + self.logo + '''"><span class="ml-3 text-xl">''' + self.title + '''</span></a>
            <p class="mt-2 text-sm text-gray-500">''' + self.subtitle + '''</p>
        </div>
        <div class="flex-grow flex flex-wrap md:pl-20 -mb-10 md:mt-0 mt-10 md:text-left text-center">
            ''' + '\n'.join(map(lambda x: x.to_html(), self.components)) + ''' 
        </div>
    </div>
</footer>'''

  def add(self, component):
    self.components.append(component)
    return self

  def add_component(self, component):
    self.components.append(component)
    return self
  def add_footercategory(self, title: str, components: list = None):    
    self.components.append(FootercategoryComponent(title, components))
    return self
    

class FootercategoryComponent(Component):
  def __init__(self, title: str, components: list = None):    
    self.title = title
    # https://stackoverflow.com/questions/4841782/python-constructor-and-default-value
    self.components = components or []

  def to_html(self):
    return '''<div class="lg:w-1/4 md:w-1/2 w-full px-4">
    <h2 class="title-font font-medium text-gray-900 tracking-widest text-sm mb-3 uppercase">''' + self.title + '''</h2>
    <nav class="list-none mb-10">
        ''' + '\n'.join(map(lambda x: x.to_html(), self.components)) + ''' 
    </nav>
</div>'''

  def add(self, component):
    self.components.append(component)
    return self

  def add_component(self, component):
    self.components.append(component)
    return self
  def add_footerlink(self, title: str, url: str):    
    self.components.append(FooterlinkComponent(title, url))
    return self
    

class FooterlinkComponent(Component):
  def __init__(self, title: str, url: str):    
    self.title = title
    self.url = url

  def to_html(self):
    return '''<li><a href="''' + self.url + '''" class="text-gray-600 hover:text-gray-800">''' + self.title + '''</a></li>'''

class FormComponent(Component):
  def __init__(self, action: str, components: list = None, method: str = 'GET'):    
    self.action = action
    # https://stackoverflow.com/questions/4841782/python-constructor-and-default-value
    self.components = components or []
    self.method = method

  def to_html(self):
    return '''<form class="max-w-full" style="width: 500px" action="''' + self.action + '''" method="''' + self.method + '''">
    ''' + '\n'.join(map(lambda x: x.to_html(), self.components)) + ''' 
</form>'''

  def add(self, component):
    self.components.append(component)
    return self

  def add_component(self, component):
    self.components.append(component)
    return self
  def add_link(self, text: str, url: str):    
    self.components.append(LinkComponent(text, url))
    return self
    

  def add_image(self, url: str, alt: str):    
    self.components.append(ImageComponent(url, alt))
    return self
    

  def add_formtext(self, label: str, name: str, placeholder: str):    
    self.components.append(FormtextComponent(label, name, placeholder))
    return self
    

  def add_formemail(self, label: str = 'Your E-mail', name: str = 'email', placeholder: str = ''):    
    self.components.append(FormemailComponent(label, name, placeholder))
    return self
    

  def add_textarea(self, label: str = 'Your Message', name: str = 'message', placeholder: str = 'Leave a comment...'):    
    self.components.append(TextareaComponent(label, name, placeholder))
    return self
    

  def add_formsubmit(self, label: str = 'Submit'):    
    self.components.append(FormsubmitComponent(label))
    return self
    

class FormemailComponent(Component):
  def __init__(self, label: str = 'Your E-mail', name: str = 'email', placeholder: str = ''):    
    self.label = label
    self.name = name
    self.placeholder = placeholder

  def to_html(self):
    return '''<div class="mb-6">
    <label for="''' + self.name + '''" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">''' + self.label + '''</label>
    <input type="email" name="''' + self.name + '''" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="''' + self.placeholder + '''" required>
</div>'''

class FormsubmitComponent(Component):
  def __init__(self, label: str = 'Submit'):    
    self.label = label

  def to_html(self):
    return '''<button type="submit" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">''' + self.label + '''</button>'''

class FormtextComponent(Component):
  def __init__(self, label: str, name: str, placeholder: str):    
    self.label = label
    self.name = name
    self.placeholder = placeholder

  def to_html(self):
    return '''<div class="mb-6">
    <label for="''' + self.name + '''" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">''' + self.label + '''</label>
    <input type="text" name="''' + self.name + '''" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="''' + self.placeholder + '''" required>
</div>'''

class HeaderComponent(Component):
  def __init__(self, text: str, size: int = 5):    
    self.text = text
    self.size = size

  def to_html(self):
    return '''<p class="mb-4 text-4xl font-extrabold leading-none tracking-tight text-gray-900 md:text-5xl lg:text-''' + str(self.size) + '''xl dark:text-white">''' + self.text + '''</p>'''

class HeroComponent(Component):
  def __init__(self, title: str, subtitle: str = '', image: str = '', color: str = 'indigo'):    
    self.title = title
    self.subtitle = subtitle
    self.image = image
    self.color = color

  def to_html(self):
    return '''<section class="bg-white">
    <div class="grid max-w-screen-xl px-4 py-8 mx-auto lg:gap-8 xl:gap-0 lg:py-16 lg:grid-cols-12">
        <div class="mr-auto place-self-center lg:col-span-7">
            <h1 class="max-w-2xl mb-4 text-4xl font-extrabold tracking-tight leading-none md:text-5xl xl:text-6xl">''' + self.title + '''</h1>
            <p class="max-w-2xl mb-6 font-light text-gray-500 lg:mb-8 md:text-lg lg:text-xl">''' + self.subtitle + '''</p>
            <a href="#" class="inline-flex items-center justify-center px-5 py-3 mr-3 text-base font-medium text-center text-white rounded-lg bg-''' + self.color + '''-700 hover:bg-''' + self.color + '''-800 focus:ring-4 focus:ring-''' + self.color + '''-300">
                Button 1                        
            </a>
            <a href="#" class="inline-flex items-center justify-center px-5 py-3 text-base font-medium text-center text-gray-900 border border-gray-300 rounded-lg hover:bg-gray-100 focus:ring-4 focus:ring-gray-100">
                Button 2
            </a> 
        </div>
        <div class="hidden lg:mt-0 lg:col-span-5 lg:flex">
            <img src="''' + self.image + '''" >
        </div>                
    </div>
</section>'''

class HtmlComponent(Component):
  def __init__(self, value: str):    
    self.value = value

  def to_html(self):
    return '''''' + self.value + ''''''

class ImageComponent(Component):
  def __init__(self, url: str, alt: str):    
    self.url = url
    self.alt = alt

  def to_html(self):
    return '''<img class="max-w-fit h-auto rounded-lg" src="''' + self.url + '''" alt="''' + self.alt + '''">'''

class LinkComponent(Component):
  def __init__(self, text: str, url: str):    
    self.text = text
    self.url = url

  def to_html(self):
    return '''<p class="text-gray-500 dark:text-gray-400">
    <a href="''' + self.url + '''" class="inline-flex items-center font-medium text-blue-600 dark:text-blue-500 hover:underline">
    ''' + self.text + '''
    <svg aria-hidden="true" class="w-5 h-5 ml-1" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
    </a>
</p>'''

class NavbarComponent(Component):
  def __init__(self, title: str, logo: str = '', components: list = None):    
    self.title = title
    self.logo = logo
    # https://stackoverflow.com/questions/4841782/python-constructor-and-default-value
    self.components = components or []

  def to_html(self):
    return '''<header class="text-white body-font">
    <div class="gradient-background mx-auto flex flex-wrap p-5 flex-col md:flex-row items-center">
        <a href="/" class="flex title-font font-bold items-center text-gray-100 mb-4 md:mb-0"><img class="object-scale-down h-10" src="''' + self.logo + '''"><span class="ml-3 text-4xl">''' + self.title + '''</span></a>
        <nav class="md:ml-auto flex flex-wrap items-center text-base justify-center">
          <button onclick="toggleDarkMode()" type="button" class="mx-3 px-3 py-2 text-xs font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800 bg-gradient-to-br from-purple-600 to-blue-500 group-hover:from-purple-600 group-hover:to-blue-500">
            Dark Mode
          </button>            
            ''' + '\n'.join(map(lambda x: x.to_html(), self.components)) + ''' 
        </nav>
        <button class="inline-flex items-center bg-gray-100 text-black border-0 py-1 px-3 focus:outline-none hover:bg-gray-200 rounded text-base mt-4 md:mt-0">Sign In<svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-4 h-4 ml-1" viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"></path></svg></button>
    </div>
</header>'''

  def add(self, component):
    self.components.append(component)
    return self

  def add_component(self, component):
    self.components.append(component)
    return self
  def add_link(self, text: str, url: str):    
    self.components.append(LinkComponent(text, url))
    return self
    

  def add_plainlink(self, text: str, url: str, classes: str = ''):    
    self.components.append(PlainlinkComponent(text, url, classes))
    return self
    

class Page(Component):
  def __init__(self, title: str, components: list = None, auto_navbar: bool = True, auto_footer: bool = True):    
    self.title = title
    # https://stackoverflow.com/questions/4841782/python-constructor-and-default-value
    self.components = components or []
    self.auto_navbar = auto_navbar
    self.auto_footer = auto_footer

  def to_html(self):
    return '''<div class="container px-5 py-24 mx-auto max-w-fit">
    ''' + '\n'.join(map(lambda x: x.to_html(), self.components)) + ''' 
</div>'''

  def add(self, component):
    self.components.append(component)
    return self

  def add_component(self, component):
    self.components.append(component)
    return self
  def add_html(self, value: str):    
    self.components.append(HtmlComponent(value))
    return self
    

  def add_text(self, value: str):    
    self.components.append(TextComponent(value))
    return self
    

  def add_link(self, text: str, url: str):    
    self.components.append(LinkComponent(text, url))
    return self
    

  def add_plainlink(self, text: str, url: str, classes: str = ''):    
    self.components.append(PlainlinkComponent(text, url, classes))
    return self
    

  def add_image(self, url: str, alt: str):    
    self.components.append(ImageComponent(url, alt))
    return self
    

  def add_header(self, text: str, size: int = 5):    
    self.components.append(HeaderComponent(text, size))
    return self
    

  def add_card(self, components: list = None, classes: str = ''):    
    self.components.append(CardComponent(components, classes))
    return self
    

  def add_alert(self, text: str, badge: str = '', color: str = 'indigo'):    
    self.components.append(AlertComponent(text, badge, color))
    return self
    

  def add_hero(self, title: str, subtitle: str = '', image: str = '', color: str = 'indigo'):    
    self.components.append(HeroComponent(title, subtitle, image, color))
    return self
    

  def add_code(self, value: str, header: str = ''):    
    self.components.append(CodeComponent(value, header))
    return self
    

  def add_divider(self):    
    self.components.append(DividerComponent())
    return self
    

  def add_section(self, id: str, name: str, level: int = 1):    
    self.components.append(SectionComponent(id, name, level))
    return self
    

  def add_form(self, action: str, components: list = None, method: str = 'GET'):    
    self.components.append(FormComponent(action, components, method))
    return self
    


  def add_pandastable(self, dataframe: str):
    advanced_add_pandastable(self, dataframe)
    return self
    

  def add_navbar(self, title: str, logo: str = '', components: list = None):    
    self.components.append(NavbarComponent(title, logo, components))
    return self
    

  def add_footer(self, title: str, subtitle: str = '', logo: str = '', components: list = None):    
    self.components.append(FooterComponent(title, subtitle, logo, components))
    return self
    

  def add_sidebar(self, components: list = None):    
    self.components.append(SidebarComponent(components))
    return self
    

  def add_codeeditor(self, value: str, language: str = 'python'):    
    self.components.append(CodeeditorComponent(value, language))
    return self
    


  def add_emgithub(self, url: str):
    advanced_add_emgithub(self, url)
    return self
    

class PlainlinkComponent(Component):
  def __init__(self, text: str, url: str, classes: str = ''):    
    self.text = text
    self.url = url
    self.classes = classes

  def to_html(self):
    return '''<a class="''' + self.classes + '''" href="''' + self.url + '''">''' + self.text + '''</a>'''

class SectionComponent(Component):
  def __init__(self, id: str, name: str, level: int = 1):    
    self.id = id
    self.name = name
    self.level = level

  def to_html(self):
    return '''<span id=''' + self.id + '''></span>'''

class SidebarComponent(Component):
  def __init__(self, components: list = None):    
    # https://stackoverflow.com/questions/4841782/python-constructor-and-default-value
    self.components = components or []

  def to_html(self):
    return '''<aside class="hidden md:block flex w-72 flex-col space-y-2 bg-slate-200 p-2 h-screen sticky top-0">
    <div class="sticky top-0">
        ''' + '\n'.join(map(lambda x: x.to_html(), self.components)) + ''' 
    </div>
</aside>'''

  def add(self, component):
    self.components.append(component)
    return self

  def add_component(self, component):
    self.components.append(component)
    return self
  def add_sidebarcategory(self, title: str, components: list = None):    
    self.components.append(SidebarcategoryComponent(title, components))
    return self
    

class SidebarcategoryComponent(Component):
  def __init__(self, title: str, components: list = None):    
    self.title = title
    # https://stackoverflow.com/questions/4841782/python-constructor-and-default-value
    self.components = components or []

  def to_html(self):
    return '''<div class="mb-8">
    <h2 class="text-lg font-medium text-gray-900 tracking-wider uppercase mb-3">''' + self.title + '''</h2>
    <ul class="ml-5 list-none">
        ''' + '\n'.join(map(lambda x: x.to_html(), self.components)) + ''' 
    </ul>
</div>'''

  def add(self, component):
    self.components.append(component)
    return self

  def add_component(self, component):
    self.components.append(component)
    return self
  def add_sidebarlink(self, title: str, url: str):    
    self.components.append(SidebarlinkComponent(title, url))
    return self
    

class SidebarlinkComponent(Component):
  def __init__(self, title: str, url: str):    
    self.title = title
    self.url = url

  def to_html(self):
    return '''<li><a href="''' + self.url + '''" class="text-gray-600 hover:text-gray-800">''' + self.title + '''</a></li>'''

class TextComponent(Component):
  def __init__(self, value: str):    
    self.value = value

  def to_html(self):
    return '''<p class="mb-6 text-lg font-normal text-gray-500 lg:text-xl sm:px-16 xl:px-48 dark:text-gray-400">''' + self.value + '''</p>'''

class TextareaComponent(Component):
  def __init__(self, label: str = 'Your Message', name: str = 'message', placeholder: str = 'Leave a comment...'):    
    self.label = label
    self.name = name
    self.placeholder = placeholder

  def to_html(self):
    return '''<div class="mb-6">
    <label for="''' + self.name + '''" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">''' + self.label + '''</label>
    <textarea name="''' + self.name + '''" rows="4" class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="''' + self.placeholder + '''"></textarea>
</div>'''


#
#
# Begin Manual Code
#
#
#
from urllib.parse import quote

def advanced_add_pandastable(self, df):
    # Pandas dataframe to html
    html = '''<div class="p-8">'''

    html += '''<div class="relative overflow-x-auto shadow-md sm:rounded-lg">'''

    html += '''<table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">'''

    # Pandas DataFrame columns to 
    html += '''<thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">'''

    html += "<tr>"

    # Get df index name
    if df.index.name is not None:
        html += '''<th scope="col" class="px-6 py-3">''' + df.index.name +  "</th>"

    for column in df.columns:
        html += '''<th scope="col" class="px-6 py-3">''' + column + "</th>"

    html += "</tr>"

    html += "</thead>"

    # Pandas DataFrame rows to html
    html += "<tbody>"
    i = 0
    for index, row in df.iterrows():
        if i % 2 == 0:
            html += '''<tr class="bg-white border-b dark:bg-gray-900 dark:border-gray-700">'''
        else:
            html += '''<tr class="bg-gray-50 border-b dark:bg-gray-800 dark:border-gray-700">'''

        for column in df.columns:
            html += '''<td class="px-6 py-4">''' + format_input(row[column]) + "</td>"
        html += "</tr>"
        i += 1

    html += "</tbody>"

    html += "</table>"

    html += "</div>"

    html += "</div>"

    self.components.append(HtmlComponent(html))
    return self


"""
A function that formats input into a human-readable string:
Input: An arbitrary type that could be string, integer, floating point, a numpy object, a pandas datetime, or something else
Output: String

Dates should be formatted using ISO-8601. Numbers below 10 should include 2 decimal places. Numbers between 10 and 100 should have 1 decimal place. Numbers between 100 and 1000 should have 0 decimal places. Numbers between 1000 and 1000000 should have 0 decimal places and be formatted with a comma for the thousands separator. Numbers between 1000000 and 1000000000 should be formatted as X.Y million. Numbers above 1000000000 should be formatted as X.Y billion
"""


def format_input(input):
    print("Input Type = ", type(input))
    is_int = "int" in type(input).__name__
    is_float = "float" in type(input).__name__

    if isinstance(input, str):
        return input
    elif is_float or is_int:
        if input < 10:
            if is_float:
                return '{:.2f}'.format(input)
            else:
                return str(input)
        elif input < 100:
            if is_float:
                return '{:.1f}'.format(input)
            else:
                return str(input)
        elif input < 1000:
            return '{:.0f}'.format(input)
        elif input < 1000000:
            return '{:,.0f}'.format(input)
        elif input < 1000000000:
            return '{:.1f} million'.format(input / 1000000)
        else:
            return '{:.1f} billion'.format(input / 1000000000)
    elif callable(getattr(input, "isoformat", None)):
        iso = input.isoformat()

        if "T00:00:00" in iso:
            return iso[0:10]

        return iso
    else:
        return str(input)


def advanced_add_emgithub(self, url):
    quoted_url = quote(url)

    emgithub = '''
    <script src="https://emgithub.com/embed-v2.js?target=''' + quoted_url +  '''&style=vs2015&type=code&showBorder=on&showLineNumbers=on&showFileMeta=on&showFullPath=on&showCopy=on&fetchFromJsDelivr=on"></script>
    '''

    self.components.append(HtmlComponent(emgithub))
