#AIRCRAFT TAKEOFF PERFORMANCE ANALYSER

A python-based aircraft takeoff performance analysis program that calculates basic aerodynamic and takeoff parameters and evaluates whether the parameters and evalutes whether the available runway is sufficient for takeoff.
This project is for educational purpose and does not depend on the aviation working procedure.

##Overview

The Aircraft Takeoff Performance Analyzer is a modular python project designed to estimate aircraft takeoff performance using user-provided aircraft,environmental and runway data.

##The program calculates:
-Dynamic pressue
-lift
-drag
-net force
-aircraft acceleration
-required takeoff runway distance
-runway safety margin
-runway sufficiency assessment

##Project structure

Aircraft takeoff performance Analyzer
|
|-main.py
|-calculations.py
|-constants.py 
|-input_handlers.py 
|-takeoff_analysis.py
|-runway_analysis.py
|-validation.py 
|-report.py
|-README.md 

##Features

The program accepts:
-aircraft mass in kg
-engine thrust in N 
-wing area in m^2 
-lift coefficient 
-takeoff speed in m/s 
-air densty in kg/m^3
-wind speed in m/s 
-runway length in m 
-runway slope in %

## Python features used
-import module
-def functions
-input()
-type conversion
-variables
-constants
-arithmetic operators
-if statemts
-comparison operators
-return statements
-print()
-exit()
-raise ValueError
-comments

##technologies used
-python 3
-python math module
-command prompt/PowerShell

##requirements
-python 3.x
-windows command prompt or PowerShell

##guide to run 
1:Download or clone the project
2:Open command prompt or PowerShell
3:Go to the project folder
4:make sure all the python fies are in the same folder
5:Run the commands

##project modules
maim.py:-runs the complete aircraft takeofff analysis
calculations.py:-preforms aerodynamic and force calculations
constants.py:-stores physical constants
input_handlers.py:-takes aircraft and runway inputs 
takeoff_analysis.py:-calculates requied takeoff distance 
ruway_analysis.py:-calculates runway safetymargin and assessments
validation.py:-performs the validue.

##Author 
ADITHYAN UDAYAKUMAR
B.TECH AEROSPACE ENGINEERING
VIT BHOPAL UNIVERSITY

#License
This project is created for educational and learning prupose only.