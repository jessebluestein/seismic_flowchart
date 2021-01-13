from graphviz import Digraph
import os

if __name__ == '__main__':

    # set name of output file as module name
    fileName = os.path.basename(__file__)
    fileName = fileName.replace('.py','')

    # long conditions that i don't want to type multiple times
    # note - need to manually set line break locations
    cond1 = 'Each story resisting more than 35% of the base shear in\n'
    cond1 += 'the direction of interest complies with Table 12.3-3.'

    cond2 = 'None of the Horizontal Irregularities of Table 12.3-1 apply.\n'
    cond2 += 'Seismic force-resisting systems consist of at least two bays\n'
    cond2 += 'of seismic force-resisting perimeter framing on each side of\n'
    cond2 += 'the structure in each orthogonal direction at each story resisting\n'
    cond2 += 'more than 35% of the base shear. (The number of bays for a shear\n'
    cond2 += 'wall shall be calculated as the length of shear wall divided by\n'
    cond2 += 'the story height or two times the length of shear wall divided\n'
    cond2 += ' by the story height, hsx, for light-frame construction.)'

    # create file
    g = Digraph('G', filename=fileName)

    # set node properties
    shape = 'box' # shape of the node
    color = 'black' # border color
    fillcolor = 'grey' # fill color
    style = 'rounded, filled' # style options

    # make nodes
    g.node('Determine Seismic Design Category (SDC)', shape = shape, color = color, style = style, fillcolor = fillcolor)
    g.node('SDC A, B or C', shape = shape, color = color, style = style, fillcolor = fillcolor)
    g.node('SDC D, E or F', shape = shape, color = color, style = style, fillcolor = fillcolor)
    g.node('ρ = 1.0', shape = shape, color = color, style = style, fillcolor = fillcolor)
    g.node('ρ = 1.3', shape = shape, color = color, style = style, fillcolor = fillcolor)
    g.node('Flexible diaphragm', shape = shape, color = color, style = style, fillcolor = fillcolor)
    g.node('Rigid diaphragm', shape = shape, color = color, style = style, fillcolor = fillcolor)
    g.node('Extreme torsional irregularity', shape = shape, color = color, style = style, fillcolor = fillcolor)
    g.node('No extreme torsional irregularity', shape = shape, color = color, style = style, fillcolor = fillcolor)
    g.node(cond1, shape = shape, color = color, style = style, fillcolor = fillcolor)
    g.node(cond2, shape = shape, color = color, style = style, fillcolor = fillcolor)

    # make edges (connect nodes)
    g.edge('Determine Seismic Design Category (SDC)', 'SDC A, B or C', splines='false')
    g.edge('Determine Seismic Design Category (SDC)', 'SDC D, E or F', splines='false')
    g.edge('SDC A, B or C', 'ρ = 1.0', splines='false')
    g.edge('SDC D, E or F', 'Flexible diaphragm', splines='false')
    g.edge('SDC D, E or F', 'Rigid diaphragm', splines='false')
    g.edge('Rigid diaphragm', 'Extreme torsional irregularity', splines='false')
    g.edge('Rigid diaphragm', 'No extreme torsional irregularity', splines='false')
    g.edge('No extreme torsional irregularity', cond1, splines='false')
    g.edge(cond1, cond2, label = 'not satisfied', splines='false')
    g.edge('Extreme torsional irregularity', 'ρ = 1.3', splines='false')
    g.edge('Flexible diaphragm', cond1, splines='false')
    g.edge(cond1, 'ρ = 1.0', label = 'satisfied', splines='false')
    g.edge(cond2, 'ρ = 1.0', label = 'satisfied', splines='false')
    g.edge(cond2, 'ρ = 1.3', label = 'not satisfied', splines='false')

    # view and save flowchart
    g.view()
