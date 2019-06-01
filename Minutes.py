def Minutes(h,m):
    return h*60+m
def HeuresMinutes(m):
    h=m//60
    m=m%60
    return[h,m]
def AjouteTemps(h1,m1,h2,m2):
    MinuteEnTout=Minutes(h1,m1)+Minutes(h2,m2)
    (h,m)=HeuresMinutes(MinuteEnTout)
    return[h,m]