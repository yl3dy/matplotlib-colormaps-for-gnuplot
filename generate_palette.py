"""
Gnuplot palette generation script.
"""

from colormaps import _plasma_data, _magma_data, _inferno_data, _viridis_data

header = """# {} colorscheme from Matplotlib converted for gnuplot.
# Originally designed by Nathaniel J. Smith, Stefan van der Walt and
# Eric Firing. Colormaps themselves are under CC0 license."""

footer = "# vim: set syntax=gnuplot tw=0:"

def make_palette(palette_data, output_file, common_name):
    """Generate single palette."""
    header_ = header.format(common_name)

    with open(output_file, 'w') as f:
        f.write(header_ + '\n\n')
        f.write('set palette defined(\\\n')

        value = 0.
        dv = 1. / (len(palette_data) - 1)
        for i in range(len(palette_data)):
            f.write('{} {} {} {}'.format(value, *palette_data[i]))
            if i != (len(palette_data) - 1):
                f.write(',\\\n')
            else:
                f.write(')\n')
            value += dv

        f.write('\n' + footer)


if __name__ == '__main__':
    palettes = ((_plasma_data, 'plasma.plt', 'Plasma'),
                (_magma_data, 'magma.plt', 'Magma'),
                (_inferno_data, 'inferno.plt', 'Inferno'),
                (_viridis_data, 'viridis.plt', 'Viridis'))

    for palette in palettes:
        make_palette(*palette)
