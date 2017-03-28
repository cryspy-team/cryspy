/*

POVxtl-Persistence of Vision Ray Tracer
Crystal Structure Drawing Program V5.5

Copyright 1996, 1997, 2000-2011 by Larry Finger, Martin Kroeker, and Brian Toby
   (all rights reserved).

Scene file created from output.cif.str 
with command line options: -b  11.14  25.97  12.10 -o  0.50  0.50  0.50 
-p -0.05  1.05 -0.05  1.05 -0.05  1.05 -v 14.30 -23.90 -36.10 -m  1.00
*/

#if (version>3.65)
#version 3.6;
#end

#include "colors.inc"
#include "chars.inc"

default {
        finish {
                ambient  0.70
                diffuse  0.30
                specular  0.08
                roughness  0.01
               }
        }

camera{
 location< 0.000000 ,0.000000, 406.814362>
 up <0, 0.1, 0>
 right <-0.1, 0, 0>
 look_at <0.000000,0.000000,0>
}
background{color White}
light_source {< 0, 0, 254.258972>
color red 4.0 green 4.0 blue 4.0
}
object{
 union{

#declare xrot =  14.3;
#declare yrot = -23.9;
#declare zrot = -36.1;
#declare xmove =   0.0;
#declare ymove =   0.0;

  cylinder{<-3.714400,-8.656550,-4.034800>,<-3.714400,-8.656550,4.034800>,0.050852 
   texture{pigment{color Black }}
   no_shadow no_reflection
  }
  cylinder{<-3.714400,-8.656550,4.034800>,<-3.714400,8.656550,4.034800>,0.050852
   texture{pigment{color Black }}
   no_shadow no_reflection
  }
  cylinder{<-3.714400,8.656550,4.034800>,<-3.714400,8.656550,-4.034800>,0.050852
   texture{pigment{color Black }}
   no_shadow no_reflection
  }
  cylinder{<-3.714400,8.656550,-4.034800>,<-3.714400,-8.656550,-4.034800>, 0.050852
   texture{pigment{color Black }}
   no_shadow no_reflection
  }
  cylinder{<-3.714400,-8.656550,-4.034800>,<3.714400,-8.656550,-4.034800>,0.050852
   texture{pigment{color Black }}
   no_shadow no_reflection
  }
  cylinder{<3.714400,-8.656550,-4.034800>,<3.714400,8.656550,-4.034800>,0.050852
   texture{pigment{color Black }}
   no_shadow no_reflection
  }
  cylinder{<3.714400,8.656550,-4.034800>,<3.714400,8.656550,4.034800>,0.050852
   texture{pigment{color Black }}
   no_shadow no_reflection
  }
  cylinder{<3.714400,8.656550,4.034800>,<3.714400,-8.656550,4.034800>,0.050852
   texture{pigment{color Black }}
   no_shadow no_reflection
  }
  cylinder{<3.714400,-8.656550,4.034800>,<3.714400,-8.656550,-4.034800>,0.050852
   texture{pigment{color Black }}
   no_shadow no_reflection
  }
  cylinder{<3.714400,8.656550,-4.034800>,<-3.714400,8.656550,-4.034800>,0.050852
   texture{pigment{color Black }}
   no_shadow no_reflection
  }
  cylinder{<-3.714400,8.656550,4.034800>,<3.714400,8.656550,4.034800>,0.050852
   texture{pigment{color Black }}
   no_shadow no_reflection
  }
  cylinder{<3.714400,-8.656550,4.034800>,<-3.714400,-8.656550,4.034800>,0.050852
   texture{pigment{color Black }}
   no_shadow no_reflection
  }
 /* Sphere for Dy_  at  0.70700  0.32800  0.05200 */ 
 sphere{< 1.53776, -2.97785, -3.61518>,  0.40000
  texture{pigment{color Magenta  }}
   finish{phong  0.20 phong_size  1.00}
 }
 /* Sphere for Dy_  at  0.98200  0.08200  0.00000 */ 
 sphere{< 3.58068, -7.23688, -4.03480>,  0.40000
  texture{pigment{color Magenta  }}
   finish{phong  0.20 phong_size  1.00}
 }
 /* Sphere for Dy_  at -0.01800  0.08200  0.00000 */ 
 sphere{<-3.84812, -7.23688, -4.03480>,  0.40000
  texture{pigment{color Magenta  }}
   finish{phong  0.20 phong_size  1.00}
 }
 /* Sphere for Dy_  at -0.01800  0.08200  1.00000 */ 
 sphere{<-3.84812, -7.23688,  4.03480>,  0.40000
  texture{pigment{color Magenta  }}
   finish{phong  0.20 phong_size  1.00}
 }
 /* Sphere for Dy_  at  0.98200  0.08200  1.00000 */ 
 sphere{< 3.58068, -7.23688,  4.03480>,  0.40000
  texture{pigment{color Magenta  }}
   finish{phong  0.20 phong_size  1.00}
 }
 /* Sphere for Dy_  at  0.01800  0.91800  1.00000 */ 
 sphere{<-3.58068,  7.23688,  4.03480>,  0.40000
  texture{pigment{color Magenta  }}
   finish{phong  0.20 phong_size  1.00}
 }
 /* Sphere for Dy_  at  0.01800  0.91800  0.00000 */ 
 sphere{<-3.58068,  7.23688, -4.03480>,  0.40000
  texture{pigment{color Magenta  }}
   finish{phong  0.20 phong_size  1.00}
 }
 /* Sphere for Dy_  at  1.01800  0.91800  0.00000 */ 
 sphere{< 3.84812,  7.23688, -4.03480>,  0.40000
  texture{pigment{color Magenta  }}
   finish{phong  0.20 phong_size  1.00}
 }
 /* Sphere for Dy_  at  1.01800  0.91800  1.00000 */ 
 sphere{< 3.84812,  7.23688,  4.03480>,  0.40000
  texture{pigment{color Magenta  }}
   finish{phong  0.20 phong_size  1.00}
 }
 /* Sphere for Dy_  at  0.29300  0.67200  0.94800 */ 
 sphere{<-1.53776,  2.97785,  3.61518>,  0.40000
  texture{pigment{color Magenta  }}
   finish{phong  0.20 phong_size  1.00}
 }
 /* Sphere for Dy_  at  0.00000  0.00000  0.00000 */ 
 sphere{<-3.71440, -8.65655, -4.03480>,  0.40000
  texture{pigment{color Magenta  }}
   finish{phong  0.20 phong_size  1.00}
 }
 /* Sphere for Dy_  at  0.00000  0.00000  1.00000 */ 
 sphere{<-3.71440, -8.65655,  4.03480>,  0.40000
  texture{pigment{color Magenta  }}
   finish{phong  0.20 phong_size  1.00}
 }
 /* Sphere for Dy_  at  0.00000  1.00000  0.00000 */ 
 sphere{<-3.71440,  8.65655, -4.03480>,  0.40000
  texture{pigment{color Magenta  }}
   finish{phong  0.20 phong_size  1.00}
 }
 /* Sphere for Dy_  at  0.00000  1.00000  1.00000 */ 
 sphere{<-3.71440,  8.65655,  4.03480>,  0.40000
  texture{pigment{color Magenta  }}
   finish{phong  0.20 phong_size  1.00}
 }
 /* Sphere for Dy_  at  1.00000  0.00000  0.00000 */ 
 sphere{< 3.71440, -8.65655, -4.03480>,  0.40000
  texture{pigment{color Magenta  }}
   finish{phong  0.20 phong_size  1.00}
 }
 /* Sphere for Dy_  at  1.00000  0.00000  1.00000 */ 
 sphere{< 3.71440, -8.65655,  4.03480>,  0.40000
  texture{pigment{color Magenta  }}
   finish{phong  0.20 phong_size  1.00}
 }
 /* Sphere for Dy_  at  1.00000  1.00000  0.00000 */ 
 sphere{< 3.71440,  8.65655, -4.03480>,  0.40000
  texture{pigment{color Magenta  }}
   finish{phong  0.20 phong_size  1.00}
 }
 /* Sphere for Dy_  at  1.00000  1.00000  1.00000 */ 
 sphere{< 3.71440,  8.65655,  4.03480>,  0.40000
  texture{pigment{color Magenta  }}
   finish{phong  0.20 phong_size  1.00}
 }
 /* Sphere for Dy_  at  0.10800  0.47100  0.00000 */ 
 sphere{<-2.91209, -0.50208, -4.03480>,  0.40000
  texture{pigment{color Magenta  }}
   finish{phong  0.20 phong_size  1.00}
 }
 /* Sphere for Dy_  at  0.10800  0.47100  1.00000 */ 
 sphere{<-2.91209, -0.50208,  4.03480>,  0.40000
  texture{pigment{color Magenta  }}
   finish{phong  0.20 phong_size  1.00}
 }
 /* Sphere for Dy_  at  0.89200  0.52900  1.00000 */ 
 sphere{< 2.91209,  0.50208,  4.03480>,  0.40000
  texture{pigment{color Magenta  }}
   finish{phong  0.20 phong_size  1.00}
 }
 /* Sphere for Dy_  at  0.89200  0.52900  0.00000 */ 
 sphere{< 2.91209,  0.50208, -4.03480>,  0.40000
  texture{pigment{color Magenta  }}
   finish{phong  0.20 phong_size  1.00}
 }
/* Labels */
  text { ttf "crystal.ttf","o" 0.15,0
    scale <1.13,1.13,1.13>
    rotate <0, 0, -zrot>
    rotate <0, -yrot, 0>
    rotate <-xrot,0, 0>
    translate <-4.21213,-9.15863,-4.53512> pigment{color Black}
  }
/* Labels */
  text { ttf "crystal.ttf","a" 0.15,0
    scale <1.13,1.13,1.13>
    rotate <0, 0, -zrot>
    rotate <0, -yrot, 0>
    rotate <-xrot,0, 0>
    translate < 4.21213,-8.65655,-4.03480> pigment{color Black}
  }
/* Labels */
  text { ttf "crystal.ttf","b" 0.15,0
    scale <1.13,1.13,1.13>
    rotate <0, 0, -zrot>
    rotate <0, -yrot, 0>
    rotate <-xrot,0, 0>
    translate <-3.71440, 9.15863,-4.03480> pigment{color Black}
  }
/* Labels */
  text { ttf "crystal.ttf","c" 0.15,0
    scale <1.13,1.13,1.13>
    rotate <0, 0, -zrot>
    rotate <0, -yrot, 0>
    rotate <-xrot,0, 0>
    translate <-3.71440,-8.65655, 4.53512> pigment{color Black}
  }
 }
rotate <xrot, 0, 0>
rotate <0, yrot, 0>
rotate <0, 0, zrot>
translate <xmove, ymove, 0>
}
