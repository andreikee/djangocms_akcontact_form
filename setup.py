from setuptools import setup, find_packages

from akcmsplugin_contact_form import __version__

setup(
    name='akcmsplugin-contact-form',
    version=__version__,
    description='A Django CMS plugin to create functional contact forms.',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    maintainer='Andrei Krivoshei',
    maintainer_email='andrei.krivoshei@gmail.com',
    url='https://github.com/andreikee/djangocms_akcontact_form',
    license='MIT',
    keywords='django djangocms plugin form contact email',
    packages=['akcmsplugin_contact_form'],
    package_dir={'akcmsplugin_contact_form': 'akcmsplugin_contact_form'},
    package_data={'akcmsplugin_contact_form': [
        'templates/akcmsplugin_contact_form/*.html']},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools'],
)
