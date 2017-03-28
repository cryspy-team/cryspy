// Crystal Structure Drawing Program DRAWxtl V5.5

// Copyright 1996, 1997, 2000-2011 by Larry Finger, Martin Kroeker, and Brian Toby
//   (all rights reserved).

// Scene file created from output.cif.str 
// with command line options: -b  11.14  25.97  12.10 -o  0.50  0.50  0.50 
// -p -0.05  1.05 -0.05  1.05 -0.05  1.05 -v 14.30 -23.90 -36.10 -m  1.00


import three;
unitsize(0.1cm);
size(250,250);
viewportmargin=(1cm,1cm);
currentprojection=perspective ( 0.00, 0.00,406.81,target=( 0.00, 0.00,0.),up=Y);

picture pic;
transform3 t=rotate(14.30,X)*rotate(-23.90,Y)*rotate(-36.10,Z);

 draw(pic, (-3.71440,-8.65655,-4.03480)--(-3.71440,-8.65655, 4.03480)--(-3.71440, 8.65655, 4.03480)--(-3.71440, 8.65655,-4.03480)--cycle,rgb(0.00,0.00,0.00) );
 draw(pic, ( 3.71440,-8.65655,-4.03480)--( 3.71440, 8.65655,-4.03480)--( 3.71440, 8.65655, 4.03480)--( 3.71440,-8.65655, 4.03480)--cycle,rgb(0.00,0.00,0.00) );
 draw(pic, (-3.71440,-8.65655,-4.03480)--( 3.71440,-8.65655,-4.03480),rgb(0.00,0.00,0.00) );
 draw(pic, (-3.71440,-8.65655, 4.03480)--( 3.71440,-8.65655, 4.03480),rgb(0.00,0.00,0.00) );
 draw(pic, (-3.71440, 8.65655, 4.03480)--( 3.71440, 8.65655, 4.03480),rgb(0.00,0.00,0.00) );
 draw(pic, (-3.71440, 8.65655,-4.03480)--( 3.71440, 8.65655,-4.03480),rgb(0.00,0.00,0.00) );
 // Sphere for Dy_  at  0.70700  0.32800  0.05200  
draw(pic, shift ( 1.53776, -2.97785, -3.61518)*scale3(0.40)*unitsphere,rgb(1.00,0.00,1.00));
 // Sphere for Dy_  at  0.98200  0.08200  0.00000  
draw(pic, shift ( 3.58068, -7.23688, -4.03480)*scale3(0.40)*unitsphere,rgb(1.00,0.00,1.00));
 // Sphere for Dy_  at -0.01800  0.08200  0.00000  
draw(pic, shift (-3.84812, -7.23688, -4.03480)*scale3(0.40)*unitsphere,rgb(1.00,0.00,1.00));
 // Sphere for Dy_  at -0.01800  0.08200  1.00000  
draw(pic, shift (-3.84812, -7.23688,  4.03480)*scale3(0.40)*unitsphere,rgb(1.00,0.00,1.00));
 // Sphere for Dy_  at  0.98200  0.08200  1.00000  
draw(pic, shift ( 3.58068, -7.23688,  4.03480)*scale3(0.40)*unitsphere,rgb(1.00,0.00,1.00));
 // Sphere for Dy_  at  0.01800  0.91800  1.00000  
draw(pic, shift (-3.58068,  7.23688,  4.03480)*scale3(0.40)*unitsphere,rgb(1.00,0.00,1.00));
 // Sphere for Dy_  at  0.01800  0.91800  0.00000  
draw(pic, shift (-3.58068,  7.23688, -4.03480)*scale3(0.40)*unitsphere,rgb(1.00,0.00,1.00));
 // Sphere for Dy_  at  1.01800  0.91800  0.00000  
draw(pic, shift ( 3.84812,  7.23688, -4.03480)*scale3(0.40)*unitsphere,rgb(1.00,0.00,1.00));
 // Sphere for Dy_  at  1.01800  0.91800  1.00000  
draw(pic, shift ( 3.84812,  7.23688,  4.03480)*scale3(0.40)*unitsphere,rgb(1.00,0.00,1.00));
 // Sphere for Dy_  at  0.29300  0.67200  0.94800  
draw(pic, shift (-1.53776,  2.97785,  3.61518)*scale3(0.40)*unitsphere,rgb(1.00,0.00,1.00));
 // Sphere for Dy_  at  0.00000  0.00000  0.00000  
draw(pic, shift (-3.71440, -8.65655, -4.03480)*scale3(0.40)*unitsphere,rgb(1.00,0.00,1.00));
 // Sphere for Dy_  at  0.00000  0.00000  1.00000  
draw(pic, shift (-3.71440, -8.65655,  4.03480)*scale3(0.40)*unitsphere,rgb(1.00,0.00,1.00));
 // Sphere for Dy_  at  0.00000  1.00000  0.00000  
draw(pic, shift (-3.71440,  8.65655, -4.03480)*scale3(0.40)*unitsphere,rgb(1.00,0.00,1.00));
 // Sphere for Dy_  at  0.00000  1.00000  1.00000  
draw(pic, shift (-3.71440,  8.65655,  4.03480)*scale3(0.40)*unitsphere,rgb(1.00,0.00,1.00));
 // Sphere for Dy_  at  1.00000  0.00000  0.00000  
draw(pic, shift ( 3.71440, -8.65655, -4.03480)*scale3(0.40)*unitsphere,rgb(1.00,0.00,1.00));
 // Sphere for Dy_  at  1.00000  0.00000  1.00000  
draw(pic, shift ( 3.71440, -8.65655,  4.03480)*scale3(0.40)*unitsphere,rgb(1.00,0.00,1.00));
 // Sphere for Dy_  at  1.00000  1.00000  0.00000  
draw(pic, shift ( 3.71440,  8.65655, -4.03480)*scale3(0.40)*unitsphere,rgb(1.00,0.00,1.00));
 // Sphere for Dy_  at  1.00000  1.00000  1.00000  
draw(pic, shift ( 3.71440,  8.65655,  4.03480)*scale3(0.40)*unitsphere,rgb(1.00,0.00,1.00));
 // Sphere for Dy_  at  0.10800  0.47100  0.00000  
draw(pic, shift (-2.91209, -0.50208, -4.03480)*scale3(0.40)*unitsphere,rgb(1.00,0.00,1.00));
 // Sphere for Dy_  at  0.10800  0.47100  1.00000  
draw(pic, shift (-2.91209, -0.50208,  4.03480)*scale3(0.40)*unitsphere,rgb(1.00,0.00,1.00));
 // Sphere for Dy_  at  0.89200  0.52900  1.00000  
draw(pic, shift ( 2.91209,  0.50208,  4.03480)*scale3(0.40)*unitsphere,rgb(1.00,0.00,1.00));
 // Sphere for Dy_  at  0.89200  0.52900  0.00000  
draw(pic, shift ( 2.91209,  0.50208, -4.03480)*scale3(0.40)*unitsphere,rgb(1.00,0.00,1.00));
 label(pic, "o",(-4.21213,-9.15863,-4.53512));
 label(pic, "a",( 4.21213,-8.65655,-4.03480));
 label(pic, "b",(-3.71440, 9.15863,-4.03480));
 label(pic, "c",(-3.71440,-8.65655, 4.53512));
add(t*pic);
