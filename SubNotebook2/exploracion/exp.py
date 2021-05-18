# %%
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
#%%

medium =  pd.read_csv('med.txt')  
#%%
medium.shape
medium.head(20)

# %%
gost= medium[medium["passenger_count"] > 6]
gost.head(20)
# %%
gost.shape

# %%
# %%
plt.figure(figsize=(15, 15), dpi=100)
plt.scatter( medium["pickup_longitude"],medium["pickup_latitude"],  c="g", alpha=0.1)
plt.xlabel("pickup_longitude")
plt.ylabel("pickup_latitude")
plt.savefig('pic.png')
# %%
close = medium[medium["pickup_latitude"] < 500]
close = close[close["pickup_longitude"] > -200]


# %%
plt.figure(figsize=(15, 15), dpi=100)
plt.scatter( medium["pickup_longitude"],medium["pickup_latitude"],  c="g", alpha=0.1)
plt.xlabel("pickup_longitude")
plt.ylabel("pickup_latitude")
plt.savefig('pic3.png')

# %%
closest = medium[(medium["pickup_latitude"] > -90) &(medium["pickup_latitude"] < 90)]
closest = medium[(medium["pickup_longitude"] > -180) &(medium["pickup_longitude"] < 180)]
#%%
plt.figure(figsize=(15, 15), dpi=100)
plt.scatter( closest["pickup_longitude"],closest["pickup_latitude"],  c="g", alpha=0.1)
plt.xlabel("pickup_longitude")
plt.ylabel("pickup_latitude")
plt.savefig('pic2.png')

# %%
city = closest[
    (closest["pickup_latitude"] > 38)&
    (closest["pickup_latitude"] < 50)&
    (closest["pickup_longitude"] > -76)&
    (closest["pickup_longitude"] < -73)&

    (closest["dropoff_latitude"] > 38)&
    (closest["dropoff_latitude"] < 50)&
    (closest["dropoff_longitude"] > -76)&
    (closest["dropoff_longitude"] < -73)    
    ]


# %%
plt.figure(figsize=(15, 15), dpi=100)
plt.scatter( city["pickup_longitude"],city["pickup_latitude"],  c="g", alpha=0.1)
plt.scatter( city["pickup_longitude"],city["pickup_latitude"],  c="r", alpha=0.1)
plt.xlabel("pickup_longitude")
plt.ylabel("pickup_latitude")
plt.savefig('city_both.png')

# %%
city.shape
# %%
