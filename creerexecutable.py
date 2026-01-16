from distutils.core import setup
import py2exe

setup(console=['your_script.py'], options={
    'py2exe': {
        'packages': ['os', 'sys', 'numpy'],
        'bundle_files': 1,
        'compressed': True
    }
})
