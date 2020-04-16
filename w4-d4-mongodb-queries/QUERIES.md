
# How to import a JSON dataset into mongodb
```
$ mongoimport --db=<dbname> --collection=<colname> <json_file>
```
# Mongodb operators
- https://docs.mongodb.com/manual/reference/operator/query/


# Some queries
```
{$or:[{founded_year:2004},{founded_year:2005}]}

{founded_year:{$in:[2004,2005]}}

{founded_year:{$in:[2004,2005]}, founded_month:10}
```

# 7 - Restaurantes con todas las notas como mínimo 50, 
#     que tengan minimo 1 nota, y que el campo de la nota no sea null
```
{
  "$and": [
    {
      "grades": {
        "$not": {
          "$elemMatch": {
            "score": {
              "$lte": 50
            }
          }
        }
      }
    },
    {
      "grades.score": {
        "$not": {
          "$type": "null"
        }
      }
    },
    {
      "grades": {
        "$not": {
          "$size": 0
        }
      }
    }
  ]
}
```
