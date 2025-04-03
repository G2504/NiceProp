#! /usr/bin/env python
# -*- coding: utf-8 -*-

#############################################################################
# NiceProp - Interactively learning NICFD
# Authors: ir. A. Giuffre', Dr. ir. M. Pini
# Content: Graphical user interface
# 2021 - TU Delft - All rights reserved
#############################################################################


import pyfiglet
import tkinter as tk
from IO import *
import thermodynamics as thermo
import isentropic_process as isos
import os


class App(tk.Frame):
    """ Class to take user input from a GUI and run the main program """
    def __init__(self, root, master=None, **kw):
        tk.Frame.__init__(self, master=master, **kw)
        idx = 0
        self.settings = {}
        self.root = root
        self.font = ('calibre', 10)

        banner = pyfiglet.figlet_format("NiceProp", justify='auto')
        print("\n\n******************************************************")
        print(banner)
        print(" Interactively learning NICFD")
        print(" Authors: ir. A. Giuffre', Dr. ir. M. Pini")
        print(" Delft University of Technology - All rights reserved")
        print("******************************************************\n")

        self.flag = tk.BooleanVar()
        tk.Checkbutton(self, text='Input from configuration file', font=self.font, var=self.flag).grid(row=idx, column=0)
        idx += 1

        tk.Label(self, text="Configuration file", justify='left', font=self.font).grid(row=idx, column=0)
        self.q1 = tk.Entry(self, font=self.font)
        self.q1.grid(row=idx, column=1)
        idx += 1

        tk.Label(self, text="\n  ************************************  BASIC SETTINGS  ************************************  ",
                 justify='center', font=self.font).grid(row=idx)
        idx += 1

        tk.Label(self, text="Working fluid", justify='left', font=self.font).grid(row=idx, column=0)
        self.q2 = tk.Entry(self, font=self.font)
        self.q2.grid(row=idx, column=1)
        idx += 1

        tk.Label(self, text="Equation of state: 'PR', 'SRK', 'HEOS' or 'REFPROP'",
                 justify='left', font=self.font).grid(row=idx, column=0)
        self.q3 = tk.Entry(self, font=self.font)
        self.q3.grid(row=idx, column=1)
        idx += 1

        tk.Label(self, text="Thermodynamic plane: 'Ts' or 'PT'", justify='left',
                 font=self.font).grid(row=idx, column=0)
        self.q4 = tk.Entry(self, font=self.font)
        self.q4.grid(row=idx, column=1)
        idx += 1

        tk.Label(self, text="Compute liquid and two-phase regions? 'Y'or 'N'", justify='left',
                 font=self.font).grid(row=idx, column=0)
        self.q36 = tk.Entry(self, font=self.font)
        self.q36.grid(row=idx, column=1)
        idx += 1

        tk.Label(self, text="\n  ***************************  ISENTROPIC TRANSFORMATION  ***************************  ",
                 justify='center', font=self.font).grid(row=idx)
        idx += 1

        tk.Label(self, text="Thermodynamic process(es): 'compression' or 'expansion' or 'None'",
                 justify='left', font=self.font).grid(row=idx, column=0)
        self.q5 = tk.Entry(self, font=self.font)
        self.q5.grid(row=idx, column=1)
        idx += 1

        tk.Label(self, text="Design nozzle/diffuser for expansion/compression process? 'Y' or 'N'",
                 justify='left', font=self.font).grid(row=idx, column=0)
        self.q6 = tk.Entry(self, font=self.font)
        self.q6.grid(row=idx, column=1)
        idx += 1

        tk.Label(self, text="Total-to-static volumetric flow ratio",
                 justify='left', font=self.font).grid(row=idx, column=0)
        self.q7 = tk.Entry(self, font=self.font)
        self.q7.grid(row=idx, column=1)
        idx += 1

        tk.Label(self, text="Total-to-static expansion ratio",
                 justify='left', font=self.font).grid(row=idx, column=0)
        self.q8 = tk.Entry(self, font=self.font)
        self.q8.grid(row=idx, column=1)
        idx += 1

        tk.Label(self, text="Inlet state definition: 'Ts' or 'PT'",
                 justify='left', font=self.font).grid(row=idx, column=0)
        self.q9 = tk.Entry(self, font=self.font)
        self.q9.grid(row=idx, column=1)
        self.q10 = tk.Entry(self, font=self.font)
        self.q10.grid(row=idx, column=2)
        self.q11 = tk.Entry(self, font=self.font)
        self.q11.grid(row=idx, column=3)
        idx += 1

        tk.Label(self, text="Inlet state definition: first input",
                 justify='left', font=self.font).grid(row=idx, column=0)
        self.q12 = tk.Entry(self, font=self.font)
        self.q12.grid(row=idx, column=1)
        self.q13 = tk.Entry(self, font=self.font)
        self.q13.grid(row=idx, column=2)
        self.q14 = tk.Entry(self, font=self.font)
        self.q14.grid(row=idx, column=3)
        idx += 1

        tk.Label(self, text="Inlet state definition: second input",
                 justify='left', font=self.font).grid(row=idx, column=0)
        self.q15 = tk.Entry(self, font=self.font)
        self.q15.grid(row=idx, column=1)
        self.q16 = tk.Entry(self, font=self.font)
        self.q16.grid(row=idx, column=2)
        self.q17 = tk.Entry(self, font=self.font)
        self.q17.grid(row=idx, column=3)
        idx += 1

        tk.Label(self, text="Label(s) associated to the thermodynamic process(es)",
                 justify='left', font=self.font).grid(row=idx, column=0)
        self.q18 = tk.Entry(self, font=self.font)
        self.q18.grid(row=idx, column=1)
        self.q19 = tk.Entry(self, font=self.font)
        self.q19.grid(row=idx, column=2)
        self.q20 = tk.Entry(self, font=self.font)
        self.q20.grid(row=idx, column=3)
        idx += 1

        tk.Label(self, text="Nozzle geometry is provided as input? 'Y' or 'N'",
                 justify='left', font=self.font).grid(row=idx, column=0)
        self.q21 = tk.Entry(self, font=self.font)
        self.q21.grid(row=idx, column=1)
        idx += 1

        tk.Label(self, text="\n***************************** COMPONENT DESIGN *****************************",
                 justify='center', font=self.font).grid(row=idx)
        idx += 1

        tk.Label(self, text="Mass flow rate [kg/s]",
                 justify='left', font=self.font).grid(row=idx, column=0)
        self.q22 = tk.Entry(self, font=self.font)
        self.q22.grid(row=idx, column=1)
        self.q23 = tk.Entry(self, font=self.font)
        self.q23.grid(row=idx, column=2)
        self.q24 = tk.Entry(self, font=self.font)
        self.q24.grid(row=idx, column=3)
        idx += 1

        tk.Label(self, text="Flow velocity [m/s]",
                 justify='left', font=self.font).grid(row=idx, column=0)
        self.q25 = tk.Entry(self, font=self.font)
        self.q25.grid(row=idx, column=1)
        self.q26 = tk.Entry(self, font=self.font)
        self.q26.grid(row=idx, column=2)
        self.q27 = tk.Entry(self, font=self.font)
        self.q27.grid(row=idx, column=3)
        idx += 1

        tk.Label(self, text="Geometry: 'rectangular' or 'circular' for nozzle, 'conical' or 'radial' for diffuser",
                 justify='left', font=self.font).grid(row=idx, column=0)
        self.q28 = tk.Entry(self, font=self.font)
        self.q28.grid(row=idx, column=1)
        idx += 1

        tk.Label(self, text="\n***************************** CONTOUR PLOT SETTINGS *****************************",
                 justify='center', font=self.font).grid(row=idx)
        idx += 1

        tk.Label(self, text="Number of grid points on x and y axes for Ts/PT contour plots",
                 justify='left', font=self.font).grid(row=idx, column=0)
        self.q29 = tk.Entry(self, font=self.font)
        self.q29.grid(row=idx, column=1)
        idx += 1

        tk.Label(self, text="Boundaries of contour plots along reduced T axis",
                 justify='left', font=self.font).grid(row=idx, column=0)
        self.q30 = tk.Entry(self, font=self.font)
        self.q30.grid(row=idx, column=1)
        self.q31 = tk.Entry(self, font=self.font)
        self.q31.grid(row=idx, column=2)
        idx += 1

        tk.Label(self, text="Boundaries of contour plots along reduced s axis",
                 justify='left', font=self.font).grid(row=idx, column=0)
        self.q32 = tk.Entry(self, font=self.font)
        self.q32.grid(row=idx, column=1)
        self.q33 = tk.Entry(self, font=self.font)
        self.q33.grid(row=idx, column=2)
        idx += 1

        tk.Label(self, text="Boundaries of contour plots along reduced P axis",
                 justify='left', font=self.font).grid(row=idx, column=0)
        self.q34 = tk.Entry(self, font=self.font)
        self.q34.grid(row=idx, column=1)
        self.q35 = tk.Entry(self, font=self.font)
        self.q35.grid(row=idx, column=2)
        idx += 1

        tk.Button(self, text="Run", command=self.run, justify='left', font=self.font).grid(row=idx, column=1)

    def run(self):
        """ Run the main program and retrieve the execution time """

        if self.flag.get():
            # Read configuration file
            self.settings = readConfigFile(self.q1.get() + '.txt')
        else:
            self.settings['fluid'] = self.q2.get()
            self.settings['equation of state'] = self.q3.get()
            self.settings['thermodynamic plane'] = self.q4.get()
            self.settings['process'] = self.q5.get()
            self.settings['plot liquid and 2 phase'] = self.q36.get()
            self.settings['design'] = self.q6.get()
            self.settings['alpha'] = float(self.q7.get())
            self.settings['beta'] = float(self.q8.get())

            if len(self.q10.get()) > 1:
                if len(self.q11.get()) > 1:
                    # 3 inputs
                    self.settings['inlet thermodynamic plane'] = \
                        np.array([self.q9.get(), self.q10.get(), self.q11.get()])
                    self.settings['inlet input 1'] = \
                        np.array([float(self.q12.get()), float(self.q13.get()), float(self.q14.get())])
                    self.settings['inlet input 2'] = \
                        np.array([float(self.q15.get()), float(self.q16.get()), float(self.q17.get())])
                    self.settings['labels'] = \
                        np.array([self.q18.get(), self.q19.get(), self.q20.get()])
                    self.settings['mass flow rate'] = \
                        np.array([float(self.q22.get()), float(self.q23.get()), float(self.q24.get())])
                    self.settings['velocity'] = \
                        np.array([float(self.q25.get()), float(self.q26.get()), float(self.q27.get())])
                else:
                    # 2 inputs
                    self.settings['inlet thermodynamic plane'] = np.array([self.q9.get(), self.q10.get()])
                    self.settings['inlet input 1'] = np.array([float(self.q12.get()), float(self.q13.get())])
                    self.settings['inlet input 2'] = np.array([float(self.q15.get()), float(self.q16.get())])
                    self.settings['labels'] = np.array([self.q18.get(), self.q19.get()])
                    self.settings['mass flow rate'] = np.array([float(self.q22.get()), float(self.q23.get())])
                    self.settings['velocity'] = np.array([float(self.q25.get()), float(self.q26.get())])
            else:
                # 1 input
                self.settings['inlet thermodynamic plane'] = self.q9.get()
                self.settings['inlet input 1'] = float(self.q12.get())
                self.settings['inlet input 2'] = float(self.q15.get())
                self.settings['labels'] = self.q18.get()
                self.settings['mass flow rate'] = float(self.q22.get())
                self.settings['velocity'] = float(self.q25.get())

            self.settings['geometry flag'] = self.q21.get()
            self.settings['geometry'] = self.q28.get()
            self.settings['samples'] = int(self.q29.get())
            self.settings['Tr vec'] = np.linspace(float(self.q30.get()), float(self.q31.get()), self.settings['samples'])
            self.settings['sr vec'] = np.linspace(float(self.q32.get()), float(self.q33.get()), self.settings['samples'])
            self.settings['Pr vec'] = np.linspace(float(self.q34.get()), float(self.q35.get()), self.settings['samples'])

        self.root.destroy()
        
        thermodynamics = thermo.ThermodynamicModel(self.settings)
        if self.settings['thermodynamic plane'] == 'Ts':
            thermodynamics.TsContour()
        elif self.settings['thermodynamic plane'] == 'PT':
            thermodynamics.PTContour()
        else:
            raise ValueError("The available choices for 'Thermodynamic plane' are 'PT' or 'Ts'")

        if (self.settings['process'] == 'expansion') or (self.settings['process'] == 'compression'):
            flow = isos.IsentropicFlowModel(thermodynamics, self.settings)
            if self.settings['design'] == 'y' or self.settings['design'] == 'Y':
                if self.settings['process'] == 'expansion':
                    if self.settings['geometry flag'] == 'y' or self.settings['geometry flag'] == 'Y':
                        massflow, velocity, geometry, x_norm, R_norm, R_throat = \
                            readNozzleCoordinates(self.settings['labels'], self.settings['samples'])
                        flow.NozzleExpansion('off-design', x_norm=x_norm, R_norm=R_norm, R_throat_vec=R_throat)
                    else:
                        flow.NozzleExpansion('design')
                elif self.settings['process'] == 'compression':
                    flow.DiffuserCompression()
                else:
                    raise ValueError("The available choices for 'Thermodynamic process' are "
                                     "'expansion' or 'compression'")
            else:
                flow.IdealProcess()

            # Assumed dimensions    # Hake et al. : chord of 30mm, throat of 8mm, span of 50mm
            dim_assumed = True
            #                     nonmonotonic, nonideal, ideal
            throat_w  = np.array([3.5,          3.5*1.152  , 3.5*2.688   ])/1000 # mm
            chord     = np.array([45.56,        49.49*1.152, 41.88*2.688 ])/1000 # mm
            blade_h   = np.array([5.85,         5.85,        5.85        ])/1000 # mm
            n_passages= np.array([5,            5,           5           ])

            # Max thermal power of ORCHID based soley on h1 (inflow enthalpy) (neglecting recouperator influence) 
            # and taking 20% margin to account for degradation of the radiators
            P_th_max  = 500000*0.8 # W

            # Print statements
            print("  Ideal process label(s):                                  " + str(self.settings['labels']))
            print("  Average value(s) of compressibility factor:              " + str(np.round(flow.Z_mean,3)))
            print("  Average value(s) of isentropic pressure-volume exponent: " + str(np.round(flow.gamma_Pv_mean,3)))
            print("  Value(s) of inlet pressue (bar):                         " + str(np.round(flow.P_vec[:,0]/100000,3)))
            print("  Value(s) of inlet temp. (K):                             " + str(np.round(flow.T_vec[:,0],3)))
            print("  Value(s) of exit pressue (bar):                          " + str(np.round(flow.P_vec[:,-1]/100000,3)))
            print("  Value(s) of exit temp. (K):                              " + str(np.round(flow.T_vec[:,-1],3)))
            print("  Value(s) of exit Mach:                                   " + str(np.round(flow.M_vec[:,-1],3)))
            print("  Value(s) of exit velocity (m/s):                         " + str(np.round(flow.V_vec[:,-1],3)))
            print("  Value(s) of throat density (kg/m^3):                     " + str(np.round(flow.D_throat[:],3)))
            print("  Value(s) of throat velocity (m/s):                       " + str(np.round(flow.V_throat[:],3)))
            print("  Value(s) of throat Z (-):                                " + str(np.round(flow.Z_throat[:],3)))
            print("  Value(s) of throat fundamental derivative:               " + str(np.round(flow.FundDerGamma_throat[:],3)))            
            if dim_assumed:
                # Find max blade height based on max thermal power
                blade_height_3_Pth = P_th_max/(3*throat_w*flow.D_throat[:]*flow.V_throat[:]*flow.h_vec[:,0])*1000
                blade_height_4_Pth = P_th_max/(4*throat_w*flow.D_throat[:]*flow.V_throat[:]*flow.h_vec[:,0])*1000
                blade_height_5_Pth = P_th_max/(5*throat_w*flow.D_throat[:]*flow.V_throat[:]*flow.h_vec[:,0])*1000
                blade_height_6_Pth = P_th_max/(6*throat_w*flow.D_throat[:]*flow.V_throat[:]*flow.h_vec[:,0])*1000

                print("  Values of max blade height (mm) for 3 passages:          " + str(np.round(blade_height_3_Pth,2)))
                print("  Values of max blade height (mm) for 4 passages:          " + str(np.round(blade_height_4_Pth,2)))
                print("  Values of max blade height (mm) for 5 passages:          " + str(np.round(blade_height_5_Pth,2)))
                print("  Values of max blade height (mm) for 6 passages:          " + str(np.round(blade_height_6_Pth,2)))
                
                f_vec     = flow.D_throat[:]*flow.V_throat[:]*throat_w*blade_h*n_passages        # mass flow rate (kg/s)
                f_max_vec = flow.D_throat[:]*flow.V_throat[:]*throat_w*blade_height_3_Pth*3/1000 # max mass flow rate (kg/s)
                Re_vec    = (flow.D_vec[:,-1]*flow.V_vec[:,-1]*chord)/flow.mu_vec[:,-1]

                print("  Value(s) of Reynolds number (e6):                        " + str(np.round(Re_vec/1000000,3)))
                print("  Value(s) of mass flow rate (kg/s):                       " + str(np.round(f_vec,3)))
                print("  Value(s) of allowed mass flow rate (kg/s):               " + str(np.round(f_max_vec,3)))
                print("  Value(s) of allowed throat area (mm2)                    " + str(np.round(throat_w*blade_height_3_Pth*3*1000,2)))
                print("  Value(s) of expected boundary layer thickness (mm)       " + str(np.round(0.37*0.25*chord/(Re_vec**(1/5))*1000,1)))
                print("  Value(s) of h3*mass flow (kW)                            " + str(np.round(flow.h_vec[:,-1]*f_vec/1000,1)))

            # Save print statements to .txt file
            home_dir, _ = os.path.split(os.path.dirname(__file__))
            dir = os.path.join(home_dir, 'output/' + self.settings['fluid'] + '/expansion')
            if not os.path.isdir(dir):
                os.makedirs(dir)
            with open(os.path.join(dir,self.settings['labels'][-1]+".txt"), "w") as file:
                print("  Ideal process label(s):                                  " + str(self.settings['labels']),file=file)
                print("  Average value(s) of compressibility factor:              " + str(np.round(flow.Z_mean,3)),file=file)
                print("  Average value(s) of isentropic pressure-volume exponent: " + str(np.round(flow.gamma_Pv_mean,3)),file=file)
                print("  Value(s) of inlet pressue (bar):                         " + str(np.round(flow.P_vec[:,0]/100000,3)),file=file)
                print("  Value(s) of inlet temp. (K):                             " + str(np.round(flow.T_vec[:,0],3)),file=file)
                print("  Value(s) of exit pressue (bar):                          " + str(np.round(flow.P_vec[:,-1]/100000,3)),file=file)
                print("  Value(s) of exit temp. (K):                              " + str(np.round(flow.T_vec[:,-1],3)),file=file)
                print("  Value(s) of exit Mach:                                   " + str(np.round(flow.M_vec[:,-1],3)),file=file)
                print("  Value(s) of exit velocity (m/s):                         " + str(np.round(flow.V_vec[:,-1],3)),file=file)
                print("  Value(s) of throat density (kg/m^3):                     " + str(np.round(flow.D_throat[:],3)),file=file)
                print("  Value(s) of throat velocity (m/s):                       " + str(np.round(flow.V_throat[:],3)),file=file)
                print("  Value(s) of throat Z (-):                                " + str(np.round(flow.Z_throat[:],3)),file=file)
                print("  Value(s) of throat fundamental derivative:               " + str(np.round(flow.FundDerGamma_throat[:],3)),file=file)            
                if dim_assumed:
                    print("  Values of max blade height (mm) for 3 passages:          " + str(np.round(blade_height_3_Pth,2)),file=file)
                    print("  Values of max blade height (mm) for 4 passages:          " + str(np.round(blade_height_4_Pth,2)),file=file)
                    print("  Values of max blade height (mm) for 5 passages:          " + str(np.round(blade_height_5_Pth,2)),file=file)
                    print("  Values of max blade height (mm) for 6 passages:          " + str(np.round(blade_height_6_Pth,2)),file=file)
                    print("  Value(s) of Reynolds number (e6):                        " + str(np.round(Re_vec/1000000,3)),file=file)
                    print("  Value(s) of mass flow rate (kg/s):                       " + str(np.round(f_vec,3)),file=file)
                    print("  Value(s) of allowed mass flow rate (kg/s):               " + str(np.round(f_max_vec,3)),file=file)
                    print("  Value(s) of expected boundary layer thickness (mm)       " + str(np.round(0.37*0.25*chord/(Re_vec**(1/5))*1000,1)),file=file)
                    print("  Value(s) of allowed throat area (mm2)                    " + str(np.round(throat_w*blade_height_3_Pth*3*1000,2)),file=file)
                    print("  Value(s) of h3*mass flow (kW)                            " + str(np.round(flow.h_vec[:,-1]*f_vec/1000,1)),file=file)