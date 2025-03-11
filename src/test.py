import CoolProp


EoS = CoolProp.AbstractState('REFPROP', 'MM')
Tc = EoS.T_critical()
Pc = EoS.p_critical()
EoS.update(CoolProp.PT_INPUTS, Pc, Tc)
sc = EoS.smass()

s_max_sat = 1.048
T_s_max_sat = 0.986875


EoS.update(CoolProp.SmassT_INPUTS, s_max_sat*sc, T_s_max_sat*Tc)
P_s_max_sat = EoS.p()/Pc

EoS.update(CoolProp.PT_INPUTS, P_s_max_sat*Pc,T_s_max_sat*Tc+5)
s_min = EoS.smass()
print(s_min/sc)
