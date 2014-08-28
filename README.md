#URL Matcher Library for PyHamcrest

This is a set of url matchers for PyHamcrest, example usage below

```
from hamcrest import assert_that
from url_matchers import has_scheme, has_netloc, \
                         has_path, has_query_args, has_exactly_query_args
url = "https://google.com/some/path?key1=val1&key2=val2"

assert_that(url, has_scheme("https"))

assert_that(url, has_scheme("http"))
>>>AssertionError:
>>>Expected: a url with scheme: http
>>>    but: was 'https://google.com/some/path?key1=val1&key2=val2'

assert_that(url, has_netloc("google.com"))
assert_that(url, has_netloc("google2.com"))
>>>AssertionError:
>>>Expected: a url with netloc: google2.com
>>>    but: was 'https://google.com/some/path?key1=val1&key2=val2'

assert_that(url, has_path("/some/path"))
assert_that(url, has_path("/some/other/path"))
>>>AssertionError:
>>>Expected: a url with path: /some/other/path
>>>    but: was 'https://google.com/some/path?key1=val1&key2=val2'


# returns true if the query string is a superset of the expected args
assert_that(url, has_query_args({"key1":, ["val1"]}))
assert_that(url, has_query_args({"key3":, ["val3"]})
>>>AssertionError:
>>>Expected: a url with query: {'key3': ['val3']}
>>>    but: was 'https://google.com/some/path?key1=val1&key2=val2'

#fails unless the query string is exactly the expected args
assert_that(url, has_exactly_query_args({
    "key1": ["val1"],
    "key2": ["val2"]
}))
assert_that(url, has_exactly_query_args({
    "key1": ["val1"],
}))
>>>AssertionError:
>>>Expected: a url with query: {'key1': ['val1']}
>>>    but: was 'https://google.com/some/path?key1=val1&key2=val2'
