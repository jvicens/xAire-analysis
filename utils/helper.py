import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from scipy import stats


reds = ["#f7ccce", "#ef9a9e", "#e7676d", "#df353d", "#d7030d", "#c1020b", "#960209", "#6b0106", "#400003"]

plt.style.use('seaborn-ticks')

label_style = {'fontsize': 14, 'fontweight': 'bold', 'color': 'black'}
ticks_style = {'fontsize': 12, 'fontweight': 'regular', 'color': 'black'}
legend_style = {'size': 12, 'weight': 'regular'}

def get_stats(data, n_round = 2):
    
    dict = {'n': round(data.count(), n_round),
            'Median': round(data.median(), n_round),
            'Mean' : round(data.mean(), n_round),
            'SD' : round(data.std(), n_round),
            's.e.m' : round(data.sem(), n_round),
            '5%' : round(np.percentile(data, q=5), n_round),
            '25%' : round(np.percentile(data, q=25), n_round),
            '75%' : round(np.percentile(data, q=75), n_round),
            '95%' : round(np.percentile(data, q=95), n_round),
            'Kurtosis' : round(stats.kurtosis(data, bias=False), n_round),
            'Skewness' : round(stats.skew(data, bias=False), n_round)
           }
    
    return dict

def normalization(sample):
    s = sample/np.sum(sample)
    return s

#### Plots samplers and automatic stations

def plot_samplers(X, Y, x, y, title='Figure'):

    plt.clf()
    plt.figure()

    plt.scatter(X, Y, color=reds[5])

    plt.plot(x, y, color=reds[5], label='Linear (x=y)')
    plt.plot(x, [x * 1.1 for x in y], '--', color=reds[2], label='Linear (x+-10%)', linewidth=.75)
    plt.plot(x, [x * 0.9 for x in y], '--', color=reds[2], linewidth=.75)

    plt.fill_between(x, [x * 1.1 for x in y], [x * 0.9 for x in y], color=reds[2], alpha=.2)

    plt.xlim(20,60)
    plt.ylim(20,60)

    plt.xlabel('Automatic station NO2 level', **label_style)
    plt.ylabel('Passive sampler average NO2 level', **label_style)
    plt.xticks(**ticks_style)
    plt.yticks(**ticks_style)
    plt.gca().spines["top"].set_visible(False)    
    plt.gca().spines["bottom"].set_visible(False)    
    plt.gca().spines["right"].set_visible(False)    
    plt.gca().spines["left"].set_visible(False) 

    plt.grid(axis='y', alpha=1, linewidth=.5, color='#eeeeee')
    plt.grid(axis='x', alpha=1, linewidth=.5, color='#eeeeee')
    plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=True) 
    plt.tick_params(axis='y', which='both', left=False, right=False, labelleft=True)
    plt.legend(frameon=False, prop= legend_style)

    plt.savefig('img/'+title+'.pdf', dpi=300, figsize=(5,5))
    #plt.savefig('img/'+title+'.png', dpi=300, figsize=(5,5))



#### Plots NO2 distributions

def plot_NO2(df):

    plt.figure()

    sns.distplot(df[df['no2_2017']<=20]['no2_2017'], bins=range(0,140,5), color=reds[0], label="< 20 µg/m3", kde= False, hist_kws=dict(width=4.7, alpha=1))
    sns.distplot(df[(df['no2_2017'] > 20) & (df['no2_2017'] <= 25)]['no2_2017'], bins=range(0,140,5), color=reds[1], label="20 - 24 µg/m3", kde= False, hist_kws=dict(width=4.7, alpha=1))
    sns.distplot(df[(df['no2_2017'] > 25) & (df['no2_2017'] <= 30)]['no2_2017'], bins=range(0,140,5), color=reds[2], label="25 - 29 µg/m3", kde= False, hist_kws=dict(width=4.7, alpha=1))
    sns.distplot(df[(df['no2_2017'] > 30) & (df['no2_2017'] <= 35)]['no2_2017'], bins=range(0,140,5), color=reds[3], label="30 - 34 µg/m3", kde= False, hist_kws=dict(width=4.7, alpha=1))
    sns.distplot(df[(df['no2_2017'] > 35) & (df['no2_2017'] <= 40)]['no2_2017'], bins=range(0,140,5), color=reds[4], label="35 - 39 µg/m3", kde= False, hist_kws=dict(width=4.7, alpha=1))
    sns.distplot(df[(df['no2_2017'] > 40) & (df['no2_2017'] <= 45)]['no2_2017'], bins=range(0,140,5), color=reds[5], label="40 - 44 µg/m3", kde= False, hist_kws=dict(width=4.7, alpha=1))
    sns.distplot(df[(df['no2_2017'] > 45) & (df['no2_2017'] < 50)]['no2_2017'], bins=range(0,140,5), color=reds[6], label="45 - 49 µg/m3", kde= False, hist_kws=dict(width=4.7, alpha=1))
    sns.distplot(df[(df['no2_2017'] > 50)]['no2_2017'], bins=range(0,140,5), color=reds[7], label="> 50µg/m3", kde= False, hist_kws=dict(width=4.7, alpha=1))

    # Decoration
    plt.xlabel('NO2 level', **label_style)
    plt.ylabel('Sampling sites', **label_style)
    plt.xticks(**ticks_style)
    plt.yticks(**ticks_style)
    plt.ylim(0,120)
    plt.gca().spines["top"].set_visible(False)    
    plt.gca().spines["bottom"].set_visible(True)    
    plt.gca().spines["right"].set_visible(False)    
    plt.gca().spines["left"].set_visible(False) 
    plt.grid(axis='y', alpha=1, linewidth=.5, color='#eeeeee')
    plt.grid(axis='y', alpha=1, linewidth=.5, color='#eeeeee')
    plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=True) 
    plt.tick_params(axis='y', which='both', left=False, right=False, labelleft=True)
    plt.legend(frameon=False, prop= legend_style)

    plt.savefig('img/Figure4a.pdf', figsize=(10,6), dpi= 300)
    # plt.savefig('img/Figure4a.png', figsize=(10,6), dpi= 300)

def plot_NO2_by_position(df):

    plt.figure()

    sns.distplot(df.loc[df['tipus'] == "tràfic", "no2_2017"], 
             bins=range(0,140,5),
             kde=False,
             color="red", label="Traffic", hist_kws=dict(width=4.7, alpha=0.6))

    sns.distplot(df.loc[df['tipus'] == "fons", "no2_2017"], 
                 bins=range(0,140,5),
                 kde=False,
                 color="dodgerblue", label="Background", hist_kws=dict(width=4.7, alpha=0.6))

    plt.axvline(x=df[df['tipus']=='fons']['no2_2017'].mean(), 
                ymin=0, ymax=1, 
                color='dodgerblue',
                linewidth=2, linestyle='--', 
                #label='Fons'
               )

    plt.axvline(x=df[df['tipus']=='tràfic']['no2_2017'].mean(), 
                ymin=0, ymax=1,
                color='red',
                linewidth=2, linestyle='--',
                #label='Transit'
               )

    # Decoration
    plt.xlabel('NO2 level', **label_style)
    plt.ylabel('Sampling sites', **label_style)
    plt.xticks(**ticks_style)
    plt.yticks(**ticks_style)
    plt.ylim(0,100)
    plt.gca().spines["top"].set_visible(False)    
    plt.gca().spines["bottom"].set_visible(True)    
    plt.gca().spines["right"].set_visible(False)    
    plt.gca().spines["left"].set_visible(False) 
    plt.grid(axis='y', alpha=1, linewidth=.5, color='#eeeeee')
    plt.grid(axis='y', alpha=1, linewidth=.5, color='#eeeeee')
    plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=True) 
    plt.tick_params(axis='y', which='both', left=False, right=False, labelleft=True)

    leg = plt.legend(frameon=False, prop= legend_style)

    plt.savefig('img/Figure4b.pdf', figsize=(10,6), dpi= 300)
    # plt.savefig('img/Figure4b.png', figsize=(10,6), dpi= 300)

def plot_NO2_by_district(df):

    fig, ax = plt.subplots()

    flierprops = dict(markerfacecolor='1', markersize=8, marker='o', linestyle='none')
    colors = ['red','dodgerblue']

    bplot=sns.boxplot(x='district', # vertical
                    y='no2_2017',
                    orient = 'v', 
                    hue='tipus', 
                    data=df, 
                    width=.5, 
                    palette=colors, 
                    linewidth=0.5,
                    flierprops=flierprops,
                    whis=[5, 95],
                    order=['Ciutat Vella', 'Eixample', 'Sants-Montjuïc', 'Les Corts', 'Sarrià-Sant Gervasi', 'Gràcia', 'Horta-Guinardó', 'Nou Barris', 'Sant Andreu', 'Sant Martí']
                    )

    for patch in bplot.artists:
        r, g, b, a = patch.get_facecolor()
        patch.set_facecolor((r, g, b, .75))

    index = 0
    for i,artist in enumerate(bplot.artists):
        col = artist.get_facecolor()
        artist.set_edgecolor(col)
        artist.set_facecolor(col)

        for j in range(i*6,i*6+6):
            line = bplot.lines[j]
            if j == 4 + 6*index:
                line.set_color('#ffffff')
                line.set_mfc('#ffffff')
                line.set_mec('#ffffff')
                index = index + 1
            else:
                line.set_color(col)
                line.set_mfc(col)
                line.set_mec(col)

    ax.set_xlabel('', **label_style)
    ax.set_ylabel('NO2 levels', **label_style)

    plt.xticks(rotation=90, **ticks_style)
    plt.yticks(**ticks_style)

    plt.gca().spines["top"].set_visible(False)    
    plt.gca().spines["bottom"].set_visible(False)    
    plt.gca().spines["right"].set_visible(False)    
    plt.gca().spines["left"].set_visible(False)   

    plt.grid(axis='x', alpha=.5, linewidth=.5, color='lightgrey')

    plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=True) 
    plt.tick_params(axis='y', which='both', left=False, right=False, labelleft=True) 

    plt.legend(frameon=False, prop= legend_style)

    for t, l in zip(ax.get_legend().texts, ['Traffic', 'Background']): t.set_text(l)

    plt.tight_layout()

    plt.savefig('img/Figure4c.pdf', figsize=(10,6), dpi= 300)
    #plt.savefig('img/Figure4c.png', figsize=(10,6), dpi= 300)

#### Plots population

def plot_population(distributions):

    plt.clf()
    plt.figure()

    plt.bar(x=(list(range(0, 4000, 250))), 
            height=distributions[0], 
            color="dodgerblue", 
            label="Barcelona", 
            width=240, 
            alpha=0.6,
            align='edge')

    plt.bar(x=(list(range(0, 4000, 250))), 
            height=distributions[1], 
            color="red", 
            label="Sampling sites", 
            width=240, alpha=0.6, 
            align='edge')


    # Decoration
    plt.xlabel('Population (inhabitants per census tract)', **label_style)
    plt.ylabel('Density', **label_style)
    plt.xticks(**ticks_style)
    plt.yticks(**ticks_style)
    plt.gca().spines["top"].set_visible(False)    
    plt.gca().spines["bottom"].set_visible(True)    
    plt.gca().spines["right"].set_visible(False)    
    plt.gca().spines["left"].set_visible(False) 
    plt.grid(axis='y', alpha=1, linewidth=.5, color='#eeeeee')
    plt.grid(axis='y', alpha=1, linewidth=.5, color='#eeeeee')
    plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=True) 
    plt.tick_params(axis='y', which='both', left=False, right=False, labelleft=True)
    plt.legend(frameon=False, prop= legend_style)

    plt.tight_layout()

    plt.savefig('img/Figure5a.pdf', dpi=300, figsize=(7,5))
    #plt.savefig('img/Figure5a.png', dpi=300, figsize=(7,5))

def plot_population_corr(df):

    plt.figure()

    sns.jointplot(x="no2_2017", y="poblacio", data=df, kind='reg',
                  joint_kws={'color':reds[5]},
                  marginal_kws={'color': reds[5]}) # Scatter and regression all green


    plt.xlabel('NO2 level', **label_style)
    plt.ylabel('Population (inhabitants per census tract)', **label_style)
    plt.xticks(**ticks_style)
    plt.yticks(**ticks_style)
    plt.gca().spines["top"].set_visible(False)    
    plt.gca().spines["bottom"].set_visible(False)    
    plt.gca().spines["right"].set_visible(False)    
    plt.gca().spines["left"].set_visible(False) 

    plt.grid(axis='y', alpha=1, linewidth=.5, color='#eeeeee')
    plt.grid(axis='x', alpha=1, linewidth=.5, color='#eeeeee')
    plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=True) 
    plt.tick_params(axis='y', which='both', left=False, right=False, labelleft=True)
    plt.legend(frameon=False, prop= legend_style)

    plt.tight_layout()

    plt.savefig('img/Figure5b.pdf', dpi=300, figsize=(5,5))
    #plt.savefig('img/Figure5b.png', dpi=300, figsize=(5,5))

#### Plots income

def plot_income(distributions):

    plt.clf()
    plt.figure()

    plt.bar(x=(list(range(0, 35000, 1000))), 
            height=distributions[0], 
            color="dodgerblue", 
            label="Barcelona", 
            width=900, 
            alpha=0.6,
            align='edge')

    plt.bar(x=(list(range(0, 35000, 1000))), 
            height=distributions[1], 
            color="red", 
            label="Sampling sites", 
            width=900, alpha=0.6, 
            align='edge')


    # Decoration
    plt.xlabel('Income (EUR)', **label_style)
    plt.ylabel('Density', **label_style)
    plt.xticks(**ticks_style)
    plt.yticks(**ticks_style)
    plt.gca().spines["top"].set_visible(False)    
    plt.gca().spines["bottom"].set_visible(True)    
    plt.gca().spines["right"].set_visible(False)    
    plt.gca().spines["left"].set_visible(False) 
    plt.grid(axis='y', alpha=1, linewidth=.5, color='#eeeeee')
    plt.grid(axis='y', alpha=1, linewidth=.5, color='#eeeeee')
    plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=True) 
    plt.tick_params(axis='y', which='both', left=False, right=False, labelleft=True)
    plt.legend(frameon=False, prop= legend_style)

    plt.tight_layout()

    plt.savefig('img/FigureS1a.pdf', dpi=300, figsize=(7,5))
    #plt.savefig('img/FigureS1a.png', dpi=300, figsize=(7,5))

def plot_income_corr(df):

    plt.clf()
    plt.figure()

    sns.jointplot(x="no2_2017", y="renta", data=df, kind='reg',
                  joint_kws={'color':reds[5]},
                  marginal_kws={'color': reds[5]})


    plt.xlabel('NO2 level', **label_style)
    plt.ylabel('Income (EUR)', **label_style)
    plt.xticks(**ticks_style)
    plt.yticks(**ticks_style)
    plt.gca().spines["top"].set_visible(False)    
    plt.gca().spines["bottom"].set_visible(False)    
    plt.gca().spines["right"].set_visible(False)    
    plt.gca().spines["left"].set_visible(False) 

    plt.grid(axis='y', alpha=1, linewidth=.5, color='#eeeeee')
    plt.grid(axis='x', alpha=1, linewidth=.5, color='#eeeeee')
    plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=True) 
    plt.tick_params(axis='y', which='both', left=False, right=False, labelleft=True)
    plt.legend(frameon=False, prop= legend_style)

    plt.tight_layout()

    plt.savefig('img/FigureS1b.pdf', dpi=300, figsize=(5,5))
    #plt.savefig('img/FigureS1b.png', dpi=300, figsize=(5,5))

#### Statistical testing

def KS_test(x, y, alpha=0.05):
    
    # raw data
    stat, p = stats.ks_2samp(x, y)

    print("stats: {}\np: {}".format(stat, p))

    if p > alpha:
        print('Null hypothesis: the independent samples are drawn from the same continuous distribution')
    else:
        print('Reject Null hypothesis: the independent samples are not drawn from the same continuous distribution')

def Pearson_corr(x, y, alpha=0.05):
    
    # raw data
    stat, p = stats.stats.pearsonr(x, y)

    print("stats: {}\np: {}".format(stat, p))

    if p > alpha:
        print('Null hypothesis: there is not a statistically significant correlation.')
    else:
        print('Reject Null hypothesis: there is a statistically significant correlation')

