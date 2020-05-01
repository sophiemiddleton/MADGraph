from object_library import all_form_factors, FormFactor

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, theta_function
# incoming nucleon id 2, outgoing nucleon id 4


#2) Elastic WABS off nucleus, simple elastic ff:
AAA = FormFactor(name = 'AAA',
                 type = 'real',
                 value = 'Znuc*(1/(1+(-2*MNul**2-2*P(-1,1)*P(-1,2))/dval))')



