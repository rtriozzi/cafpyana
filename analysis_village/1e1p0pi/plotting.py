import matplotlib
import matplotlib.pyplot as plt

def UpdateMatplotlibStyle(
    ax,
    xlabel,
    ylabel,
    **legend_kwargs
):
    
    """
        Tweak matplotlib settings.
    """

    # labels
    ax.set_xlabel(xlabel, fontsize=14, loc='right')
    ax.set_ylabel(ylabel, fontsize=14, loc='top')
    ax.legend(frameon=True, fancybox=False, handlelength=1, **legend_kwargs)

    # ticks
    ax.minorticks_on()
    ax.tick_params(which='major', length=6, direction='in', labelsize=12, right=True, top=True)
    ax.tick_params(which='minor', length=3, direction='in', right=True, top=True)

    return ax