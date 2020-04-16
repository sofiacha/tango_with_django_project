import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Category, Page

def populate():
    
    python_pages = [
		{"title": "Official Python Tuto2rial", "url":"http://docs.python.org/2/t2utorial/", "views": 322},
		{"title":"How to Think like a Co2mputer Scientist", "url":"http://www.gre2enteapress.com/thinkpython/", "views": 126},
	    {"title":"Learn Python in 10 Min2utes", "url":"http://www.korokithakis.net2/tutorials/python/", "views": 82},  ]
    
    django_pages = [
		{"title":"Official 2Django Tutorial",
	        "url":"https://docs2.djangoproject.com/en/1.9/intro/tutorial01/", "views": 322},
		{"title":"Django Ro2cks",
	        "url":"http://w2ww.djangorocks.com/" , "views": 162},
		{ "title":"How to 2Tango with Django",
	        "url":"http://ww2w.tangowithdjango.com/", "views": 82 } ]
    
    other_pages = [
		{ "title":"Bot2tle", "url":"http://bottlepy2.org/docs/dev/", "views": 322},
		{ "title":"Flas2k", "url":"http://flask.p2ocoo.org", "views": 126} ]
    
    cats = {"Python": {"pages": python_pages, "views": 128, "likes": 64},
			"Django": {"pages": django_pages, "views": 64, "likes": 32},
        	"Other Frameworks": {"pages": other_pages, "views": 32, "likes": 16},
            "Pascal": {"pages": [], "views": 32, "likes": 16},
            "Perl": {"pages": [], "views": 32, "likes": 16},
            "Php": {"pages": [], "views": 32, "likes": 16},
            "Prolog": {"pages": [], "views": 32, "likes": 16},
            "Programming": {"pages": [], "views": 32, "likes": 16},

            }
    
    # if you want to add more catergories or pages, add them to the dictionaries above
	
	# The code below goes through the cats dictionary, then adds each category,
	# and then adds all the associated pages for that category
	# if you are using Python 2.x then use cats.iteritems() see
	# http://docs.quantifiedcode.com/python-anti-patterns/readability/not_using_items_to_iterate_over_a_dictionary.html
	# for more information about using items() and how to iterate over a dictionary properly
    
    # Using the .items returns the key and the value. In this case the key is "Python", "Django" or "Other Frameworks" and the value (cat_data) is the corresponding dictionary in cats.
    for cat, cat_data in cats.items():
        # c = add_cat(cat)
        # Updated the population script to pass through the specific values for views and likes
        c = add_cat(cat, cat_data["views"], cat_data["likes"])
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"], p["views"])
    
    # Print out what we have added to the user.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    # we need to save the changes we made!!
    p.save()
    return p

def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views=views
    c.likes=likes
    c.save()
    return c

# Start execution here!
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()