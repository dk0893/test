
# coding: utf-8

# In[ ]:

get_ipython().magic('load_ext autoreload')
get_ipython().magic('autoreload 2')
get_ipython().magic('matplotlib inline')
import sys, os, math, re
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns # グラフスタイル

#np.set_printoptions?
#np.set_printoptions( precision=3 ) # 有効桁3で丸める、default=8
#np.set_printoptions( precision=3, suppress=True, linewidth=100 ) # 有効桁3で丸める、指数表示の禁止、default=False
np.set_printoptions( suppress=True, linewidth=100 ) # 指数表示の禁止、default=False
#np.set_printoptions( formatter={'float': '{: 0.3f}'.format} ) # 桁を揃える

pd.set_option( 'display.max_columns', 100 )


# In[ ]:

FPATH = "./data"


# In[ ]:

df = pd.read_csv( os.path.join(FPATH, "Cars93.csv") )

df.head()


# In[ ]:

df.dtypes


# In[ ]:

sel_col = [ 'MPG.city', 'MPG.highway', 'EngineSize', 'Horsepower', 'RPM', 'Rev.per.mile',
            'Fuel.tank.capacity', 'Passengers', 'Length', 'Wheelbase', 'Width', 'Turn.circle', 'Weight' ]


# In[ ]:

df_nu = df.loc[:, sel_col + ['Price']]
print( df_nu.shape )


# In[ ]:

df_nu.describe()


# In[ ]:



