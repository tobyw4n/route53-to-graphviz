#!/usr/bin/env python
import boto.route53
import pygraphviz as pgv

G=pgv.AGraph()
G.graph_attr.update(outputorder='edgesfirst')
G.node_attr.update(color='gray', style='filled', fillcolor='gray')

# i have multiple aws accounts and setup my BOTO_CONFIG file with profiles
# http://boto.readthedocs.org/en/latest/boto_config_tut.html
accounts = [ 'profile1', 'profile2', 'profile3' ]
region = 'us-east-1'

# a quick list of graphviz color names so i can give each hosted zone its own color
colors = [  'blue', 'crimson', 'green', 'orange', 'yellow', 'aquamarine', 
            'turquoise4', 'coral', 'purple', 'brown', 'olivedrab', 'orchid', 
            'limegreen', 'navy', 'pink', 'cornflowerblue', 'gold', 'darkseagreen2',
            'goldenrod2', 'khaki', 'lavenderblush3', 'steelblue2', 'springgreen',
            'tomato2', 'wheat2'  ]

i = 0

for account in accounts:
  r53 = boto.route53.connect_to_region(region, profile_name=account)
  zones = r53.get_zones()

  for zone in zones:
    records = zone.get_records()
    zonename = zone.name.rstrip('\.')
    color = colors[i]

    print "%s -> %s" % (zonename, color)
    
    for record in records:
      value = record.to_print()
      name = record.name.rstrip('\.')
      rtype = record.type
      if rtype == 'CNAME':
        if G.has_node(name):
          G.get_node(name).attr['color'] = color
          G.get_node(name).attr['fillcolor'] = color
        else:
          G.add_node(name, color=color, fillcolor=color)
        G.add_node(value)
        G.add_edge(zonename, name, dir='forward')
        G.add_edge(name, value, dir='forward')
      if rtype == 'A':
        values = value.split(',')
        for avalue in values:
          if G.has_node(name):
            G.get_node(name).attr['color'] = color
            G.get_node(name).attr['fillcolor'] = color
          else:
            G.add_node(name, color=color, fillcolor=color)
          G.add_node(avalue)
          G.add_edge(zonename, name, dir='forward')
          G.add_edge(name, avalue, dir='forward')

    i += 1

G.write('route53-to-graphviz.dot')