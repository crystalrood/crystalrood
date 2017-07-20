__all__ = ['stock_utils']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers([u'makeNumeric', u'numval', u'presentValue', u'geomSeries', u'futureValue', u'annuityPayout'])
@Js
def PyJsHoisted_makeNumeric_(s, this, arguments, var=var):
    var = Scope({u'this':this, u's':s, u'arguments':arguments}, var)
    var.registers([u's'])
    return var.get(u'filterChars')(var.get(u's'), Js(u'1234567890.-'))
PyJsHoisted_makeNumeric_.func_name = u'makeNumeric'
var.put(u'makeNumeric', PyJsHoisted_makeNumeric_)
@Js
def PyJsHoisted_numval_(val, digits, minval, maxval, this, arguments, var=var):
    var = Scope({u'digits':digits, u'maxval':maxval, u'arguments':arguments, u'val':val, u'minval':minval, u'this':this}, var)
    var.registers([u'digits', u'maxval', u'dec', u'val', u'minval'])
    var.put(u'val', var.get(u'makeNumeric')(var.get(u'val')))
    if ((var.get(u'val')==Js(u'')) or var.get(u'isNaN')(var.get(u'val'))):
        var.put(u'val', Js(0.0))
    var.put(u'val', var.get(u'parseFloat')(var.get(u'val')))
    if (var.get(u'digits')!=var.get(u"null")):
        var.put(u'dec', var.get(u'Math').callprop(u'pow', Js(10.0), var.get(u'digits')))
        var.put(u'val', (var.get(u'Math').callprop(u'round', (var.get(u'val')*var.get(u'dec')))/var.get(u'dec')))
    if ((var.get(u'minval')!=var.get(u"null")) and (var.get(u'val')<var.get(u'minval'))):
        var.put(u'val', var.get(u'minval'))
    if ((var.get(u'maxval')!=var.get(u"null")) and (var.get(u'val')>var.get(u'maxval'))):
        var.put(u'val', var.get(u'maxval'))
    return var.get(u'parseFloat')(var.get(u'val'))
PyJsHoisted_numval_.func_name = u'numval'
var.put(u'numval', PyJsHoisted_numval_)
@Js
def PyJsHoisted_presentValue_(fv, r, y, this, arguments, var=var):
    var = Scope({u'y':y, u'this':this, u'r':r, u'arguments':arguments, u'fv':fv}, var)
    var.registers([u'y', u'r', u'fv'])
    return (var.get(u'fv')/var.get(u'Math').callprop(u'pow', (Js(1.0)+var.get(u'r')), var.get(u'y')))
PyJsHoisted_presentValue_.func_name = u'presentValue'
var.put(u'presentValue', PyJsHoisted_presentValue_)
@Js
def PyJsHoisted_geomSeries_(z, m, n, this, arguments, var=var):
    var = Scope({u'this':this, u'z':z, u'm':m, u'arguments':arguments, u'n':n}, var)
    var.registers([u'z', u'm', u'amt', u'n'])
    pass
    if (var.get(u'z')==Js(1.0)):
        var.put(u'amt', (var.get(u'n')+Js(1.0)))
    else:
        var.put(u'amt', ((var.get(u'Math').callprop(u'pow', var.get(u'z'), (var.get(u'n')+Js(1.0)))-Js(1.0))/(var.get(u'z')-Js(1.0))))
    if (var.get(u'm')>=Js(1.0)):
        var.put(u'amt', var.get(u'geomSeries')(var.get(u'z'), Js(0.0), (var.get(u'm')-Js(1.0))), u'-')
    return var.get(u'amt')
PyJsHoisted_geomSeries_.func_name = u'geomSeries'
var.put(u'geomSeries', PyJsHoisted_geomSeries_)
@Js
def PyJsHoisted_futureValue_(p, r, y, this, arguments, var=var):
    var = Scope({u'y':y, u'p':p, u'r':r, u'this':this, u'arguments':arguments}, var)
    var.registers([u'y', u'p', u'r'])
    return (var.get(u'p')*var.get(u'Math').callprop(u'pow', (Js(1.0)+var.get(u'r')), var.get(u'y')))
PyJsHoisted_futureValue_.func_name = u'futureValue'
var.put(u'futureValue', PyJsHoisted_futureValue_)
@Js
def PyJsHoisted_annuityPayout_(p, r, y, this, arguments, var=var):
    var = Scope({u'y':y, u'p':p, u'r':r, u'this':this, u'arguments':arguments}, var)
    var.registers([u'y', u'p', u'r'])
    return (var.get(u'futureValue')(var.get(u'p'), var.get(u'r'), (var.get(u'y')-Js(1.0)))/var.get(u'geomSeries')((Js(1.0)+var.get(u'r')), Js(0.0), (var.get(u'y')-Js(1.0))))
PyJsHoisted_annuityPayout_.func_name = u'annuityPayout'
var.put(u'annuityPayout', PyJsHoisted_annuityPayout_)
pass
pass
pass
pass
pass
pass
pass


# Add lib to the module scope
stock_utils = var.to_python()