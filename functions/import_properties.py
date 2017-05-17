''' import material and process properties from the settings files '''

import json

def import_settings(material):
    ''' import material and process properties from the settings files '''

    jsfile = open('./settings/settings.json')
    data = json.load(jsfile)
    jsfile.close()

    # material
    rho = data[material]['rho']
    Cp = data[material]['Cp']
    k = data[material]['k']
    T_melt = data[material]['T_melt']
    emmi = data[material]['emmi']

    # process
    L_pow = data['process']['L_pow']
    L_spot = data['process']['L_spot']
    L_vel = data['process']['L_vel']
    T_inf = data['process']['T_inf']
    hc_air = data['process']['hc_air']

    return (rho, Cp, k, T_melt, emmi, L_pow, L_spot,
            L_vel, T_inf, hc_air)

