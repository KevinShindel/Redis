JSON.GET "KEY" # get data of all dict
JSON.GET "KEY" $.field # get data only for specified field

JSON.SET "KEY" $ '{"key" : "value"}' # create data
JSON.SET "KEY" $.dict_key "value" # update field

JSON.GET ru204:book:701 $.inventory[0].status # get sliced item field
JSON.GET ru204:book:701 $.author $.pages $.genres[0] # get few fields

JSON.ARRLEN ru204:book:18161 $.inventory # fild length of array
JSON.MGET ru204:book:18161 ru204:book:684 $.title # multiple document get fields

JSON.STRLEN ru204:book:206 $.title # retrieve len of string

JSON.ARRAPPEND ru204:book:18161 $.inventory '{"stock_number": "18161_5","status": "maintenance"}' # Adding an element to an array with JSON.ARRAPPEND
JSON.ARRINSERT ru204:book:18161 $.inventory 1 '{"stock_number": "18161_2","status": "available"}' # Inserting a new element into an array with JSON.ARRINSERT
JSON.ARRPOP ru204:book:18161 $.inventory  # Removing elements from an array with JSON.ARRPOP
JSON.NUMINCRBY ru204:book:701 $.checked_out 1 # INCREMENT INT BY PASSED VALUE
JSON.NUMINCRBY ru204:book:701 $.checked_out -1 # DECREASE INT BY PASSED VALUE

JSON.STRAPPEND ru204:book:18161 $.author '", Esq."' # APPEND STRING FIELD BY VALUE
JSON.SET ru204:book:18161 $.has_ebook_version false # SET BOOLEAN FIELD
JSON.TOGGLE ru204:book:18161 $.has_ebook_version # SWITCH BOOLEAN FIELD

JSON.DEL ru204:book:18161 $.genres # REMOVE DOCUMENT FIELD

JSONPath Selector	Description
$	the root object or element
@	current object or element
.	child operator, used to denote a child element of the current element
..	recursive scan
*	wildcard, returning all objects or elements regardless of their names
[]	subscript operator / array operator
,	union operator, returns the union of the children or indexes indicated
:	array slice operator; you can slice arrays using the syntax [start:step]
()	lets you pass a script expression in the underlying implementation’s script language
?()	applies a filter/script expression to query all items that meet certain criteria

# Find books with num of pages between 350 and 500
FT.SEARCH index:bookdemo '@pages:[350 500]' LIMIT 0 0

# Find num books with provided genres
FT.SEARCH index:bookdemo "@genres:{speculative fiction}" LIMIT 0 0*
*
# Let's revisit our first search query for the book titled "Aftertime":
FT.SEARCH index:bookdemo "@title:aftertime"

# Find book by title and return only title
FT.SEARCH index:bookdemo "@title:aftertime" RETURN 1 title

# Find books and return 2 fields
FT.SEARCH index:bookdemo "@title:shadow" RETURN 2 title author

# Find books and return only ID
FT.SEARCH index:bookdemo "@title:cat" NOCONTENT

# Search by TAGs
FT.SEARCH index:bookdemo "@genres:{science fiction \\(dystopia\\) @genres:{science fiction \\(apocalyptic\\)}" nocontent

# Querying Timestamp Values
FT.SEARCH index:bookdemo "@date_created:[1659917106 1660521906]"



# Search by text and numbers
FT.SEARCH index:bookdemo "@author: Stephen King @pages:[-inf (350]" RETURN 2 title pages

# Search by tAGs
FT.SEARCH index:bookdemo "@author: Stephen King @genres:{horror} @title: Tower" RETURN 1 title
FT.SEARCH index:bookdemo "@genres:{Young Adult | Adventure \\(survival\\)" NOCONTENT
FT.SEARCH index:bookdemo "@genres:{Young Adult} -@genres:{horror}" NOCONTENT

# Geographic Searches
FT.SEARCH index:geotest "@location:[-122.4783 37.8175 500 m]"
FT.SEARCH index:library "@coordinates:[-73.9616473 40.772253 3 km]" RETURN 2 city $.address.street
FT.SEARCH index:library "@coordinates:[-73.9616473 40.772253 3 km] @facilities:{wifi}"

# Drop Index
FT.DROPINDEX index:library

# Aggregation
FT.AGGREGATE index:bookdemo * GROUPBY 1 @year_published REDUCE COUNT 0 AS total_published SORTBY 2 @total_published DESC MAX 10
FT.AGGREGATE index:bookdemo * GROUPBY 1 @year_published REDUCE COUNT 0 AS total_published FILTER "@total_published>52" FILTER "@year_published>2017"  SORTBY 2 @total_published DESC MAX 10
FT.AGGREGATE index:bookdemo "@year_published:[2000 +inf]" GROUPBY 1 @year_published REDUCE AVG 1 @pages as average_pagecount REDUCE MAX 1 @pages as max_pagecount REDUCE MIN 1 @pages as min_pagecount APPLY floor(@average_pagecount) AS average_pagecount SORTBY 2 @year_published ASC LIMIT 0 21

# Sorting results
# When querying an index, it is possible to sort the results by one of the indexed fields. 
# Supported field types are TEXT and NUMERIC


# Show all indexes 
```text
FT._LIST
1) "index:bookdemo"
2) "index:users:profiles"
3) "index:products
4) "inventory-index"
5) "search:locations" 
```

# Show info about index
```text
FT.INFO index:bookdemo

1) "index_name"
  2) "index:bookdemo"
  3) "index_options"
  4) (empty list or set)
  5) "index_definition"
  6) 1) "key_type"
     2) "JSON"
     3) "prefixes"
     4) 1) "ru204:book:"
     5) "default_score"
     6) "1"
  7) "attributes"
  8) 1) 1) "identifier"
        2) "$.author"
        3) "attribute"
        4) "author"
        5) "type"
        6) "TEXT"
        7) "WEIGHT"
        8) "1"
     2) 1) "identifier"
        2) "$.title"
        3) "attribute"
        4) "title"
        5) "type"
        6) "TEXT"
        7) "WEIGHT"
        8) "1"
     3) 1) "identifier"
        2) "$.description"
        3) "attribute"
        4) "description"
        5) "type"
        6) "TEXT"
        7) "WEIGHT"
        8) "1"
     4) 1) "identifier"
        2) "$.year_published"
        3) "attribute"
        4) "year_published"
        5) "type"
        6) "NUMERIC"
        7) "SORTABLE"
     5) 1) "identifier"
        2) "$.pages"
        3) "attribute"
        4) "pages"
        5) "type"
        6) "NUMERIC"
        7) "SORTABLE"
     6) 1) "identifier"
        2) "$.metrics.score"
        3) "attribute"
        4) "score"
        5) "type"
        6) "NUMERIC"
        7) "SORTABLE"
     7) 1) "identifier"
        2) "$.genres[*]"
        3) "attribute"
        4) "genres"
        5) "type"
        6) "TAG"
        7) "SEPARATOR"
        8) ""
  9) "num_docs"
  10) "1486"
  11) "max_doc_id"
  12) "1486"
  13) "num_terms"
  14) "29095"
  15) "num_records"
  16) "185593"
  17) "inverted_sz_mb"
  18) "1.1262779235839844"
  19) "vector_index_sz_mb"
  20) "0"
  21) "total_inverted_index_blocks"
  22) "68338"
  23) "offset_vectors_sz_mb"
  24) "0.21737957000732422"
  25) "doc_table_size_mb"
  26) "0.11415290832519531"
  27) "sortable_values_size_mb"
  28) "0.1020355224609375"
  29) "key_table_size_mb"
  30) "0.046214103698730469"
  31) "records_per_doc_avg"
  32) "124.89434814453125"
  33) "bytes_per_record_avg"
  34) "6.3633217811584473"
  35) "offsets_per_term_avg"
  36) "1.1415139436721802"
  37) "offset_bits_per_record_avg"
  38) "8.6072778701782227"
  39) "hash_indexing_failures"
  40) "0"
  41) "indexing"
  42) "0"
  43) "percent_indexed"
  44) "1"
  45) "gc_stats"
  46) 1) "bytes_collected"
     2) "0"
     3) "total_ms_run"
     4) "0"
     5) "total_cycles"
     6) "0"
     7) "average_cycle_time_ms"
     8) "-nan"
     9) "last_run_time_ms"
     10) "0"
     11) "gc_numeric_trees_missed"
     12) "0"
     13) "gc_blocks_denied"
     14) "0"
  47) "cursor_stats"
  48) 1) "global_idle"
     2) "0"
     3) "global_total"
     4) "0"
     5) "index_capacity"
     6) "128"
     7) "index_total"
     8) "0"  

```

# Explain query 
```text
FT.EXPLAIN / FT.EXPLAINCLI
FT.EXPLAINCLI index:bookdemo "@author:Stephen King @pages:[-inf 500]"
1) "INTERSECT {"
2) "  @author:INTERSECT {"
3) "    @author:UNION {"
4) "      @author:stephen"
5) "      @author:+stephen(expanded)"
6) "    }"
7) "    @author:UNION {"
8) "      @author:king"
9) "      @author:+king(expanded)"
10) "    }"
11) "  }"
12) "  NUMERIC {-inf <= @pages <= 500.000000}"
13) "}"
14) ""  
```

# Index profile

```text
FT.PROFILE index:bookdemo SEARCH QUERY "@author:Stephen King @pages:[-inf 500]"
1) 1) "3"
      2) 
2) 1) 1) "Total profile time"
      2) "0.434"
    2) 1) "Parsing time"
      2) "0.052999999999999999"
    3) 1) "Pipeline creation time"
      2) "0.064000000000000001"
    4) 1) "Iterators profile"
      2) 1) "Type"
          2) "INTERSECT"
          3) "Time"
          4) "0.20100000000000001"
          5) "Counter"
          6) "3"
          7) "Child iterators"
          8) 1) "Type"
            2) "INTERSECT"
            3) "Time"
            4) "0.083000000000000004"
            5) "Counter"
            6) "15"
            7) "Child iterators"
            8) 1) "Type"
                2) "UNION"
                3) "Query type"
                4) "UNION"
                5) "Time"
                6) "0.045999999999999999"
                7) "Counter"
                8) "22"
                9) "Child iterators"
                10) 1) "Type"
                  2) "TEXT"
                  3) "Term"
                  4) "stephen"
                  5) "Time"
                  6) "0.010999999999999999"
                  7) "Counter"
                  8) "20"
                  9) "Size"
                  10) "35"
                11) 1) "Type"
                  2) "TEXT"
                  3) "Term"
                  4) "+stephen"
                  5) "Time"
                  6) "0.0030000000000000001"
                  7) "Counter"
                  8) "3"
                  9) "Size"
                  10) "4"
            9) 1) "Type"
                2) "TEXT"
                3) "Term"
                4) "king"
                5) "Time"
                6) "0.012"
                7) "Counter"
                8) "15"
                9) "Size"
                10) "74"
          9) 1) "Type"
            2) "UNION"
            3) "Query type"
            4) "NUMERIC"
            5) "Time"
            6) "0.098000000000000004"
            7) "Counter"
            8) "15"
            9) "Child iterators"
            10) 1) "Type"
                2) "NUMERIC"
                3) "Term"
                4) "202 - 326.946"
                5) "Time"
                6) "0.029999999999999999"
                7) "Counter"
                8) "13"
                9) "Size"
                10) "158"
            11) 1) "Type"
                2) "NUMERIC"
                3) "Term"
                4) "326.946 - 454.514"
                5) "Time"
                6) "0.0080000000000000002"
                7) "Counter"
                8) "12"
                9) "Size"
                10) "163"
            12) 1) "Type"
                2) "NUMERIC"
                3) "Term"
                4) "454.514 - 589.523"
                5) "Time"
                6) "0.01"
                7) "Counter"
                8) "10"
                9) "Size"
                10) "155"
    5) 1) "Result processors profile"
      2) 1) "Type"
          2) "Index"
          3) "Time"
          4) "0.20899999999999999"
          5) "Counter"
          6) "3"
      3) 1) "Type  
```

# RedisJSON configuration
```text
FT.CONFIG GET *
1) 1) "EXTLOAD"
    2) "null"
2) 1) "SAFEMODE"
    2) "true"
3) 1) "CONCURRENT_WRITE_MODE"
    2) "false"
4) 1) "NOGC"
    2) "false"
5) 1) "MINPREFIX"
    2) "2"
6) 1) "FORKGC_SLEEP_BEFORE_EXIT"
    2) "0"
7) 1) "MAXDOCTABLESIZE"
    2) "1000000"
8) 1) "MAXSEARCHRESULTS"
    2) "10000"
9) 1) "MAXAGGREGATERESULTS"
    2) "10000"
10) 1) "MAXEXPANSIONS"
    2) "200"
11) 1) "MAXPREFIXEXPANSIONS"
    2) "200"
12) 1) "TIMEOUT"
    2) "500"
13) 1) "INDEX_THREADS"
    2) "8"
14) 1) "SEARCH_THREADS"
    2) "20"
15) 1) "FRISOINI"
    2) "null"
16) 1) "ON_TIMEOUT"
    2) "return"
17) 1) "GCSCANSIZE"
    2) "100"
18) 1) "MIN_PHONETIC_TERM_LEN"
    2) "3"
19) 1) "GC_POLICY"
    2) "fork"
20) 1) "FORK_GC_RUN_INTERVAL"
    2) "30"
21) 1) "FORK_GC_CLEAN_THRESHOLD"
    2) "100"
22) 1) "FORK_GC_RETRY_INTERVAL"
    2) "5"
23) 1) "FORK_GC_CLEAN_NUMERIC_EMPTY_NODES"
    2) "true"
24) 1) "_FORK_GC_CLEAN_NUMERIC_EMPTY_NODES"
    2) "true"
25) 1) "_MAX_RESULTS_TO_UNSORTED_MODE"
    2) "1000"
26) 1) "UNION_ITERATOR_HEAP"
    2) "20"
27) 1) "CURSOR_MAX_IDLE"
    2) "300000"
28) 1) "NO_MEM_POOLS"
    2) "false"
29) 1) "PARTIAL_INDEXED_DOCS"
    2) "false"
30) 1) "UPGRADE_INDEX"
    2) "Upgrade config for upgrading"
31) 1) "_NUMERIC_COMPRESS"
    2) "false"
32) 1) "_FREE_RESOURCE_ON_THREAD"
    2) "true"
33) 1) "_PRINT_PROFILE_CLOCK"
    2) "true"
34) 1) "RAW_DOCID_ENCODING"
    2) "false"
35) 1) "_NUMERIC_RANGES_PARENTS"
    2) "0"
36) 1) "DEFAULT_DIALECT"
    2) "1"
37) 1) "VSS_MAX_RESIZE"
    2) "0"  
```

# Drop index
```text
FT.DROPINDEX index:bookdemo
```

# Create index
```text
FT.CREATE index:bookdemo:2015+
  ON JSON 
  PREFIX 1 "ru204:book:"
  FILTER '@year_published > 2014'
SCHEMA 
  $.year_published AS year_published NUMERIC SORTABLE
```

# Create temporary index (dropped after 30 seconds)
```text
FT.CREATE index:bookdemo:temporary
    ON JSON 
    PREFIX 1 "ru204:book:"
    TEMPORARY 30
SCHEMA 
    $.year_published AS year_published NUMERIC SORTABLE
```

# Index score 

```text
Now, every document has a default score of 0.5. If new documents are added with a higher book_score value,
 they will appear higher in the search results. 
 If documents have a lower book_score than 0.5, they will appear lower in the search results. 
Existing documents may also be updated with a new book_score value.
```

```text
FT.CREATE index:bookdemo:scored
    ON JSON 
    PREFIX 1 "ru204:book:"
    SCORE 0.5 
    SCORE_FIELD "book_score" 
SCHEMA 
    $.author AS author TEXT
    $.title AS title TEXT
```

# Stopwords (When creating an index, stop-words can be overwritten or disabled completely by using the STOPWORDS clause)
```text
FT.CREATE index:bookdemo:stopwords
    ON JSON 
    PREFIX 1 "ru204:book:"
    STOPWORDS 3 science fiction reality
SCHEMA (
    $.author AS author TEXT
    $.title AS title TEXT
...
```

# To disable stopwords
```text
...
STOPWORDS 0
...
```

# Change index 
```text
FT.ALTER index:bookdemo SCHEMA ADD $.metrics.rating_votes AS votes NUMERIC SORTABLE
```