# -*-coding:Utf-8 -*

import logging
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
root = logging.getLogger('')
root.propagate
root.setLevel(logging.DEBUG)
root.addHandler(ch)
    
log = logging.getLogger()