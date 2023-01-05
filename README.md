# Video 7 show notes for Python

* Link to this [page](https://bit.ly/rickScalaClojureB62): `https://bit.ly/rickScalaClojureB62` TODO
* Link to related [video](https://youtu.be/1kbAUob3Bi0) TODO 


## Tags

```
#python #java #functionalprogramming #scala #base62 

```



# Base62Encoder URLShortener



### Example URL shortener services:
* https://www.shorturl.at/
* https://bitly.com/
* https://tinyurl.com/

### URL shortener services and Base 62 explained:
* [WikiPedia URL Shortening](https://en.wikipedia.org/wiki/URL_shortening)
* [Base 62](https://en.wikipedia.org/wiki/Base62).

### URL shortener services and Base 62 tutorials with example code:
* [How a URL Shortening Application Works](https://dzone.com/articles/how-a-url-shortening-application-works)
* [Designing the Shortening URL system like Bit.ly, loading 6 billion clicks a month](https://itnext.io/designing-the-shortening-url-system-like-bit-ly-loading-6-billion-clicks-a-month-78b3e48eee8c)

# Videos in this series
* [First Video in Base62 language series 3rd Vlog video](https://www.youtube.com/watch?v=07Wkf9OZE3U)  [Show Notes]()
* [Second Video in Base62 language series 4th Vlog video](https://www.youtube.com/watch?v=sOhzb6OqyGA) [Show Notes](https://gist.github.com/RichardHightower/035fda0b65de540574e458dedf9dae6d)
* [Third Video in Base62 language series 5th Vlog video](https://www.youtube.com/watch?v=TlQZn9MajlY)  [Show Notes](https://gist.github.com/RichardHightower/1d64d0c958a7643c8b0b573c08138e1f)
* [Fourth Video in Base62 language series 6th Vlog video](https://www.youtube.com/watch?v=1kbAUob3Bi0) [Show notes](https://gist.github.com/RichardHightower/5b45e5162cf8295f73e71d67ad4a442d)

# Related articles
* [Comparing Basic FP support part 1 --Rick Hightower](https://www.linkedin.com/pulse/comparing-basic-fp-support-part-1-rick-hightower/)
* [Is Java a good FP language? Comparing Basic FP support part 2 --Rick Hightower](https://www.linkedin.com/pulse/java-good-fp-language-comparing-basic-support-part-2-rick-hightower/)
* [Translating to Clojure: a learning task (Part 1) --Tom Hicks](https://hickst.hashnode.dev/translating-to-clojure-a-learning-task-part-1)


# Where is Rick?
* [LinkedIn](https://www.linkedin.com/in/rickhigh/)
* [Rick's YouTube Channel](https://www.youtube.com/channel/UCgCx8XtYUGW9aSfzXhP2m6Q)
* [Where Rick works](http://www.cloudurable.com/)


## Title: Porting Base62Encoder/Decoder from Scala to Python

Porting Base62Encoder/Decoder from Scala to Python.

[Link To video](https://youtu.be/1kbAUob3Bi0)

## Scala to Python

### Main Method

<table>
<tr>
<th>
Scala
</th>
<th>
Python
</th>
</tr>

<tr>
<td>
<sub>

```scala 
def main(args: Array[String]): Unit = {
  val id = 12345678910L
  val strId = convertToEncodedString(id)
  val newId = convertToLong(strId)
  println(s"$id $strId $newId")

  val longURL = "https://www.somewebiste.com/dp/..."
  val urlId = Math.abs(longURL.hashCode)
  val shortHandle = convertToEncodedString(urlId)
  println(s"$urlId $shortHandle ${convertToLong(shortHandle)}")

}
```
</sub>
</td>

<td >
<sub>

```python

def main():
    print("Output", convert_to_encoded_string(12345678910), convert_to_long("DTVD3O"))
    long_url = "https://www.somewebiste.com/dp..."
    url_id = abs(hash(long_url))
    short_handle = convert_to_encoded_string(url_id)
    print("url id", url_id, "short handle", short_handle, convert_to_long(short_handle))

if __name__ == "__main__":
    main()
  
```

</sub>
</td>

</tr>
</table>



### convertToEncodedString

<table>
<tr>
<th>
Scala
</th>
<th>
Python
</th>
</tr>

<tr>
<td>
<sub>

```scala 
def convertToEncodedString(id: Long): String = {
  val builder: List[String] = List()
  val placeHolder = findStartBucket(id)
  val results = accumulateDigits(placeHolder, id, builder)
  val bucketValue = powDigitsBase(1)
  val digitIndex: Int = (results._2 / bucketValue).toInt
  val acc = results._2 - (bucketValue * digitIndex)
  val newBuilder: List[String] = appendSafeToList(results._3, digitIndex)
  //Put the remainder in the ones column
  val place1DigitIndex = (acc % bucketValue).toInt
  val finalBuilder = newBuilder ++ List(DIGITS(place1DigitIndex).toString)
  finalBuilder.mkString("")
}

private def accumulateDigits(placeHolder: Int, acc: Long, 
                     builder: List[String]): (Int, Long, List[String]) = {
  if (!(placeHolder > 1)) {
    return (placeHolder, acc, builder)
  }
  val bucketValue = powDigitsBase(placeHolder)
  val digitIndex = (acc / bucketValue).toInt
  accumulateDigits(placeHolder - 1, acc - (bucketValue * digitIndex), 
       appendSafeToList(builder, digitIndex))
}
```
</sub>
</td>

<td >
<sub>

```python
def convert_to_encoded_string(an_id):
    builder = []
    place_holder = find_start_bucket(an_id)
    (_, results, _) = accumulate_digits(place_holder, an_id, builder)
    bucket_value = pow_digits_base(1)
    digit_index = math.floor(results / bucket_value)
    acc = results - (bucket_value * digit_index)
    append_safe(builder, digit_index)
    # Put the remainder in the ones column
    place1_digit_index = math.floor(acc % bucket_value)
    append_safe(builder, place1_digit_index)
    return "".join(builder)

def accumulate_digits(place_holder, acc, builder):
    if place_holder <= 1:
        return [place_holder, acc, builder]

    bucket_value = pow_digits_base(place_holder)
    digit_index = math.floor(acc / bucket_value)
    return accumulate_digits(place_holder - 1, acc - (bucket_value * digit_index), append_safe(builder, digit_index))
```

</sub>
</td>

</tr>
</table>


### findStartBucket

<table>
<tr>
<th>
Scala
</th>
<th>
Python
</th>
</tr>

<tr>
<td>
<sub>

```scala
private def findStartBucket(value: Long): Int = {
  val i = Range(0, 15, 1).find(i => value < powDigitsBase(i.toLong))
  i.getOrElse(0)
}
```
</sub>
</td>

<td >
<sub>

```python
def find_start_bucket(bucket_value):
    index = (i for i in range(0, 14) if bucket_value < pow_digits_base(i))
    try:
        return next(index)
    except StopIteration:
        return 0
```

</sub>
</td>

</tr>
</table>



### powDigitsBase

<table>
<tr>
<th>
Scala
</th>
<th>
Python
</th>
</tr>

<tr>
<td>
<sub>

```scala
private def powDigitsBase(exponent: Long): Long = 
                        doPow(exponent, DIGITS.length)

private def doPow(exponent: Long, base: Int): Long = {
  if (exponent == 0) return 1
  doPow(exponent - 1, base) * base
}

```
</sub>
</td>

<td >
<sub>

```python 
def pow_digits_base(exponent):
    return do_pow(exponent, len(DIGITS))

def do_pow(exponent, base):
    if exponent == 0: return 1
    return do_pow(exponent - 1, base) * base
```

</sub>
</td>

</tr>
</table>




### appendSafeToList

<table>
<tr>
<th>
Scala
</th>
<th>
Python
</th>
</tr>

<tr>
<td>
<sub>

```scala

private def appendSafeToList(builder: List[String], digitIndex: Int): List[String] = {
  if (digitIndex != 0) builder ++ List((DIGITS(digitIndex)).toString)
  else if (builder.nonEmpty) builder ++ List((DIGITS(digitIndex)).toString)
  else builder
}
```
</sub>
</td>

<td >
<sub>

```python
def append_safe(builder, digit_index):
    digit_index = math.floor(digit_index)
    if digit_index != 0:
        builder.append(DIGITS[digit_index])
    else:
        if len(builder) > 0:
            builder.append(DIGITS[digit_index])
    return builder
```

</sub>
</td>

</tr>
</table>




### convertToLong

<table>
<tr>
<th>
Scala
</th>
<th>
Python
</th>
</tr>

<tr>
<td>
<sub>

```scala

def convertToLong(strId: String): Long = 
                            doConvertToLong(strId.toCharArray)

private def doConvertToLong(chars: Array[Char]): Long = {
  val (acc, _) = chars.reverse.foldLeft(0L, 0) { (pos, ch) =>
    val (acc, position) = pos
    val value = computeValue(ch, position)
    (acc + value, position + 1)
  }
  acc
}
```
</sub>
</td>

<td >
<sub>

```python
def convert_to_long(str_id):
    return do_convert_to_long(str_id)

def do_convert_to_long(str_id):
    chars = [char for char in str_id]
    chars.reverse()

    def do_reduce(pos, ch):
        (acc, position) = pos
        value = compute_value(ch, position)
        return acc + value, position + 1

    (result, _) = foldl(do_reduce, (0, 0), chars)
    return result


def foldl(func, acc, xs):
    return functools.reduce(func, xs, acc)
```
</sub>
</td>

</tr>
</table>




### computeValue

<table>
<tr>
<th>
Scala
</th>
<th>
Python
</th>
</tr>

<tr>
<td>
<sub>

```scala 
private def computeValue(c: Char, position: Int) = {
  val digitIndex = findIndexOfDigitInTable(c)
  val multiplier = powDigitsBase(position)
  digitIndex * multiplier
}
```
</sub>
</td>

<td >
<sub>

```python
def compute_value(c, position):
    digit_index = find_index_of_digit_in_table(c)
    multiplier = pow_digits_base(position)
    return digit_index * multiplier

```

</sub>
</td>

</tr>
</table>






----


## Python full example

```python 
import math
import functools

DIGITS = [
    # 0    1    2    3    4    5    6    7    8    9
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    # 10    11   12   13  14   15   16   17    18    19   20  21
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
    # 22    23   24   25  26   27   28   29    30    31   32  33    34  35
    'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    # 36  37  38   39   40   41    42    43   44  45   46    47
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',  # Easy to add more characters
    # if not using lookup tables.
    # 48  49   50   51   52   53   54   55  56   57   58  59   60   61   // 62   63, 64
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def convert_to_encoded_string(an_id):
    builder = []
    place_holder = find_start_bucket(an_id)
    (_, results, _) = accumulate_digits(place_holder, an_id, builder)
    bucket_value = pow_digits_base(1)
    digit_index = math.floor(results / bucket_value)
    acc = results - (bucket_value * digit_index)
    append_safe(builder, digit_index)
    # Put the remainder in the ones column
    place1_digit_index = math.floor(acc % bucket_value)
    append_safe(builder, place1_digit_index)
    return "".join(builder)


def find_start_bucket(bucket_value):
    index = (i for i in range(0, 14) if bucket_value < pow_digits_base(i))
    try:
        return next(index)
    except StopIteration:
        return 0


def pow_digits_base(exponent):
    return do_pow(exponent, len(DIGITS))

def do_pow(exponent, base):
    if exponent == 0: return 1
    return do_pow(exponent - 1, base) * base


def accumulate_digits(place_holder, acc, builder):
    if place_holder <= 1:
        return [place_holder, acc, builder]

    bucket_value = pow_digits_base(place_holder)
    digit_index = math.floor(acc / bucket_value)
    return accumulate_digits(place_holder - 1, acc - (bucket_value * digit_index), append_safe(builder, digit_index))


def append_safe(builder, digit_index):
    digit_index = math.floor(digit_index)
    if digit_index != 0:
        builder.append(DIGITS[digit_index])
    else:
        if len(builder) > 0:
            builder.append(DIGITS[digit_index])
    return builder


def convert_to_long(str_id):
    return do_convert_to_long(str_id)


def compute_value(c, position):
    digit_index = find_index_of_digit_in_table(c)
    multiplier = pow_digits_base(position)
    return digit_index * multiplier


def foldl(func, acc, xs):
    return functools.reduce(func, xs, acc)


def do_convert_to_long(str_id):
    chars = [char for char in str_id]
    chars.reverse()

    def do_reduce(pos, ch):
        (acc, position) = pos
        value = compute_value(ch, position)
        return acc + value, position + 1

    (result, _) = foldl(do_reduce, (0, 0), chars)
    return result


def find_index_of_digit_in_table(c):
    return DIGITS.index(c)


def main():
    print("Output", convert_to_encoded_string(12345678910), convert_to_long("DTVD3O"))
    long_url = "https://www.somewebiste.com/dp/0201616165/?_encoding=UTF8&pd_rd_w=vwEcs&content-id=amzn1.sym.8cf3b8ef-6a74-45dc-9f0d-6409eb523603&pf_rd_p=8cf3b8ef-6a74-45dc-9f0d-6409eb523603&pf_rd_r=BQ0KD40K57XG761DBNBA&pd_rd_wg=DtkHk&pd_rd_r=f94b60b7-9080-4065-b77f-6377ec854d17&ref_=pd_gw_ci_mcx_mi";
    url_id = abs(hash(long_url))
    short_handle = convert_to_encoded_string(url_id)
    print("url id", url_id, "short handle", short_handle, convert_to_long(short_handle))


if __name__ == "__main__":
    main()


```


