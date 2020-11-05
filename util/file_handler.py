

# data 파일을 읽어들이는 프로그램

from dataclasses import dataclass
"""
context path    : C:/SBAProject/
fname           : cabage/data/  or  titanic/data/  or  ...
"""

@dataclass
class FileReader:

    context : str = '' 
    fname : str = ''
    train: object = None
    test: object = None
    id: str = ''
    label: str = ''

    