from setuptools import setup, find_packages

version = '1.1'

setup(name='policy.localauthorities',
      version=version,
      description="",
      long_description=open("README.rst").read() + "\n" +
                       open("CHANGES.txt").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='https://github.com/collective/',
      license='gpl',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['policy'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone',
          'Products.LinguaPlone',
          'cirb.zopemonitoring',
          # -*- Extra requirements: -*-
          'cirb.footersitemap',
    	  'collective.ckeditor',
          'collective.plonefinder',
          'webcouturier.dropdownmenu',
          'collective.easyslider',
          'collective.js.jqueryui',
          'collective.quickupload',
          'Products.PloneFormGen',
          'Solgema.ContextualContentMenu',
          'Solgema.fullcalendar',
          'collective.js.colorpicker',
          'collective.js.fullcalendar',
          'plone.app.jquerytools',
          'plone.app.theming',
          'plonetheme.localauthorities'


      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
