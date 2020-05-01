from object_library import all_form_factors, FormFactor

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, theta_function
# incoming nucleon id 2, outgoing nucleon id 4

# t = (- 2*MNul**2 - 2*P(-1,1)*P(-1,2))

AAA = FormFactor(name = 'AAA',
                 type = 'real',
                 value = '((Znuc**2*(aval**2*(- 2*MNul**2 - 2*P(-1,1)*P(-1,2))/(1+aval**2*(- 2*MNul**2 - 2*P(-1,1)*P(-1,2))))**2*(1/(1+(- 2*MNul**2 - 2*P(-1,1)*P(-1,2))/dval))**2)+Znuc*(apval**2*(- 2*MNul**2 - 2*P(-1,1)*P(-1,2))/(1+apval**2*(- 2*MNul**2 - 2*P(-1,1)*P(-1,2))))**2*((1+(- 2*MNul**2 - 2*P(-1,1)*P(-1,2))*inelastic1)/(1+(- 2*MNul**2 - 2*P(-1,1)*P(-1,2))*inelastic2)**4)**2)**0.5'
                 )


'''
1) WAB_OFF_NUCLEUS, ff = 1:
AAA = FormFactor(name = 'AAA',
                 type = 'real',
                 value = 'Znuc')

2) Elastic WABS off nucleus, simple elastic ff:

AAA = FormFactor(name = 'AAA',
                 type = 'real',
                 value = 'Znuc*(1/(1+(-2*MNul**2-2*P(-1,1)*P(-1,2))/dval))')

3) Elastic WABs off a single proton with ff =1

- model with Znuc =1, Anuc=1, MNul=0.938 AAA = 1:

AAA = FormFactor(name = 'AAA',
                 type = 'real',
                 value = '1')


'''

