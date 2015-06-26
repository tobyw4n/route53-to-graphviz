![example image](route53-small.jpeg?raw=true)

To get that image I ran the following graphviz command:

`neato -Goverlap=prism1000 -Gsplines=curved -Tjpg route53.dot -o route53.jpg`

The output image was huge and not the best format to view large DNS zones. I used JPG for example only and shrank it considerably to remove the details on purpose.

I've been using SVG format and zgrviewer to navigate the large map while still seeing the details.

`neato -Goverlap=prism1000 -Gsplines=curved -Tsvg route53.dot -o route53.svg`