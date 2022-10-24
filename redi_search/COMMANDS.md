# Search by TAGS
FT.SEARCH books-idx "@isbn:{9780393059168}"
FT.SEARCH authors-idx "@author_id:{690}"
```[command] [index] [@tag:{search text}]```

# Search with numbers
FT.SEARCH books-idx "@published_year:[2014 2018]" // search between 2014 and 2018
FT.SEARCH books-idx "@published_year:[2014 (2016]" // search between 2014 and 2015 (2016 not included)
FT.SEARCH books-idx "@published_year:[2017 +inf]" return 1 published_year // >= 2017 
FT.SEARCH books-idx "@published_year:[-inf 2014]" return 1 published_year // <= 2014 

# Next, find the titles of books having an average rating of at least 4 and being published on or after 2015
FT.SEARCH books-idx "@average_rating:[4 +inf] @published_year:[2015 +inf]" RETURN 2 title average_rating


# Working with dates and time 
FT.SEARCH checkouts-idx "@checkout_date: [1606780800 1609459200]" 
FT.SEARCH checkouts-idx "@checkout_date: [1606780800 +inf]" 
FT.SEARCH users-idx "@last_login:[1607693100 +inf]"

#Boolean logic
FT.SEARCH books-idx "dogs|cats" // find in all TEXT fields dogs OR cats

# Multiple fields
FT.SEARCH books-idx "@authors:rowling @title:goblet" // AND
FT.SEARCH books-idx "@authors:rowling | @title:potter" // OR
FT.SEARCH books-idx "@authors:tolkien -@title:ring" // NOT INCLUDE RING

# Sorting results
FT.SEARCH books-idx "@published_year:[2018 +inf]" SORTBY published_year DESC // sorting by published_year with descending

# limiting results
FT.SEARCH books-idx "@authors:Agatha Christie" SORTBY published_year LIMIT 0 5 // show only 5 results
FT.SEARCH books-idx "@published_year:[2000 +inf]" LIMIT 100 100 // Starting at offset 100, get the next 100 books

# Full-text searching
FT.SEARCH books-idx "John Le Carre"

```When you index a field as TEXT, RediSearch stores the root of the word in the index, not the word itself. So the word “thinking” becomes “think,” “running” becomes “run,” and so on. This is known as stemming.```

FT.SEARCH books-idx "@title:running" RETURN 1 title

# Prefix searching
FT.SEARCH books-idx "atwood hand*"
FT.SEARCH books-idx "agat* orie*"

# Highlight results
FT.SEARCH books-idx illusion HIGHLIGHT
FT.SEARCH books-idx "nurture" HIGHLIGHT FIELDS 2 title subtitle

# Summarize results ?
FT.SEARCH books-idx shield HIGHLIGHT SUMMARIZE FIELDS 1 description FRAGS 1 LEN 20


# Search and return specified field
FT.SEARCH authors-idx "@author_id:{690}" return 1 name
FT.SEARCH books-idx "@categories:{Fantasy}" return 1 published_year

# Aggregation functions
FT.SEARCH books-idx * LIMIT 0 0 // 6810
FT.AGGREGATE books-idx * GROUPBY 0 REDUCE COUNT 0 AS total // TOTAL - 6810

# Try finding the number of books in the books-idx index with the category “Fiction.” 
FT.SEARCH books-idx "@categories:{Fiction}" LIMIT 0 0

# Group by aggregation
FT.AGGREGATE books-idx python GROUPBY 1 @categories
FT.AGGREGATE books-idx marauder GROUPBY 2 @published_year @average_rating

# Group by and sorting 
FT.AGGREGATE users-idx *
                        GROUPBY 2 @last_login @last_name 
                        SORTBY 1 @last_name
FT.AGGREGATE books-idx "@published_year:[1983 1983]" GROUPBY 2 @authors @title SORTBY 2 @authors @title

# Reducing aggregated data 
FT.AGGREGATE books-idx * GROUPBY 1 @categories
                         REDUCE COUNT 0 AS books_count
                         SORTBY 2 @books_count DESC

FT.AGGREGATE books-idx * 
                        GROUPBY 1 @authors 
                        REDUCE COUNT 0 AS books_count
                        SORTBY 2 @books_count DESC

# Now try finding the average rating of all books that mention “tolkien.”
FT.AGGREGATE books-idx tolkien GROUPBY 0 REDUCE AVG 1 @average_rating as avg_rating

#  finding all books with two co-authors. Authors are stored in a TEXT field, with coauthors separated by semicolons, so one way to do this is to use the split() function in an APPLY step to split the authors. At the end, you’ll
# need a FILTER expression to match only books with two authors.
FT.AGGREGATE books-idx *
                    APPLY "split(@authors, ';')" AS authors_list
                    GROUPBY 1 @title
                    REDUCE COUNT_DISTINCT 1 authors_list AS authors_count
                    FILTER "@authors_count==2"

FT.AGGREGATE users-idx *
                    GROUPBY 2 @last_login @user_id 
                    APPLY "day(@last_login)" as last_login_day
                    APPLY "timefmt(@last_login_day)" AS "last_login_str"
                    GROUPBY 1 "@last_login_str"
                    REDUCE COUNT_DISTINCT 1
                    "@user_id" AS num_logins 
                    FILTER "@num_logins>1"

# Partial indexes
FT.CREATE books-older-idx 
                    ON HASH PREFIX 1 ru203:book:details:
                    FILTER "@published_year<1990" SCHEMA
                    isbn TAG SORTABLE
                    title TEXT WEIGHT 2.0 SORTABLE
                    subtitle TEXT SORTABLE
                    thumbnail TAG NOINDEX
                    description TEXT SORTABLE
                    published_year NUMERIC SORTABLE
                    average_rating NUMERIC SORTABLE
                    authors TEXT SORTABLE
                    categories TAG SEPARATOR ";" 
                    author_ids TAG SEPARATOR ";"

FT.CREATE books-newer-idx 
                    ON HASH PREFIX 1 ru203:book:details:
                    FILTER "@published_year>=1990" SCHEMA
                    isbn TAG SORTABLE
                    title TEXT WEIGHT 2.0 SORTABLE
                    subtitle TEXT SORTABLE
                    thumbnail TAG NOINDEX
                    description TEXT SORTABLE
                    published_year NUMERIC SORTABLE
                    average_rating NUMERIC SORTABLE
                    authors TEXT SORTABLE
                    categories TAG SEPARATOR ";"
                    author_ids TAG SEPARATOR ";"

FT.CREATE books-fiction-idx ON HASH PREFIX 1 ru203:book:details: FILTER "@categories=='Fiction'" SCHEMA isbn TAG SORTABLE title TEXT WEIGHT 2.0 SORTABLE subtitle TEXT SORTABLE thumbnail TAG NOINDEX description TEXT SORTABLE published_year NUMERIC SORTABLE average_rating NUMERIC SORTABLE authors TEXT SORTABLE categories TAG SEPARATOR ";" author_ids TAG SEPARATOR ";"

# Spellchecking

# Try searching for spell-check suggestions for the term “monter.”
FT.SPELLCHECK books-idx monter

# Now try running a fuzzy-matching query to search for documents with similar terms to “monter.”
FT.SEARCH books-idx "%monter%"