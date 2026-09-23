import pandas as pd, numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
fm.fontManager.addfont('HumorSans.ttf')
plt.xkcd(scale=1, length=100, randomness=2)
plt.rcParams['font.family']='Humor Sans'
G='#9a9a9a'; R='#b5523b'; K='#333333'; B='#4a6f8a'
df=pd.read_csv('repo/data/condemned_buildings_joined.csv')
b=df[~df.is_vacant_land]
def note(fig,t,step):
    fig.text(0.02,0.97,step,fontsize=11,color=G,va='top')
    fig.text(0.02,-0.04,t,fontsize=9,color=G)
def save(fig,n): fig.savefig(f'repo/sketches/{n}.png',dpi=130,bbox_inches='tight',facecolor='white'); plt.close(fig)

# 1 hook
fig,ax=plt.subplots(figsize=(8,4.5)); ax.axis('off'); ax.set_xlim(0,1); ax.set_ylim(-0.05,1)
ax.text(0.5,0.72,'Condemned is not the same as gone',ha='center',fontsize=22)
ax.text(0.5,0.55,f'{len(b):,} buildings in Pittsburgh are on the city\'s condemned list',ha='center',fontsize=13)
ax.text(0.5,0.44,'Which ones are still worth saving?',ha='center',fontsize=13,color=R)
x0=0.18
for i in range(8):
    x=x0+i*0.085; c=R if i in (1,4,5) else G
    ax.add_patch(plt.Rectangle((x,0.08),0.07,0.2,fill=False,ec=c,lw=2))
    ax.plot([x,x+0.035,x+0.07],[0.28,0.35,0.28],color=c,lw=2)
ax.text(0.5,0.0,'[full-width photo or illustration of a rowhouse street goes here]',ha='center',fontsize=9,color=G)
note(fig,'Sketch 1: Shorthand title section','SETUP / HOOK'); save(fig,'01_hook')

# 2 age
fig,ax=plt.subplots(figsize=(8,4.5))
yrs=b.year_built.dropna(); bins=range(1800,2000,10)
n,edges,_=ax.hist(yrs,bins=bins,color=G,ec='white')
for p,e in zip(ax.patches,edges[:-1]):
    if e<1940: p.set_color(B)
ax.axvline(1940,color=K,ls='--',lw=1)
pct=(yrs<1940).mean()
ax.set_title(f'Nearly all of them are over 85 years old ({pct:.0%} built before 1940)',fontsize=13,loc='left')
ax.set_xlabel('year built'); ax.set_ylabel('condemned buildings')
ax.spines[['top','right']].set_visible(False)
ax.annotate('median: 1910',xy=(1910,n.max()*0.9),xytext=(1945,n.max()*0.8),arrowprops=dict(arrowstyle='->',color=K),fontsize=11)
note(fig,'Sketch 2: Tableau histogram. Blue = built before 1940. Check the 1900 spike (possible default year)','SETUP'); save(fig,'02_age')

# 3 scores
fig,ax=plt.subplots(figsize=(8,4.5))
sc=b.pli_score_max.value_counts().reindex([1,2,3,4]).fillna(0)
labels=['1  intact, no\nimmediate danger','2  compromised,\npossibly dangerous','3  compromised,\ndangerous','4  imminently\ndangerous']
cols=[B,G,G,R]
ax.barh(labels[::-1],sc.values[::-1],color=cols[::-1])
for y,v in enumerate(sc.values[::-1]): ax.text(v+15,y,f'{int(v):,}',va='center',fontsize=11)
ax.set_title('Only a handful are about to fall down',fontsize=14,loc='left')
ax.set_xlabel('condemned buildings (latest PLI inspection score)')
ax.spines[['top','right']].set_visible(False)
note(fig,'Sketch 3: bar chart of PLI score. Highlight score 1 (reusable?) vs score 4 (must go)','RISING TENSION'); save(fig,'03_scores')

# 4 map
fig,ax=plt.subplots(figsize=(7,6))
s=b.dropna(subset=['latitude','pli_score_max'])
ax.scatter(s.longitude,s.latitude,s=6,c=np.where(s.pli_score_max<=1,B,np.where(s.pli_score_max>=3,R,G)),alpha=0.7)
ax.set_xticks([]); ax.set_yticks([])
ax.set_title('Where they are: clustered in a few neighborhoods',fontsize=13,loc='left')
top=b.neighborhood.value_counts().head(4)
ax.text(0.02,0.02,'Top: '+', '.join(top.index),transform=ax.transAxes,fontsize=9)
ax.text(0.98,0.95,'blue = score 0 to 1\ngrey = 2\nred = 3 to 4',transform=ax.transAxes,ha='right',va='top',fontsize=9)
note(fig,'Sketch 4: Tableau dot map, click a neighborhood to filter. Rivers + neighborhood outlines added in final','RISING TENSION'); save(fig,'04_map')

# 5 carbon
fig,ax=plt.subplots(figsize=(8,4.5))
ax.bar(['reuse +\nrenovate','demolish +\nbuild new'],[1,2.2],color=[B,R],width=0.5)
ax.set_yticks([]); ax.set_ylabel('embodied carbon (kgCO2e)')
ax.text(0,1.05,'?',ha='center',fontsize=18); ax.text(1,2.25,'?',ha='center',fontsize=18)
ax.set_title('Every teardown throws away carbon that was already spent',fontsize=13,loc='left')
ax.spines[['top','right']].set_visible(False)
note(fig,'Sketch 5: bar heights are placeholders. Real values = floor area x published benchmark (source TBD)','TURNING POINT'); save(fig,'05_carbon')

# 6 triage matrix
fig,ax=plt.subplots(figsize=(7,6))
ax.axhline(0.5,color=K,lw=1); ax.axvline(0.5,color=K,lw=1)
ax.set_xlim(0,1); ax.set_ylim(0,1); ax.set_xticks([]); ax.set_yticks([])
ax.set_xlabel('structural risk (PLI score)  ->'); ax.set_ylabel('reuse value (age, masonry, size, location)  ->')
for (x,y,t,c) in [(0.25,0.75,'SAVE FIRST\nstabilize + reuse',B),(0.75,0.75,'SALVAGE\ndeconstruct,\nkeep materials',G),(0.25,0.25,'MOTHBALL\nsecure + wait',G),(0.75,0.25,'DEMOLISH',R)]:
    ax.text(x,y,t,ha='center',va='center',fontsize=13,color=c)
rng=np.random.default_rng(1); ax.scatter(rng.random(60),rng.random(60),s=8,color=G,alpha=0.6)
ax.set_title('A simple triage: not every condemned building\nneeds the same answer',fontsize=13,loc='left')
note(fig,'Sketch 6: interactive scatter, each dot a building. Dots here are placeholders','RESOLUTION'); save(fig,'06_triage')

# 7 CTA
fig,ax=plt.subplots(figsize=(8,4.5)); ax.axis('off'); ax.set_xlim(0,1); ax.set_ylim(-0.05,1)
ax.text(0.5,0.8,'Before the permit, run a reuse check',ha='center',fontsize=20)
steps=['1. PLI score\n1 or 2?','2. Built before\n1940, masonry?','3. In a priority\nneighborhood?','4. Send to\nLand Bank']
for i,t in enumerate(steps):
    x=0.13+i*0.25; ax.add_patch(plt.Rectangle((x-0.1,0.3),0.2,0.25,fill=False,ec=B,lw=2)); ax.text(x,0.425,t,ha='center',va='center',fontsize=10)
    if i<3: ax.annotate('',xy=(x+0.15,0.425),xytext=(x+0.1,0.425),arrowprops=dict(arrowstyle='->',color=K))
ax.text(0.5,0.12,'[closing text + link to downloadable list of "save first" buildings]',ha='center',fontsize=9,color=G)
note(fig,'Sketch 7: closing section in Shorthand','CALL TO ACTION'); save(fig,'07_cta')
