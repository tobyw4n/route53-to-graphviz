![example image](route53-small.jpeg?raw=true)

To get that image I ran the following graphviz command:

`neato -Goverlap=prism1000 -Gsplines=curved -Tjpg route53.dot -o route53.jpg`

The resulting image was huge and not the best format to view large DNS zones. I used JPG for an example and shrank it considerably to remove the details.

I've been using SVG format and zgrviewer to navigate such a large map and still see the details.

`neato -Goverlap=prism1000 -Gsplines=curved -Tsvg route53.dot -o route53.svg`