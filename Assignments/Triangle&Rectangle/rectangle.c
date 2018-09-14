#include<stdio.h>
#include<limits.h>
#include<graphics.h>
#include<stdlib.h>
#include <math.h>
#include <dos.h>
#include <conio.h>
// modulus function
int mod(int a)
{
  if(a < 0)
	return -1*a;
  else
	return a;
}
// function for making ofmaking a line
void dda(int X0, int Y0, int X1, int Y1)
{
  int dx = X1 - X0;
  int dy = Y1 - Y0;
  int i;
  int steps = mod(dx) > mod(dy) ? mod(dx) : mod(dy);
  float xinc = dx / (float)steps;
  float yinc = dy / (float)steps;
  float x = X0;
  float y = Y0;
  for(i = 0; i < steps; i++)
  {
    putpixel(x, y, WHITE);
    x += xinc;
    y += yinc;
    delay(7);
  }
}
void m_lt_one(int x0, int y0, int x1, int y1)
{
	int dx, dy, x, y, change_y, p;

	dx = x1 - x0;
	dy = y1 - y0;
	change_y = 1;

	if ( dy < 0)
	{
		change_y = -1;
		dy = -dy;
	}

	p = 2*dy - dx;
	y = y0;

	for (x = x0; x <= x1; x++)
	{
		putpixel(x, y, WHITE);
		if ( p > 0)
		{
			y = y + change_y;
			p = p + 2*dy - 2*dx;
		}
		else{
			p = p + 2*dy;
		}
		delay(7);
	}
}
void m_gt_one(int x0, int y0, int x1, int y1)
{
	int x, y, dx, dy, p, change_x;

	dx = x1 - x0;
	dy = y1 - y0;
	change_x = 1;

	if ( dx < 0)
	{
		change_x = -1;
		dx = -dx;
	}

	p = 2*dx - dy;
	x = x0;

	for( y = y0; y <= y1; y++)
	{
		putpixel(x, y, WHITE);
		if( p > 0)
		{
			x = x + change_x;
			p = p + 2*dx- 2*dy;
		}
		else
		{
			p = p + 2*dx;
		}
		delay(7);
	}
}
void bresenham(int x0, int y0, int x1, int y1)
{
    if(mod(x1 - x0) > mod(y1 - y0))
    {
	if(x1 > x0)
	    m_lt_one(x0, y0, x1, y1);
	else
	    m_lt_one(x1, y1, x0, y0);
    }
    else
    {
	if(y1 > y0)
	    m_gt_one(x0, y0, x1, y1);
	else
	    m_gt_one(x1, y1, x0, y0);
    }
}
// driver program
int main()
{
    int gd = DETECT, gm;
	int choice;
	int x0, x1, x2, x3, y3, y2, y0, y1;
	clrscr();
	printf("\nEnter the choice for the algorithm\n1. for dda\n2. for bresenham\t");
	scanf("%d", &choice);
	printf("Enter the four vertices of rectangle\n");
	scanf("%d%d",&x0, &y0);
	scanf("%d%d",&x1, &y1);
	scanf("%d%d",&x2, &y2);
	scanf("%d%d",&x3, &y3);
	clrscr();
	initgraph(&gd, &gm, "C:\\TC\\BGI");
	if(choice == 1)
	{
		dda(x0, y0, x1, y1);
		dda(x1, y1, x2, y2);
		dda(x2, y2, x3, y3);
		dda(x3, y3, x0, y0);
	}
	else
	{
		bresenham(x0, y0, x1, y1);
		bresenham(x1, y1, x2, y2);
		bresenham(x2, y2, x3, y3);
		bresenham(x3, y3, x0, y0);
	}
    getch();
    return 0;
}
