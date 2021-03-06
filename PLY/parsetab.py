
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = 'F6684FFC6A3F9743CD609A6E3CDC27FB'
    
_lr_action_items = {'$end':([0,1,2,3,4,5,7,9,10,11,12,13,15,19,26,],[-14,-10,-2,-1,-7,-3,-9,-4,0,-6,-5,-8,-11,-12,-13,]),'NAME':([6,],[14,]),'FOR':([0,],[11,]),'WORDS':([25,],[26,]),'WHERE':([0,],[4,]),'MISC':([0,],[7,]),'BOOK':([0,],[6,]),'THEME':([0,],[5,]),'CHAPTERS':([18,],[20,]),',':([20,23,],[21,24,]),'BY':([0,],[9,]),'VERSES':([22,],[23,]),'INTEGER':([6,16,21,24,],[15,18,22,25,]),'STR':([17,],[19,]),'DATE':([0,],[12,]),':':([8,14,],[16,17,]),'STATS':([0,],[8,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'booknum':([0,],[3,]),'empty':([0,],[1,]),'start':([0,],[10,]),'book':([0,],[2,]),'data':([0,],[13,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> booknum','start',1,'p_start','Project5.py',49),
  ('start -> book','start',1,'p_start','Project5.py',50),
  ('start -> THEME','start',1,'p_start','Project5.py',51),
  ('start -> BY','start',1,'p_start','Project5.py',52),
  ('start -> DATE','start',1,'p_start','Project5.py',53),
  ('start -> FOR','start',1,'p_start','Project5.py',54),
  ('start -> WHERE','start',1,'p_start','Project5.py',55),
  ('start -> data','start',1,'p_start','Project5.py',56),
  ('start -> MISC','start',1,'p_start','Project5.py',57),
  ('start -> empty','start',1,'p_start','Project5.py',58),
  ('booknum -> BOOK INTEGER','booknum',2,'p_booknum','Project5.py',69),
  ('book -> BOOK NAME : STR','book',4,'p_book','Project5.py',73),
  ('data -> STATS : INTEGER CHAPTERS , INTEGER VERSES , INTEGER WORDS','data',10,'p_data','Project5.py',77),
  ('empty -> <empty>','empty',0,'p_empty','Project5.py',81),
]
