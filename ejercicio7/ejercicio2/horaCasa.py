import pprint
from time import *

print("Hora de ir a casa" if int(strftime("%H", localtime())) >= 19 else f'{18 - localtime()[3]}:{60 - localtime()[4]}:{60 - localtime()[5]}')