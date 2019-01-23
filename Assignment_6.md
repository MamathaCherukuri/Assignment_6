

```python
import pandas as pd
```

###1 Read the dataset using pandas


```python
tags_df=pd.read_csv("tags.csv")
```


```python
tags_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>userId</th>
      <th>movieId</th>
      <th>tag</th>
      <th>timestamp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>60756</td>
      <td>funny</td>
      <td>1445714994</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>60756</td>
      <td>Highly quotable</td>
      <td>1445714996</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>60756</td>
      <td>will ferrell</td>
      <td>1445714992</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>89774</td>
      <td>Boxing story</td>
      <td>1445715207</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>89774</td>
      <td>MMA</td>
      <td>1445715200</td>
    </tr>
  </tbody>
</table>
</div>




```python
ratings_df=pd.read_csv("ratings.csv")
```


```python
ratings_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>userId</th>
      <th>movieId</th>
      <th>rating</th>
      <th>timestamp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1</td>
      <td>4.0</td>
      <td>964982703</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>3</td>
      <td>4.0</td>
      <td>964981247</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>6</td>
      <td>4.0</td>
      <td>964982224</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>47</td>
      <td>5.0</td>
      <td>964983815</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>50</td>
      <td>5.0</td>
      <td>964982931</td>
    </tr>
  </tbody>
</table>
</div>




```python
movies_df=pd.read_csv("movies.csv")
```


```python
movies_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>movieId</th>
      <th>title</th>
      <th>genres</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Toy Story (1995)</td>
      <td>Adventure|Animation|Children|Comedy|Fantasy</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Jumanji (1995)</td>
      <td>Adventure|Children|Fantasy</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Grumpier Old Men (1995)</td>
      <td>Comedy|Romance</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Waiting to Exhale (1995)</td>
      <td>Comedy|Drama|Romance</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Father of the Bride Part II (1995)</td>
      <td>Comedy</td>
    </tr>
  </tbody>
</table>
</div>



###2 Extract the first row from tags and print its type


```python
tags_df.iloc[0,:]
```




    userId                2
    movieId           60756
    tag               funny
    timestamp    1445714994
    Name: 0, dtype: object



###3 Extract row 0,11,2000 from tags and print its type


```python
tags_df.iloc[0,:]

```




    userId                2
    movieId           60756
    tag               funny
    timestamp    1445714994
    Name: 0, dtype: object




```python
tags_df.iloc[11,:]

```




    userId               18
    movieId             431
    tag            gangster
    timestamp    1462138749
    Name: 11, dtype: object




```python
tags_df.iloc[2000,:]
```




    userId              474
    movieId            5450
    tag               women
    timestamp    1138039255
    Name: 2000, dtype: object



###4 print index columns of a data frame


```python
tags_df.index
```




    RangeIndex(start=0, stop=3683, step=1)




```python
tags_df.columns.values.tolist()
```




    ['userId', 'movieId', 'tag', 'timestamp']



###5Calculate descriptive statistics for the ratings column of the ratings data data frame
verify using describe


```python
ratings_df["rating"].describe()
```




    count    100836.000000
    mean          3.501557
    std           1.042529
    min           0.500000
    25%           3.000000
    50%           3.500000
    75%           4.000000
    max           5.000000
    Name: rating, dtype: float64



###6 Filter out ratings with rating >5


```python

rating_gt_5=ratings_df[ratings_df.rating >5.0]
rating_gt_5
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>userId</th>
      <th>movieId</th>
      <th>rating</th>
      <th>timestamp</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
</div>



###7 Find how many null values, missing values are present.Deal
with them. Print out how many rows have been modified.


```python
ratings_df.isnull().values.any()
```




    False




```python
tags_df.isnull().values.any()
```




    False




```python
movies_df.isnull().values.any()
```




    False




```python
ratings_df.isnull().sum()
```




    userId       0
    movieId      0
    rating       0
    timestamp    0
    dtype: int64




```python
tags_df.isnull().sum()
```




    userId       0
    movieId      0
    tag          0
    timestamp    0
    dtype: int64




```python
movies_df.isnull().sum()
```




    movieId    0
    title      0
    genres     0
    dtype: int64



###8 Filter out movies from the movies DataFrame that are 
of type "Animation"


```python
movies_df_Anim=movies_df[movies_df.genres =="Animation"]
movies_df_Anim
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>movieId</th>
      <th>title</th>
      <th>genres</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>6973</th>
      <td>66335</td>
      <td>Afro Samurai: Resurrection (2009)</td>
      <td>Animation</td>
    </tr>
    <tr>
      <th>7059</th>
      <td>69469</td>
      <td>Garfield's Pet Force (2009)</td>
      <td>Animation</td>
    </tr>
    <tr>
      <th>7195</th>
      <td>72603</td>
      <td>Merry Madagascar (2009)</td>
      <td>Animation</td>
    </tr>
    <tr>
      <th>7279</th>
      <td>74791</td>
      <td>Town Called Panic, A (Panique au village) (2009)</td>
      <td>Animation</td>
    </tr>
    <tr>
      <th>7439</th>
      <td>81018</td>
      <td>Illusionist, The (L'illusionniste) (2010)</td>
      <td>Animation</td>
    </tr>
    <tr>
      <th>8142</th>
      <td>102007</td>
      <td>Invincible Iron Man, The (2007)</td>
      <td>Animation</td>
    </tr>
    <tr>
      <th>8145</th>
      <td>102058</td>
      <td>Hulk Vs. (2009)</td>
      <td>Animation</td>
    </tr>
    <tr>
      <th>8593</th>
      <td>117545</td>
      <td>Asterix: The Land of the Gods (Astérix: Le dom...</td>
      <td>Animation</td>
    </tr>
    <tr>
      <th>8718</th>
      <td>126090</td>
      <td>Hedgehog in the Fog (1975)</td>
      <td>Animation</td>
    </tr>
    <tr>
      <th>8874</th>
      <td>134019</td>
      <td>The Monkey King (1964)</td>
      <td>Animation</td>
    </tr>
    <tr>
      <th>8986</th>
      <td>138966</td>
      <td>Nasu: Summer in Andalusia (2003)</td>
      <td>Animation</td>
    </tr>
    <tr>
      <th>8993</th>
      <td>139640</td>
      <td>Ooops! Noah is Gone... (2015)</td>
      <td>Animation</td>
    </tr>
    <tr>
      <th>9214</th>
      <td>151769</td>
      <td>Three from Prostokvashino (1978)</td>
      <td>Animation</td>
    </tr>
    <tr>
      <th>9237</th>
      <td>153236</td>
      <td>Genius Party (2007)</td>
      <td>Animation</td>
    </tr>
    <tr>
      <th>9340</th>
      <td>160718</td>
      <td>Piper (2016)</td>
      <td>Animation</td>
    </tr>
    <tr>
      <th>9343</th>
      <td>160848</td>
      <td>The Red Turtle (2016)</td>
      <td>Animation</td>
    </tr>
    <tr>
      <th>9380</th>
      <td>163112</td>
      <td>Winnie the Pooh Goes Visiting (1971)</td>
      <td>Animation</td>
    </tr>
    <tr>
      <th>9382</th>
      <td>163386</td>
      <td>Winnie the Pooh and the Day of Concern (1972)</td>
      <td>Animation</td>
    </tr>
    <tr>
      <th>9384</th>
      <td>163639</td>
      <td>DC Super Hero Girls: Hero of the Year (2016)</td>
      <td>Animation</td>
    </tr>
    <tr>
      <th>9495</th>
      <td>170597</td>
      <td>A Plasticine Crow (1981)</td>
      <td>Animation</td>
    </tr>
    <tr>
      <th>9537</th>
      <td>172583</td>
      <td>Investigation Held by Kolobki (1986)</td>
      <td>Animation</td>
    </tr>
    <tr>
      <th>9539</th>
      <td>172587</td>
      <td>Vacations in Prostokvashino (1980)</td>
      <td>Animation</td>
    </tr>
    <tr>
      <th>9540</th>
      <td>172589</td>
      <td>Winter in Prostokvashino (1984)</td>
      <td>Animation</td>
    </tr>
    <tr>
      <th>9549</th>
      <td>172909</td>
      <td>Cheburashka (1971)</td>
      <td>Animation</td>
    </tr>
    <tr>
      <th>9561</th>
      <td>173355</td>
      <td>Travels of an Ant (1983)</td>
      <td>Animation</td>
    </tr>
    <tr>
      <th>9587</th>
      <td>175401</td>
      <td>Wolf and Calf (1984)</td>
      <td>Animation</td>
    </tr>
    <tr>
      <th>9601</th>
      <td>176051</td>
      <td>LEGO DC Super Hero Girls: Brain Drain (2017)</td>
      <td>Animation</td>
    </tr>
    <tr>
      <th>9624</th>
      <td>178111</td>
      <td>Fireworks, Should We See It from the Side or t...</td>
      <td>Animation</td>
    </tr>
    <tr>
      <th>9729</th>
      <td>190219</td>
      <td>Bunny (1998)</td>
      <td>Animation</td>
    </tr>
    <tr>
      <th>9735</th>
      <td>193573</td>
      <td>Love Live! The School Idol Movie (2015)</td>
      <td>Animation</td>
    </tr>
  </tbody>
</table>
</div>




```python
###9 Find the avarage rating of movies
```


```python
ratings_df["rating"].mean()
```




    3.501556983616962




```python
###10 Perform an inner join of movies and tags based on movieid
```


```python
merged_df=pd.merge(movies_df,tags_df,on="movieId")
merged_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>movieId</th>
      <th>title</th>
      <th>genres</th>
      <th>userId</th>
      <th>tag</th>
      <th>timestamp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Toy Story (1995)</td>
      <td>Adventure|Animation|Children|Comedy|Fantasy</td>
      <td>336</td>
      <td>pixar</td>
      <td>1139045764</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Toy Story (1995)</td>
      <td>Adventure|Animation|Children|Comedy|Fantasy</td>
      <td>474</td>
      <td>pixar</td>
      <td>1137206825</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>Toy Story (1995)</td>
      <td>Adventure|Animation|Children|Comedy|Fantasy</td>
      <td>567</td>
      <td>fun</td>
      <td>1525286013</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>Jumanji (1995)</td>
      <td>Adventure|Children|Fantasy</td>
      <td>62</td>
      <td>fantasy</td>
      <td>1528843929</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>Jumanji (1995)</td>
      <td>Adventure|Children|Fantasy</td>
      <td>62</td>
      <td>magic board game</td>
      <td>1528843932</td>
    </tr>
  </tbody>
</table>
</div>




```python
merged_df1=pd.merge(movies_df,ratings_df,on="movieId")
merged_df1.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>movieId</th>
      <th>title</th>
      <th>genres</th>
      <th>userId</th>
      <th>rating</th>
      <th>timestamp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Toy Story (1995)</td>
      <td>Adventure|Animation|Children|Comedy|Fantasy</td>
      <td>1</td>
      <td>4.0</td>
      <td>964982703</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Toy Story (1995)</td>
      <td>Adventure|Animation|Children|Comedy|Fantasy</td>
      <td>5</td>
      <td>4.0</td>
      <td>847434962</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>Toy Story (1995)</td>
      <td>Adventure|Animation|Children|Comedy|Fantasy</td>
      <td>7</td>
      <td>4.5</td>
      <td>1106635946</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>Toy Story (1995)</td>
      <td>Adventure|Animation|Children|Comedy|Fantasy</td>
      <td>15</td>
      <td>2.5</td>
      <td>1510577970</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>Toy Story (1995)</td>
      <td>Adventure|Animation|Children|Comedy|Fantasy</td>
      <td>17</td>
      <td>4.5</td>
      <td>1305696483</td>
    </tr>
  </tbody>
</table>
</div>



###11 Print out the 5 movies that belong to the Comedy genre and have a rating greater than 4


```python
merged_df1[(merged_df1.rating >= 4.0) & (merged_df1.genres == 'Comedy')]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>movieId</th>
      <th>title</th>
      <th>genres</th>
      <th>userId</th>
      <th>rating</th>
      <th>timestamp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>384</th>
      <td>5</td>
      <td>Father of the Bride Part II (1995)</td>
      <td>Comedy</td>
      <td>6</td>
      <td>5.0</td>
      <td>845553938</td>
    </tr>
    <tr>
      <th>386</th>
      <td>5</td>
      <td>Father of the Bride Part II (1995)</td>
      <td>Comedy</td>
      <td>43</td>
      <td>5.0</td>
      <td>848994281</td>
    </tr>
    <tr>
      <th>388</th>
      <td>5</td>
      <td>Father of the Bride Part II (1995)</td>
      <td>Comedy</td>
      <td>58</td>
      <td>4.0</td>
      <td>847719151</td>
    </tr>
    <tr>
      <th>389</th>
      <td>5</td>
      <td>Father of the Bride Part II (1995)</td>
      <td>Comedy</td>
      <td>66</td>
      <td>4.0</td>
      <td>1113190367</td>
    </tr>
    <tr>
      <th>392</th>
      <td>5</td>
      <td>Father of the Bride Part II (1995)</td>
      <td>Comedy</td>
      <td>103</td>
      <td>4.0</td>
      <td>1431957598</td>
    </tr>
    <tr>
      <th>393</th>
      <td>5</td>
      <td>Father of the Bride Part II (1995)</td>
      <td>Comedy</td>
      <td>107</td>
      <td>4.0</td>
      <td>829322340</td>
    </tr>
    <tr>
      <th>396</th>
      <td>5</td>
      <td>Father of the Bride Part II (1995)</td>
      <td>Comedy</td>
      <td>120</td>
      <td>4.0</td>
      <td>860070029</td>
    </tr>
    <tr>
      <th>398</th>
      <td>5</td>
      <td>Father of the Bride Part II (1995)</td>
      <td>Comedy</td>
      <td>147</td>
      <td>4.5</td>
      <td>1203267700</td>
    </tr>
    <tr>
      <th>400</th>
      <td>5</td>
      <td>Father of the Bride Part II (1995)</td>
      <td>Comedy</td>
      <td>169</td>
      <td>5.0</td>
      <td>1078284788</td>
    </tr>
    <tr>
      <th>403</th>
      <td>5</td>
      <td>Father of the Bride Part II (1995)</td>
      <td>Comedy</td>
      <td>200</td>
      <td>4.0</td>
      <td>1229876436</td>
    </tr>
    <tr>
      <th>410</th>
      <td>5</td>
      <td>Father of the Bride Part II (1995)</td>
      <td>Comedy</td>
      <td>337</td>
      <td>4.0</td>
      <td>860255784</td>
    </tr>
    <tr>
      <th>412</th>
      <td>5</td>
      <td>Father of the Bride Part II (1995)</td>
      <td>Comedy</td>
      <td>389</td>
      <td>4.0</td>
      <td>857934242</td>
    </tr>
    <tr>
      <th>1022</th>
      <td>18</td>
      <td>Four Rooms (1995)</td>
      <td>Comedy</td>
      <td>44</td>
      <td>4.0</td>
      <td>869252115</td>
    </tr>
    <tr>
      <th>1023</th>
      <td>18</td>
      <td>Four Rooms (1995)</td>
      <td>Comedy</td>
      <td>66</td>
      <td>4.0</td>
      <td>1113190353</td>
    </tr>
    <tr>
      <th>1026</th>
      <td>18</td>
      <td>Four Rooms (1995)</td>
      <td>Comedy</td>
      <td>103</td>
      <td>5.0</td>
      <td>1431969228</td>
    </tr>
    <tr>
      <th>1028</th>
      <td>18</td>
      <td>Four Rooms (1995)</td>
      <td>Comedy</td>
      <td>179</td>
      <td>4.0</td>
      <td>852115405</td>
    </tr>
    <tr>
      <th>1029</th>
      <td>18</td>
      <td>Four Rooms (1995)</td>
      <td>Comedy</td>
      <td>182</td>
      <td>5.0</td>
      <td>1055153282</td>
    </tr>
    <tr>
      <th>1030</th>
      <td>18</td>
      <td>Four Rooms (1995)</td>
      <td>Comedy</td>
      <td>256</td>
      <td>5.0</td>
      <td>1447000271</td>
    </tr>
    <tr>
      <th>1034</th>
      <td>18</td>
      <td>Four Rooms (1995)</td>
      <td>Comedy</td>
      <td>380</td>
      <td>4.0</td>
      <td>1494278868</td>
    </tr>
    <tr>
      <th>1036</th>
      <td>18</td>
      <td>Four Rooms (1995)</td>
      <td>Comedy</td>
      <td>483</td>
      <td>4.0</td>
      <td>1215897224</td>
    </tr>
    <tr>
      <th>1038</th>
      <td>18</td>
      <td>Four Rooms (1995)</td>
      <td>Comedy</td>
      <td>501</td>
      <td>5.0</td>
      <td>844974006</td>
    </tr>
    <tr>
      <th>1039</th>
      <td>18</td>
      <td>Four Rooms (1995)</td>
      <td>Comedy</td>
      <td>521</td>
      <td>4.0</td>
      <td>852713356</td>
    </tr>
    <tr>
      <th>1041</th>
      <td>18</td>
      <td>Four Rooms (1995)</td>
      <td>Comedy</td>
      <td>606</td>
      <td>4.0</td>
      <td>1171327151</td>
    </tr>
    <tr>
      <th>1048</th>
      <td>19</td>
      <td>Ace Ventura: When Nature Calls (1995)</td>
      <td>Comedy</td>
      <td>45</td>
      <td>4.5</td>
      <td>1091306129</td>
    </tr>
    <tr>
      <th>1049</th>
      <td>19</td>
      <td>Ace Ventura: When Nature Calls (1995)</td>
      <td>Comedy</td>
      <td>56</td>
      <td>5.0</td>
      <td>835799219</td>
    </tr>
    <tr>
      <th>1058</th>
      <td>19</td>
      <td>Ace Ventura: When Nature Calls (1995)</td>
      <td>Comedy</td>
      <td>112</td>
      <td>4.0</td>
      <td>1513989970</td>
    </tr>
    <tr>
      <th>1075</th>
      <td>19</td>
      <td>Ace Ventura: When Nature Calls (1995)</td>
      <td>Comedy</td>
      <td>240</td>
      <td>5.0</td>
      <td>849122301</td>
    </tr>
    <tr>
      <th>1077</th>
      <td>19</td>
      <td>Ace Ventura: When Nature Calls (1995)</td>
      <td>Comedy</td>
      <td>274</td>
      <td>4.0</td>
      <td>1171934796</td>
    </tr>
    <tr>
      <th>1078</th>
      <td>19</td>
      <td>Ace Ventura: When Nature Calls (1995)</td>
      <td>Comedy</td>
      <td>276</td>
      <td>4.0</td>
      <td>858351186</td>
    </tr>
    <tr>
      <th>1080</th>
      <td>19</td>
      <td>Ace Ventura: When Nature Calls (1995)</td>
      <td>Comedy</td>
      <td>284</td>
      <td>4.0</td>
      <td>832786975</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>100044</th>
      <td>162344</td>
      <td>Tom Segura: Mostly Stories (2016)</td>
      <td>Comedy</td>
      <td>111</td>
      <td>5.0</td>
      <td>1516154577</td>
    </tr>
    <tr>
      <th>100083</th>
      <td>163527</td>
      <td>Comedy Central Roast of David Hasselhoff (2010)</td>
      <td>Comedy</td>
      <td>89</td>
      <td>4.0</td>
      <td>1520408953</td>
    </tr>
    <tr>
      <th>100153</th>
      <td>165103</td>
      <td>Keeping Up with the Joneses (2016)</td>
      <td>Comedy</td>
      <td>111</td>
      <td>4.0</td>
      <td>1516154574</td>
    </tr>
    <tr>
      <th>100158</th>
      <td>165483</td>
      <td>Joe Rogan: Triggered (2016)</td>
      <td>Comedy</td>
      <td>111</td>
      <td>4.0</td>
      <td>1517441316</td>
    </tr>
    <tr>
      <th>100197</th>
      <td>166492</td>
      <td>Office Christmas Party (2016)</td>
      <td>Comedy</td>
      <td>111</td>
      <td>4.5</td>
      <td>1516153370</td>
    </tr>
    <tr>
      <th>100256</th>
      <td>167018</td>
      <td>Why Him? (2016)</td>
      <td>Comedy</td>
      <td>111</td>
      <td>4.5</td>
      <td>1516141949</td>
    </tr>
    <tr>
      <th>100270</th>
      <td>167634</td>
      <td>Fist Fight (2017)</td>
      <td>Comedy</td>
      <td>111</td>
      <td>4.5</td>
      <td>1516153933</td>
    </tr>
    <tr>
      <th>100282</th>
      <td>167854</td>
      <td>Dana Carvey: Straight White Male, 60 (2016)</td>
      <td>Comedy</td>
      <td>89</td>
      <td>4.5</td>
      <td>1520409087</td>
    </tr>
    <tr>
      <th>100285</th>
      <td>168144</td>
      <td>Joe Rogan: Live (2006)</td>
      <td>Comedy</td>
      <td>111</td>
      <td>4.0</td>
      <td>1516156395</td>
    </tr>
    <tr>
      <th>100364</th>
      <td>168632</td>
      <td>Bill Burr: Walk Your Way Out (2017)</td>
      <td>Comedy</td>
      <td>111</td>
      <td>4.0</td>
      <td>1517441031</td>
    </tr>
    <tr>
      <th>100366</th>
      <td>168846</td>
      <td>Neal Brennan: 3 Mics (2017)</td>
      <td>Comedy</td>
      <td>111</td>
      <td>4.5</td>
      <td>1516154968</td>
    </tr>
    <tr>
      <th>100385</th>
      <td>170357</td>
      <td>Dave Chappelle: The Age of Spin (2017)</td>
      <td>Comedy</td>
      <td>111</td>
      <td>4.0</td>
      <td>1517440967</td>
    </tr>
    <tr>
      <th>100388</th>
      <td>170411</td>
      <td>Dave Chappelle: Deep in the Heart of Texas (2017)</td>
      <td>Comedy</td>
      <td>105</td>
      <td>4.0</td>
      <td>1526207357</td>
    </tr>
    <tr>
      <th>100482</th>
      <td>173205</td>
      <td>The Meyerowitz Stories (2017)</td>
      <td>Comedy</td>
      <td>414</td>
      <td>4.0</td>
      <td>1521847441</td>
    </tr>
    <tr>
      <th>100502</th>
      <td>173963</td>
      <td>Empties (2007)</td>
      <td>Comedy</td>
      <td>105</td>
      <td>5.0</td>
      <td>1526207493</td>
    </tr>
    <tr>
      <th>100503</th>
      <td>174045</td>
      <td>Goon: Last of the Enforcers (2017)</td>
      <td>Comedy</td>
      <td>111</td>
      <td>4.0</td>
      <td>1517440969</td>
    </tr>
    <tr>
      <th>100524</th>
      <td>174551</td>
      <td>Obsession (1965)</td>
      <td>Comedy</td>
      <td>105</td>
      <td>5.0</td>
      <td>1526207135</td>
    </tr>
    <tr>
      <th>100529</th>
      <td>174909</td>
      <td>Logan Lucky (2017)</td>
      <td>Comedy</td>
      <td>212</td>
      <td>4.5</td>
      <td>1527794983</td>
    </tr>
    <tr>
      <th>100575</th>
      <td>176329</td>
      <td>Ari Shaffir: Double Negative (2017)</td>
      <td>Comedy</td>
      <td>111</td>
      <td>4.0</td>
      <td>1517440844</td>
    </tr>
    <tr>
      <th>100607</th>
      <td>177185</td>
      <td>Maz Jobrani: Immigrant (2017)</td>
      <td>Comedy</td>
      <td>89</td>
      <td>4.5</td>
      <td>1520409502</td>
    </tr>
    <tr>
      <th>100618</th>
      <td>177615</td>
      <td>Lady Bird (2017)</td>
      <td>Comedy</td>
      <td>414</td>
      <td>4.5</td>
      <td>1521844149</td>
    </tr>
    <tr>
      <th>100643</th>
      <td>178613</td>
      <td>Dave Chappelle: Killin' Them Softly (2000)</td>
      <td>Comedy</td>
      <td>105</td>
      <td>4.0</td>
      <td>1526207359</td>
    </tr>
    <tr>
      <th>100649</th>
      <td>179119</td>
      <td>The Death of Stalin (2017)</td>
      <td>Comedy</td>
      <td>380</td>
      <td>4.0</td>
      <td>1536872796</td>
    </tr>
    <tr>
      <th>100660</th>
      <td>179427</td>
      <td>Dane Cook: Troublemaker (2014)</td>
      <td>Comedy</td>
      <td>111</td>
      <td>4.0</td>
      <td>1516155015</td>
    </tr>
    <tr>
      <th>100709</th>
      <td>181065</td>
      <td>Jack Whitehall: At Large (2017)</td>
      <td>Comedy</td>
      <td>89</td>
      <td>4.0</td>
      <td>1520408963</td>
    </tr>
    <tr>
      <th>100746</th>
      <td>183959</td>
      <td>Tom Segura: Disgraceful (2018)</td>
      <td>Comedy</td>
      <td>111</td>
      <td>4.5</td>
      <td>1517440654</td>
    </tr>
    <tr>
      <th>100761</th>
      <td>184791</td>
      <td>Fred Armisen: Standup for Drummers (2018)</td>
      <td>Comedy</td>
      <td>89</td>
      <td>4.0</td>
      <td>1520409064</td>
    </tr>
    <tr>
      <th>100809</th>
      <td>188797</td>
      <td>Tag (2018)</td>
      <td>Comedy</td>
      <td>514</td>
      <td>4.0</td>
      <td>1535941279</td>
    </tr>
    <tr>
      <th>100820</th>
      <td>190209</td>
      <td>Jeff Ross Roasts the Border (2017)</td>
      <td>Comedy</td>
      <td>338</td>
      <td>4.0</td>
      <td>1530148487</td>
    </tr>
    <tr>
      <th>100835</th>
      <td>193609</td>
      <td>Andrew Dice Clay: Dice Rules (1991)</td>
      <td>Comedy</td>
      <td>331</td>
      <td>4.0</td>
      <td>1537157606</td>
    </tr>
  </tbody>
</table>
<p>2645 rows × 6 columns</p>
</div>




```python
### 12.Split "genres in to multiple columns"
```


```python
from sklearn.preprocessing import MultiLabelBinarizer


# Binarise labels
mlb = MultiLabelBinarizer()
expandedLabelData = mlb.fit_transform(movies_df["genres"])
labelClasses = mlb.classes_


# Create a pandas.DataFrame from our output
expandedLabels = pandas.DataFrame(expandedLabelData, columns=labelClasses)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-52-2fd17569a90a> in <module>()
          9 
         10 # Create a pandas.DataFrame from our output
    ---> 11 expandedLabels = pandas.DataFrame(expandedLabelData, columns=labelClasses)
    

    NameError: name 'pandas' is not defined



```python
movies_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>movieId</th>
      <th>title</th>
      <th>genres_0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Toy Story (1995)</td>
      <td>Adventure|Animation|Children|Comedy|Fantasy</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Jumanji (1995)</td>
      <td>Adventure|Children|Fantasy</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Grumpier Old Men (1995)</td>
      <td>Comedy|Romance</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Waiting to Exhale (1995)</td>
      <td>Comedy|Drama|Romance</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Father of the Bride Part II (1995)</td>
      <td>Comedy</td>
    </tr>
  </tbody>
</table>
</div>




```python
###13. Extract year from title (1995)
```


```python

```


```python

```
