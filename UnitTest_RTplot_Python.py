import RTplot_Python
import time
import threading
import numpy as np



GUI_Off = False


myPlotter = RTplot_Python.RTplot_Python(40,3,False)
myPlotter.Add_New_Plot(2, 5, (True, False,True),(-1,1,-0.1,1),("Pos X vs Time","a","a","X","m"),("X", "Noisy shifted X"),(False,True),(False,False),'none')
myPlotter.Add_New_Plot(1, 5, (True, True, False),(-0.7,0.7,-1,1),("Time vs Pos Y","Y","m","a","a"),("Y"),(True,False),(True,True),'none')
myPlotter.New_Row()
myPlotter.Add_New_Plot(1, 0, (False, False,False),(-0.7,0.7,-0.1,0.9),("Pos Y vs Pos X","Y","m","X","m"),("End-Effector",),(True,True),(True,False),'o')
myPlotter.Add_New_Plot(1, 1, (False, False,False),(-0.7,0.7,-0.1,0.9),("Pos Y vs Pos X with History","Y","m","X","m"),("End-Effector",),(True,True),(True,False),'o')
myPlotter.Add_New_Plot(2, 0, (False, False,True),(-0.8,0.8,0,1),("Pos Y vs Pos Z","Y","m","Z","m"),("Vulture","End-Effector"),(True,True),(True,False),'star')



class DATAUpdate(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        time00 = time.time()

        while not (GUI_Off):
            mytime = time.time()-time00
            PosX = 0.5+0.2*np.sin(2*np.pi*0.2*mytime)
            PosY = 0.2*np.cos(2*np.pi*0.2*mytime)

            myPlotter.Data["T_1"] = mytime
            myPlotter.Data["Y_1_1"] = PosX
            myPlotter.Data["Y_1_2"] = PosX+ 0.05 + 0.04*np.random.rand(1,)

            myPlotter.Data["T_2"] = mytime
            myPlotter.Data["Y_2_1"] = PosY

            myPlotter.Data["T_3"] = mytime
            myPlotter.Data["X_3_1"] = PosY
            myPlotter.Data["Y_3_1"] = PosX

            myPlotter.Data["T_4"] = mytime
            myPlotter.Data["X_4_1"] = PosY
            myPlotter.Data["Y_4_1"] = PosX

            myPlotter.Data["T_5"] = mytime
            myPlotter.Data["X_5_1"] = PosY+ 0.1 * np.sin(2*np.pi*0.5*mytime+np.pi/2)
            myPlotter.Data["Y_5_1"] = PosX + 0.1*np.sin(2*np.pi*0.5*mytime)
            myPlotter.Data["X_5_2"] = PosY
            myPlotter.Data["Y_5_2"] = PosX

            time.sleep(0.002)



DATAUpdate_Object = DATAUpdate()
DATAUpdate_Object.start()


myPlotter.Start_Plotting()

GUI_Off = True



DATAUpdate_Object.join()



