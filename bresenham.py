# Desta Ari Alfananda
# 20051397008
# 2020B

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def BRESENHAM(x1,x2,y1,y2):
    #menentukan delta X dan delta Y
    x=x1
    y=y1
    deltaX = abs(x2-x1)
    deltaY = abs(y2-y1)

    #menghitung p
    p = (2 * deltaY) - (deltaX)
    duady = 2 * deltaY
    duaDyDx = 2 * (deltaY-deltaX) 

    #Menentukan titik awal dan titim akhir
    if(x1>x2):
        x = x2
        y = y2
        xend = x1
        
    else:
        x = x1
        y = y1
        xend = x2

    #Memulai menggambar menggunakan BRESENHAM
    #Membersihkan window
    glClear(GL_COLOR_BUFFER_BIT)
    #Menentukan warna
    glColor3f(1.0,0.0,0.0)
    #Spesifikasikan diameter dari pixel yang akan digammbar
    glPointSize(10.0)
    #Memilih mode point
    glBegin(GL_POINTS)
    glVertex2i(x,y)

    #looping dari langkah ke 1 sampai langkah terakhir
    while x<xend:
        x +=1
        
        if(p<0):
            p+=duady
        elif(y1>y2):
            y+=1
        else:
            y-=1
            
        p += duaDyDx
        
        glVertex2i(x,y)  
    
    glEnd()
    glFlush()

def main():
    x1 = int(15)
    y1 = int(10)
    x2 = int(50)
    y2 = int(35)

    #inisialisasi glut
    glutInit(sys.argv)
    #inisialisasi tipe display glut
    glutInitDisplayMode(GLUT_RGB)
    #inisialisasi ukuran layar glut
    glutInitWindowSize(500,500)
    #inisiasliasi posisi layar glut
    glutInitWindowPosition(0,0)
    #inisialisasi pembuatan window
    glutCreateWindow("Menggambar garis menggunakan BRESENHAM")
    glutDisplayFunc(lambda: BRESENHAM(x1,y1,x2,y2))
    glutIdleFunc(lambda: BRESENHAM(x1,y1,x2,y2))
    
    #Memberihkan layar dan memberikan warna
    glClearColor(0.0,0.0,0.0,1.0)
    #Set origin dari grid dan ukurannya 100 x 100
    gluOrtho2D(0,100,0,100)
    glutMainLoop()
    
main()