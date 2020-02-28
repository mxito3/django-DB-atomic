# import sys
# import os.path
# root_directory=os.path.abspath(os.path.join(os.path.abspath(__file__),"../../../"))
# print(root_directory)
# sys.path.append(root_directory)
import os
import django

from atomic import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'atomic.settings')
django.setup()