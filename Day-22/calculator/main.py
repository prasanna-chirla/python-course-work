#module
import logic
logic.add(10,20)
logic.sub(10,20)
logic.mul(10,20)
logic.rem(10,20)
logic.pow(10,20)
logic.div(10,20)

#if name is big can give short name(alias)
import logic as lg
lg.add(10,20)
lg.sub(10,20)
lg.mul(10,20)
lg.rem(10,20)
lg.pow(10,20)
lg.div(10,20)

#extract only necessary files
from logic import add,mul
add(12,32)
mul(3,32)

#
from logic import *
add(10,20)
sub(10,20)
mul(10,20)
rem(10,20)
pow(10,20)
div(10,20)