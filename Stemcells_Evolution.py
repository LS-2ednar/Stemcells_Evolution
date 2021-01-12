"""
Track Module Thoght Experiment 
Stochastic Process to Model the growth of Stemcells
"""
import numpy as np
import matplotlib.pyplot as plt


Stemcells   = [500]
DiCells     = [0]
DeadCells   = [0]

TransitionMatrix = [[0.7, 0.25, 0.05],[0, 0.85, 0.15],[0, 0, 1]]

Br = [0.03,0.06,0]
Dr = [0.5,0.3,0]

def stoch_growth(StemCells,DiCells,DeadCells,TransitionMatrix,Br,Dr,GN=0):
    
    #figure out if the function might still recompute
    if Stemcells[GN]<1 or GN > 2500:
        print(f'It Worked no more stemcells after {GN} Generations')
        ax1 = plt.subplot()
        ins1 = ax1.plot(StemCells, 'g', label='Stem Cells')
        plt.ylabel('Stem Cells [-]')
        plt.ylim(0)
        plt.xlim(0,GN)
        plt.xlabel('Generations [-]')
        ax2 = ax1.twinx()
        ins2 = ax2.plot(DiCells, 'orange',label = 'Dif. Cells')
        ins3 = ax2.plot(DeadCells, 'k', label = 'Dead Cells')
        plt.ylabel('Dif. & Dead Cells [-]')
        # plt.ylim(0,2e10)
        ins = ins1 + ins2 + ins3
        labs = [l.get_label () for l in ins]
        ax1.legend(ins , labs, loc = 9)
        plt.title('Stem Cell Evolution')
        plt.show()
        print(Stemcells)
        return
     
    SCC = np.random.choice(3,1,p=[TransitionMatrix[0][0],TransitionMatrix[0][1],TransitionMatrix[0][2]])
    DCC = np.random.choice(2,1,p=[TransitionMatrix[1][1],TransitionMatrix[1][2]])
    print(f'SCC = {SCC}')
    print(f'DCC = {DCC}')
    
    #updating every State in reversed order to ensure maximal number of available cells
    newDeadCells1 = 1
    newDeadCells2 = 1
    addnewDiCells = 1
    
    if SCC == 0:
        newStemcells    = Stemcells[GN]*Br[0]
    elif SCC ==2:
        newStemcells    = -Stemcells[GN]*Dr[0]
        newDeadCells1    = Stemcells[GN]*Dr[0]
    else:
        addnewDiCells   = Stemcells[GN]*Br[1]
        newStemcells    = -Stemcells[GN]*Br[1]
          
    if DCC == 0:
        newDiCells      = DiCells[GN]*Br[1]
    else:
        newDiCells      = -DiCells[GN]*Dr[1]
        newDeadCells2    = DiCells[GN]*Dr[1]
    
    StemCells.append(Stemcells[GN]+newStemcells)
    DiCells.append(DiCells[GN]+newDiCells+addnewDiCells)
    DeadCells.append(DeadCells[GN]+newDeadCells1+newDeadCells2)
    GN += 1
    return stoch_growth(StemCells,DiCells,DeadCells,TransitionMatrix,Br,Dr,GN)

#----------------------------------------------------------------------------#
stoch_growth(Stemcells,DiCells,DeadCells,TransitionMatrix,Br,Dr,0)
#----------------------------------------------------------------------------#
