import graph
from math import tan, pi

def calculation(ideal,actual):
    return ((actual-ideal)/ideal)*100


def area_rectangle(naming):
    if(naming=="abfh"):
        x1,y1=graph.x_act_pos3,graph.y_act_pos3
        x2,y2=graph.x_act_pos1,graph.y_act_pos1
        x3,y3=graph.x_act_pos1to2,graph.y_act_pos1to2
        x4,y4=graph.x_act_pos4to3,graph.y_act_pos4to3

        a_abfh=(x1*y2+x2*y3+x3*y4+x4*y1)-(y1*x2+y2*x3+y3*x4+y4*x1)
        a_abfh=abs(a_abfh*0.5)

        return(a_abfh)

    elif(naming=="fcdh"):
        x1,y1=graph.x_act_pos1to2,graph.y_act_pos1to2
        x2,y2=graph.x_act_pos2,graph.y_act_pos2
        x3,y3=graph.x_act_pos4,graph.y_act_pos4
        x4,y4=graph.x_act_pos4to3,graph.y_act_pos4to3

        a_fcdh=(x1*y2+x2*y3+x3*y4+x4*y1)-(y1*x2+y2*x3+y3*x4+y4*x1)
        a_fcdh=abs(a_fcdh*0.5)

        return(a_fcdh)

    elif(naming=="gdae"):
        x1,y1=graph.x_act_pos2to4,graph.y_act_pos2to4
        x2,y2=graph.x_act_pos4,graph.y_act_pos4
        x3,y3=graph.x_act_pos3,graph.y_act_pos3
        x4,y4=graph.x_act_pos3to1,graph.y_act_pos3to1

        a_gdae=(x1*y2+x2*y3+x3*y4+x4*y1)-(y1*x2+y2*x3+y3*x4+y4*x1)
        a_gdae=abs(a_gdae*0.5)

        return(a_gdae)

    elif(naming=="ebcg"):
        x1,y1=graph.x_act_pos3to1,graph.y_act_pos3to1
        x2,y2=graph.x_act_pos1,graph.y_act_pos1
        x3,y3=graph.x_act_pos2,graph.y_act_pos2
        x4,y4=graph.x_act_pos2to4,graph.y_act_pos2to4

        a_ebcg=(x1*y2+x2*y3+x3*y4+x4*y1)-(y1*x2+y2*x3+y3*x4+y4*x1)
        a_ebcg=abs(a_ebcg*0.5)

        return(a_ebcg)

    elif(naming=="aeih"):
        x1,y1=graph.x_act_pos3,graph.y_act_pos3
        x2,y2=graph.x_act_pos3to1,graph.y_act_pos3to1
        x3,y3=graph.x_act_posdist,graph.y_act_posdist
        x4,y4=graph.x_act_pos4to3,graph.y_act_pos4to3

        a_aeih=(x1*y2+x2*y3+x3*y4+x4*y1)-(y1*x2+y2*x3+y3*x4+y4*x1)
        a_aeih=abs(a_aeih*0.5)

        return(a_aeih)
    
    elif(naming=="ebfi"):
        x1,y1=graph.x_act_pos3to1,graph.y_act_pos3to1
        x2,y2=graph.x_act_pos1,graph.y_act_pos1
        x3,y3=graph.x_act_pos1to2,graph.y_act_pos1to2
        x4,y4=graph.x_act_posdist,graph.y_act_posdist

        a_ebfi=(x1*y2+x2*y3+x3*y4+x4*y1)-(y1*x2+y2*x3+y3*x4+y4*x1)
        a_ebfi=abs(a_ebfi*0.5)

        return(a_ebfi)

    elif(naming=="fcgi"):
        x1,y1=graph.x_act_pos1to2,graph.y_act_pos1to2
        x2,y2=graph.x_act_pos2,graph.y_act_pos2
        x3,y3=graph.x_act_pos2to4,graph.y_act_pos2to4
        x4,y4=graph.x_act_posdist,graph.y_act_posdist

        a_fcgi=(x1*y2+x2*y3+x3*y4+x4*y1)-(y1*x2+y2*x3+y3*x4+y4*x1)
        a_fcgi=abs(a_fcgi*0.5)

        return(a_fcgi)

    elif(naming=="gdhi"):
        x1,y1=graph.x_act_pos2to4,graph.y_act_pos2to4
        x2,y2=graph.x_act_pos4,graph.y_act_pos4
        x3,y3=graph.x_act_pos4to3,graph.y_act_pos4to3
        x4,y4=graph.x_act_posdist,graph.y_act_posdist

        a_gdhi=(x1*y2+x2*y3+x3*y4+x4*y1)-(y1*x2+y2*x3+y3*x4+y4*x1)
        a_gdhi=abs(a_gdhi*0.5)

        return(a_gdhi)

def area_triangle(naming):
    if(naming=="abi"):
        x1, y1 =graph.x_act_pos3,graph.y_act_pos3
        x2, y2 =graph.x_act_pos1,graph.y_act_pos1
        x3, y3 =graph.x_act_posdist,graph.y_act_posdist
        
        area_abi= (x1*y2 + x2*y3 + x3*y1) - (y1*x2 + y2*x3 + y3*x1)
        area_abi= abs(area_abi * 0.5)

        return(area_abi)

    elif(naming=="bci"):
        x1, y1 =graph.x_act_pos1,graph.y_act_pos1
        x2, y2 =graph.x_act_pos2,graph.y_act_pos2
        x3, y3 =graph.x_act_posdist,graph.y_act_posdist
        
        area_bci= (x1*y2 + x2*y3 + x3*y1) - (y1*x2 + y2*x3 + y3*x1)
        area_bci= abs(area_bci * 0.5)

        return(area_bci)

    elif(naming=="cdi"):
        x1, y1 =graph.x_act_pos2,graph.y_act_pos2
        x2, y2 =graph.x_act_pos4,graph.y_act_pos4
        x3, y3 =graph.x_act_posdist,graph.y_act_posdist
        
        area_cdi= (x1*y2 + x2*y3 + x3*y1) - (y1*x2 + y2*x3 + y3*x1)
        area_cdi= abs(area_cdi * 0.5)

        return(area_cdi)


    elif(naming=="dia"):
        x1, y1 =graph.x_act_pos4,graph.y_act_pos4
        x2, y2 =graph.x_act_pos3,graph.y_act_pos3
        x3, y3 =graph.x_act_posdist,graph.y_act_posdist
        
        area_dia= (x1*y2 + x2*y3 + x3*y1) - (y1*x2 + y2*x3 + y3*x1)
        area_dia= abs(area_dia * 0.5)

        return(area_dia)

    
    
    




            
       
    
    
