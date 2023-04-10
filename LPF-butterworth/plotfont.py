import matplotlib.pyplot as plt

def font_func(fontD_size = 24, title_font_size = 28, axis_label_font_size = 20, axis_ticklabel_font_size = 24, legend_font_size = 24):
    #Fonts
    #Default Font
    #fontD_size = 20;
    #title_font_size = 24;
    #axis_label_font_size = 20;
    #axis_ticklabel_font_size = 20;
    fontD = {'family' : 'Times New Roman','size' : fontD_size,'weight' : 'normal',}
    #Label
    axis_label_font = {'family':'Times New Roman', 'size': axis_label_font_size,'color': 'black'}
    title_font = {'family':'Times New Roman', 'size': title_font_size, 'color':'black', 'weight':'bold', 'verticalalignment':'bottom','horizontalalignment':'center','usetex':False}
    #Tick Label
    axis_ticklabel_font = {'family':'Times New Roman', 'size':axis_ticklabel_font_size,'color': 'black'}
    plt.rc('axes.formatter',use_mathtext = True) #activate math
    #Assign Times New Roman font to math
    plt.rcParams['mathtext.fontset'] = 'stix'
    #plt.rcParams['mathtext.rm'] = 'Times New Roman'
    #plt.rcParams['mathtext.it'] = 'Times New Roman:italic'
    #plt.rcParams['mathtext.bf'] = 'Times New Roman:bold'
    #matplotlib.mathtext.DELTA = 0.5

    print('Font size =',fontD_size,'; ', 'Title Font Size =',title_font_size,'; ', 'Axis Label Font Size =',axis_label_font_size,'; ', 'Axis Ticklabel Font Size =',axis_ticklabel_font_size, ';')
    return fontD, axis_label_font, axis_ticklabel_font