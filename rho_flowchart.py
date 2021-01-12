from graphviz import Digraph
import os

if __name__ == '__main__':

    # set name of output file as mofule name
    fileName = os.path.basename(__file__)
    fileName = fileName.replace('.py','')

    # long conditions that i don't want to type multiple times
    # note - need to manually set line break locations
    cond1 = 'Each story resisting more than 35% of the base\nshear in the direction of interest shall complies with Table 12.3-3.'
    cond2 = 'Structures are regular in plan at all levels provided \nthat the seismic force-resisting systems consist of at \nleast two bays of seismic force-resisting perimeter framing \non each side of the structure in each orthogonal direction at each \nstory resisting more than 35% of the base shear. The number \nof bays for a shear wall shall be calculated as the length of shear \nwall divided by the story height or two times the length of shear wall \ndivided by the story height, hsx, for light-frame construction.'

    # make flowchart
    g = Digraph('G', filename=fileName)
    g.edge('Determine Seismic Design Category (SDC)', 'SDC A, B or C')
    g.edge('Determine Seismic Design Category (SDC)', 'SDC D, E or F')
    g.edge('SDC A, B or C', 'ρ = 1.0')
    g.edge('SDC D, E or F', 'Flexible diaphragm')
    g.edge('SDC D, E or F', 'Rigid diaphragm')
    g.edge('Rigid diaphragm', 'Extreme torsional irregularity')
    g.edge('Rigid diaphragm', 'Not extreme torsional irregularity')
    g.edge('Not extreme torsional irregularity', cond1)
    g.edge('Not extreme torsional irregularity', cond2)
    g.edge('Extreme torsional irregularity', 'ρ = 1.3')
    g.edge('Flexible diaphragm', cond1)
    g.edge('Flexible diaphragm', cond2)
    g.edge(cond1, 'ρ = 1.0')
    g.edge(cond2, 'ρ = 1.0')

    # view and save flowchart
    g.view()
