#author:Akhil P Jacob
#HLDynamic-Integrations
from matplotlib import pyplot as plt
from matplotlib import style


def draw_Line(x,y,name,ycontent,xcontent):
    plt.plot(x,y)#[1,2],[3,4]
    plt.title(name)
    plt.ylabel(ycontent)
    plt.xlabel(xcontent)
    plt.show()

def draw_Histo(x1,y1,x2,y2,label1,width1,label2,width2,xcontent,ycontent,heading):
    plt.bar(x1,y1,label=label1,width=width1)
    plt.bar(x2,y2,label=label2,width=width2)
    plt.legend()
    plt.xlabel(xcontent)
    plt.ylabel(ycontent)
    plt.title(heading)
    plt.show()

def draw_scatter(x,y,x1,y1,label1,label2,color1,color2,xlab,ylab,heading): 
    plt.scatter(x,y, label=label1,color=color1)
    plt.scatter(x1,y1,label=label2,color=color2)
    plt.xlabel(label1)
    plt.ylabel(label2)
    plt.title(heading)
    plt.legend()
    plt.show()